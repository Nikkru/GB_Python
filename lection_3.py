path = '/Users/nikkru/Yandex.Disk.localized/GB_Python/file with numbers.txt'
f = open(path, 'r')
data = f.read() + ' '
print(data)
print(type(data))
f.close()

numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]
    print(numbers)
out = []
for e in numbers:
    if not e % 2:
        out.append((e, e ** 2))
print(out)