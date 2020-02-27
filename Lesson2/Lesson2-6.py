my_list = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."}),
    (2, {"название": "тонер", "цена": 99, "количество": 15, "eд": "кг."})
]
i = 0
j = 0
new_dict = {}
new_dict_coll = []
dict_coll = []
t = my_list[1]
x=t[1]
mykeys = x.keys()
print(mykeys)
for newkey in mykeys:
    for elem_t in my_list:
        x = elem_t[1]
        new_dict_coll.append(x[newkey])
        j = j +1
    dict_coll.append(new_dict_coll[:])
    new_dict_coll.clear()
    new_dict[newkey] = dict_coll[i]
    print(str(i))
    i = i + 1
print("---------Исходный список--------")
print(my_list)
print("---------------------------------")
print("---------Итоговый словарь--------")
print(new_dict)
print("---------------------------------")
