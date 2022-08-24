#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

#Пример:
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

#Для определенности считаем n >= 0
def FibList(n):
    last = 1
    cur = 0
    li = [0,]
    for i in range(n):
        temp = cur
        cur += last
        last = temp 
        li.append(cur)
    #сконструируем отрицательную половину
    li2 = []
    for i in range(1, len(li)):
        if i % 2:
            li2.append(li[i])
        else:
            li2.append(-li[i])
    li2.reverse()
    return li2 + li


print(FibList(8))