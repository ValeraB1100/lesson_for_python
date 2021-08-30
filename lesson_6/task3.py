class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name             #имя         тут я для себя перевод пишу, с английским не очень(
        self.surname = surname       #фамилия
        self.position = position     #должность
        self.income = income         #доход ссылается на словарь (оклад, премия)


class Position(Worker):
    def get_full_name(self):
        print(f"полное имя: {self.name} {self.surname}")

    def get_total_income(self):
        total = 0
        for i in self.income.values():
            total += int(i)
        print(total)

a = Position("Jon", "Smit", "Meneger", {"wage": 10000, "bonus": 1000})
a.get_full_name()
a.get_total_income()


#уахахахаха, когда тут с первого раза заработало я аж подпрыгнул от радости,
# не знаю правильно или нет, но я сделал минут за 30, во я крутой) делал сам, даже браузер не открывал,
# кроме страницы задачи
