# # homework 1 task 1
# weekends = [6, 7]
# weekdays = range(1, 8)
# for i in weekdays:
#     print(i, end=";")
# day = int(input("\nday of weeks, please: "))
# if day in weekends:
#     print("it is a weekend\n")
# elif day in weekdays:
#     print("it is a workday\n")
# else:
#     print("incorrect value, sorry\n")

# task 2
# задача 2. Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# !(X or Y or Z) = !X and !Y and !Z

# a = 5
# b = 6
# res = a == b
#
# print(str(res))
# for x in [True, False]:
#   print(not(x or False or False) == True)

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            if not (x or y or z) == (not x and not y and not z):
                print('not ( ', x, ' or ', y, ' or ', z, ' == (not ', x,  ' and not ', y, ' and not ', z, ')')

'''
задача 3. 
Напишите программу, которая принимает на вход координаты точки (X и Y), 
и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
*Пример:*

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
'''
# x = int(input("Enter number for x coordinat: "))
# y = int(input("Enter number for y coordinat: "))
# if x > 0 and y > 0:
#     print(1)
# elif x > 0 and y < 0:
#     print(4)
# elif x < 0 and y < 0:
#     print(3)
# elif x < 0 and y > 0:
#     print(2)
# elif x == 0 and y > 0:
#     print("y")
# elif x > 0 and y == 0:
#     print("x")
# elif x < 0 and y == 0:
#     print("-y")
# elif x == 0 and y < 0:
#     print("-x")
# else:
#     print("0:0")