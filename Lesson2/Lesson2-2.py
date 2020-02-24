print("--------- Задание 2---------")
i = int(input("Сколько ввести элементов?"))
my_list = []
for elem_no in range(0,i):
    new_elem = input('Введите элемент списка: ')
    my_list.append(new_elem)
print("Начальный спискок: " + str(my_list))

if i%2 > 0:
    j = i - 1
else:
    j = i
for elem_no in range(0,j-1,2):
    #print(str(elem_no))
    my_list[elem_no], my_list[elem_no+1] = my_list[elem_no+1], my_list[elem_no]
print("Итоговый список: " + str(my_list))

