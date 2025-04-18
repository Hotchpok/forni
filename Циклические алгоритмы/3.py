import random  # Импортируем модуль для генерации случайных чисел


def point_in_polygon(polygon, point):
    """
    Проверяет, находится ли точка внутри многоугольника.
    Используется алгоритм "ray casting" (метод выпускания луча).
    """
    # Распаковываем координаты проверяемой точки
    x, y = point
    # Количество вершин многоугольника
    n = len(polygon)
    # Флаг нахождения точки внутри многоугольника
    inside = False
    # Берем первую вершину многоугольника
    p1x, p1y = polygon[0]

    # Проходим по всем сторонам многоугольника (включая замыкающую сторону)
    for i in range(n + 1):
        # Берем следующую вершину (используем modulo для замыкания многоугольника)
        p2x, p2y = polygon[i % n]

        # Проверяем, находится ли точка между y-координатами стороны
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    # Если сторона не горизонтальная
                    if p1y != p2y:
                        # Находим x-координату пересечения луча и стороны
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    # Если сторона вертикальная или луч пересекает сторону слева
                    if p1x == p2x or x <= xinters:
                        # Меняем флаг (нечетное число пересечений = точка внутри)
                        inside = not inside
        # Переходим к следующей стороне
        p1x, p1y = p2x, p2y

    return inside


def monte_carlo_polygon_area(polygon, iterations=100000):
    """
    Вычисляет площадь многоугольника методом Монте-Карло.
    """
    # Находим минимальные и максимальные координаты многоугольника
    min_x = min(p[0] for p in polygon)  # Минимальная x-координата
    max_x = max(p[0] for p in polygon)  # Максимальная x-координата
    min_y = min(p[1] for p in polygon)  # Минимальная y-координата
    max_y = max(p[1] for p in polygon)  # Максимальная y-координата

    # Вычисляем площадь ограничивающего прямоугольника
    rect_area = (max_x - min_x) * (max_y - min_y)

    # Счетчик точек, попавших внутрь многоугольника
    inside_count = 0

    # Генерируем случайные точки и проверяем их принадлежность многоугольнику
    for _ in range(iterations):
        # Генерируем случайные координаты в пределах ограничивающего прямоугольника
        rand_x = random.uniform(min_x, max_x)
        rand_y = random.uniform(min_y, max_y)

        # Проверяем, попадает ли точка в многоугольник
        if point_in_polygon(polygon, (rand_x, rand_y)):
            inside_count += 1  # Увеличиваем счетчик

    # Вычисляем площадь как долю точек внутри, умноженную на площадь прямоугольника
    return (inside_count / iterations) * rect_area


# Пример использования:
# Задаем вершины многоугольника (должны быть упорядочены по часовой или против часовой стрелки)
polygon = [(0, 0), (4, 0), (4, 3), (2, 5), (0, 3)]

# Вычисляем площадь методом Монте-Карло
area = monte_carlo_polygon_area(polygon)
print(f"Приближенная площадь многоугольника: {area}")