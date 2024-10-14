from src.vacancy_api import HH
from src.vacancy import Vacancy
from src.vacancy_json import HHVacancy
from src.utils import top_vacancy, filter_vacancy


def user_interaction():
    search_query = input("Введите запрос: ")
    hh = HH()
    city_search = input("Введите город: ")
    hh.load_vacancies(search_query)
    filter_words = input("Введите ключевые слова для вакансий: ").split()
    salary = int(input("Введите зарплату: "))
    top_n = input("Введите количество вакансий: ")
    vacancy = Vacancy(search_query, city_search, salary)
    vacancy.reform_file(hh.vacancies)
    res_city = vacancy.filter_city()
    res_salary = vacancy.__le__(salary, res_city)
    result_fil_words = filter_vacancy(res_salary, filter_words)
    sd = HHVacancy()
    sd.safe_vacancy(result_fil_words)
    result_of_top = top_vacancy(top_n, result_fil_words)
    return result_of_top

print("Все что было найдено по запросу.")
print(user_interaction())
