import json


def get_mode() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие: ")
    print("1. Найти сотрудника")
    print("2. Вывести список сотрудников по должности")
    print("3. Вевести список сотрудников по зарплате")
    print("4. Добавить нового сотрудника")
    print("5. Удалить сотрудника из базы")
    print("6. Обновить данные сотрудника")
    print("7. Сохранитиь данные в формате json")
    print("8. Сохранить данные в формате scv")
    print("9. Закончить работу")
    print("=" * 20 + "\n")
    return int(input("Введите номер необходимого действия: "))


def get_search_key():
    print("\n" + "-" * 20)
    print("Выберите вид поиска: ")
    print("1. id")
    print("2. Фамилия")
    print("3. Имя")
    print("4. Должность")
    print("5. Телефон")
    print("-" * 20 + "\n")
    return int(input("Введите номер поиска: ")) - 1


def get_search_empl(data):
    search_data = input("Введите " + data + " сотрудника: ")
    return search_data


def print_to_console_found_empl(found_empl):
    if found_empl == None:
        print("Данные не найдены")
    else:
        print(found_empl.values())


def get_search_by_position():
    search_position = input("Введите искомую должность: ")
    return search_position


def print_to_console_celection(found_list):
    if found_list == None:
        print("Данные не найдены")
    else:
        for i in range(len(found_list)):
            print(found_list[i])


def get_search_by_salary():
    search_salary = input("Введите диапазон окладов: ")
    return search_salary


def get_salary_range():
    hi_salary = input("Введите верхнюю границу: ")
    low_salary = input("Введите нижнюю границу: ")
    return [hi_salary, low_salary]


def get_add_new_employee():
    print("\n" + "-" * 20)
    print("Введите данные сотрудника: ")
    new_employee = []
    temp = {}
    temp["last_name"] = input("фамилия: ")
    temp["first_name"] = input("имя: ")
    temp["position"] = input("должность: ")
    temp["phone_number"] = input("номер телефона: ")
    temp["salary"] = float(input("оклад: "))
    new_employee.append(temp)
    return new_employee