import requests


class Parser:
    pass
    # def get_vacancies(self, name_companies: list[str], keywords: list[str]) -> list[dict]:
    #     words = '+'.join(keywords)
    #     lst = []
    #     employers_id = self.get_employer(name_companies)
    #     for i in employers_id:
    #         url = f'https://api.hh.ru/vacancies?per_page=15&employer_id={i["id"]}&text={words}'
    #         response = requests.get(url).json()
    #         if response['items']:
    #             # print(response['items'])
    #             for j in response['items']:
    #                 lst.append(self.parse_vacancies(j, i['company']))
    #     return lst
    #
    # def get_employer(self, name_companies: list[str]) -> list[dict]:
    #     employer_id = []
    #     for name in name_companies:
    #         url = f'https://api.hh.ru/employers?text={name}&only_with_vacancies=True'
    #         response = requests.get(url).json()
    #         for i in response['items']:
    #             employer_id.append({'company': name, 'id': i['id']})
    #     # print(employer_id)
    #     return employer_id
    #
    # def parse_vacancies(self, vacancy: dict, company: str) -> dict:
    #     employer = company
    #     # print(employer)
    #     description = vacancy['name']
    #     salary = self.salary(vacancy['salary'])
    #     url = vacancy['alternate_url']
    #     experience = vacancy['experience']['name']
    #     vacancy = {'employer': employer,
    #                'description': description,
    #                'salary': salary,
    #                'url': url,
    #                'experience': experience}
    #     return vacancy
    #
    # def salary(self, salary: dict | None):
    #     if salary:
    #         if salary['to']:
    #             return (salary['from'] + salary['to']) / 2
    #         else:
    #             return salary['from']
    #     else:
    #         return 'No info'

# test = Parser()
# employers = ['Yandex', 'Avito', 'Сбербанк']
# pprint(test.get_vacancies(employers, ['python']))
