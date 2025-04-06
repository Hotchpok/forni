# тут нечего объяснять

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

n = 10
print(f"Рекурсивно: F({n}) = {fibonacci_recursive(n)}")  
print(f"Итеративно: F({n}) = {fibonacci_iterative(n)}")   