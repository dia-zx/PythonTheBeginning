#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
# -6782 -> 23
# -0,56 -> 11

def NumberCalc(f):
    st = str(f)
    s = 0
    for i in range(len(st)):
        if '0' <= st[i] <= '9':
            s += int(st[i])
    return s

print(NumberCalc(-6782))
print(NumberCalc(-0.56))