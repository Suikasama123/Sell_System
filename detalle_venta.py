class DetalleVenta:
    def __init__(self):
        self.items = []

    def agregar(self, producto, cantidad):
        if cantidad <= producto.cantidad_disponible:
            subtotal = producto.precio * cantidad
            self.items.append({
                "producto": producto,
                "cantidad": cantidad,
                "subtotal": subtotal
            })
            producto.decrementar_cantidad(cantidad)
        else:
            raise ValueError("Cantidad solicitada no disponible en stock.")

    def eliminar_producto(self, producto):
        self.items = [item for item in self.items if item["producto"] != producto]

    def calcular_total(self):
        return sum(item["subtotal"] for item in self.items)

    def finalizar_compra(self):
        total = self.calcular_total()
        print(f"Compra finalizada. Total a pagar: {total}")
        return total
