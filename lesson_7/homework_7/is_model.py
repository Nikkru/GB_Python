import json
import csv

first_name = ''
last_name = ''
employee = ''
fone_numbers = ''
birthdate = ''
full_name = first_name + ' ' + last_name
salary: int = 0
work_experiance: int = 0
date_employment = ''
new_person = ('first_name',
              'last_name',
              'employee',
              'birthdate',
              'date_employment',
              'work_experiance',
              'salary',
              'fone_numbers')

is_ = {'employee': employee,
                   'first_name': first_name,
                   'last_name': last_name,
                   'fone_numbers': fone_numbers,
                   'birthdate': birthdate,
                   'salary': salary,
                   'date_employment': date_employment,
                   'work_experiance': work_experiance}


def add_person_in_base():
    first_name = input('имя: ')
    last_name = input('фамилия: ')
    employee = input('должность: ')
    birthdate = input('дата рождения: ')
    date_employment = input('дата приема на работу: ')
    work_experiance = int(input('стаж: '))
    fone_number = input('номер телефона: ')
    salary = int(input('оклад: '))

    fone_numbers = list(fone_number.split(','))
    full_name = first_name + ' ' + last_name

    new_man = {'employee': employee,
                           'first_name': first_name,
                           'last_name': last_name,
                           'fone_numbers': fone_numbers,
                           'birthdate': birthdate,
                           'salary': salary,
                           'date_employment': date_employment,
                           'work_experiance': work_experiance}
    is_.update({full_name: new_man})
    with open('is_json.json', 'w') as file:
        json.dump(is_, file, indent=6)
    print(is_)


def pint_is(dict):
    for key in dict:
        print(key)


def dell_person_from_base(full_name):
    is_.pop(full_name)
    print(f'{full_name} is deleted from IS now.\n')


def write_json(employees: list):
    with open(Path.cwd() / 'database02.json', 'w', encoding='utf-8') as fout:
        for employee in employees:
            fout.write(json.dumps(employee) + '\n')
