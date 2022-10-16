# Задача 1. Напишите программу,
# которая принимает на вход вещественное или целое число и показывает сумму его цифр.
# Через строку нельзя решать.
# *Пример:*
'''
- 6782 -> 23
- 0,56 -> 11
'''
s = 0
i = 1
listN = []
n = int(input("enter a number, please: "))
while n % 10 > 1:
    s = s + n % 10
    n //= 10
print(s)
# n = float(input("enter a number, please: "))
# while n % 10 != 0:
#     s = int(n % (10*i))
#     listN.append(s)
#     i *= 10
# print(listN)
#     n = n * 10
# print(n)
# while n / 10 > 10:
#     s += n % 10
#     n = n / 10
# print(s)
# while n * 10 < 0:
#     n = n * 10
#     s += 1
# print(n)
# print(s)

