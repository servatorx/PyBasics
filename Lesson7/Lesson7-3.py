class Kletka:
    def __init__(self, param1):
        self.cells = param1

    def make_order(self, rows):
        my_rows = self.cells // rows
        ost = self.cells % rows
        my_String = ""

        for stars in range(0, my_rows):
            my_String = my_String + "*" * my_rows + "\n"
        my_String += ost * "*"
        return f"{my_String}"

    def __add__(self, other):
        return f"Сумма ячеек: {self.cells + other.cells}"

    def __sub__(self, other):
        if self.cells - other.cells > 0:
            return f"Разность ячеек: {self.cells - other.cells}"
        else:
            return f"Клетка не вычитается"

    def __mul__(self, other):
        return f"Произведение ячеек: {self.cells * other.cells}"

    def __truediv__(self, other):
        return f"Деление ячеек: {self.cells // other.cells}"


my_kletka1 = Kletka(12)
my_kletka2 = Kletka(11)

print(my_kletka1.make_order(3))
print(my_kletka1 + my_kletka2)
print(my_kletka1 - my_kletka2)
print(my_kletka1 * my_kletka2)
print(my_kletka1 / my_kletka2)