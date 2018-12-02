print ("Zadacha 1")
a = abs(int(input(' Vvedite celoe chislo: ')))
max = 0
while a > 0:
    c = a % 10
    if c > max:
        max = c
    a = a // 10
print ("Maximalnaya cifra = ", max)
print ('Programma zavershena')



print ("Zadacha 2")
a = int(input(' Vvedite chislo a: '))
b = int(input (' Vvedite chislo b: '))
a = a + b
b = a - b
a = a - b
print ("a = ", a)
print ("b = ", b)
print ('Programma zavershena')


print ("Zadacha 3")
import math
a = float(input('Vvedite kofficient a: '))
b = float(input('Vvedite koefficient b: '))
c = float(input('Vvedite koefficient c: '))
D = b ** 2 - 4 * a * c
print (" Discriminant = ", D)
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print (" x1 = ", x1)
    print (" x2 = ", x2)
else:
    if D == 0:
        x = (-b + math.sqrt(D)) / (2 * a)
        print("x = ", x)
    else:
        print ("Uravnenie ne imeet kornei")
    
        



