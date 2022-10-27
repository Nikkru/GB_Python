# найти мексимальную возрастающую последовательность чисел в списке

list1 = [1,5,2,3,4,6,1,7]
list2 = [1,5,2,3,4,7,1]
list3 = [1,5,3,0,4,7,0,8,9,10]

def seaching(L):
    list_tnp = []
    list_ind = []
    for i in L:
        j = min(L)
        print(f'min {j}')
        ind = L.index(j)
        print(f'ind {ind}')
        while j+1 in L:
            j+=1
        list_tnp.append(f'{min(L)} - {j}')
        list_ind.append(j - min(L))
        print(f'{min(L)} - {j}')
        L.pop(ind)
        print(L)
    print(list_tnp)
    print(list_ind)
    print(f'{list_tnp[list_ind.index(max(list_ind))]}')

# seaching(list1)
# seaching(list2)
seaching(list3)
