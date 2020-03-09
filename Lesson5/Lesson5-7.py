import json
firm_list = []
dict_ = {}
aver_inc = 0
i = 0
with open("firms.txt", "r", encoding='UTF8') as f_obj:
    for element in f_obj:
        f_name, f_form, income, expences = element.split()
        real_inc = int(income) - int(expences)
        if real_inc > 0:
            aver_inc += int(income)
        dict_[f_name] = real_inc
        i += 1
aver_inc = aver_inc/i
firm_list.append(dict_)
firm_list.append({"average_profit": aver_inc})
print(firm_list)
with open("firm_json.txt", "w", encoding="UTF8") as json_file:
    json.dump(firm_list, json_file)
