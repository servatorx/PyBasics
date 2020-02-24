# Задание 1

x = 1
y = 17.2
st = "Sum = "
z = x+y
st = st + str(z)
print(st)
print('-----------------------')
# Задание 2
print('Введите секунды: ')
sec = int(input())
hours = sec//3600
sec = sec - hours*3600
if hours <10:
    hours_str = "0"+str(hours)
else:
    hours_str=str(hours)

minutes = sec//60
sec = sec - minutes*60
if minutes <10:
    minutes_str = "0"+str(minutes)
else:
    minutes_str=str(minutes)

if sec <10:
    sec_str = "0"+str(sec)
else:
    sec_str=str(sec)

print('Время: {}:{}:{}'.format(hours_str, minutes_str,sec_str))
print('-----------------------')
# Задание 3
print('Введите число: ')
my_number = int(input())
my_num2 = str(my_number) + str(my_number)
my_num3 = str(my_number) + str(my_number) + str(my_number)
summa = int(my_number)+int(my_num2)+int(my_num3)
print(str(summa))

print('-----------------------')

# Задание 4

print('Введите число: ')
my_number = int(input())
if my_number < 10:
    max = my_number
else:
    max = 1
while my_number >=9:
        new_number= my_number%10

        if new_number> max: max =new_number
        print(str(new_number))
        my_number = my_number//10
else:
        print('самое большое число: ' + str(max))

print('-----------------------')

# Задание 5
print('Введите выручку: ')
income = int(input())
print('Введите расходы: ')
expenses = int(input())
if income >= expenses:
    print('Фирма работает с прибылью')
    profit = income/expenses
    print('Рентабельность: ' + str(profit))
    print('Введите количество сотрудников: ')
    persons = int(input())
    profit2 = income/persons
    print('Прибыль на одного сотрудника: ' + str(profit2))
else:
    print('Фирма работает с убытками')

print('-----------------------')

# Задание 6
print('Введите результат в первый день (А): ')
a = int(input())
print('Введите необходимое количество км (В): ')
b = int(input())
z = a
den = 1
while z < b:
    den = den + 1
    z = z * 0.1 + z
    print(str(round(z, 2)))
else:
    print('На день: ' + str(den) + ' спортмен достиген резальтат не менее ' + str(b) + ' км.')


