import time
# Рекурсивный алгоритм (факториал)
def factorial_rec(n):
    if n == 1:
        return 1
    return n * factorial_rec(n - 1)
# Эвристический алгоритм (жадный поиск максимума)
def heuristic_max(arr):
    max_val = arr[0]
    for x in arr:
        if x > max_val:
            max_val = x
    return max_val
n = 10
array = list(range(1, 10001))

start = time.time()
factorial_rec(n)
time_rec = time.time() - start
start = time.time()
heuristic_max(array)
time_heur = time.time() - start

print("=" * 78)
print(f"| {'Алгоритм':20} | {'Тип алгоритма':18} | {'Сложность':10} | {'Время (с)':12} |")
print("=" * 78)
print(f"| {'Факториал':20} | {'Рекурсивный':18} | {'O(n)':10} | {time_rec:<12.6f} |")
print(f"| {'Поиск максимума':20} | {'Эвристический':18} | {'O(n)':10} | {time_heur:<12.6f} |")
print("=" * 78)
print("-" * 70)

