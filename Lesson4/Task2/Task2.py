#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности
#Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

#вариант 1
def Translate(li):
    return list(set(li))

#вариант 2
def Translate2(li):
    res = []
    for item in li:
        if item in res:
            continue
        res.append(item)
    return res

print(Translate2([1, 2, 3, 5, 1, 5, 3, 10]))
print(Translate([1, 2, 3, 5, 1, 5, 3, 10]))