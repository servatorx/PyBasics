import random
my_list = [random.randint(0, 20) for i in range (1,20)]
print(my_list)
t = [el for el in my_list if my_list.count(el) == 1]
print(t)