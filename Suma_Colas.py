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
    
    def Pedir_Datos(self):
        n_a = int(input("Ingrese la cantidad de elementos para la Cola A y B: "))
        print("Ingrese los valores para la Cola A:")
        for _ in range(n_a):
            valor = int(input())
            cola_a.encolar(valor)
            print(f"Valor {valor} encolado en Cola A")
            print(f"Cola a: {cola_a.items}")

        print("\nIngrese los valores para la Cola B:")
        for _ in range(n_a):
            valor = int(input())
            cola_b.encolar(valor)
            print(f"Valor {valor} encolado en Cola B")
            print(f"Cola b: {cola_b.items}")

    def sumar_colas(self, cola_a, cola_b):
        while not cola_a.Vacia() and not cola_b.Vacia():
            valor_a = cola_a.desencolar()
            valor_b = cola_b.desencolar()
            print(f"\nValores a: {valor_a} y valor b: {valor_b} desencolados")
            print(f"Cola a: {cola_a.items} y Cola b: {cola_b.items}")
            self.valor_suma = valor_a + valor_b
            print(f"Suma de los valores a y b: {self.valor_suma}")
            cola_resultado.encolar(valor_a + valor_b)
            print(f"\nEncolando {self.valor_suma} en {cola_resultado.items}")
        return cola_resultado
    
    def restriccion(self):
        print("\nCola Resultado:")
        while not cola_resultado.Vacia():
            print(cola_resultado.desencolar())

cola_a = Cola()
cola_b = Cola()
cola_resultado = Cola()

cola_resultado.Pedir_Datos()
cola_resultado.sumar_colas(cola_a,cola_b)
cola_resultado.restriccion()
