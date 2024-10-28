class Contingencia:
    def __init__(self):
        self.estado_contingencia = False
        self.facturas_pendientes = []

    def iniciar_contingencia(self):
        self.estado_contingencia = True
        print("Modo de contingencia activado.")

    def registrar_factura(self, factura):
        if self.estado_contingencia:
            self.facturas_pendientes.append(factura)
            print(f"Factura {factura.id_factura} registrada en contingencia.")

    def enviar_facturas_pendientes(self):
        if not self.estado_contingencia and self.facturas_pendientes:
            print("Enviando facturas pendientes...")
            for factura in self.facturas_pendientes:
                factura.enviar_factura()
            self.facturas_pendientes = []
