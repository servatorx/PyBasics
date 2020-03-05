from itertools import cycle, count
from sys import argv
try:
    print("q - выход")
    sc_n, start_num = argv
    for i in count(int(start_num)):
        print(str(i))
        exit = input()
        if exit == "q":
            break

except ValueError:
    print("Неверные параметры!")