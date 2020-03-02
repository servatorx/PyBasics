def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
        z = x**y
    except ValueError:
        return "Ошибка значения"
    return z

print(my_func(2,-3))

def my_func2(x, y):
    try:
        x = float(x)
        y = int(y)
        z = x
        for _ in range(abs(y)-1):
            z = z * x
            result = 1/z
    except ValueError:
        return "Ошибка значения"
    return result

print(my_func2(2, -3))