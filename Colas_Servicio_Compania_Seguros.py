class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def tamano(self):
        return len(self.items)

    def ver_frente(self):
        if not self.esta_vacia():
            return self.items[0]
        return None

class SistemaColasSeguros:
    def __init__(self):
        self.servicios = {
            1: Cola(), 
            2: Cola(),  
            3: Cola(),  
        }
        self.numeros_atencion = {1: 0, 2: 0, 3: 0}

    def llegada_cliente(self, servicio):
        if servicio in self.servicios:
            self.numeros_atencion[servicio] += 1
            numero_cliente = self.numeros_atencion[servicio]
            self.servicios[servicio].encolar(numero_cliente)
            print(f"Cliente {numero_cliente} asignado al servicio {servicio}")
        else:
            print(f"Servicio {servicio} no existe.")

    def atender_cliente(self, servicio):
        if servicio in self.servicios:
            if not self.servicios[servicio].esta_vacia():
                cliente_atendido = self.servicios[servicio].desencolar()
                print(f"Atendiendo cliente {cliente_atendido} del servicio {servicio}")
            else:
                print(f"No hay clientes en espera para el servicio {servicio}")
        else:
            print(f"Servicio {servicio} no existe.")

sistema = SistemaColasSeguros()

while True:
    entrada = input("Ingrese 'C' para llegada de cliente o 'A' para atender, seguido del número de servicio (Ej: C1 o A2): ").strip().upper()
    
    if entrada.startswith("C"):
        servicio = int(entrada[1])
        sistema.llegada_cliente(servicio)
    elif entrada.startswith("A"):
        servicio = int(entrada[1])
        sistema.atender_cliente(servicio)
    elif entrada == "S":
        break
    else:
        print("Entrada no válida.")
