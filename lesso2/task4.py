# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

stroka = input('введите что-нибудь: ')
lst = stroka.split()
j=0
for i in lst:
    if len(lst) > 10:
        i = i[0: 10]
    print(f'{j}. {i}')
    j+=1