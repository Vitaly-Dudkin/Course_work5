from HH import Parser
from DBManager import DBManager


def main():
    while True:
        match input("\n>>> ").split():
            case "help", :
                print("\nCommand number | Description"
                      "\n      (1)      | Load vacancies"
                      "\n      (2)      | Get list of employers"
                      "\n      (3)      | Get all vacancies"
                      "\n      (4)      | Get average salary"
                      "\n      (5)      | Get all vacancies with higher salary"
                      "\n      (6)      | Get all vacancies with keyword"
                      "\n     quit      | Close an application")
            case "1", :
                dbmanger.save_vacancies(
                    parser.get_vacancies(["OZON", "Билайн", "ВКонтакте", "Тинкофф", "Yandex", "Avito",
                                          "Сбербанк", "Wildberries", "Касперский", "Росатом"], []))
                print(f'Vacancies successfully loaded')
            case "2", :
                dbmanger.get_companies_and_vacancies_count()

            case "3", :
                dbmanger.get_all_vacancies()

            case "4", :
                print(dbmanger.get_avg_salary())

            case "5", :
                dbmanger.get_vacancies_with_higher_salary()

            case "6", :
                dbmanger.get_vacancies_with_keyword("python")

            case "quit", :
                dbmanger.conn.close()
                return 0

            case _:
                print(f"Wrong command")


if __name__ == "__main__":
    parser = Parser()
    dbmanger = DBManager()
    main()
