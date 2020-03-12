class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def asphalt(self):
        massa = self._length * self._width * 25 * 0.005
        print(f"Необходимая масса асфальта: {massa}")


my_road = Road(5000, 20)
my_road.asphalt()







