"""
Модуль взаимодействия пользователя с программой - интерфейс
"""


def view_data(data, title):
    print(f'{title} = {data}')


def get_value():
    return int(input('value: '))