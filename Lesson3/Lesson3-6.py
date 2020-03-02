def int_func(my_word):
    new_string = []
    res = []
    for i in my_word.split():
        new_string.append(i[0].upper()+i[1:])
    res = " ".join(new_string)
    return res

print(int_func(input("Введите строку: ")))