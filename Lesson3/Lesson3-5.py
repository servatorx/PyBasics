def my_fc():
    stopc = False
    result = 0
    while stopc == False:

        x = input("Введите числа разделенные пробелами, q - выход: ").split()
        print(x)
        for i in range(len(x)):
            if x[i] == 'q':
                stopc = True
                #print(stopc)
            else:
                result = result + int(x[i])

        print("Текущий результат: " + str(result))

#x = input("Введите числа разделенные пробелами")
#stopc = False
my_fc()

