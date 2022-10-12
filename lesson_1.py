try:    
    a = int(input("first number, please "))
    b = int(input("second number, please "))
    if (a * a == b) or (b & b == a):
        print("yes")
    else:
        print("no")
except:
    print("incoorect input")