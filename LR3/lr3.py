# Лабораторная работа №3

def task_1():
    print("Задание 1")
    rate = float(input("Введите курс доллара: "))
    for dollars in range(1, 21):
        print("Стоимость", dollars, "USD:", dollars * rate, "RUB")

def task_2():
    print("Задание 2")
    n = int(input("Введите число n: "))
    for i in range(1, 11):
        print("Результат:", n, "*", i, "=", n * i)

def task_3():
    print("Задание 3")
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    s = 0
    for i in range(a, b + 1):
        s += i ** 2
    print("Сумма квадратов:", s)

def task_4():
    print("Задание 4")
    n = int(input("Введите пятизначное число: "))
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    print("Число наоборот:", rev)

def task_5():
    print("Задание 5")
    n = int(input("Введите n: "))
    fact = 1
    s = 0
    for i in range(1, n + 1):
        fact *= i
        s += fact
    print("Сумма факториалов:", s)

def task_6():
    print("Задание 6")
    n = int(input("Введите количество чисел: "))
    count = 0
    i = 0
    while i < n:
        x = float(input("Введите число: "))
        if x < 0 and count == i:
            count += 1
        i += 1
    print("Количество отрицательных чисел в начале:", count)

def task_7():
    print("Задание 7")
    n = int(input("Введите n: "))
    a, b = 1, 1
    while a <= n:
        a, b = b, a + b
    print("Первое число Фибоначчи больше n:", a)

def task_8():
    print("Задание 8")
    n = input("Введите число: ")
    m = min(n)
    print("Количество минимальных цифр:", n.count(m))

def task_9():
    print("Задание 9")
    n = int(input("Введите n: "))
    f = int(input("Введите первый член прогрессии: "))
    s = int(input("Введите шаг прогрессии: "))
    if s != 0 and n >= f and (n - f) % s == 0:
        print("Результат: YES")
    elif n == f:
        print("Результат: YES")
    else:
        print("Результат: NO")

def task_10():
    print("Задание 10")
    n = input("Введите число: ")
    max_digit = max(n)
    min_digit = min(n)
    if n.index(max_digit) < n.index(min_digit):
        print("Левее стоит: максимальная цифра")
    else:
        print("Левее стоит: минимальная цифра")

def task_11():
    print("Задание 11")
    fact = int(input("Введите факториал: "))
    n = 1
    p = 1
    while p < fact:
        n += 1
        p *= n
    if p == fact:
        print("Искомое число:", n)
    else:
        print("Результат: такого числа нет")

def task_12():
    print("Задание 12")
    n = int(input("Введите сумму: "))
    notes = [64, 32, 16, 8, 4, 2, 1]
    for note in notes:
        cnt = n // note
        if cnt > 0:
            print("Купюра", note, "- количество:", cnt)
        n %= note

def task_13():
    print("Задание 13")
    for bulls in range(11):
        for cows in range(21):
            calves = 100 - bulls - cows
            if calves >= 0 and 10 * bulls + 5 * cows + 0.5 * calves == 100:
                print("Быков:", bulls, "Коров:", cows, "Телят:", calves)

def task_14():
    print("Задание 14")
    n = int(input("Введите n: "))
    s = 0
    for i in range(1, n + 1):
        s += i ** i
    print("Сумма:", s)

def task_15():
    print("Задание 15")
    n = int(input("Введите n: "))
    s = 0
    for i in range(1, n + 1):
        s += i ** i
    print("Сумма:", s)

tasks = {
    "1": task_1, "2": task_2, "3": task_3, "4": task_4, "5": task_5,
    "6": task_6, "7": task_7, "8": task_8, "9": task_9, "10": task_10,
    "11": task_11, "12": task_12, "13": task_13, "14": task_14, "15": task_15
}

while True:
    print("\nЛР3")
    print("Выберите задание от 1 до 15")
    print("0 - Выход")
    choice = input("Выберите задание: ")
    if choice == "0":
        print("Выход из программы.")
        break
    elif choice in tasks:
        tasks[choice]()
    else:
        print("Ошибка: такого задания нет.")