from functools import reduce
my_list = [el for el in range(100, 1001,2)]
my_reduce = lambda p_1, p_2: p_1 * p_2

print(reduce(my_reduce,my_list))