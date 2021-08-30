from time import monotonic
# не понял что тут требовалось Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

# аааааа, я гееений, после решения второй тут убрал всякую фигню, так лучше,
# но все равно как-то не очень получилось, но это работает


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        if self.__color != "красный":
            print("сначала должен идти красный, потом желтый, в конце зеленый и никак иначе")
            exit()
        lst = ["красный", "желтый", "зеленый"]
        t = monotonic()
        i = 0
        while i < 7:
            if monotonic() - t > 1:
                t = monotonic()
                print(f"до смены {self.__color} сигнала на "
                      f"{lst[lst.index(self.__color) + 1]} осталось {7 - i}")
                i += 1
        i = 0
        while i < 2:
            if monotonic() - t > 1:
                t = monotonic()
                print(f"до смены {lst[lst.index(self.__color) + 1]} сигнала на "
                      f"{lst[lst.index(self.__color) + 2]} осталось {2 - i}")
                i += 1
        i = 0
        while i < 7:
            if monotonic() - t > 1:
                t = monotonic()
                print(f"до смены {lst[lst.index(self.__color) + 2]} сигнала на "
                      f"{self.__color} осталось {7 - i}")
                i += 1


a = TrafficLight("красный")
a.running()
