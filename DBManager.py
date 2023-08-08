import psycopg2
from config import *


class DBManager:
    """
    DBManager class that manages the connection and interaction
    with a PostgreSQL database, and a Parser class that includes
    various methods to retrieve and manipulate data from the database.
    """

    def __init__(self):
        """
        create a connection with PostgreSQL
        """
        self.conn = psycopg2.connect(host=HOST,
                                     port=PORT,
                                     database=DATABASE,
                                     user=USER,
                                     password=PASSWORD)

    def save_vacancies(self, vacancies: list[dict]):
        """
        save vacancies to the appropriate table,
        :param vacancies:
        """
        employers = []
        with self.conn.cursor() as cursor:
            for vacancy in vacancies:
                cursor.execute(
                    f"insert into vacancies(description, "
                    f"employer, experience, salary, url) values(%s,%s,%s,%s,%s)",
                    (vacancy["description"], vacancy["employer"].lower(),
                     vacancy["experience"], vacancy["salary"], vacancy["url"]))
                if vacancy["employer"] not in employers:
                    employers.append(vacancy["employer"])
        self.conn.commit()
        self.save_employers(employers)

    def save_employers(self, employers: list[str]):
        with self.conn.cursor() as cursor:
            for employer in employers:
                cursor.execute(f"SELECT id FROM employers WHERE company_name=%s", [employer.lower()])
                if not cursor.fetchall():
                    cursor.execute("INSERT INTO employers(company_name) values(%s)", [employer])
        self.conn.commit()

    def get_companies_and_vacancies_count(self):
        """
        print a list of all companies and the number of vacancies
        for each company.
        """
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT company_name FROM employers")
            for company in cursor.fetchall():
                cursor.execute("SELECT COUNT(*) FROM vacancies WHERE employer=%s", company)
                print(f"Company: {company[0]}. Number of vacancies: {cursor.fetchall()[0][0]} ")

    def get_all_vacancies(self):
        """
        gets a list of all vacancies with the company name,
        vacancy name and salary, and a link to the vacancy.
        """
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM vacancies")
            for vacancy in cursor.fetchall():
                self.show_vacancy(vacancy)

    def get_avg_salary(self) -> int:
        """
        receives an average salary for vacancies.
        :return: average salary for vacancies.
        """
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT salary FROM vacancies")
            salaries = cursor.fetchall()
            return round(sum(map(sum, salaries)) / len(salaries))

    def get_vacancies_with_higher_salary(self):
        """
        Gets a list of all vacancies whose salary is above the average for all vacancies.
        :return: list of all vacancies whose salary is above the average for all vacancies
        """
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM vacancies WHERE salary>%s", [self.get_avg_salary()])
            for vacancy in cursor.fetchall():
                self.show_vacancy(vacancy)

    def get_vacancies_with_keyword(self, *keyword):
        """
        gets a list of all jobs whose title contains the words passed to the method, for example "python".
        :param keyword:
        :return: list of all jobs whose title contains the words passed to the method
        """
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM vacancies WHERE position(%s in description)>0", keyword)
            for vacancy in cursor.fetchall():
                self.show_vacancy(vacancy)

    @staticmethod
    def show_vacancy(vacancy: tuple):
        _, description, employer, experience, salary, url = vacancy
        print(f"\nVacancy: {description}\n"
              f"Employer {employer}\n"
              f"Experience {experience}\n"
              f"Salary {salary if salary else 'No info'}\n"
              f"URL {url}")

