import xml.etree.ElementTree as ET
from certificado_digital import CertificadoDigital


class AdministradorXML:
    def __init__(self, certificado_digital):
        self.xml_factura = ""
        self.ruta_archivo = ""
        self.certificado_digital = certificado_digital

    def generar_XML(self, factura):
        factura_element = ET.Element("Factura")
        ET.SubElement(factura_element, "ID").text = str(factura.id_factura)
        ET.SubElement(factura_element, "FechaEmision").text = factura.fecha_emision.isoformat()
        ET.SubElement(factura_element, "Total").text = str(factura.total)
        # Agregar más elementos según sea necesario
        self.xml_factura = ET.tostring(factura_element, encoding='unicode')

    def exportar_XML(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        with open(self.ruta_archivo, 'w') as file:
            file.write(self.xml_factura)

    def firmar_XML(self):
        firma = self.certificado_digital.firmar_documento(self.xml_factura)
        self.xml_factura += f"\n<Firma>{firma}</Firma>"

    def enviar_XML(self):
        # Simulación de envío de XML
        print(f"XML enviado a la autoridad tributaria desde {self.ruta_archivo}")
