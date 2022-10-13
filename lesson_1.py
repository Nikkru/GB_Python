# # ## lesson 1 task 1
# try:
#     a = int(input("first number, please "))
#     b = int(input("second number, please "))
#     if (a * a == b) or (b & b == a):
#         print("yes")
#     else:
#         print("no")
# except:
#     print("incorrect input")

# # homework 1 task 2
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

# # lesson 1 task 2
# N = int(input("enter an integer, please: "))
# for i in range(-N, N + 1):
#     print(i, end="; ")

# # lesson 1 task 3
try:
    floatNum = float(input("enter a float number, please: "))
    # print(floatNum)
except:
    print("incorrect value, sorry\n")

str_float = str(floatNum)
list_float = list(str_float)
# print(list_float)

i = 1
number_after_point = ""

while i < len(list_float):
    if list_float[i] == '.':
        # print(list_float[i + 1])
        number_after_point = str(list_float[i + 1])
    i += 1
if number_after_point == "0":
    print("No")
else:
    print(number_after_point)