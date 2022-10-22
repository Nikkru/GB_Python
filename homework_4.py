# задача 1.
# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

try:
    N = int(input("enter a natural number: "))
    # if N <= 0:
    #     N = ""
except:
    print("Sorry, incorrect input")
try:
    tmp = N + 10
except:
    print("a negative number or zero is not a natural")


def search_natural_divisors(n):
   divisor = 2
   natural_divisors = []
   while divisor * divisor <= n:
       while not n % divisor:
           natural_divisors.append(divisor)
           n //= divisor
       divisor += 1
   if n > 1:
       natural_divisors.append(n)
   print(natural_divisors)
search_natural_divisors(N)
