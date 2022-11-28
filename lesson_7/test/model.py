import json


def json_file_write(data, json_data):
    with open(json_data, 'w') as file:
        json.dump(data, file, indent=3)


def get_add_new_employee():
    print("\n" + "-" * 20)
    print("Введите данные сотрудника: ")
    new_employee = {}
    temp = {}
    temp["first_name"] = input("имя: ")
    temp["last_name"] = input("фамилия: ")
    temp["position"] = input("должность: ")
    temp["phone_number"] = input("номер телефона: ")
    temp["salary"] = float(input("оклад: "))
    key = f'{temp["first_name"]} {temp["last_name"]}'
    new_employee.update({key: temp})
    print(new_employee)
    return new_employee


def read_json_in_data(json_) -> list:
    with open(json_, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def get_key(dictonary_):
    keys = sorted(dictonary_)
    n = 0
    print('\n')
    for key in keys:
        n += 1
        print(f'{n}. {key}')


def get_value(dictionary_, key_1, key_2):
    print(f'{key_1} {key_2}: {dictionary_[key_1][key_2]}')


def get_key1_by_value2(dictionary_, value_2, finding):
    list_ = []
    for items in dictionary_.items():
        if items(value_2) == finding:
            list_.append(items.keys())
    print(list_)

