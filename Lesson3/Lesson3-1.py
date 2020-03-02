def division(numb1, numb2):
    try:
        n1 = int(numb1)
        n2 = int(numb2)
        result = n1 / n2
    except ZeroDivisionError:
        return "Ошибка деления на 0"
    except ValueError:
        return "Ошибка формата числа"
    return result
num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")
print(division(num1,num2))
