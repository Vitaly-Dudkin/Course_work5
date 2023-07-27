import requests
from pprint import pprint


class Parser:
    """
    The Parser class is designed to get job vacancies
    from the hh.ru website based on specified
    keywords and company names.
    """
    def get_vacancies(self, name_companies: list[str], keywords: list[str]) -> list[dict]:
        words = '+'.join(keywords)
        lst = []
        employers_id = self.get_employer(name_companies)
        for i in employers_id:
            url = f'https://api.hh.ru/vacancies?per_page=15&employer_id={i["id"]}&text={words}'
            response = requests.get(url).json()
            if response['items']:
                for j in response['items']:
                    lst.append(self.parse_vacancies(j, i['company']))
        return lst

    def get_employer(self, name_companies: list[str]) -> list[dict]:
        employer_id = []
        for name in name_companies:
            url = f'https://api.hh.ru/employers?text={name}&only_with_vacancies=True'
            response = requests.get(url).json()
            for id_company in response['items']:
                employer_id.append({'company': name, 'id': id_company['id']})
        return employer_id

    def parse_vacancies(self, vacancy: dict, company: str) -> dict:
        employer = company
        description = vacancy['name']
        salary = self.salary(vacancy['salary'])
        url = vacancy['alternate_url']
        experience = vacancy['experience']['name']
        vacancy = {'employer': employer,
                   'description': description,
                   'salary': salary,
                   'url': url,
                   'experience': experience}
        return vacancy

    def salary(self, salary: dict | None):
        if salary:
            if salary['to'] and salary['from']:
                return (salary['from'] + salary['to']) / 2
            elif salary['to']:
                return salary['to']
            else:
                return salary['from']
        else:
            return 0


test = Parser()

pprint(test.get_vacancies(['Yandex'], []))