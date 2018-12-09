print("Zadacha 1, easy")
import random
my_list = []
my2_list = []
for _ in range(10):
    my_list.append(random.randint(-10, 10))
print(my_list)
for i in range(len(my_list)):
    my_list[i] = my_list[i]**2
print(my_list)
print()

print("Zadacha 2, easy")
fruits1 = ["яблоко", "банан", "апельсин", "мандарин", "киви"]
fruits2 = ["груша", "лимон", "киви", "гранат", "персик", "яблоко"]
new = []
n = 0
print(fruits1)
print(fruits2)
for fruit1 in fruits1:
    for fruit2 in fruits2:
        if fruit1 == fruit2:
            new.append(fruit1)
            n += 1
print(new)

print()
print("Zadacha 3,easy")
import random
my_list = []
for _ in range(10):
    my_list.append(random.randint(-100, 100))
print(my_list)
for element in my_list[:]:
    if element > 0 and (element % 3 == 0) and (element % 4 != 0):
        element = element
    else:
        my_list.remove(element)
print(my_list)
