import random
import time

def insertionsort(L):
    for i in range(1, len(L)):
        current = L[i]
        j = i - 1

        while j >= 0 and L[j] > current:
            L[j + 1] = L[j]
            j -= 1

        L[j + 1] = current

    return L

def mergesort(L):
    if len(L) <= 1:
        return L

    middle = len(L) // 2
    left = mergesort(L[:middle])
    right = mergesort(L[middle:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

def create_random_list(size):
    L = list(range(size))
    random.shuffle(L)
    return L

def print_times(L):
    print("{0:7}".format(len(L)), end=":")

    for func in (insertionsort, mergesort):
        L_copy = L[:]

        t1 = time.perf_counter()
        func(L_copy)
        t2 = time.perf_counter()

        print("{0:10.1f}".format((t2 - t1) * 1000), end="")

    print()


print("Задание 1. Сортировка вставками")
L = [3, 6, 8, 2, 9, 1, 7, 0, 5, 9, 4]
print("Исходный список:", L)
print("Отсортированный список:", insertionsort(L[:]))


print("\nЗадание 2. Сортировка слиянием")
L = [3, 6, 8, 2, 9, 1, 7, 0, 5, 9, 4]
print("Исходный список:", L)
print("Отсортированный список:", mergesort(L[:]))


print("\nЗадание 3. Формирование входных данных случайным образом")
for list_size in [5, 10, 20, 30]:
    L = create_random_list(list_size)
    print("Случайный список размера", list_size, ":", L)
    print("После сортировки вставками:", insertionsort(L[:]))
    print("После сортировки слиянием:", mergesort(L[:]))


print("\nЗадание 4. Тестирование алгоритмов через assert")
L = create_random_list(30)
L1 = L[:]
L2 = L[:]

assert insertionsort(L1) == mergesort(L2)

print("Результат проверки: алгоритмы работают одинаково")


print("\nЗадание 5. Сравнение скорости работы алгоритмов")
print(" Размер : вставками   слиянием")

for size in [10, 100, 500, 1000, 2000, 3000]:
    L = create_random_list(size)
    print_times(L)