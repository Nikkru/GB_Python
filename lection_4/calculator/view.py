"""
Модуль взаимодействия пользователя с программой - интерфейс
"""


def view_data(data):
    print(f'result = {data}')


def get_value():
    return int(input('value: '))