# Задача 1 Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
'''*Пример:*

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

list_N = [1, 2, 4, 6, 45, 32, 45, 88]

def sum_odd_elemente(list_1):
    odd_positions = []
    sum = 0
    for i in range(len(list_1)):
        if i == 1:
            odd_positions.append(list_1[i])
        elif i % 2 != 0:
            sum += list_1[i]
            odd_positions.append(list_1[i])
    string_odd_positions = str(odd_positions).strip('[]')
    print(f"на нечетных позициях элементы {string_odd_positions}, ответ: {sum}")

sum_odd_elemente(list_N)