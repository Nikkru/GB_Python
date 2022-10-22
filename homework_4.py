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

N = [0, 23, 34, 43, 56, 54, 67, 1, 2, 3, 412, 2, 45, 67, 98, 9, 33, 44, 55, 32, 23]

def counter_not_repeat(n):
    tmp_set = set()
    tmp_list = []
    for x in n:
        if tmp_set.add(x):
            tmp_set.add(x)
    tmp_list = list(tmp_set)
    print(tmp_list)
counter_not_repeat(N)