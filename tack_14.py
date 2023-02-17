num = int(input('Vvod - '))
sp = []
f = 1
counter = 1
t = 0
if not num == 0:
    while f <= num:
#        print (f)
        sp.insert(t, f)
        t += 1
        f = 2**counter
        counter += 1
    print(sp)
else:
    print('error')






