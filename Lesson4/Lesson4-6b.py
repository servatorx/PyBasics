from itertools import cycle, count
from sys import argv
try:
    print("q - выход")
    sc_n, my_str = argv
    my_list = my_str.split()
    #print(my_list)
    i_cyc = cycle(my_list)
    exit = ""

    while exit != 'q':
        print(next(i_cyc), end ='')
        exit = input()

except ValueError:
    print("Неверные параметры!")