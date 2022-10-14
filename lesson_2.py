# # task 2
#
# N = int(input("enter a number of iterations: "))
# a = -3
# A = [1]
# A.append(a)
# print(A)
# for i in range(N - 2):
#     b = A[-1] * a
#     A.append(b)
# print(A)

# task 3

# M = {}
# n = int(input("enter a integer: "))
# for i in range(1, n+1):
#     M[i] = 3*i + 1
#
#     i += 1
# print(M)

# task 4

str_1 = input("Wright some words here, please: ")
str_2 = input("Wright some words here, please: ")
list_1 = str_1.split()
list_2 = str_2.split()
count_repeat = 0
for i in range(len(list_1)):
    if list_1[i] in list_2:
        count_repeat += 1
    i += 1
print(count_repeat)
