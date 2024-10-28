class Categoria:
    def __init__(self, nombre, descripcion, descuento=0.0):
        self.nombre = nombre
        self.descripcion = descripcion
        self.descuento = descuento

    def actualizar(self, descripcion=None, descuento=None):
        if descripcion:
            self.descripcion = descripcion
        if descuento is not None:
            self.descuento = descuento
