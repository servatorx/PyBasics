class MyError(Exception):
    def __init__(self, text):
        self.text = text


my_list = []
while True:
    try:
        user_input = input("Введите число, для выхода - q: ")
        if user_input == "q":
            break

        if user_input.isdigit():
            my_list.append(int(user_input))
        else:
            raise MyError("Введено не число!")

    except MyError as err:
        print(err)

print(my_list)