# Написать программу на любом языке в любой парадигме для
# бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого
# элемента нет в массиве.

# Для решения данной задачи я использовала императивную парадигму: структурную парадигму(команды выполняются одна за
# другой, не используется go to), процедурную парадигму для создания отдельной функции бинарного поиска; а также
# декларативную парадигму: функциональную парадигму(функции sorted(), len() "зашиты" в Python).
def binary_search(array, x):
    if array == sorted(array):
        i = len(array) // 2
        k = i
        while i > 1:
            if x == array[i]:
                return k
            if x > array[i]:
                array = list(array[i:])
                i = len(array) // 2
                k += i
            if x < array[i]:
                array = list(array[:i])
                i = len(array) // 2
                k -= i
        if i == 1:
            if x == array[i]:
                return k
            if x == array[0]:
                return k - 1
            else:
                return -1
    else:
        print("Массив был неотсортирован.Бинарный поиск был невозможен. Поиск произведен в отсортированном массиве.")
        array1 = sorted(array)
        print(array1)
        return binary_search(array1, x)


arr = [1, 2, 3, 4, 5, 6, 7, 8]
a = 8
print(binary_search(arr, a))

arr1 = [26, 23, 45, 67, 77, 354, 324, 1, 234]
a1 = 77
print(binary_search(arr1, a1))
