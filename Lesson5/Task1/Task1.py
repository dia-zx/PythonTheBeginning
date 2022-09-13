# Напишите программу, удаляющую из текста все слова содержащие "абв".

def sol1(st: str):
    li = st.split()
    res = ""
    for it in li:
        if it.find("абв") < 0:
            if res != '':
                res += " "
            res += it
    return res


st = "Приветабв, ответ, абв. Как дела? отлабвлично!"
print(sol1(st))
