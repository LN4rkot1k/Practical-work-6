def prime_nums(n):  # функция, проверяющая простоту числа и выводящая число в файл
    file = open('output6.5.3.txt', 'w')

    for number in range(2, n):
        prime_number = True

        for i in range(2, number):
            if number % i == 0:
                prime_number = False
        if prime_number:
            numbers = str(number)
            file.write(numbers + ' ')  # Вывод чисел через пробел
    file.close()
