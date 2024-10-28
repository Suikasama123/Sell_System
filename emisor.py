class Emisor:
    def __init__(self, id_emisor, nombre, nit, direccion, telefono):
        self.id_emisor = id_emisor
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.telefono = telefono

    def mostrar_informacion(self):
        return {
            "ID Emisor": self.id_emisor,
            "Nombre": self.nombre,
            "NIT": self.nit,
            "Dirección": self.direccion,
            "Teléfono": self.telefono,
        }
