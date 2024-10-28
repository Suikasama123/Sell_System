class DetalleFactura:
    def __init__(self, id_detalle, producto, cantidad, precio_unitario):
        self.id_detalle = id_detalle
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = self.calcular_subtotal()

    def calcular_subtotal(self):
        return self.cantidad * self.precio_unitario

    def obtener_descripcion_producto(self):
        return self.producto.descripcion

    def aplicar_descuento(self, porcentaje):
        self.precio_unitario -= self.precio_unitario * (porcentaje / 100)
        self.subtotal = self.calcular_subtotal()
