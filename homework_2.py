# Задача 1. Напишите программу,
# которая принимает на вход вещественное или целое число и показывает сумму его цифр.
# Через строку нельзя решать.
# *Пример:*
'''
- 6782 -> 23
- 0,56 -> 11
'''
'''
Честно говоря, мозг сломал пока нашел решение. 
Неделю убил. 
Раз пять бросал. 
Понимаю, что надо бы все пригладить, но серое вещество на нуле.
'''

# sum_numbers_number = 0
# number_decimal_places = 1
# try:
#     n = float(input("enter a number, please: "))
#     fractional_part_n = n - int(n)
#
#     while n - round(n, number_decimal_places) != 0:
#         number_decimal_places += 1
#
#     int_frac_n = round(fractional_part_n, number_decimal_places) * (10 ** number_decimal_places)
#
#     while int(n) > 0:
#         sum_numbers_number = sum_numbers_number + n % 10
#         n //= 10
#
#     while int(int_frac_n) > 0:
#         sum_numbers_number = sum_numbers_number + int_frac_n % 10
#         int_frac_n //= 10
#     print(int(sum_numbers_number))
# except: print("Please, enter correct number!")



# Задача 2. Напишите программу,
# которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.
# *Пример:*
'''
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''
list_n = [1]
list_N = []
try:
    N = int(input("enter a number, please: "))
    for i in range(N):
        i += 1
        list_n.append(list_n[i - 1] * i)
        list_N.append(list_n[-1])
    print(list_N)
except: print("Please, enter correct number!")

# Задача 3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# Нельзя юзать find или count.