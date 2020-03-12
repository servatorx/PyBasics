class Stationery:
    def __init__(self, title="картинка"):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки: {self.title}")

class Pen(Stationery):
    def draw(self):
        print(f"Рисум с помощью РУЧКИ: {self.title}")

class Pencil(Stationery):
    def draw(self):
        print(f"Рисум с помощью КАРАНДАША: {self.title}")

class Handle(Stationery):
    def draw(self):
        print(f"Рисум с помощью МАРКЕРА: {self.title}")

my_st = Stationery("чертеж")
my_st.draw()

my_pen = Pen("человечек")
my_pen.draw()
my_pencil = Pencil("схема")
my_pencil.draw()
my_handle = Handle()
my_handle.draw()