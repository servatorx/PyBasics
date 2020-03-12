class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала")
    def stop(self):
        print(f"Машина {self.name} остановилась")
    def turn(self, direction):
        print(f"Машина повернула {direction}")
    def showSpeed(self):
        print(f"Машина {self.name} имеет скорость: {self.speed}")


class TownCar(Car):
    def showSpeed(self):
        if self.speed > 60:
            print(f"Городская машина {self.name} имеет скорость: {self.speed}, скорость превышена!")
        else:
            print(f"Городская машина {self.name} имеет скорость: {self.speed}")

class WorkCar(Car):
    def showSpeed(self):
        if self.speed > 40:
            print(f"Рабочая машина {self.name} имеет скорость: {self.speed}, скорость превышена!")
        else:
            print(f"Рабочая машина {self.name} имеет скорость: {self.speed}")

class PoliceCar(Car):
    def showSpeed(self):
        if self.is_police == True:
            print(f"Машина {self.name} имеет скорость: {self.speed}, но она полицейская!")

my_car1 = Car(40, "красный", "Lexus")
my_car1.go()
my_car1.turn("направо")
my_car1.showSpeed()
town_car1 = TownCar(65, "белый", "Lada")
town_car1.go()
town_car1.showSpeed()
town_car2 = TownCar(59, "зеленый", "BMW")
town_car2.showSpeed()
work_car1 = WorkCar(45, "Оранжевый", "мусоровоз")
work_car1.turn("направо")
work_car1.turn("налево")
work_car1.showSpeed()
pol_car = PoliceCar(120, "белый", "Camry", True)
pol_car.showSpeed()