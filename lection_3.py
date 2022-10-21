path = '/Users/nikkru/Yandex.Disk.localized/GB_Python/file with numbers.txt'
f = open(path, 'r')
data = f.read() + ' '
print(data)
print(type(data))
f.close()

list_string =data
numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]
#     print(numbers)
# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e ** 2))
# print(out)
#
def select(f, col):
    return [f(x) for  x in col]

def where(f, col):
    return [x for x in col if f(x)]

print(list_string)
list_string = list_string.split()
print(list_string)

# res = select(int, list_string)
res = map(int, list_string)
# res = where(lambda x: not x%2, res)
res = list(filter(lambda x: not x%2, res))
# res = select(lambda x: (x, x**2), res)
res = list(map(lambda x: (x, x**2), res))
print(res)

# li = [x for x in range(1, 20)] # создаем список чисел
# print(li)
# li = list(map(lambda  x: x+10, li))
# print(li)
#
# data_2 = list(map(int, input("enter a numbers: ").split()))
# print(data_2)

data_2 = map(int, '1 2 3 44 55 6'.split())
for e in data_2: # итератор - можно сделать итерацию только один раз!
    print(e)

data_3 = [x for x in range(1, 10)]
res = list(filter(lambda x: not x%2, data_3))
print(res)