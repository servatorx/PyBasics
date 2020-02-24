my_list = [7, 5, 3, 3, 2]
i=0
length = len(my_list)
print(length)
new_num = int(input(("Введите число: ")))
x = my_list.count(new_num)
print("таких сомволов имеется: " + str(x))
for elem in my_list:
    print(elem)
    if i == (length - 1):
        my_list.append(new_num)
        break
    if new_num >= elem:
        if my_list.count(new_num) > 1 and new_num == my_list[i+1]:
            print("пропустили " + str(x) + " чисел " + str(new_num))
            i = i + x
        my_list.insert(i,new_num)
        break
    i = i + 1
print(my_list)