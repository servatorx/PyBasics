class complex_d:
    def __init__(self, comp_d):
        self.real_p, self.im_part = self.spl_com(comp_d)
        print(self.real_p, self.im_part)

    def spl_com(self, param):
        i = param.split('+')[0]
        j = param.split('+')[1]
        return int(i), int(j[0:-1])


    def __add__(self, other):
        tp_r = self.real_p + other.real_p
        tp_i = self.im_part + other.im_part
        return f"{str(tp_r)} + {str(tp_i)}i"

    def __mul__(self, other):
        tp_r = (self.real_p * other.real_p - self.im_part * other.im_part)
        tp_i = (self.real_p * other.im_part + other.real_p * self.im_part)
        return f"{str(tp_r)} + {str(tp_i)}i"


cp1 = complex_d("2+1i")
cp2 = complex_d("3+4i")
print(cp1 + cp2)
print(cp1 * cp2)