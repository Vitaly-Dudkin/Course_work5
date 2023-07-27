from HH import Parser
from DBManager import DBManager


def main():
    pass
    # vacancies = parser.get_vacancies(['Yandex', 'Avito', 'Сбербанк'], ['python', 'SQL'])
    # dbmanger.save_vacancies(vacancies)
    # dbmanger.get_companies_and_vacancies_count()
    dbmanger.save_vacancies(parser.get_vacancies(
        ['МТС'],
        []))
    # 'OZON', 'Билайн', 'ВКонтакте', 'Тинкофф', 'Yandex', 'Avito', 'Сбербанк',], ['']))
    # print(parser.get_vacancies(['Мегафон'],[]))
    # print(dbmanger.get_vacancies_with_keyword('Менеджер'))


if __name__ == '__main__':
    parser = Parser()
    dbmanger = DBManager()
    main()
