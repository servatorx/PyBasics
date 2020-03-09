try:
    f_obj = open("text.txt", "r")
    strings_list = f_obj.readlines()
    f_obj.close()
    print("Количество строк: " + str(len(strings_list)))

    i = 1
    for words_ in strings_list:
        print("Количество слов в строке " + str(i) + ": " + str(len(words_.split())))
    i += 1

except IOError:
    print("Произошла ошибка ввода-вывода!")
