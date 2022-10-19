sp = []
sp.append(True)
sp = sp + [1213, "абба", 54654, [1,2,3,5] ]
print(sp)
sp.insert(1,999)
print("after insert ",sp)

print(sp[-1][-1])

a = sp.pop(-1)
print("after pop ", a)

a.remove(2)
print("after remove  ", a)
for i in a: print(i)

mas_2dim= [] 
for i in range(5):
    temp = []
    for j in range(5):
        temp.append(i+j)
    mas_2dim.append(temp)

for i in range(len(mas_2dim)):
    print(mas_2dim[i])