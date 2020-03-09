from random import randint
try:
    f_obj = open("rand_numbers.txt", "w", encoding='UTF8')
    summ = 0
    for i in range(1, 20):
        x = randint(0,100)
        summ += x
        f_obj.write(str(x) + " ")
except IOError:
    print("Произошла ошибка ввода-вывода!")
print("Сумма всех цифр: " + str(summ))