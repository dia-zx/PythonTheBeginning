# Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# В этом случае можно пропустить совсем тривиальные (т.е. задачу 1 или 2 тут точно решать не имеет смысла) - исходите из уровня группы и студента.


# 27. Строка содержит набор чисел. Показать большее и меньшее число
#Символ-разделитель - пробел

# *******************************************************************
# было:

def FindMinMax(s):
    li = s.split(' ')
    min = max = float(li[0])
    for i in range(1, len(li)):
        temp = float(li[i])
        if max < temp:
            max = temp
        if min > temp:
            min = temp
    return (min, max)


(_min, _max) = FindMinMax("2 7 -1 10 13.2 5.3")
print(f"min: {_min}")
print(f"max: {_max}")


# *******************************************************************
# стало:

def FindMinMax(s):
    li = list(map(float, s.split(' ')))
    _min = min(li)
    _max = max(li)
    return (_min, _max)


(_min, _max) = FindMinMax("2 7 -1 10 13.2 5.3")
print(f"min: {_min}")
print(f"max: {_max}")
