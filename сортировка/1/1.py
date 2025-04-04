def counting_sort(numbers):
    if not numbers:
        return []

    min_num = min(numbers)
    max_num = max(numbers)

    count = [0] * (max_num - min_num + 1)

    for num in numbers:
        count[num - min_num] += 1

    sorted_numbers = []
    for i in range(len(count)):
        sorted_numbers.extend([i + min_num] * count[i])

    return sorted_numbers


def main():
    try:
        with open('numbers.txt', 'r') as file:
            data = file.read()
            numbers = list(map(int, data.split()))

        sorted_numbers = counting_sort(numbers)

        with open('result.txt', 'w') as file:
            file.write(' '.join(map(str, sorted_numbers)))

        print("Сортировка завершена. Результат записан в result.txt")

    except FileNotFoundError:
        print("Файл numbers.txt не найден")
        
    except ValueError:
        print("Файл содержит некорректные данные (не числа)")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()