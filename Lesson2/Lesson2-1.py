print("--------- Задание 1---------")
my_list = [12,(2.6,"abc"),'string_here',True,{"a":6,"b":11.2}]
print("Переменная my_list типа: " + str(type(my_list)))

for i in my_list:
    text = "Элемент " + str(i) + " имеет тип: " + str(type(i))
    print(text)
