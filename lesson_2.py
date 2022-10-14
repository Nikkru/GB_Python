# task 2

N = int(input("enter a number of iterations: "))
a = -3
A = [1]
A.append(a)
print(A)
for i in range(N - 2):
    b = A[-1] * a
    A.append(b)
print(A)