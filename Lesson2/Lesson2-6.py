#my_list = [
#    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
#    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
#    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."}),
#    (2, {"название": "тонер", "цена": 99, "количество": 15, "eд": "кг."})
#]
namet = ""
my_list = []
new_tupl = ()
added_dict = dict.fromkeys(["название", "цена", "количество", "ед"])
k = 1

print("Введите запрашиваемые данные, для окончания ввода введите вместо названия: QQ")
while True:
    namet = str(input("Ввеедите НАЗВАНИЕ товара: "))
    print(namet)
    if namet.upper() == 'QQ':
        break
    price = input("Ввеедите ЦЕНУ товара: ")
    qty = input("Ввеедите КОЛИЧЕСТВО товара: ")
    units = input("Ввеедите ЕДИНИЦЫ ИЗМЕРЕНИЯ товара: ")
    added_dict["название"] = str(namet)
    added_dict["цена"] = price
    added_dict["количество"] = qty
    added_dict["ед"] = str(units)
    new_tupl = (k, added_dict.copy())
    my_list.append(new_tupl)
    added_dict.clear()
    k= k + 1

print(my_list)
i = 0
j = 0
new_dict = {}
new_dict_coll = []
dict_coll = []
t = my_list[0]
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
