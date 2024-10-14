from abc import ABC, abstractmethod
import json
import os.path


class JSONVacancy(ABC):

    @abstractmethod
    def safe_vacancy(self, stock_list):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class HHVacancy(JSONVacancy):

    def __init__(self):
        self.file_name_save = 'data/suitable_vacancies.json'

    def safe_vacancy(self, stock_list):
        if stock_list is None:
            print("Вакансий с такими критериями нету ,соси")
        elif stock_list is not None:
            if os.path.exists(self.file_name_save):
                with open(self.file_name_save, 'r', encoding="utf-8") as file:
                    data = json.load(file)
                for i in stock_list:
                    if i not in data:
                        data.append(i)
                with open(self.file_name_save, 'w', encoding="utf-8") as file:
                    json.dump(data, file, indent=4,
                              ensure_ascii=False)
            else:
                with open(self.file_name_save, 'w', encoding="utf-8") as file:
                    json.dump(stock_list, file, indent=4, ensure_ascii=False)

    def delete_vacancy(self):
        pass
