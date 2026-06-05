# Рекурсивный подход и итеративный подход
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
n = 7
print(f"Факториал для n = {n}")


result_rec = factorial_recursive(n)
result_iter = factorial_iterative(n)
print(f"Рекурсивно: {result_rec}")
print(f"Итеративно: {result_iter}")



