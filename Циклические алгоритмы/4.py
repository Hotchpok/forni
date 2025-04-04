import random


# Наша цель: найти такие x1, x2, x3, x4, чтобы x1² + x2² + x3² + x4² = 30
def target_function(x1, x2, x3, x4):
    return x1 ** 2 + x2 ** 2 + x3 ** 2 + x4 ** 2


# Параметры алгоритма
TARGET_VALUE = 30  # Желаемый результат (правая часть уравнения)
NUM_VARIABLES = 4  # Сколько переменных ищем (x1-x4)
POPULATION_SIZE = 50  # Количество решений в популяции
MAX_GENERATIONS = 100  # Максимальное число поколений
MUTATION_CHANCE = 0.2  # Вероятность мутации


# Создает случайное решение (x1, x2, x3, x4)
def create_random_solution():
    return [random.uniform(-5, 5) for _ in range(NUM_VARIABLES)]


# Оценивает качество решения (чем ближе к 0, тем лучше)
def evaluate(solution):
    x1, x2, x3, x4 = solution
    return abs(target_function(x1, x2, x3, x4) - TARGET_VALUE)


# Выбирает родителя из популяции (турнирный отбор)
def select_parent(population):
    # Берем 3 случайных решения и выбираем лучшее
    candidates = random.sample(population, 3)
    return min(candidates, key=lambda x: evaluate(x))


# Скрещивает двух родителей для получения потомков
def crossover(parent1, parent2):
    # Простое смешивание: берем половину генов от каждого родителя
    child = []
    for i in range(NUM_VARIABLES):
        if random.random() < 0.5:
            child.append(parent1[i])
        else:
            child.append(parent2[i])
    return child


# Добавляет случайные изменения в решение
def mutate(solution):
    for i in range(NUM_VARIABLES):
        if random.random() < MUTATION_CHANCE:
            # Меняем значение на небольшое случайное число
            solution[i] += random.uniform(-1, 1)
    return solution


# Основной алгоритм
def genetic_algorithm():
    # Создаем начальную популяцию
    population = [create_random_solution() for _ in range(POPULATION_SIZE)]
    best_solution = None
    best_score = float('inf')

    for generation in range(MAX_GENERATIONS):
        # Оцениваем все решения
        population.sort(key=lambda x: evaluate(x))
        current_best = population[0]
        current_score = evaluate(current_best)

        # Обновляем лучшее решение
        if current_score < best_score:
            best_solution = current_best.copy()
            best_score = current_score

        # Если нашли хорошее решение - останавливаемся
        if best_score < 0.001:
            print(f"Найдено решение на поколении {generation}")
            break

        # Создаем новое поколение
        new_generation = []

        # Сохраняем 2 лучших решения (элитизм)
        new_generation.extend(population[:2])

        # Заполняем популяцию
        while len(new_generation) < POPULATION_SIZE:
            # Выбираем родителей
            parent1 = select_parent(population)
            parent2 = select_parent(population)

            # Создаем потомка
            child = crossover(parent1, parent2)
            child = mutate(child)

            new_generation.append(child)

        population = new_generation

        # Выводим прогресс каждые 10 поколений
        if generation % 10 == 0:
            print(f"Поколение {generation}: Лучший результат = {best_score:.4f}")

    return best_solution


# Запускаем алгоритм
print("Поиск решения...")
solution = genetic_algorithm()
x1, x2, x3, x4 = solution
print(f"\nНайдено решение:")
print(f"x1 = {x1:.4f}, x2 = {x2:.4f}, x3 = {x3:.4f}, x4 = {x4:.4f}")
print(
    f"Проверка: {x1 ** 2:.2f} + {x2 ** 2:.2f} + {x3 ** 2:.2f} + {x4 ** 2:.2f} = {target_function(x1, x2, x3, x4):.2f} (цель: {TARGET_VALUE})")