# Лабораторная работа №2
import math

def task_1():
    print("Задание 1")
    x = float(input("Введите x: "))
    y = float(input("Введите y: "))
    if x < 4:
        print("Область: I")
    else:
        print("Область: II")

def task_2():
    print("Задание 2")
    x = float(input("Введите x: "))
    y = float(input("Введите y: "))
    if y > 3:
        print("Область: I")
    else:
        print("Область: II")

def task_3a():
    print("Задание 3а")
    x = float(input("Введите x: "))
    if x <= 2:
        y = x
    else:
        y = 2
    print("Значение y:", y)

def task_3b():
    print("Задание 3б")
    x = float(input("Введите x: "))
    if x <= 3:
        y = -x
    else:
        y = -3
    print("Значение y:", y)

def task_4():
    print("Задание 4")
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    if a > b:
        print("Большее число:", a)
        print("Меньшее число:", b)
    else:
        print("Большее число:", b)
        print("Меньшее число:", a)

def task_5():
    print("Задание 5")
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print("Максимум:", max(a, b))
    print("Минимум:", min(a, b))

def task_6():
    print("Задание 6")
    birth_year = int(input("Введите год рождения: "))
    birth_month = int(input("Введите месяц рождения: "))
    current_year = int(input("Введите текущий год: "))
    current_month = int(input("Введите текущий месяц: "))
    age = current_year - birth_year
    if current_month < birth_month:
        age -= 1
    print("Возраст человека:", age)

def task_7():
    print("Задание 7")
    x = float(input("Введите x: "))
    if x > 0:
        y = math.sin(x) ** 2
    else:
        y = 1 - 2 * (math.sin(x) ** 2)
    print("Значение y:", y)

def task_8():
    print("Задание 8")
    x = float(input("Введите x: "))
    if x > 0:
        y = math.sin(x ** 2)
    else:
        y = 1 + 2 * (math.sin(x) ** 2)
    print("Значение y:", y)

def task_9():
    print("Задание 9")
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    if b % a == 0:
        print("Результат: YES")
    else:
        print("Результат: NO")

def task_10():
    print("Задание 10")
    n = int(input("Введите натуральное число: "))
    print("Четность:", "четное" if n % 2 == 0 else "нечетное")
    print("Оканчивается на 7:", "да" if n % 10 == 7 else "нет")

def task_11():
    print("Задание 11")
    n = int(input("Введите двузначное число: "))
    a = n // 10
    b = n % 10
    if a > b:
        print("Результат: первая цифра больше")
    elif b > a:
        print("Результат: вторая цифра больше")
    else:
        print("Результат: цифры равны")

def task_12():
    print("Задание 12")
    n = int(input("Введите трехзначное число: "))
    if n // 100 == n % 10:
        print("Палиндром: YES")
    else:
        print("Палиндром: NO")

def task_13():
    print("Задание 13")
    n = int(input("Введите трехзначное число: "))
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    print("Все цифры одинаковые:", "да" if a == b == c else "нет")
    print("Есть одинаковые цифры:", "да" if a == b or b == c or a == c else "нет")

def task_14():
    print("Задание 14")
    n = int(input("Введите число: "))
    last = n % 10
    print("Последняя цифра четная:", "да" if last % 2 == 0 else "нет")
    print("Последняя цифра нечетная:", "да" if last % 2 != 0 else "нет")

def task_15():
    print("Задание 15")
    t = float(input("Введите время в минутах: "))
    r = t % 5
    if r < 3:
        print("Светофор:", "зеленый")
    else:
        print("Светофор:", "красный")

def task_16():
    print("Задание 16")
    kg = int(input("Введите массу в килограммах: "))
    print("Полных тонн:", kg // 1000)

def task_17():
    print("Задание 17")
    print("Количество квадратов 130x130:", (543 // 130) * (130 // 130))

def task_18():
    print("Задание 18")
    n = int(input("Введите количество месяцев: "))
    print("Номер месяца:", n % 12 + 1)

def task_19():
    print("Задание 19")
    n = int(input("Введите трехзначное число: "))
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    print("Перевернутое число:", c * 100 + b * 10 + a)

def task_20():
    print("Задание 20")
    n = int(input("Введите трехзначное число: "))
    a = n // 100
    bc = n % 100
    print("Результат:", bc * 10 + a)

def task_21():
    print("Задание 21")
    n = int(input("Введите трехзначное число: "))
    ab = n // 10
    c = n % 10
    print("Результат:", c * 100 + ab)

def task_22():
    print("Задание 22")
    n = int(input("Введите трехзначное число: "))
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    print("Результат:", b * 100 + a * 10 + c)

def task_23():
    print("Задание 23")
    n = int(input("Введите трехзначное число: "))
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    print("Результат:", a * 100 + c * 10 + b)

def task_24():
    print("Задание 24")
    n = int(input("Введите трехзначное число: "))
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    print("Все перестановки:")
    print(a * 100 + b * 10 + c)
    print(a * 100 + c * 10 + b)
    print(b * 100 + a * 10 + c)
    print(b * 100 + c * 10 + a)
    print(c * 100 + a * 10 + b)
    print(c * 100 + b * 10 + a)

def task_25():
    print("Задание 25")
    n = int(input("Введите число: "))
    print("Количество единиц:", n % 10)
    print("Количество десятков:", (n // 10) % 10)

def task_26():
    print("Задание 26")
    print("Искомое число x:", 372)

def task_27():
    print("Задание 27")
    n = int(input("Введите число n: "))
    x = 10 * (n % 100) + n // 100
    print("Искомое число x:", x)

def task_28():
    print("Задание 28")
    n = int(input("Введите число n: "))
    a = n % 10
    bc = n // 10
    x = a * 100 + bc
    print("Искомое число x:", x)

def task_29():
    print("Задание 29")
    n = int(input("Введите число n: "))
    b = n // 100
    a = (n % 100) // 10
    c = n % 10
    x = a * 100 + b * 10 + c
    print("Искомое число x:", x)

def task_30():
    print("Задание 30")
    h = int(input("Введите часы: "))
    m = int(input("Введите минуты: "))
    s = int(input("Введите секунды: "))
    angle = (h % 12) * 30 + m * 0.5 + s / 120
    print("Угол часовой стрелки:", angle)

def task_31():
    print("Задание 31")
    y = float(input("Введите угол: "))
    total_minutes = y / 0.5
    hours = int(total_minutes // 60)
    minutes = int(total_minutes % 60)
    print("Полных часов:", hours)
    print("Полных минут:", minutes)

def task_32():
    print("Задание 32")
    y = float(input("Введите угол: "))
    total_minutes = y / 0.5
    hours = int(total_minutes // 60)
    minutes = int(total_minutes % 60)
    minute_angle = (total_minutes * 6) % 360
    print("Угол минутной стрелки:", minute_angle)
    print("Полных часов:", hours)
    print("Полных минут:", minutes)

def task_33():
    print("Задание 33. Проверка логических условий")

    A = int(input("Введите A: "))
    B = int(input("Введите B: "))
    C = int(input("Введите C: "))

    a_result = A > 100 and B > 100
    print("а) Оба числа A и B больше 100:", a_result)

    b_result = (A % 2 == 0 and B % 2 != 0) or (A % 2 != 0 and B % 2 == 0)
    print("б) Одно из чисел A и B четное, а другое нечетное:", b_result)

    v_result = A > 0 or B > 0
    print("в) Хотя бы одно из чисел A и B положительное:", v_result)

    g_result = A % 3 == 0 and B % 3 == 0 and C % 3 == 0
    print("г) Все числа A, B и C кратны 3:", g_result)

    d_result = ((A < 50 and B >= 50 and C >= 50) or
                (B < 50 and A >= 50 and C >= 50) or
                (C < 50 and A >= 50 and B >= 50))
    print("д) Ровно одно из чисел A, B, C меньше 50:", d_result)

    e_result = A < 0 or B < 0 or C < 0
    print("е) Хотя бы одно из чисел A, B, C отрицательное:", e_result)

def task_34():
    print("Задание 34")
    x1 = int(input("Введите x1: "))
    y1 = int(input("Введите y1: "))
    x2 = int(input("Введите x2: "))
    y2 = int(input("Введите y2: "))
    if x1 == x2 or y1 == y2:
        print("Ход ладьи возможен: YES")
    else:
        print("Ход ладьи возможен: NO")

def task_35a():
    print("Задание 35а")
    x = float(input("Введите x: "))
    y = float(input("Введите y: "))
    print("Принадлежит области:", x <= -1 and y <= -2)

def task_35b():
    print("Задание 35б")
    x = float(input("Введите x: "))
    y = float(input("Введите y: "))
    print("Принадлежит области:", y >= 1 or y <= -3)

tasks = {
    "1": task_1, "2": task_2, "3a": task_3a, "3b": task_3b, "4": task_4,
    "5": task_5, "6": task_6, "7": task_7, "8": task_8, "9": task_9,
    "10": task_10, "11": task_11, "12": task_12, "13": task_13, "14": task_14,
    "15": task_15, "16": task_16, "17": task_17, "18": task_18, "19": task_19,
    "20": task_20, "21": task_21, "22": task_22, "23": task_23, "24": task_24,
    "25": task_25, "26": task_26, "27": task_27, "28": task_28, "29": task_29,
    "30": task_30, "31": task_31, "32": task_32, "33": task_33, "34": task_34,
    "35a": task_35a, "35b": task_35b
}

while True:
    print("\nЛР2")
    print("Доступные задания: 1, 2, 3a, 3b, 4 ... 35a, 35b")
    print("0 - Выход")
    choice = input("Выберите задание: ")
    if choice == "0":
        print("Выход из программы.")
        break
    elif choice in tasks:
        tasks[choice]()
    else:
        print("Ошибка: такого задания нет.")