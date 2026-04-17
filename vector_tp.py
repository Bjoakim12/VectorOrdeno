class Vector:
    def __init__(self, v):
        self.vector = v

    def seleccion(self):
        a = self.vector[:]
        n = len(a)

        for i in range(n):
            pos = i
            for j in range(i+1, n):
                if a[j] < a[pos]:
                    pos = j

            aux = a[i]
            a[i] = a[pos]
            a[pos] = aux

        return a

    def insercion(self):
        a = self.vector[:]
        n = len(a)

        for i in range(1, n):
            x = a[i]
            j = i - 1

            while j >= 0 and x < a[j]:
                a[j+1] = a[j]
                j = j - 1

            a[j+1] = x

        return a

    def burbujeo(self):
        a = self.vector[:]
        n = len(a)

        for i in range(n):
            for j in range(n-1):
                if a[j] > a[j+1]:
                    aux = a[j]
                    a[j] = a[j+1]
                    a[j+1] = aux

        return a


# programa principal
vec = [5, 3, 8, 1, 4]

v = Vector(vec)

print("Original:", v.vector)
print("Seleccion:", v.seleccion())
print("Insercion:", v.insercion())
print("Burbujeo:", v.burbujeo())
