# Прямоугольники и квадраты

import os
from functions import Rectangle
from functions import Square

t = input('Введите название файла с выходными данными прямоугольника ')

if os.path.exists("D:\TempD\PycharmProjetcs\PR6\program's\Task 6.5.1\input_1.txt"):  # проверка существования файла
    file = open('input_1.txt', 'r')
    a, b = map(int, file.readline().split())  # считывание значений сторон
    Rectangle(a, b, t)  # вызов функции
    file.close()
else:
    f = open('%s.txt' % t, 'w')
    f.write('Файл с входными данными не обнаружен')
    f.close()

g = input('Введите название файла с выходными данными квадрата ')

if os.path.exists("D:\TempD\PycharmProjetcs\PR6\program's\Task 6.5.1\input_2.txt"):  # проверка существования файла
    file = open('input_2.txt', 'r')
    c = int(file.readline())  # считывание значения стороны
    Square(g, c)  # вызов функции
else:
    f = open('%s.txt' % g, 'w')
    f.write('Файл с входными данными не обнаружен')
    f.close()
