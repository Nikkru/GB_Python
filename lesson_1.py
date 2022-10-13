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

# lesson 1 task 2
# N = int(input("enter an integer, please: "))
# print(list(range(-N, N+1)))
'''
for i in range(-N, N + 1):
    print(i, end="; ")
'''

# lesson 1 task 3
# try:
#     float_num = float(input("enter a float number, please: "))
#     if (float_num % 1 != 0):
#         print(int(float_num * 10 % 10))
#     else:
#         print("NO")
# except:
#     print("incorrect value, sorry\n")


# lesson 1 task 4
# try:
#  x = int(input("Enter an integer, please: "))
#  if ((x % 5 == x % 10 == 0) or x % 15 == 0) and x % 30 != 0:
#      print("x - our number\n")
#  else:
#      print("x - don't our number")
# except:
#     print("sorry, incorrect value was inputed")