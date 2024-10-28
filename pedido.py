from datetime import datetime


class Pedido:
    def __init__(self, id_pedido, cliente):
        self.id_pedido = id_pedido
        self.fecha = datetime.now()
        self.estado = "Pendiente"
        self.total = 0.0
        self.cliente = cliente
        self.detalles = []

    def agregar_detalle(self, detalle_pedido):
        self.detalles.append(detalle_pedido)
        self.calcular_total()

    def calcular_total(self):
        self.total = sum(detalle.subtotal for detalle in self.detalles)

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def eliminar_pedido(self):
        print(f"Pedido {self.id_pedido} eliminado.")

    def buscar(self, id_pedido):
        if self.id_pedido == id_pedido:
            return self
        else:
            return None
