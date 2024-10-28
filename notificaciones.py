class Notificaciones:
    def __init__(self):
        self.destinatarios = []
        self.mensaje_alerta = ""

    def configurar_notificaciones(self, destinatarios):
        self.destinatarios = destinatarios

    def enviar_alerta_renovacion_CUIS(self):
        self.mensaje_alerta = "Su CUIS está próximo a vencer."
        self.enviar_alerta()

    def enviar_alerta_renovacion_CUFD(self):
        self.mensaje_alerta = "Su CUFD está próximo a vencer."
        self.enviar_alerta()

    def notificar_contingencia(self):
        self.mensaje_alerta = "El sistema ha entrado en modo de contingencia."
        self.enviar_alerta()

    def enviar_alerta(self):
        for destinatario in self.destinatarios:
            print(f"Enviando alerta a {destinatario}: {self.mensaje_alerta}")
