# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
# необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то
# новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
el_rey = int(input('введите число или  911 для выхода: '))
while el_rey != 911:
    for i in range(len(my_list)): #проходим по списку
        if my_list[i] == el_rey:      #если есть похожий элемент то вставляем после него
            my_list.insert(i + 1, el_rey)
            break
        elif my_list[0] < el_rey:  #если елемент больше первого в списке, то вставляем на первое место
            my_list.insert(0, el_rey)
        elif my_list[-1] > el_rey:    # если елемент менбше последнего, то вставляем в конец
            my_list.append(el_rey)
        elif my_list[i] > el_rey and my_list[i + 1] < el_rey:  #если елемент меньше предыдущего, но больше следующего,
            my_list.insert(i + 1, el_rey)                   #то вставляем между ними
            break
    print(f"текущий список: {my_list}")
    el_rey = int(input("Введите число или 911 для выхода: "))