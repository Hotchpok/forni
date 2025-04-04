def f(x):
    return x**2
a = 2
b = 6


n = 1000

dx = (b - a) / n

area = 0
for i in range(n):
    x = a + i * dx
    area += f(x) * dx


print(f"Площадь под графиком функции на отрезке [{a}; {b}] равна: {area}")