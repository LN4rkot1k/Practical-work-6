import os
from functions_3 import prime_nums

if os.path.exists("D:\TempD\PycharmProjetcs\PR6\program's\Task 6.5.3\input6.5.3.txt"):  # проверка существования файла
    file = open('input6.5.3.txt', 'r')
    Number = int(file.readline())
    prime_nums(Number)

else:  # если файл с исходными данными не существует, то пишем об этом
    file = open('output6.5.3.txt', 'w')
    file.write('Файл с входными данными не обнаружен')
    file.close()