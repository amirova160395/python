print("Zadacha 1 - Фибоначчи")
def fibonacci(i):
	while i > 1:
   	 return fibonacci(i-1) + fibonacci(i-2)
	return i
n = int(input("n = "))
m = int(input("m = "))
for i in range(n, m):
	print(fibonacci(i))
print()

print("Zadacha 2 - сортировка по возрастанию")
from random import randint
l = int(input("Введите кол-во элементов списка: "))
my_list = [randint(-1000, 1000) for i in range(l)]
print("Исходный список: ", my_list)
def sort_to_max(my_list):
    i = 0
    j = 0
    for i in range(l):
        for j in range(l):
            if my_list[i] < my_list[j]:
                my_list[i] = my_list[j] + my_list[i]
                my_list[j] = my_list[i] - my_list[j]
                my_list[i] = my_list[i] - my_list[j]    #если i-й меньше j-го, они меняются местами (наподобие поменять местами 2 переменные без использования третьей)
            j += 1
        i += 1
    print("Новый список: ", my_list)
sort_to_max(my_list)
print()
print("Zadacha 4 - параллелограмм?") #работает только при последовательном введении координат, т.е. А-B-C-D
print ("Введите координаты вершин 4-угольника")
x_1 = float(input("x1 = "))
y_1 = float(input("y1 = "))
x_2 = float(input("x2 = "))
y_2 = float(input("y2 = "))
x_3 = float(input("x3 = "))
y_3 = float(input("y3 = "))
x_4 = float(input("x4 = "))
y_4 = float(input("y4 = "))
def is_it_paral (x_1,x_2,x_3,x_4,y_1,y_2,y_3,y_4):
        if (x_1 - x_2) == (x_4 - x_3) and (y_1 - y_2) == (y_4 - y_3):
                print ("Параллелограмм")
        else:
                print ("Не параллелограмм")
is_it_paral (x_1,x_2,x_3,x_4,y_1,y_2,y_3,y_4)
print()

print("Zadacha 3 - фильтр")
from random import randint
l = int(input("Введите кол-во элементов списка: "))
my_list = [randint(-1000, 1000) for i in range(l)]
print("Исходный список: ", my_list)
print("1 - больше, 2 - меньше, 3 - равно")
p = int(input("Введите вариант: ")) #Выбор фильтра больше/меньше/равно
r = int(input("Введите аргумент: ")) #С чем сравнивают
j = 0
def filt(my_list):
        if p == 1:
                for j in range (l):
                        if my_list[j] < r: #удаляет элементы списка, кот-е меньше r
                                my_list[j] = []
                        j += 1
                print ("Новый список: ", my_list)
        if p == 2:
                for j in range (l):
                        if my_list[j] > r:  #удаляет элементы, кот-е больше r
                                my_list[j] = []
                        j += 1
                print ("Новый список: ", my_list)
        if p == 3:        
                for j in range (l):
                        if my_list[j] != r:  #удаляет элементы, кот-е не равны r
                                my_list[j] = []
                        j += 1
                print ("Новый список: ", my_list)
filt(my_list)
print()


