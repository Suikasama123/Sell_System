class DetallesPedido:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        self.subtotal = self.calcular_subtotal()

    def calcular_subtotal(self):
        return self.producto.precio * self.cantidad

    def cambiar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad
        self.subtotal = self.calcular_subtotal()

    def pedir(self):
        print(f"Producto {self.producto.nombre} pedido en cantidad de {self.cantidad}.")
