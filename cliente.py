class Cliente:
    def __init__(self, id_cliente, nombre, nit, direccion, celular):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.celular = celular

    def validar_nit(self):
        # Simulación de validación de NIT
        return True if self.nit and len(self.nit) >= 7 else False

    def mostrar_informacion(self):
        return {
            "ID Cliente": self.id_cliente,
            "Nombre": self.nombre,
            "NIT": self.nit,
            "Dirección": self.direccion,
            "Celular": self.celular,
        }
