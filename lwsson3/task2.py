# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.

def func(name, surname, age, city, mail, number):
    print(f"Имя: {name}, фамилия: {surname}, год рождения: {age}, город проживания: {city}, e-mail: {mail}, номер телефона: {number}")

func(name="Валера", surname="Будяцкий", age="05.12.2000", city="Новокузнецк", mail="vBiii1100@mail.ru", number="88005553535")