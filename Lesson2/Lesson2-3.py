print("--------- Задание 3---------")
month = int(input("Введите номер месяца"))
zima = [12,1,2]
vesna = [3,4,5]
leto = [6,7,8]
osen = [9,10,11]
if int(month) in zima:
    print("Это - зима")
elif int(month) in vesna:
    print("Это - весна")
elif int(month) in leto:
    print("Это - лето")
else:
    print("Это - осень")

print("------по словарю--------")
dict_month = {"zima": [12,1,2], "vesna": [3,4,5], "leto": [6,7,8], "osen": [9,10,11]}
#print(dict_month["zima"])
if month in dict_month["zima"]:
    print("Этот месяц - зима")
elif month in dict_month["vesna"]:
    print("Этот месяц - весна")
elif month in dict_month["leto"]:
    print("Этот месяц - лето")
else:
    print("Этот месяц - осень")
#print(dict_month.items())