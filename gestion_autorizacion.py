import uuid
from datetime import datetime, timedelta


class GestionAutorizacion:
    def __init__(self):
        self.CUIS = self.generar_CUIS()
        self.CUFD = self.generar_CUFD()
        self.fecha_vencimiento_CUIS = datetime.now() + timedelta(days=365)
        self.fecha_vencimiento_CUFD = datetime.now() + timedelta(days=1)

    def verificar_vigencia_CUIS(self):
        return datetime.now() < self.fecha_vencimiento_CUIS

    def verificar_vigencia_CUFD(self):
        return datetime.now() < self.fecha_vencimiento_CUFD

    def renovar_CUIS(self):
        self.CUIS = self.generar_CUIS()
        self.fecha_vencimiento_CUIS = datetime.now() + timedelta(days=365)

    def renovar_CUFD(self):
        self.CUFD = self.generar_CUFD()
        self.fecha_vencimiento_CUFD = datetime.now() + timedelta(days=1)

    def generar_CUIS(self):
        # Simulación de generación de CUIS
        return f"CUIS-{uuid.uuid4()}"

    def generar_CUFD(self):
        # Simulación de generación de CUFD
        return f"CUFD-{uuid.uuid4()}"

    def simular_autorizacion(self):
        print("Simulación de autorización exitosa.")
