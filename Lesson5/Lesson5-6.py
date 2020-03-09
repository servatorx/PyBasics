dict_ = {}
total = 0
with open("predm.txt", "r", encoding='UTF8') as f_obj:
    for element in f_obj:
        predm, hours = element.split(":")
        x = hours.split()
        for h in x:
            if h == "-":
                continue
            else:
                total += int(h.split("(")[0])
        dict_[str(predm)] = total
        total = 0
print(dict_)