#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

# Для определенности считаем что числа целые..
def ToBinary(d):
    res = ""
    if d<0:
        sgn = -1 #знак числа
        d = -d
    else:
        sgn = 1
        
    while d != 0:
        if d & 1:
            res = "1" + res
        else:
            res = "0" + res
        d = d >> 1
    if sgn<0:
        res = "-" + res
    return res

print(ToBinary(-1))