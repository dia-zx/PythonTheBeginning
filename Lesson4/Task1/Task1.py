#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

#li - в этот список заносим множители для n, 
def multiples(li, n):
    i=0
    for i in range(2, n+1):
        if n%i ==0:
            break
    li.append(i)
    n //= i
    if n==1:
        return
    multiples(li, n)
    return

m = []
multiples(m, 17*11*5*7)
print(m)