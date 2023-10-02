# ● Условие
# На вход подается число n.
# ● Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.
# ● Пример вывода:
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# 1 * 6 = 6
# ..
# 1 * 9 = 9

#Я выбираю использование императивной парадигмы:структурной парадигмы(точно не буду использовать go to),
#так как скрипт короткий то нет необходимости использовать процедурную парадигму.

n = int(input('Введите число n:'))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f'{i} * {j} = {i*j}')
    print()