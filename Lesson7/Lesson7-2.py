from abc import ABC, abstractmethod

class odezhda(ABC):
    def __init__(self, param1):
        self.param1 = param1

    @abstractmethod
    def potrebleine(self):
        pass

class palto(odezhda):
    @property
    def potrebleine(self):
        return round((self.param1/6.5+0.5),2)

class kostum(odezhda):
    def potrebleine(self):
        return round((self.param1*2+0.3),2)


my_palto = palto(10)
print(f"Потребление для пальто: {my_palto.potrebleine}")     # с @property

my_kostum = kostum(11)
print(f"Потребление для костюма: {my_kostum.potrebleine()}")  # без @property

print(f"Общий расход ткани: {my_palto.potrebleine + my_kostum.potrebleine()}")