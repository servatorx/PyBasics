from sys import argv
try:
    sc_n, hours, rate, bonus = argv
    total_zp = float(hours)*float(rate) + float(bonus)
    print("Зарплата: " + str(total_zp))
except ValueError:
    print("Неверные параметры!")

