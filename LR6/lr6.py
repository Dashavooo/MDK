# Лабораторная работа №6

def task_1():
    print("Задание 1")
    a = input("Введите числа через пробел: ").split()
    digits = {}
    for num in a:
        for ch in num:
            if ch.isdigit():
                digits[ch] = digits.get(ch, 0) + 1
    print("Количество каждой цифры:")
    for k in sorted(digits):
        print("Цифра", k, "-", digits[k])

def task_2():
    print("Задание 2")
    a = set(map(int, input("Введите элементы первого списка: ").split()))
    b = set(map(int, input("Введите элементы второго списка: ").split()))
    common = sorted(a & b)
    print("Количество общих чисел:", len(common))
    print("Общие числа:", common)

def task_3():
    print("Задание 3")
    n = int(input("Введите количество строк: "))
    words = set()
    for _ in range(n):
        line = input("Введите строку: ").split()
        for word in line:
            words.add(word)
    print("Количество различных слов:", len(words))

def task_4():
    print("Задание 4")
    n = int(input("Введите количество школьников: "))
    all_known = set()
    everyone_known = None

    for i in range(n):
        k = int(input(f"Сколько языков знает школьник {i+1}: "))
        current = set()
        for _ in range(k):
            current.add(input("Введите язык: "))

        if everyone_known is None:
            everyone_known = current.copy()
        else:
            everyone_known &= current

        all_known |= current

    everyone_known = sorted(everyone_known)
    all_known = sorted(all_known)

    print("Языки, которые знают все школьники:", len(everyone_known))
    for lang in everyone_known:
        print(lang)

    print("Языки, которые знает хотя бы один школьник:", len(all_known))
    for lang in all_known:
        print(lang)

def task_5():
    print("Задание 5")
    a = set(map(int, input("Введите элементы первого множества: ").split()))
    b = set(map(int, input("Введите элементы второго множества: ").split()))
    c = a | (b - a)
    print("Третье множество:", sorted(c))

def task_6():
    print("Задание 6")
    n = int(input("Введите количество строк: "))
    freq = {}
    for _ in range(n):
        for word in input("Введите строку: ").split():
            freq[word] = freq.get(word, 0) + 1

    print("Количество повторений слов:")
    for word, count in freq.items():
        print(word, "-", count)

def task_7():
    print("Задание 7")
    n = int(input("Введите количество строк: "))
    freq = {}
    for _ in range(n):
        for word in input("Введите строку: ").split():
            freq[word] = len(word)
    longest = max(freq, key=freq.get)
    print("Самое длинное слово:", longest)

def task_8():
    print("Задание 8")
    n = int(input("Введите количество строк: "))
    freq = {}
    for _ in range(n):
        for word in input("Введите строку: ").split():
            freq[word] = freq.get(word, 0) + 1

    max_count = max(freq.values())
    words = [w for w, c in freq.items() if c == max_count]
    print("Самое частое слово:", min(words))

def task_9():
    print("Задание 9")
    n = int(input("Введите количество записей о покупках: "))
    sales = {}

    for _ in range(n):
        surname, item, count = input("Введите: покупатель товар количество: ").split()
        count = int(count)

        if surname not in sales:
            sales[surname] = {}

        sales[surname][item] = sales[surname].get(item, 0) + count

    print("Продажи интернет-магазина:")
    for buyer in sorted(sales):
        print(buyer + ":")
        for item in sorted(sales[buyer]):
            print(item, sales[buyer][item])

def task_10():
    print("Задание 10")
    n = int(input("Введите количество областей: "))
    regions = {}

    for _ in range(n):
        line = input("Введите область и города в формате Область: город1, город2: ")
        region, cities = line.split(":")
        cities = cities.split(",")

        for city in cities:
            regions[city.strip().replace(".", "")] = region.strip()

    m = int(input("Введите количество запросов: "))
    for _ in range(m):
        city = input("Введите город: ").strip()
        print("Область города:", regions[city])

tasks = {
    "1": task_1, "2": task_2, "3": task_3, "4": task_4, "5": task_5,
    "6": task_6, "7": task_7, "8": task_8, "9": task_9, "10": task_10
}

while True:
    print("\nЛР6")
    print("Выберите задание от 1 до 10")
    print("0 - Выход")
    choice = input("Выберите задание: ")
    if choice == "0":
        print("Выход из программы.")
        break
    elif choice in tasks:
        tasks[choice]()
    else:
        print("Ошибка: такого задания нет.")