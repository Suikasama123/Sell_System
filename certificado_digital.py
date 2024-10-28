import hashlib


class CertificadoDigital:
    def __init__(self, ruta_certificado, contrasena):
        self.ruta_certificado = ruta_certificado
        self.contrasena = contrasena
        self.certificado = None

    def cargar_certificado(self):
        # Simulación de carga de certificado
        self.certificado = f"Certificado cargado desde {self.ruta_certificado}"

    def firmar_documento(self, data):
        # Simulación de firma digital utilizando hash SHA256
        firma = hashlib.sha256((data + self.contrasena).encode()).hexdigest()
        return firma

    def verificar_firma(self, data, firma):
        firma_calculada = hashlib.sha256((data + self.contrasena).encode()).hexdigest()
        return firma_calculada == firma
