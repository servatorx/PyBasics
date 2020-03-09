try:
    f_obj = open("salary.txt", "r", encoding='UTF8')
    strings_list = f_obj.readlines()
    f_obj.close()
    i = 1
    salary_sum = 0
    for lines_ in strings_list:
        fam_zp = lines_.split()
        salary_sum += float(fam_zp[1])
        if float(fam_zp[1]) < 20000:
            print(fam_zp[0])
        i += 1

except IOError:
    print("Произошла ошибка ввода-вывода!")
print("Средний доход сотрудников: " + str(round(salary_sum/i,2)))