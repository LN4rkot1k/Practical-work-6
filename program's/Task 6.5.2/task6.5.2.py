# Все о цифрах в числе
import os
from functions_2 import numbers

if os.path.exists("D:\TempD\PycharmProjetcs\PR6\program's\Task 6.5.2\input6.5.2.txt"):  # проверяет существует ли файл
    file = open('input6.5.2.txt', 'r')
    Number = file.readline().split()  # считывает значения
    Number = int(Number[0])
    numbers(Number)
    file.close()
else:
    f1 = open("output.txt", "w")
    f1.write("Файл с входными данными не обнаружен")
    f1.close()
