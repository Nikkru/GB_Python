"""
Модель данных с логикой
"""
x = 0
y = 0


def init(a, b):
    global x
    global y
    x = a
    y = b


def calculation():
    return x + y