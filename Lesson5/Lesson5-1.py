
while True:
    line = input("Введите данные (пустой ввод - выход): ")
    if line == "":
        break
    try:
        f_obj = open("text.txt", "a")
        print(line, file = f_obj)
        f_obj.close()
    except IOError:
        print("Произошла ошибка ввода-вывода!")

