class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for el in self.matrix:
            for i in el:
                print(str(i) + " ", end="")
            print()
        return ""
    def __add__(self, other):
            k = 0
            tp = []
            for i in self.matrix:
                n = 0
                tp.append([])
                for j in i:

                    summ = j + other.matrix[k][n]
                    #print(tp)
                    tp[k].insert(n+1,summ)

                    n +=1
                k+=1
            return tp


m_1 = Matrix([[1,2, 3],[4,5, 3],[7,8, 0]])
print(m_1)
m3 = Matrix([[13,2,5],[3,4,1],[0,3,1]])
print(m3)

#m4 = Matrix(m_1.__add__(m3))
m4 = Matrix(m_1 + m3)
print("Сумма матриц:")
print(m4)
