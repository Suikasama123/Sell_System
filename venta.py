from datetime import datetime


class Venta:
    def __init__(self, id_venta, vendedor, cliente, factura):
        self.id_venta = id_venta
        self.vendedor = vendedor
        self.cliente = cliente
        self.fecha = datetime.now()
        self.factura = factura

    def registrar(self):
        print(f"Venta {self.id_venta} registrada con éxito.")

    def eliminar(self):
        print(f"Venta {self.id_venta} eliminada.")

    def buscar(self, id_venta):
        if self.id_venta == id_venta:
            return self
        else:
            return None
