# Задача 1 Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
'''*Пример:*

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

# list_N = [1, 2, 4, 6, 45, 32, 45, 88]
#
# def sum_odd_elemente(list_1):
#     odd_positions = []
#     sum = 0
#     for i in range(len(list_1)):
#         if i == 1:
#             odd_positions.append(list_1[i])
#         elif i % 2 != 0:
#             sum += list_1[i]
#             odd_positions.append(list_1[i])
#     string_odd_positions = str(odd_positions).strip('[]')
#     print(f"на нечетных позициях элементы {string_odd_positions}, ответ: {sum}")
#
# sum_odd_elemente(list_N)

# Задача 2.
# Напишите программу,
# которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
'''
*Пример:*

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''
# list_N = [2, 3, 4, 10, 11, 12, 13]
#
# def list_sum(list_n):
#     list_sum = []
#     sum = 0
#     for i in range(int(len(list_n)/2)):
#         sum = list_n[i] + list_n[-1*(i+1)]
#         list_sum.append(sum)
#     print(list_sum)
#
# list_sum(list_N)

# Задача 3.
# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
'''
*Пример:*

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''
list_N = [1.1, 1.2, 3.1, 5, 10.01, 0.0002]

def subtraction_max_min_fractional(list_n):
    list_tmp = []
    list_tmp_char = []
    list_int = []
    maximum = 0
    minimum = 0
    for i in range(len(list_n)):
        list_tmp.append(str(list_n[i]))
        list_tmp_char.append(list(list_tmp[i]))
    for j in range(len(list_n)):
       if '.' in list_tmp[j]:
           index = list_tmp[j].index('.')
           del list_tmp_char[j][:index+1]
       else:
           list_tmp_char[j] = ['0']
           index = 0
    maximum = len(list_tmp_char[0])
    for x in list_tmp_char:
        if len(x) > maximum:
            maximum = len(x)
    for x in list_tmp_char:
        while len(x) != maximum:
            x.append('0')
        list_int.append(int(''.join(x)))
    maximum = list_int[0]
    minimum = list_int[-1]
    for x in list_int:
        if x > maximum:
            maximum = x
    for x in list_int:
        if 0 < x < minimum:
            minimum = x
    resultat = f'0,{maximum - minimum}'
    print(resultat)

subtraction_max_min_fractional(list_N)