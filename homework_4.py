# задача 1.
# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
#
# try:
#     N = int(input("enter a natural number: "))
#     # if N <= 0:
#     #     N = ""
# except:
#     print("Sorry, incorrect input")
# try:
#     tmp = N + 10
# except:
#     print("a negative number or zero is not a natural")
#
#
# def search_natural_divisors(n):
#    divisor = 2
#    natural_divisors = []
#    while divisor * divisor <= n:
#        while not n % divisor:
#            natural_divisors.append(divisor)
#            n //= divisor
#        divisor += 1
#    if n > 1:
#        natural_divisors.append(n)
#    print(natural_divisors)
# search_natural_divisors(N)

# задача 2 .
# Задайте последовательность чисел.
# Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
#
# N = [0, 23, 34, 43, 56, 54, 67, 1, 2, 3, 412, 2, 45, 67, 98, 9, 33, 44, 55, 32, 23]
# # ПЕРВЫЙ ВАРИАНТ через преобразование списка во множество
# def list_not_repeat(n):
#     tmp_set = set()
#     tmp_list = []
#     for x in n:
#         if tmp_set.add(x):
#             tmp_set.add(x)
#     tmp_list = list(tmp_set)
#     print(f'первый результат неповторяющихся значений {tmp_list}')
# print(f'исходный список - {N}')
# list_not_repeat(N)
#
# # ВТОРОЙ ВАРИАНТ через фильтрование списка
#
# def list_not_repeat_2(n):
#     tmp_list = [n[0]]
#     for i in range(1, len(n)):
#         for j in range(len(tmp_list)):
#             if n[i] == tmp_list[j]:
#                 break
#             elif j == len(tmp_list)-1:
#                 tmp_list.append(n[i])
#     print(f'второй результат неповторяющихся значений {tmp_list}')
# list_not_repeat_2(N)

# задача 3.
# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
'''
*Пример:*
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''
import random

K = int(input("enter a natural number: "))

def create_list_degrees():
    return [x for x in range(K + 1)]
def rndm_a():
    return  random.randint(1, 101)
def rndm_b():
    return  random.randint(0, 101)
def create_list_coef():
    return ([rndm_b()]+[rndm_a() for x in range(K)])
def create_list_degrees():
    list_tmp = [x for x in range(K+1)]

    return list_tmp
def create_dictionary(list1, list2):
    dictionary_degree_coef = {}
    for i in range(len(list1)):
        dictionary_degree_coef[list1[i]] = list2[-i]
    return dictionary_degree_coef

list_coef = create_list_coef()
list_degrees = create_list_degrees()
dict_coef = create_dictionary(list_degrees, list_coef)
print(create_list_degrees())
print(f'coef = {list_coef}')
print(dict_coef)

def create_polinom2(N, x):
    polinom = []
    for i in range(N, -1, -1):
        if i == 0:
            a = f'{x[i]}'
        elif i == 1:
            a = f'{x[i]}*x'
        elif x[i] == 0:
            break
        else:
            a = f'{x[i]}*x^{i}'
        polinom.append(a)
    return polinom
polinom = create_polinom2(K, dict_coef)
print(polinom)

def create_polinom_str(l):
    tmp = ('+'.join(l))
    tmp += "=0"
    return tmp

str_polinom = create_polinom_str(polinom)
print(str_polinom)
def write_file(N):
    with open('file43.txt', 'w') as data:
        data.write(N)

write_file(create_polinom_str(polinom))

