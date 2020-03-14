class MyError(Exception):
    def __init__(self, text):
        self.text = text


new_number = int(input("Введите целое число №1: "))
new_number2 = int(input("Введите целое число №2: "))

try:
    if new_number2 == 0:
        raise MyError("Ошибка деления на 0")
    else:
        print(int(new_number) / int(new_number2))
except MyError as err:
    print(err)