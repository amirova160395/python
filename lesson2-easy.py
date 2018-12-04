
print ("Zadacha 1")
fruits = [ 'яблоко', 'апельсин', 'банан', 'груша', 'лимон']
print (fruits)
for index, value in enumerate(fruits, 1):
    print ("{}. {}".format(index, value))
print ()



print ("Zadacha 3")
from random import randint
len_1 = int(input("Введите кол-во элементов списка: "))
list_1 = [randint(-1000, 1000) for i in range(len_1)]
print ("Исходный список  = ", list_1)
j = 0
for element in list_1:
    if list_1[j] % 2 == 0:
        list_1[j] = list_1[j] / 4
    else:
        list_1[j] = list_1[j] * 2
    j += 1
print ("Новый список = ", list_1)


