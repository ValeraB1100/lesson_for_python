#либо я крутой, либо тут задачки простые, у меня только с первыми двумя сложности возникли,
# а потом легко пошло, за 1,5 часа три задачки сделал, а первые 2 за 2 часа)
# ну на счет первой я так и не совсем понял, с этим таймером...

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    def draw(self):
        print(f"Это {self.title}, она пишет чернилами")


class Pencil(Stationery):
    def draw(self):
        print(f"Это {self.title}, он рисует графитом")

class Handle(Stationery):
    def draw(self):
        print(f"Это {self.title}, он маркирует")

pen = Pen("ручка")
pen.draw()
pencil = Pencil("карандаш")
pencil.draw()
handle = Handle("маркер")
handle.draw()