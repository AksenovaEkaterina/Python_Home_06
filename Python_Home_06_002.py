# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

from itertools import count
from typing import List


def find(list1):
    max_elem = max(list1)+1
    count = [0]*max_elem
    for i in list1:
        count[i]+=1
    data = [i for i in list1]
    result = list(filter(lambda i: count[i]==1, data))
    print(result)
list_num = [1, 2, 3, 5, 1, 5, 3, 10]
find(list_num)