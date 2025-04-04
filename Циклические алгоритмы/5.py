def find_shortest_path(maze):
    # Находим стартовую и финишную позиции
    start = None
    end = None
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'С':
                start = (i, j)
            elif maze[i][j] == 'В':
                end = (i, j)

    if not start or not end:
        return None, "Нет старта или выхода в лабиринте!"

    # Возможные направления движения (вверх, вниз, влево, вправо)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Очередь для BFS: хранит (x, y, длина пути, сам путь)
    queue = []
    queue.append((start[0], start[1], 0, [start]))

    # Множество посещённых клеток
    visited = set()
    visited.add(start)

    while queue:
        x, y, dist, path = queue.pop(0)  # Извлекаем первый элемент (FIFO)

        # Если дошли до выхода
        if (x, y) == end:
            return dist, path

        # Проверяем все соседние клетки
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Проверяем, что не вышли за границы лабиринта
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                # Проверяем, что клетка не стена и не посещена
                if maze[nx][ny] != 'X' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    new_path = path + [(nx, ny)]
                    queue.append((nx, ny, dist + 1, new_path))

    return None, "Путь не найден!"


# Задаём лабиринт (X — стены, 0 — свободные клетки, С — старт, В — выход)
maze = [
    ['С', '0', '0', '0', '0', 'X', '0', '0'],
    ['0', '0', 'X', '0', '0', 'X', '0', '0'],
    ['X', '0', 'X', '0', '0', 'X', '0', 'X'],
    ['0', '0', 'X', '0', '0', '0', '0', '0'],
    ['0', '0', 'X', '0', 'X', 'X', 'X', '0'],
    ['X', '0', '0', '0', '0', '0', '0', '0'],
    ['X', '0', '0', '0', 'X', '0', '0', 'В']
]

# Находим кратчайший путь
length, path = find_shortest_path(maze)

if length is not None:
    print(f"Длина кратчайшего пути: {length}")
    print("Путь (координаты (строка, столбец)):")
    for step in path:
        print(step, end=" → " if step != path[-1] else "\n")
else:
    print(path)