import random
class Vector:
    def __init__(self):
        self.vector = []
    
    def orden_seleccion(self):
        pass

    def orden_insercion(self):
        n = len(self.vector)

        for i in range(1, n):
            x = self.vector[i]
            j = i - 1

            while j >= 0 and x < self.vector[j]:
                self.vector[j + 1] = self.vector[j]
                j = j - 1

            self.vector[j + 1] = x

    def orden_burbujeo(self):
        pass
    
    # Métodos para generar vectores
    def generar_ordenado(self, n):
        self.vector = list(range(n))
    
    def generar_desordenado(self, n):
        self.vector = list(range(n, 0, -1))  # descendente
    
    def generar_random(self, n):
        self.vector = [random.randint(0, 100) for _ in range(n)]
