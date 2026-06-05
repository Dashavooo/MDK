# Лабораторная работа №4
from random import randint

def task_1():
    print("Задание 1")
    a = [randint(163, 190) for _ in range(12)]
    print("Список ростов:", a)

def task_2():
    print("Задание 2")
    a1 = int(input("Введите первый член прогрессии: "))
    d = int(input("Введите разность прогрессии: "))
    a = [a1 + i * d for i in range(10)]
    print("Первые 10 членов прогрессии:", a)

def task_3():
    print("Задание 3")
    a = list(map(int, input("Введите элементы списка через пробел: ").split()))
    print("Список в обратном порядке:", a[::-1])

def task_4():
    print("Задание 4")
    a = list(map(int, input("Введите элементы списка через пробел: ").split()))
    s = 0
    sign = 1
    for x in a:
        s += sign * x
        sign *= -1
    print("Знакопеременная сумма:", s)

def task_5():
    print("Задание 5")
    a = list(map(int, input("Введите 42 числа через пробел: ").split()))
    total = sum(a)
    print("Общее количество учеников:", total)
    if 1000 <= total <= 9999:
        print("Результат: YES")
    else:
        print("Результат: NO")

def task_6a():
    print("Задание 6а")
    a = list(map(int, input("Введите элементы списка через пробел: ").split()))
    even = [x for x in a if x % 2 == 0]
    print("Четные элементы:", even)

def task_6b():
    print("Задание 6б")
    a = list(map(int, input("Введите элементы списка через пробел: ").split()))
    zero_end = [x for x in a if x % 10 == 0]
    print("Элементы, оканчивающиеся на 0:", zero_end)

def task_7():
    print("Задание 7")
    math_scores = list(map(int, input("Введите баллы по математике: ").split()))
    rus_scores = list(map(int, input("Введите баллы по русскому: ").split()))
    inf_scores = list(map(int, input("Введите баллы по информатике: ").split()))
    names = input("Введите фамилии через пробел: ").split()

    result = []
    for i in range(len(names)):
        total = math_scores[i] + rus_scores[i] + inf_scores[i]
        result.append((total, i, names[i]))

    result.sort(reverse=True)

    print("Список зачисленных:")
    for i in range(min(10, len(result))):
        print("Номер:", result[i][1], "Фамилия:", result[i][2], "Сумма баллов:", result[i][0])

def task_8():
    print("Задание 8")
    a = list(map(int, input("Введите неубывающий список: ").split()))
    if not a:
        print("Количество различных элементов: 0")
    else:
        count = 1
        for i in range(1, len(a)):
            if a[i] != a[i - 1]:
                count += 1
        print("Количество различных элементов:", count)

def task_9():
    print("Задание 9")
    a = list(map(int, input("Введите элементы списка: ").split()))
    for i in range(0, len(a) - 1, 2):
        a[i], a[i + 1] = a[i + 1], a[i]
    print("Результат:", a)

def task_10():
    print("Задание 10")
    a = list(map(int, input("Введите элементы списка: ").split()))
    k1 = int(input("Введите k1: "))
    k2 = int(input("Введите k2: "))
    res = a[k2 + 1:] + a[k1:k2 + 1] + a[:k1]
    print("Результат:", res)

def task_11():
    print("Задание 11")
    a = input("Введите имена через пробел: ").split()
    count = 0
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            count += 1
    print("Количество пар одинаковых имен рядом:", count)

def task_12():
    print("Задание 12")
    sizes = list(map(int, input("Введите размеры обуви: ").split()))
    print("Различные размеры обуви:", sorted(set(sizes)))

def task_13():
    print("Задание 13")
    g17 = [x.strip() for x in input("Введите студентов группы 17 через запятую: ").split(',')]
    g18 = [x.strip() for x in input("Введите студентов группы 18 через запятую: ").split(',')]
    g19 = [x.strip() for x in input("Введите студентов группы 19 через запятую: ").split(',')]
    all_groups = [g17, g18, g19]
    print("Общее число студентов:", len(g17) + len(g18) + len(g19))
    print("Самая малочисленная группа:", min(all_groups, key=len))
    print("Самая большая группа:", max(all_groups, key=len))
    print("Общий список студентов:", sorted(g17 + g18 + g19))

def task_14():
    print("Задание 14")
    marks = [5, 4, 5, 3, 2, 5, 4, 3, 5, 5, 4, 2, 2, 3]
    print("Средний балл:", sum(marks) / len(marks))
    print("Оценки:", "; ".join(map(str, marks)))

def task_15():
    print("Задание 15")
    a = [x for x in range(1, 10001) if (x % 7 == 0 and x % 3 == 0) or x % 9 == 0]
    print("Список чисел:", a)

def task_16():
    print("Задание 16")
    n = int(input("Введите n: "))
    a = [11 * i for i in range(1, n + 1)]
    print("Список:", a)

def task_17():
    print("Задание 17")
    a = [[1, 10], [2, 20], [3, 30], [4, 40]]
    b = [x for pair in a for x in pair]
    print("Результат:", b)

def task_18():
    print("Задание 18")
    a = list(range(1, 21))
    b = [x ** 2 if x % 2 == 0 else x + 2 for x in a]
    print("Преобразованный список:", b)

tasks = {
    "1": task_1, "2": task_2, "3": task_3, "4": task_4, "5": task_5,
    "6a": task_6a, "6b": task_6b, "7": task_7, "8": task_8, "9": task_9,
    "10": task_10, "11": task_11, "12": task_12, "13": task_13, "14": task_14,
    "15": task_15, "16": task_16, "17": task_17, "18": task_18
}

while True:
    print("\nЛР4")
    print("Доступные задания: 1,2,3,4,5,6a,6b,7...18")
    print("0 - Выход")
    choice = input("Выберите задание: ")
    if choice == "0":
        print("Выход из программы.")
        break
    elif choice in tasks:
        tasks[choice]()
    else:
        print("Ошибка: такого задания нет.")