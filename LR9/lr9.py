import numpy as np

print("Задание 1")
a = np.zeros(15)
print("Вектор из 15 нулей:")
print(a)

print("\nЗадание 2")
a = np.full(8, 3.2)
print("Вектор размера 8, заполненный числом 3.2:")
print(a)

print("\nЗадание 3")
a = np.zeros(15)
a[4] = 1
print("Вектор из 15 нулей, пятый элемент равен 1:")
print(a)

print("\nЗадание 4")
a = np.arange(12, 44)
print("Вектор со значениями от 12 до 43:")
print(a)

print("\nЗадание 5")
a = np.random.random((3, 3, 2))
print("Массив 3x3x2 со случайными значениями:")
print(a)

print("\nЗадание 6")
a = np.random.random((12, 12))
print("Массив 12x12:")
print(a)
print("Минимум:", a.min())
print("Максимум:", a.max())

print("\nЗадание 7")
a = np.ones((6, 6))
a[0, :] = 0
a[-1, :] = 0
a[:, 0] = 0
a[:, -1] = 0
print("Матрица с 1 внутри и 0 на границах:")
print(a)

print("\nЗадание 8")
a = np.zeros((8, 8), dtype=int)
a[1::2, ::2] = 1
a[::2, 1::2] = 1
print("Матрица 8x8 в шахматном порядке:")
print(a)

print("\nЗадание 9")
a = np.tile([[0, 1], [1, 0]], (4, 4))
print("Матрица 8x8 в шахматном порядке через tile:")
print(a)

print("\nЗадание 10")
a = np.arange(8).reshape(4, 2)
b = np.arange(10).reshape(2, 5)
c = np.dot(a, b)
print("Матрица 4x2:")
print(a)
print("Матрица 2x5:")
print(b)
print("Результат перемножения:")
print(c)

print("\nЗадание 11")
a = np.arange(10)
a[(a > 4) & (a < 7)] *= -1
print("Массив после изменения знака у элементов между 4 и 7:")
print(a)

print("\nЗадание 12")
a = np.tile(np.arange(6), (6, 1))
print("Матрица 6x6 со значениями в строках от 0 до 5:")
print(a)

print("\nЗадание 13")
a = np.array([5, 2, 9, 1, 7, 3])
print("Исходный вектор:")
print(a)
print("Отсортированный вектор:")
print(np.sort(a))

print("\nЗадание 14")
a = np.array([1, 2, 3])
b = np.array([1, 2, 3])
c = np.array([1, 2, 4])
print("Первый и второй массив одинаковы:", np.array_equal(a, b))
print("Первый и третий массив одинаковы:", np.array_equal(a, c))

print("\nЗадание 15")
a = np.array([4, 8, 1, 10, 3])
a[a.argmax()] = -1
print("Массив после замены максимального элемента на -1:")
print(a)

print("\nЗадание 16")
a = np.array([0.1, 0.5, 1.3, 2.7, 3.8])
value = float(input("Введите заданное значение: "))
nearest = a[np.abs(a - value).argmin()]
print("Ближайшее число в массиве:", nearest)

print("\nЗадание 17")
dtype = [('x', float), ('y', float), ('color', int, (3,))]

points = np.array([
    (1.5, 2.3, [255, 0, 0]),
    (4.1, 5.2, [0, 255, 0]),
    (7.0, 8.5, [0, 0, 255])
], dtype=dtype)

print("Структурированный массив с координатами и цветом:")
print(points)


print("\nЗадание 18")
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
], dtype=float)

result = A - A.mean(axis=1, keepdims=True)

print("Исходная матрица:")
print(A)
print("Матрица после вычитания среднего из каждой строки:")
print(result)

print("\nЗадание 19")
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Исходная матрица:")
print(A)

A[[0, 1]] = A[[1, 0]]

print("Матрица после замены первой и второй строки:")
print(A)

print("\nЗадание 20")

def distance_point_to_line(p, p0, p1):
    v = p1 - p0
    w = p - p0
    return abs(v[0] * w[1] - v[1] * w[0]) / np.linalg.norm(v)

P0 = np.array([
    [0, 0],
    [1, 1],
    [2, 0]
], dtype=float)

P1 = np.array([
    [4, 0],
    [1, 5],
    [5, 3]
], dtype=float)

p = np.array([2, 2], dtype=float)

print("Точка p:", p)
print("Расстояния от точки p до каждой линии:")

for i in range(len(P0)):
    d = distance_point_to_line(p, P0[i], P1[i])
    print(f"Линия {i + 1}: расстояние = {d}")

print("\nЗадание 21")
A = np.array([4, 10, 2, 8, 15, 3, 20, 7])
n = int(input("Введите n: "))

result = np.sort(A)[-n:][::-1]

print("Исходный массив:")
print(A)
print(f"{n} наибольших значений:")
print(result)

print("\nЗадание 22")
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([
    [1, 0, 3],
    [4, 9, 6]
])

different = np.sum(A != B)

print("Матрица A:")
print(A)
print("Матрица B:")
print(B)
print("Количество отличающихся элементов:", different)

print("\nЗадание 23")
A = np.array([1, 3, 6, 9, 12, 15, 18, 20, 21])

result = A[(A > 4) & (A % 3 == 0)]

print("Исходный массив:")
print(A)
print("Элементы больше 4 и кратные 3:")
print(result)

print("\nЗадание 24")
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = A.reshape(3, 2)

print("Матрица A размера 2x3:")
print(A)
print("Матрица после изменения размера на 3x2:")
print(B)

print("\nЗадание 25")
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

scalar_product = np.vdot(A, B)

print("Матрица A:")
print(A)
print("Матрица B:")
print(B)
print("Скалярное произведение матриц:", scalar_product)