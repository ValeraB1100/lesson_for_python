# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

from random import randint


def generator(lst):
    for i in range(1, len(lst)):
        if lst[i] > lst[i-1]:
            yield lst[i]


list0 = []
a = int(input("введите количество элементов в списке: "))
b = int(input("введите минимальный элемент списка: "))
c = int(input("введите максимальный элемент списка: "))
while len(list0) < a:
    list0.append(randint(b, c))
print(list0)
list1 = []
for el in generator(list0):
    list1.append(el)
print(list1)