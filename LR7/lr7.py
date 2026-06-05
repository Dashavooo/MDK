# Лабораторная работа №7
# Работа с текстовыми файлами. Строки.

def task_1():
    print("\nЗадание 1")
    input_file = "input1.txt"
    output_file = "output1.txt"

    with open(input_file, "r", encoding="utf-8") as f:
        a = int(f.readline())
        b = int(f.readline())

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(str(a + b))

    print("Сумма записана в файл:", output_file)


def task_2():
    print("\nЗадание 2")
    filename = "input2.txt"
    symbol = input("Введите символ: ")

    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    if symbol in text:
        print("Результат: Yes")
    else:
        print("Результат: No")


def task_3():
    print("\nЗадание 3")
    input_file = "input3.txt"

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    print("Сумма чисел в каждой строке:")
    for i, line in enumerate(lines, start=1):
        numbers = list(map(int, line.split()))
        print(f"Строка {i}: {sum(numbers)}")


def task_4():
    print("\nЗадание 4")
    filename = "input4.txt"

    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    letters = sum(1 for ch in text if ch.isalpha() and ch.isascii())
    words = len(text.split())

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    print("Количество латинских букв:", letters)
    print("Количество слов:", words)
    print("Количество строк:", len(lines))


def task_5():
    print("\nЗадание 5")
    filename = "input5.txt"

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    print("а) Первая строка:")
    if len(lines) >= 1:
        print(lines[0].rstrip())
    else:
        print("Файл пуст")

    print("б) Пятая строка:")
    if len(lines) >= 5:
        print(lines[4].rstrip())
    else:
        print("Пятой строки нет")

    print("в) Первые 5 строк:")
    for line in lines[:5]:
        print(line.rstrip())

    s1 = int(input("Введите номер начальной строки s1: "))
    s2 = int(input("Введите номер конечной строки s2: "))

    print("г) Строки с s1-й по s2-ю:")
    for line in lines[s1 - 1:s2]:
        print(line.rstrip())

    print("д) Весь файл:")
    for line in lines:
        print(line.rstrip())


def task_6():
    print("\nЗадание 6")
    filename = "input6.txt"

    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    if not lines:
        print("Файл пуст")
        return

    max_len = max(len(line) for line in lines)
    max_index = next(i for i, line in enumerate(lines) if len(line) == max_len)

    print("а) Длина самой длинной строки:", max_len)
    print("б) Номер самой длинной строки:", max_index + 1)
    print("в) Самая длинная строка:", lines[max_index])


def task_7():
    print("\nЗадание 7")
    input_file = "input7.txt"
    output_a = "output7a.txt"
    output_b = "output7b.txt"

    with open(input_file, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    with open(output_a, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line[::-1] + "\n")

    with open(output_b, "w", encoding="utf-8") as f:
        for line in reversed(lines):
            f.write(line[::-1] + "\n")

    print("Файл а) создан:", output_a)
    print("Файл б) создан:", output_b)


def task_8():
    print("\nЗадание 8")
    file1 = "input8_1.txt"
    file2 = "input8_2.txt"

    with open(file1, "r", encoding="utf-8") as f:
        lines1 = [line.rstrip("\n") for line in f.readlines()]

    with open(file2, "r", encoding="utf-8") as f:
        lines2 = [line.rstrip("\n") for line in f.readlines()]

    same = True
    for i in range(len(lines1)):
        if lines1[i] != lines2[i]:
            print("Файлы не совпадают")
            print("Номер первой различающейся строки:", i + 1)
            same = False
            break

    if same:
        print("Файлы совпадают")


def task_9():
    print("\nЗадание 9")
    filename = "input9.txt"

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    n = int(lines[0].strip())
    segments = [0] * (n - 1)

    for line in lines[1:]:
        parts = line.split()
        start = int(parts[-2])
        end = int(parts[-1])

        for i in range(start - 1, end - 1):
            segments[i] += 1

    max_passengers = max(segments)

    print("Перегоны с наибольшим числом пассажиров:")
    for i, val in enumerate(segments):
        if val == max_passengers:
            print(f"{i + 1}-{i + 2}")


def task_10():
    print("\nЗадание 10")
    filename = "input10.txt"

    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    k = int(lines[0])
    scores = []

    for line in lines[1:]:
        parts = line.split()
        exam1, exam2, exam3 = map(int, parts[-3:])

        if exam1 >= 40 and exam2 >= 40 and exam3 >= 40:
            scores.append(exam1 + exam2 + exam3)

    if len(scores) <= k:
        print("Проходной балл: 0")
        return

    scores.sort(reverse=True)

    if scores[0] == scores[k]:
        print("Проходной балл: 1")
    else:
        print("Проходной балл:", scores[k - 1])


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
    "10": task_10
}

while True:
    print("\nЛР7")
    print("Выберите задание от 1 до 10")
    print("0 - Выход")

    choice = input("Выберите задание: ")

    if choice == "0":
        print("Выход из программы.")
        break
    elif choice in tasks:
        tasks[choice]()
    else:
        print("Ошибка: такого пункта нет.")