import os
import shutil
#Easy1
try:
    for i in range(1, 10):
        os.mkdir("dir_" + str(i))
except:
    print("Already exist")
a = input("enter something ")
print(a)
try:
    for i in range(3, 8):
        os.rmdir("dir_" + str(i))
except:
    print("Already removed")
print()

#Easy2
list = os.listdir()
for i in list:
    print(i)
#Easy 3
shutil.copy(r'lesson5.py', r'backup_file.py')

#Normal
#Решение нашла в сети, разобрала, и даже немного поняла
import os
import easy
9
exitos ='a'
while exitos != '0':
    print('Перейти в папку - выбрать 1')
    print('Просмотреть содержимое текущей папки - выбрать 2')
    print('Удалить папку - выбрать 3')
    print('Создать папку - выбрать 4')
    print('для выхода - выбрать 0')
    exitos = input('Выбрать: ' )
    print(exitos)
    if exitos == '1':
        dir_name = input ('наберите полный путь папки: ')
        easy.change_dir(dir_name)
    elif exitos == '2':
        dir_name = os.getcwd()
        easy.list_dir(dir_name)
    elif exitos == '3':
        dir_name = input('наберите полный путь папки: ')
        easy.delete_dir(dir_name)
    elif exitos == '4':
        dir_name = input('наберите полный путь папки: ')
        easy.make_dir(dir_name)
    elif exitos == '0':
        pass
    else:
        print('Такого пункта меню нет')
