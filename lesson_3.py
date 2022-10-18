# (1+1/N)**N

def posl(N):
    sum = 0
    for _ in range(N):
        sum = sum + (1 + 1 / N) ** N
        N = (1+1/N)**N
    return sum

try:
    n = int(input("enter a number, please: "))
    print(posl(n))
except:
    print("Please, enter number")