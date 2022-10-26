# найти мексимальную возрастающую последовательность чисел в списке

list1 = [1,5,2,3,4,6,1,7]
list2 = [1,5,2,3,4,7,1]

def min_num(L):
    print(min(L))
    return min(L)

def seaching(L):
    j = min(L)
    while j+1 in L:
        j+=1
    print(f'{min(L)} - {j}')
seaching(list1)
seaching(list2)
