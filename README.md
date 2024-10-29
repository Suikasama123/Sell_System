# Sistema de Facturación Electrónica

## Descripción

Este repositorio contiene el código fuente y la documentación del sistema de **Facturación Electrónica** desarrollado conforme a la normativa del Servicio de Impuestos Nacionales (SIN) de Bolivia. El sistema tiene como objetivo la emisión, transmisión y almacenamiento seguro de facturas, utilizando tecnologías como XML, códigos únicos (CUIS, CUFD, CUF) y firma digital.

## Características Principales
- **Emisión de Facturas Electrónicas** en formato XML con firma digital.
- **Gestor de Contingencias** que permite la emisión de facturas offline y la sincronización automática una vez restablecida la conexión.
- **Verificación mediante Código QR**, permitiendo a los clientes verificar la autenticidad de las facturas.
- **Notificaciones Automáticas** para la renovación de los códigos CUIS y CUFD.
- **Generación de Representación Gráfica** de las facturas en formato PDF.

## Estructura del Proyecto
- **/src**: Código fuente del sistema.
- **/docs**: Documentación del proyecto, incluyendo el informe de arquitectura y los diagramas de clases.
- **/tests**: Pruebas unitarias e integración del sistema.

## Requisitos
- **Java 11+** o **Python 3.x** para la ejecución del código fuente.
- **MySQL** o **PostgreSQL** para la gestión de la base de datos.
- **Vertabelo** para modelado y ajustes en la base de datos.
- **Certificados Digitales** válidos para la firma de las facturas.

## Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Suikasama123/facturacion-electronica.git
   cd facturacion-electronica
   ```
2. Configurar el archivo `.env` con las credenciales de la base de datos y la configuración del entorno.
3. Ejecutar el script de inicialización de la base de datos:
   ```bash
   python setup_db.py
   ```
4. Ejecutar la aplicación:
   ```bash
   python main.py
   ```

## Uso del Sistema
1. **Emisión de Factura**: Ingrese al sistema y seleccione "Emitir Factura". Rellene los datos del cliente y el producto/servicio vendido.
2. **Contingencia**: Si no hay conexión a Internet, la factura será registrada en modo de contingencia y sincronizada posteriormente.
3. **Verificación**: Los clientes pueden verificar la autenticidad de las facturas escaneando el código QR incluido en las mismas.

## Pruebas y Validación
El sistema ha sido probado bajo diferentes escenarios:
- **Pruebas Unitarias**: Verificación de cada módulo de forma independiente.
- **Pruebas de Integración**: Asegurando la correcta interacción entre los módulos.
- **Pruebas de Rendimiento**: Simulación de usuarios concurrentes para evaluar la capacidad del sistema.

### Limitaciones Detectadas
- **Firma Digital**: Hubo dificultades técnicas para una integración exitosa de la firma digital, por lo que se recomienda un mayor desarrollo en esta parte.

## Recomendaciones
- **Investigación de Firmas Digitales**: Se recomienda explorar opciones adicionales para la implementación de firma digital y su validación.
- **Automatización de Notificaciones**: Implementar notificaciones push para la renovación del CUIS y CUFD.
- **Optimizar la UX**: Mejorar la experiencia del usuario mediante pruebas de usabilidad.

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abra un *issue* para discutir cualquier cambio que desee realizar. Puede contactar al autor del proyecto a través del correo asociado a este repositorio.

## Licencia
Este proyecto está licenciado bajo la **Licencia MIT**. Consulte el archivo `LICENSE` para obtener más detalles.
