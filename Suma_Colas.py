class Cola:
    def __init__(self):
        self.items = []

    def Vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.Vacia():
            return self.items.pop(0)
        return None

    def tamano(self):
        return len(self.items)

    def Frente(self):
        if not self.Vacia():
            return self.items[0]
        return None

def sumar_colas(cola_a, cola_b):
    cola_resultado = Cola()
    while not cola_a.Vacia() and not cola_b.Vacia():
        valor_a = cola_a.desencolar()
        valor_b = cola_b.desencolar()
        cola_resultado.encolar(valor_a + valor_b)
    return cola_resultado

cola_a = Cola()
cola_b = Cola()

n_a = int(input("Ingrese la cantidad de elementos para la Cola A: "))
print("Ingrese los valores para la Cola A:")
for _ in range(n_a):
    valor = int(input())
    cola_a.encolar(valor)
    print(f"Valor {valor} encolado en Cola A")

n_b = int(input("Ingrese la cantidad de elementos para la Cola B: "))
print("Ingrese los valores para la Cola B:")
for _ in range(n_b):
    valor = int(input())
    cola_b.encolar(valor)
    print(f"Valor {valor} encolado en Cola B")

cola_resultado = sumar_colas(cola_a, cola_b)

print("\nCola Resultado:")
while not cola_resultado.Vacia():
    print(cola_resultado.desencolar())
