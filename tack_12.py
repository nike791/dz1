a = int(input('sum '))
b = int(input('proiz '))
z = 1
for i in range(1, b+1):
    if b == a*i-i**2:
        z = a-i
        print(i,z)
        break 

