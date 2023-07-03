def transform(current, target, commands, max_depth):
    if current == target:
        return commands

    if max_depth == 0:
        return None

    # Применяем первую команду
    res = transform(current * 2, target, commands + ["умножить на 2"], max_depth - 1)
    if res:
        return res

    # Применяем вторую команду
    res = transform(current + 8, target, commands + ["прибавить 8"], max_depth - 1)
    if res:
        return res

    # Применяем обе команды
    res = transform(current * 2 + 8, target, commands + ["умножить на 2", "прибавить 8"], max_depth - 1)
    if res:
        return res

    return None

# Исходные данные
start = 45
target = 376
max_depth = 4

# Решение задачи
result = transform(start, target, [], max_depth)

if result:
    print("Найдено решение: ")
    print(result)
else:
    print("Решение не найдено")