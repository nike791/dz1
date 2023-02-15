a = float (input('Введите любое целое число = '))
b = float (a)
n = int (0)
s = int (0)
x = 10
i = 1
while a > 10:
    a //= 10
    n +=1
else:
    a //= 10
    n += 1
#n += 1
x **= n - 1
#print (b % x)
#print (n, x)
while n > 1:
    c = int(b / x)
    b = (b % x)
    s = (c + s)
    n -= 1
    x /= 10
    print (i, 'цифра = ', c)
    i += 1
c = int (b % 10)
s = int (c + s)
print (i, 'цифра = ', c)
print ('Сумма цифр = ', s)


