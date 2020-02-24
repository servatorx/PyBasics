print("--------- Задание 4---------")
my_string = input("Введите несколько слов: ")
my_list = my_string.split(" ")
#print(my_list)
i = 1
for elem in my_list:
    print(str(i) + ". " + elem)
    i = i + 1
