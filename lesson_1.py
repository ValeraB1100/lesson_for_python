# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько
# чисел и строк и сохраните в переменные, выведите на экран.

a = 100
print(a)
b = int(input("Введите число"))
c = str(input("Введите строку"))
print(b)
print(с)

#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в
# формате чч:мм:сс. Используйте форматирование строк.

timeuser = int(input('Введите время в секундах: '))
hour = timeuser // 3600
print(hour)
minute = timeuser % 3600 // 60
print(minute)
seconds = timeuser % 3600 % 60
print(seconds)
print(f'Время {hour:02}:{minute:02}:{seconds:02}')

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем
# 3 + 33 + 333 = 369.

n = int(input("Введите число: "))
summa = n + int(str(n) * 2) + int(str(n) * 3)
print(summa)

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.

a = input()
i = 0
c = 0
while len(a) > i:
    if c<int(a[i]):
        c = int(a[i])
    i += 1
print(c)

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

viruchka = int(input("Введите значение выручки:"))
zaderzka = int(input("Введите значение издержек:"))
a = viruchka - zaderzka

if viruchka > zaderzka:
    print("работаем с прибылью")
    rent = a / viruchka
else:
    print("работаем с издержками")
chiclsotr = int(input("Введите численность ваших сотрудников: "))
odinsotr =  a / chiclsotr
print(odinsotr)

# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день
# спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий
# результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить
# одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
#
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

a = int(input('результат в первый день: '))
b = int(input('конечный результат: '))
c = 1 #номер дня
while a < b:
    a = a * 1.1
    c += 1
print(c)