def numbers(Number):
    f = open("output.txt", 'w')  # создает файл
    f.write("Число:" + str(Number) + "\n")  # Выводит число
    t = len(str(Number))
    f.write("Количество цифр:" + str(t) + "\n")  # Выводит количество цифр
    sum = 0
    p = 1
    while Number > 0:  # Цикл считает сумму и произведение
        sum = sum + (Number % 10)
        p = p * (Number % 10)
        Number = Number // 10
    f.write("Сумма цифр:" + str(sum) + "\n")  # выводит сумму цифр
    f.write("Произведение цифр:" + str(p) + "\n")  # выводит  произведение цифр
    f.close()
