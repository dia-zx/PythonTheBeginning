# Даны два файла в каждом из которых находится запись многочлена.
# Сформировать файл содержащий сумму многочленов.


# разделяет на множители и убирает "= ...."
# "39*X^5 + 97*X^4 + 33*X^3 + 4*X^2 + 77*X + 70 = 0"  --->>>  ['39*X^5', '97*X^4', '33*X^3', '4*X^2', '77*X', '70']
def splitting(line):
    i = str.find(line, "=")
    if i < 0:
        return None  # Неверный формат многочлена
    line = str.upper(line[:i])  # удаляем '=' и все что справа
    line = str.replace(line, " ", "")  # удаляем пробелы
    line = str.replace(line, "-", "+-")  # добавим '+' перед '-'
    return str.split(line, "+")


# возвращает строку без первого числа и само число
#'39*X^5' -->>>  ("*X^5", "39")
def GetNum(st):
    i = 0
    for i in range(0, len(st)):
        if not (str.isnumeric(st[i]) or st[i] == '-'):
            if st[0:i] == '-':
                return (st[i::], '-1') # для случая '-X' 
            return (st[i::], st[0:i])
    return ("", st)


# возвращает список с [множитель, степень X]
# ['39*X^5', '97*X^4', '33*X^3', '4*X^2', '77*X', '70'] --->>>  [[39, 5], [97, 4], [33, 3], [4, 2], [77, 1], [70, 0]]
def translate(list):
    result = []
    for item in list:
        (item, stnum) = GetNum(item)
        if str.find(item, "X") == -1:
            result.append([int(stnum), 0])
            continue
        ml = 1
        pw = 1
        if stnum != "":
            ml = int(stnum)

        pos = str.find(item, "^")
        if pos >= 0:
            pw = int(item[pos + 1 : :])
            result.append([ml, pw])
            continue
        result.append([ml, 1])
    return result


# складываем многочлены
def sum(mn1, mn2):
    for item in mn2:
        flag = True
        for item2 in mn1:
            if item2[1] != item[1]:
                continue
            item2[0] += item[0]
            flag = False
            break
        if flag:  # такой степени X нет в mn1, добавим...
            mn1.append(item)
    return mn1


# формирует строку многочлена
# [[42, 5], [104, 4], [34, 3], [4, 2], [88, 1], [80, 0]] ---->>> "42*X^5 + 104*X^4 + 34*X^3 + 4*X^2 + 88*X + 80 = 0"
def GetStrMn(mn):
    st = ""
    for item in mn:
        if item[0] == 0:
            continue
        if st != "":
            st += " + "
        st += str(item[0])
        if item[1] == 0:
            continue
        st += "*X"
        if item[1] > 1:
            st += f"^{item[1]}"
    st += " = 0"    
    return str.replace(st, "+ -", "- ")




f = open("file1.txt", "r")
st1 = f.readline()
f.close()

f = open("file2.txt", "r")
st2 = f.readline()
f.close()


mn1 = translate(splitting(st1))
mn2 = translate(splitting(st2))

# пробежимся по исходным многочленам и упростим: X^5 + 3*X^5...  ---->>> 4*X^5
mn1 = sum([], mn1)
mn2 = sum([], mn2)

sum(mn1, mn2)  # складываем два многочлена
mn1.sort(key=lambda x: x[1], reverse=True)  # сортируем по степеням
print(st1)
print(st2)
print("************ результат ***********\n")
result = GetStrMn(mn1)
print(result)

f = open("result.txt", "w")
f.write(result)
f.close()
