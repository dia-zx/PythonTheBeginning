#Реализуйте алгоритм перемешивания списка.

from random import  randint

def mix(L):
    for i in range(len(L)*2):
        SwapList(L, randint(0, len(L)-1), randint(0, len(L)-1))
    return L

#перемещение двух элементов списка
def SwapList(list, i1, i2):
    temp = list[i1]
    list[i1] = list[i2]
    list[i2] = temp


s = [10, 25, 96, 45, 3, 21]
print(mix(s))