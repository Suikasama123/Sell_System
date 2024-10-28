class Producto:
    def __init__(self, id_producto, nombre, descripcion, precio, codigo, cantidad_disponible, categoria=None):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.codigo = codigo
        self.cantidad_disponible = cantidad_disponible
        self.categoria = categoria

    def mostrar_informacion(self):
        return {
            "ID Producto": self.id_producto,
            "Nombre": self.nombre,
            "Descripción": self.descripcion,
            "Precio": self.precio,
            "Código": self.codigo,
            "Cantidad Disponible": self.cantidad_disponible,
            "Categoría": self.categoria.nombre if self.categoria else "Sin categoría",
        }

    def incrementar_cantidad(self, nro):
        self.cantidad_disponible += nro

    def decrementar_cantidad(self, nro):
        if nro <= self.cantidad_disponible:
            self.cantidad_disponible -= nro
        else:
            raise ValueError("No hay suficiente stock del producto.")
