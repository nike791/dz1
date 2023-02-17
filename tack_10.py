import random
n = int(input('Введите кол-во монет '))
sp = []
count = i = 0
for i in range (n):
    sp.append(random.randint(0, 1))
print (sp)

for i in range(n):
    if sp[i] == 0:
        count += 1
print (count)
