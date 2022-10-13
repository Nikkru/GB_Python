# try:
#     a = int(input("first number, please "))
#     b = int(input("second number, please "))
#     if (a * a == b) or (b & b == a):
#         print("yes")
#     else:
#         print("no")
# except:
#     print("incorrect input")

weekends = [6, 7]
weekdays = range(1, 8)
for i in weekdays:
    print(i, end=";")
day = int(input("day of weeks, please: "))
if day in weekends:
    print("it is a weekend")
elif day in weekdays:
    print("it is a workday")
else:
    print("incorrect value, sorry")
