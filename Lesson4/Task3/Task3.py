#Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k. 
# 
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


def solution(k):
    st = ""
    for i in range(k, -1, -1):
        r = randint(0, 100)
        if r == 0:
            continue
        if len(st):
            st += " + "
        if i == 0:
            st += str(r)
            continue
        if i == 1:
            st += str(r) + "*X"
            continue
        st += str(r) + "*X^" + str(i)
    st += " = 0"
    return st


f = open("file.txt","w")
f.write(solution(5))
f.close()

print(solution(5))