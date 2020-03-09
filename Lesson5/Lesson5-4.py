dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
try:
    f_obj = open("numbers.txt", "r", encoding='UTF8')
    f_obj_rus = open("numbers_rus.txt", "w", encoding='UTF8')
    for lines_ in f_obj:
        lin_l = lines_.split()
        eng_num = lin_l[0]
        print(dict[eng_num] + " - " + lin_l[2], file=f_obj_rus)
except IOError:
    print("Произошла ошибка ввода-вывода!")
