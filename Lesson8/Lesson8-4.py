
class Warehouse:
    def __init__(self, name):
        self.name = name
        self.storage = {}

    def inc(self, item_name, qty):
        old_item = self.storage.get(item_name)
        #print(old_item)
        if old_item is not None:
            self.storage[item_name] = qty + int(old_item)
        else:
            self.storage[item_name] = qty
        #print(self.storage)

    def out(self, item_name, qty):
        old_value = self.storage.get(item_name)
        print(f"Было на складе: {old_value}")
        if old_value is not None:
            if old_value < qty:
                print(f"На складе нет достатоного количества товара: {item_name}")
            else:
                self.storage[item_name] = int(old_value) - qty
        else:
            #self.storage[item_name] = qty
            print(f"На складе нет: {item_name}")
        print(f"Стало на складе: {self.storage[item_name]}")
        #print(self.storage)


class electronics:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def __str__(self):
        return f"Модель {self.name}"


class monitor(electronics):
    def __init__(self, name, brand, size):
        super().__init__(name, brand)
        self.size = size


class printer(electronics):
    def __init__(self, name, brand, ppm):
        super().__init__(name, brand)
        self.ppm = ppm


class scanner(electronics):
    def __init__(self, name, brand, color):
        super().__init__(name, brand)
        self.color = color

def cls():
    print ('\n' * 15)

def showWhItems(WH_name):
    #cls()
    i = 1
    my_list = []
    print(f"На складе {WH_name.name}:")
    for el in WH_name.storage:
        print(f"{i} - Модель: {el}, количество: {WH_name.storage[el]}")
        my_list.append([el, i-1])

        i += 1
    return my_list

def moveItems(wh1, wh2, item_code, qty):
    #cls()
    print(f"Перемещение товара: {item_code} ")
    #print(f"Имеется на складе: {wh1.storage[item_code]}")
    if int(qty) > wh1.storage[item_code]:
        print("Нехватает количества товара для перемещения!")
    else:
        Warehouse.out(wh1, item_code, qty)
        Warehouse.inc(wh2, item_code, qty)
def showQtys():
    print(f"На складе {WH1.name}:")
    for el in WH1.storage:
        print(f"Модель: {el}, количество: {WH1.storage[el]}")
    print("---------------------------")
    print(f"На складе {WH2.name}:")
    for el in WH2.storage:
        print(f"Модель: {el}, количество: {WH2.storage[el]}")

class MyError(Exception):
    def __init__(self, text):
        self.text = text

monitor1 = monitor("SP-9492", "Samsung", 24)
monitor2 = monitor("VP-32168-4K", "ViewSonic", 37)
printer1 = printer("BRN-1056", "Brother", 22)
printer2 = printer("LJ1046", "HP", 16)
scanner1 = scanner("T1054", "Epson", "Color")
scanner1 = scanner("PL33", "Canon", "b/w")

#print(monitor1)

WH1 = Warehouse("Moscow")
WH2 = Warehouse("London")
WH1.inc(monitor1.name, 2)
WH1.inc(monitor2.name, 5)
WH1.inc(printer1.name, 13)
WH2.inc(scanner1.name, 4)
WH2.inc(monitor2.name, 6)
WH2.inc(printer2.name, 1000)

cls()
print(f"На складе {WH1.name}:")
for el in WH1.storage:
    print(f"Модель: {el}, количество: {WH1.storage[el]}")
print("---------------------------")
print(f"На складе {WH2.name}:")
for el in WH2.storage:
    print(f"Модель: {el}, количество: {WH2.storage[el]}")
#WH2.inc(printer2.name, 14)
#WH2.out(printer2.name, 13)



while True:
    print("---------------------------")
    print("1 - Перемещение товара между скаладми")
    print("2 - Посмотреть остатки")
    print("q - Выход")
    user_code = input("Введите выбор действия: ")
    if user_code =="q":
        break
    if not user_code.isdigit():
        print("Ошибочный ввод")
        break
    if int(user_code) == 1:
        cls()
        print("С какого на какой склад переместить товары?")
        print(f"1 - С {WH1.name} на {WH2.name}")
        print(f"2 - С {WH2.name} на {WH1.name}")
        user_code = input()
        if int(user_code) == 1:
            items = showWhItems(WH1)
            try:
                user_code = input("Введите номер товара для перемещения: ")
                qty = input("Введите количество товара для перемещения: ")
                if user_code.isdigit() and qty.isdigit():
                    cls()
                    moveItems(WH1, WH2, items[(int(user_code)) - 1][0], int(qty))
                    print("Остатки после перемещения:")
                    showWhItems(WH1)
                else:
                    raise MyError("Введено не число!")
            except MyError as err:
                print(err)
                user_code = 0
        if int(user_code) == 2:
            items = showWhItems(WH2)
            try:
                user_code = input("Введите номер товара для перемещения: ")
                qty = input("Введите количество товара для перемещения: ")
                if user_code.isdigit() and qty.isdigit():
                    cls()
                    moveItems(WH2, WH1, items[(int(user_code)) - 1][0], int(qty))
                    print("Остатки после перемещения:")
                    showWhItems(WH2)
                else:
                    raise MyError("Введено не число!")
            except MyError as err:
                print(err)
                user_code = 0
    if int(user_code) == 2:
        cls()
        showQtys()


