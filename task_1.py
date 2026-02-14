class Case:
    def __init__(self, test_case_id, name, step_description, expected_result):
        self.test_case_id = test_case_id
        self.name = name
        self.step_description = step_description
        self.expected_result = expected_result

    def print_test_case_info(self):
        print(f"ID тест-кейса:  {self.test_case_id}"
              f"\nНазвание: {self.name}"
              f"\nОписание шага: {self.step_description}"
              f"\nОжидаемый результат: {self.expected_result}")

class ExtendedCase(Case):
    def __init__(self, test_case_id, name, step_description, expected_result, precondition, environment):
        super().__init__(test_case_id, name, step_description, expected_result)
        self.precondition = precondition
        self.environment = environment
#исправить метод - убрать то, что есть в родительском классе. Удаляю, добавлю ссылку вызовом метода через super на родителя
    def print_test_case_info(self):
        print(f"\nПредусловие:  {self.precondition}"
              f"\nОкружение: {self.environment}")
        super().print_test_case_info()  # должен вывести строки по методу родителя
casе = ExtendedCase('1', 'Наличие кнопки Принять', 
                    '1. Открыть вкладку приёма документов ' 
                    '2. Проверить наличие кнопки ', 
                    'Кнопка доступна', 
                    'Открыть сервис', 
                    'Яндекс Браузер')

casе.print_test_case_info()