class Vendedor:
    def __init__(self, id_vendedor, nombre, username, password, rol):
        self.id_vendedor = id_vendedor
        self.nombre = nombre
        self.username = username
        self.password = password
        self.rol = rol

    def autenticar(self, username, password):
        return self.username == username and self.password == password

    def mostrar_informacion(self):
        return {
            "ID Vendedor": self.id_vendedor,
            "Nombre": self.nombre,
            "Rol": self.rol,
        }
