# Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# В этом случае можно пропустить совсем тривиальные (т.е. задачу 1 или 2 тут точно решать не имеет смысла) - исходите из уровня группы и студента.


#11 - Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
# *******************************************************************
# было:
n = 5
li = []
for i in range (0, n):
    li.append((-3)**i)
    
print(li)

# *******************************************************************
# стало:
n = 5
li = [(-3)**i for i in range(n)]
print(li)