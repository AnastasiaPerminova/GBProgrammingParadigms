import random

array = [i for i in range(-10, 10)]
random.shuffle(array)
print(array)


def sort_list_imperative(numbers):
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


def sort_list_declarative(numbers):
    numbers.sort(reverse=True)
    return numbers


print(sort_list_declarative(array))
print(sort_list_imperative(array))
