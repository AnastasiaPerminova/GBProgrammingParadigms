# Корреляция
# ● Контекст
# Корреляция - статистическая мера, используемая для оценки
# связи между двумя случайными величинами.
# ● Ваша задача
# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать
# функциональную, т.к. в этом примере она значительно
# упростит вам жизнь.


from statistics import mean
from math import pow, sqrt
from functools import reduce
from scipy.stats import pearsonr


def pearson_correlation(data1, data2):
    def delta_data(data):
        mean_data = mean(data)

        def delta_element(x):
            return x - mean_data

        return list(map(delta_element, data))

    print(mean(data1))
    print(delta_data(data1))
    print(mean(data2))
    print(delta_data(data2))
    dividend = reduce(lambda x, y: x + y, list(map(lambda x, y: x * y, delta_data(data1), delta_data(data2))))

    divider = sqrt(reduce(lambda x, y: x + y,list(map(lambda x: pow(x, 2), delta_data(data1)))) *
                                                        reduce(lambda x, y: x + y, list(map(lambda x: pow(x, 2), delta_data(data2)))))
    return dividend / divider


a = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
b = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

print(pearson_correlation(a, b))
print(pearsonr(a, b))
