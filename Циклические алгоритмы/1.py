def korenb(f, a, b, eps):
    if f(a) * f(b) >= 0:
        raise ValueError('nuzhni Raznie Znacheniya')

    while (b - a) / 2 > eps:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

def f(x):
    return x**3 - x - 2


a = 1
b = 2
eps = 1e-6

root = korenb(f, a, b, eps)
print(f"KopeHb ypaBHeHNR: {root}")