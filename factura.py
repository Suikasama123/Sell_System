import qrcode
import uuid
import base64
import io
import xml.etree.ElementTree as ET
from certificado_digital import CertificadoDigital
from datetime import datetime


class Factura:
    def __init__(self, id_factura, cliente, emisor):
        self.id_factura = id_factura
        self.fecha_emision = datetime.now()
        self.cliente = cliente
        self.emisor = emisor
        self.detalles = []
        self.total = 0.0
        self.estado = "Pendiente"
        self.codigo_qr = None
        self.firma_digital = None
        self.CUF = self.generar_CUF()

    def agregar_detalle(self, detalle):
        self.detalles.append(detalle)
        self.calcular_total()

    def calcular_total(self):
        self.total = sum(detalle.subtotal for detalle in self.detalles)

    def generar_codigo_qr(self):
        data_qr = f"FacturaID:{self.id_factura}|CUF:{self.CUF}|Total:{self.total}"
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data_qr)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        # Convertir imagen a base64 para almacenar
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        self.codigo_qr = base64.b64encode(buffered.getvalue()).decode()

    def firmar_factura(self, certificado_digital):
        data = f"{self.id_factura}{self.fecha_emision}{self.total}"
        self.firma_digital = certificado_digital.firmar_documento(data)

    def validar_datos(self):
        return all([self.cliente, self.emisor, self.detalles, self.total > 0])

    def exportar_XML(self):
        factura_element = ET.Element("Factura")
        ET.SubElement(factura_element, "ID").text = str(self.id_factura)
        ET.SubElement(factura_element, "FechaEmision").text = self.fecha_emision.isoformat()
        ET.SubElement(factura_element, "Total").text = str(self.total)
        # Agregar más elementos según sea necesario
        tree = ET.ElementTree(factura_element)
        tree.write(f"factura_{self.id_factura}.xml")

    def generar_CUF(self):
        # Simulación de generación de CUF
        return str(uuid.uuid4())

    def enviar_factura(self):
        # Simulación de envío de factura
        print(f"Factura {self.id_factura} enviada a la Administración Tributaria.")
