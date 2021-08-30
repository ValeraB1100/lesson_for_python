class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("машина поехала")

    def stop(self):
        print("машина остановилась")

    def turn(self, direction):
        print(f"машина повернула {direction}")

    def show_speed(self):
        print(f"текущая скорость автомобиля {self.speed}")

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("превышена скорость!!!")
        else:
            print(f"текущая скорость автомобиля {self.speed}")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("превышена скорость!!!")
        else:
            print(f"текущая скорость автомобиля {self.speed}")


class PoliceCar(Car):
    pass

town_car = TownCar(65, "white", "Lada Granta", True)
print(town_car.name)
town_car.go()
town_car.turn("налево")
town_car.show_speed()
sport_car = SportCar(80, "black", "Lamborgini", True)
work_car = WorkCar(41, "silver", "Зил", True)
police_car = PoliceCar(60, "yellow", "Shkoda Oktavia", True)