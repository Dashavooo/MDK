# Лабораторная работа №5
# Вариант 1

from math import *
from functools import reduce

def task_1():
    print("\nЗадание 1. Примеры определения функций")

    def square(x):
        return x * x

    def factorial(n):
        p = 1
        for i in range(1, n + 1):
            p *= i
        return p

    def is_even(n):
        return n % 2 == 0

    print("Квадрат числа 5:", square(5))
    print("Факториал числа 5:", factorial(5))
    print("Число 8 четное:", is_even(8))


def task_2():
    print("\nЗадание 2. Вычислить значение функции y = x^6 - 2x - 7")

    def f(x):
        return x**6 - 2 * x - 7

    x = float(input("Введите x: "))
    print("Значение функции y:", f(x))


def task_3():
    print("\nЗадание 3. Вычислить z1 и z2")

    def z1(x, y):
        return sin(x + 1) - y - 1.2

    def z2(x, y):
        return 2 * x + cos(y) - 2

    x = float(input("Введите x: "))
    y = float(input("Введите y: "))

    print("Значение z1:", z1(x, y))
    print("Значение z2:", z2(x, y))


def task_4():
    print("\nЗадание 4. Подсчет четных чисел в первой последовательности и нечетных во второй")

    def is_even(n):
        return n % 2 == 0

    print("Первая последовательность: a1, a2, ..., a8")
    a = list(map(int, input("Введите 8 целых чисел через пробел: ").split()))

    print("Вторая последовательность: b1, b2, ..., b8")
    b = list(map(int, input("Введите 8 целых чисел через пробел: ").split()))

    even_count_a = 0
    odd_count_b = 0

    for num in a:
        if is_even(num):
            even_count_a += 1

    for num in b:
        if not is_even(num):
            odd_count_b += 1

    print("Количество четных чисел в первой последовательности:", even_count_a)
    print("Количество нечетных чисел во второй последовательности:", odd_count_b)


def task_5():
    print("\nЗадание 5. Найти минимальное и максимальное значения списка")

    def min_max_list(nums):
        return min(nums), max(nums)

    def min_max_args(*nums):
        return min(nums), max(nums)

    a = list(map(int, input("Введите элементы списка через пробел: ").split()))

    mn1, mx1 = min_max_list(a)
    mn2, mx2 = min_max_args(*a)

    print("Способ 1. Функция принимает список")
    print("Минимальное значение:", mn1)
    print("Максимальное значение:", mx1)

    print("Способ 2. Функция принимает набор параметров")
    print("Минимальное значение:", mn2)
    print("Максимальное значение:", mx2)


def task_6():
    print("\nЗадание 6. Перевод числа из десятичной системы в N-ричную")

    def convert(n, base):
        digits = "0123456789ABCDEF"
        if n < base:
            return digits[n]
        return convert(n // base, base) + digits[n % base]

    num = int(input("Введите натуральное число: "))
    base = int(input("Введите основание системы счисления (2..16): "))

    if 2 <= base <= 16:
        print("Число в новой системе счисления:", convert(num, base))
    else:
        print("Ошибка: основание должно быть от 2 до 16")


def task_7():
    print("\nЗадание 7. Проверка, является ли число простым")

    def is_prime(n, d=2):
        if n < 2:
            return False
        if d * d > n:
            return True
        if n % d == 0:
            return False
        return is_prime(n, d + 1)

    n = int(input("Введите натуральное число: "))
    print("Число простое:", "YES" if is_prime(n) else "NO")


def task_8():
    print("\nЗадание 8. Остатки от деления чисел на 7")

    a = list(map(float, input("Введите вещественные числа через пробел: ").split()))
    result = list(map(lambda x: x % 7, a))

    print("Список остатков от деления на 7:", result)


def task_9():
    print("\nЗадание 9. Имена с заглавной буквы")

    names = ['катя', 'маша', 'таня', 'саша']
    names = list(map(lambda x: x.capitalize(), names))

    print("Преобразованный список имен:", names)


def task_10():
    print("\nЗадание 10. Переписать код через map и lambda")

    names = ['Маша', 'Петя', 'Вася']
    result = list(map(lambda x: hash(x), names))

    print("Список после преобразования:", result)

from functools import reduce

def task_11():
    print("\nЗадание 11")

    sentences = [
        'научиться плести рыболовные сети',
        'обучать нейронные сети',
        'паук ловит в сети мух'
    ]

    cap_count = reduce(lambda total, sentence: total + sentence.count('сети'), sentences, 0)

    print("Количество слов 'сети':", cap_count)


def task_12():
    print("\nЗадание 12")

    numbers = list(map(int, input("Введите натуральные числа через пробел: ").split()))
    result = list(filter(lambda x: x % 7 == 0, numbers))

    print("Числа, кратные 7:", result)


def task_13():
    print("\nЗадание 13")

    names = input("Введите имена абитуриентов через запятую: ").split(",")
    math_scores = list(map(int, input("Введите баллы по математике через пробел: ").split()))
    rus_scores = list(map(int, input("Введите баллы по русскому через пробел: ").split()))
    inf_scores = list(map(int, input("Введите баллы по информатике через пробел: ").split()))

    names = [name.strip() for name in names]

    result = list(zip(names, math_scores, rus_scores, inf_scores))

    print("Итоговый список:", result)

tasks = {
    "1": task_1,
    "2": task_2,
    "3": task_3,
    "4": task_4,
    "5": task_5,
    "6": task_6,
    "7": task_7,
    "8": task_8,
    "9": task_9,
    "10": task_10,
    "11": task_11,
    "12": task_12,
    "13": task_13
}

while True:
    print("\nЛР5. Вариант 1")
    print("Выберите задание от 1 до 13")
    print("0 - Выход")

    choice = input("Выберите задание: ")

    if choice == "0":
        print("Выход из программы.")
        break
    elif choice in tasks:
        tasks[choice]()
    else:
        print("Ошибка: такого пункта нет.")