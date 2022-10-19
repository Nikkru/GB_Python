# (1+1/N)**N

# def posl(N):
#     sum = 0
#     for _ in range(N):
#         sum = sum + (1 + 1 / N) ** N
#         N = (1+1/N)**N
#     return sum
#
# try:
#     n = int(input("enter a number, please: "))
#     print(posl(n))
# except:
#     print("Please, enter number")

# task 2

# list_base = ["2223", '0.3456', 'go ahead', "no sorry", '1234', '123']

# def looking_for_N(N, list_n):
#     count = 0
#     for i in list_n:
#         i = str(i)
#         if N in i:
#             print("yes")
#             count += 1
#     print(count)
# try:
#     n = input("Enter some word or number: ")
#     looking_for_N(n, list_base)
# except:
#     print("Enter correct text")

# task 3

list_A = ["abc", "bce", "abced", "abcd", "abcde", "abc"]

def looking_for_string(N, list_N):
    count = 0
    position = 0
    for i in range(len(list_N)):
        if list_N[i] == N and count == 0:
            count = 1
        elif list_N[i] == N and count == 1:
            position = i
            count = 2
    if count == 2:
        print(f'{N} incoming in list {list_N} with {position} position')
    else:
        print("-1")

n = input("enter some string: ")
looking_for_string(n, list_A)
