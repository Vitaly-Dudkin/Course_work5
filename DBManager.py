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
        self.create_table_employers()

    def create_table_employers(self):
        with self.conn.cursor() as cursor:
            cursor.execute(f'create table if not exists employers('
                           f'company_name varchar(200) PRIMARY KEY)')
        self.conn.commit()

    def create_table_vacancies(self, company):
        """
        create table for DATABASE vacancy if it doesn't exist
        :param company:
        """
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public'")
            lst = [i[0] for i in cursor.fetchall() if i != 'employers']
            if company not in lst:
                cursor.execute(f'create table {company}(id serial PRIMARY KEY,'
                               f'description text,'
                               f'employer varchar(50),'
                               f'experience varchar(30),'
                               f'salary int,'
                               f'url varchar(100))')

                cursor.execute(f"insert into employers (company_name) values ('{company}');")
                cursor.execute(f'alter table {company} '
                               f'add constraint fk_{company}_employer foreign key (employer) references employers(company_name);')

            self.conn.commit()

    def save_vacancies(self, vacancies: list[dict]):
        """
        save vacancies to the appropriate table,
        :param vacancies:
        """
        with self.conn.cursor() as cursor:
            for vacancy in vacancies:
                self.create_table_vacancies(vacancy['employer'].lower())
                cursor.execute(
                    f'insert into {vacancy["employer"].lower()}(description, '
                    f'employer, experience, salary, url) values(%s,%s,%s,%s,%s)',
                    (vacancy['description'], vacancy['employer'].lower(), vacancy['experience'],
                     vacancy['salary'], vacancy['url']))
        self.conn.commit()

    def get_companies_and_vacancies_count(self):
        """
        print a list of all companies and the number of vacancies
        for each company.
        """
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public'")
            for company in cursor.fetchall():
                cursor.execute(f'SELECT count(*) FROM {company[0]}')
                print(f'Company: {company[0].capitalize()} Vacancies: {cursor.fetchall()[0][0]}')

    def get_all_vacancies(self):
        """
        gets a list of all vacancies with the company name,
        vacancy name and salary, and a link to the vacancy.
        """
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public'")
            for company in cursor.fetchall():
                cursor.execute(f'SELECT * FROM {company[0]}')
                self.get_vacancies(cursor.fetchall())

    def get_vacancies(self, vacancy: list):
        for info_vacancy in vacancy:
            print(f'Name vacancy: {info_vacancy[1]}\n'
                  f'Name company: {info_vacancy[2]}\n'
                  f'Experience: {info_vacancy[3]}\n'
                  f'Salary: {info_vacancy[4]}\n'
                  f'url: {info_vacancy[5]}\n')

    def get_avg_salary(self):
        """
        receives an average salary for vacancies.
        :return: average salary for vacancies.
        """
        with self.conn.cursor() as cursor:
            total = 0
            count = 0
            cursor.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public'")
            for company in cursor.fetchall():
                cursor.execute(f'SELECT salary, description FROM {company[0]}')
                for i in cursor.fetchall():
                    if i[0] != 'Null':
                        total += float(i[0])
                        count += 1
            # print(f'Average Salary: {total / count:0.0f}')
            return round(total / count)

    def get_vacancies_with_higher_salary(self):
        """
        Gets a list of all vacancies whose salary is above the average for all vacancies.
        :return: list of all vacancies whose salary is above the average for all vacancies
        """

        lst = []
        salary = self.get_avg_salary()
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public'")
            for company in cursor.fetchall():
                cursor.execute(f'SELECT description from {company[0]} where salary > {salary}')
                for i in cursor.fetchall():
                    if i[0] not in lst:
                        lst.append(i[0])
        return '\n'.join(lst)

    def get_vacancies_with_keyword(self, keyword):
        """
        gets a list of all jobs whose title contains the words passed to the method, for example "python".
        :param keyword:
        :return: list of all jobs whose title contains the words passed to the method
        """
        lst = []
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='public'")
            for company in cursor.fetchall():
                cursor.execute(f'SELECT description from {company[0]}')
                for i in cursor.fetchall():
                    if keyword in i[0] and i[0] not in lst:
                        lst.append(i[0])
        return '\n'.join(lst)


test = DBManager()
# test.get_companies_and_vacancies_count()
