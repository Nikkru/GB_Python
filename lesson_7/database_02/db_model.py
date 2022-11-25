import csv
import json


def read_csv() -> list:
    employees = []
    with open('database.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = {}
            temp["id"] = int(row[0])
            temp["last_name"] = row[1]
            temp["first_name"] = row[2]
            temp["position"] = row[3]
            temp["phone_number"] = row[4]
            temp["salary"] = float(row[5])
            employees.append(temp)
    return employees


def get_key(key):
    list_key = ["id", "last_name", "first_name", "position", "phone_number", "salary"]
    return list_key[key]


def find_employee(full_list, key, search_data):
    for employee in full_list:
        if search_data in employee[key]:
            return employee


def del_employee(full_list, search_data, key="last_name"):
    for i in range(len(full_list)):
        if search_data in full_list[i][key]:
            full_list.pop(i)
            return full_list


def replacement_employee(full_list, last_name, new_data, key="last_name"):
    for i in range(len(full_list)):
        if last_name in full_list[i][key]:
            full_list[i]["last_name"] = new_data[0]["last_name"]
            full_list[i]["first_name"] = new_data[0]["first_name"]
            full_list[i]["position"] = new_data[0]["position"]
            full_list[i]["phone_number"] = new_data[0]["phone_number"]
            full_list[i]["salary"] = new_data[0]["salary"]
            return full_list


def get_list_empl_by_pos(full_list, search_pos):
    found_list = []
    for employee in full_list:
        if search_pos == employee["position"]:
            found_list.append(employee)
    return found_list


def get_last_id():
    with open('database.csv', 'rb') as file:
        file.seek(-300, 2)
        last_str = file.readlines()[-1].decode('utf-8')
        last_id = ''
        for char in last_str:
            if char != ',':
                last_id += char
            else: break
    return int(last_id)


def export_data_json(data) -> list:
    with open('database.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, sort_keys=True, indent=6)


def write_csv(employees: list):
    with open('database.csv', 'w', encoding='utf-8', newline="") as fout:
        csv_writer = csv.writer(fout)
        for employee in employees:
            csv_writer.writerow(employee.values())


def append_to_csv(last_id, data_new_employee):
    employees = read_csv()
    temp = {}
    temp["id"] = last_id + 1
    temp["last_name"] = data_new_employee[0]["last_name"]
    temp["first_name"] = data_new_employee[0]["first_name"]
    temp["position"] = data_new_employee[0]["position"]
    temp["phone_number"] = data_new_employee[0]["phone_number"]
    temp["salary"] = data_new_employee[0]["salary"]
    employees.append(temp)
    write_csv(employees)

def add_new_person(last_id, database):
    temp = {}
    temp["id"] = last_id + 1
    temp["last_name"] = temp[0]["last_name"]
    temp["first_name"] = temp[0]["first_name"]
    temp["position"] = temp[0]["position"]
    temp["phone_number"] = temp[0]["phone_number"]
    temp["salary"] = temp[0]["salary"]
    database.append(temp)


def add_to_database_json(json_file, data):
    with open(json_file, 'w') as file:
        json.dump(data, file)


def write_json(employees: list):
    with open('database02.json', 'w', encoding='utf-8') as fout:
        for employee in employees:
            fout.write(json.dumps(employee) + '\n')


def find_employees_by_salary_range(full_list, hi_sal, low_sal) -> list:
    found_list = []
    for employee in full_list:
        if low_sal < float(employee["salary"]) < hi_sal:
            found_list.append(employee)
    return found_list


def json_file_read(json_data):
    data = {}
    with open(json_data, 'r') as json_file:
        data = json.load(json_file)
    return data


def json_file_write(data, json_data):
    with open(json_data, 'w') as file:
        json.dump(data, file)