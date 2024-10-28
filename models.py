import hashlib
import uuid
import qrcode
import base64
import io
from datetime import datetime, timedelta
from database import Database
from decimal import Decimal

db = Database()

class Usuario:
    def __init__(self, id_usuario=None, nombre=None, username=None, password=None, rol=None):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.username = username
        self.password = password
        self.rol = rol

    def registrar(self):
        password_hash = hashlib.sha256(self.password.encode()).hexdigest()
        query = '''
            INSERT INTO usuarios (nombre, username, password, rol)
            VALUES (?, ?, ?, ?)
        '''
        db.execute_query(query, (self.nombre, self.username, password_hash, self.rol))

    def autenticar(self):
        password_hash = hashlib.sha256(self.password.encode()).hexdigest()
        query = '''
            SELECT * FROM usuarios WHERE username = ? AND password = ?
        '''
        user = db.fetchone(query, (self.username, password_hash))
        if user:
            self.id_usuario, self.nombre, self.username, self.password, self.rol = user
            return True
        return False

class Cliente:
    def __init__(self, id_cliente=None, id_usuario=None, nombre=None, nit=None, direccion=None, telefono=None):
        self.id_cliente = id_cliente
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.telefono = telefono

    def guardar(self):
        if self.id_cliente:
            query = '''
                UPDATE clientes SET nombre=?, nit=?, direccion=?, telefono=?
                WHERE id=?
            '''
            db.execute_query(query, (self.nombre, self.nit, self.direccion, self.telefono, self.id_cliente))
        else:
            query = '''
                INSERT INTO clientes (id_usuario, nombre, nit, direccion, telefono)
                VALUES (?, ?, ?, ?, ?)
            '''
            cursor = db.execute_query(query, (self.id_usuario, self.nombre, self.nit, self.direccion, self.telefono))
            self.id_cliente = cursor.lastrowid  # Obtenemos el id_cliente generado

    @staticmethod
    def obtener_cliente_por_usuario(id_usuario):
        query = 'SELECT * FROM clientes WHERE id_usuario = ?'
        cliente_data = db.fetchone(query, (id_usuario,))
        if cliente_data:
            return Cliente(*cliente_data)
        return None

    @staticmethod
    def obtener_cliente_por_id(id_cliente):
        query = 'SELECT * FROM clientes WHERE id = ?'
        cliente_data = db.fetchone(query, (id_cliente,))
        if cliente_data:
            return Cliente(*cliente_data)
        return None

class Producto:
    def __init__(self, id_producto=None, nombre=None, descripcion=None, precio=None, codigo=None, cantidad_disponible=None, categoria=None):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = Decimal(precio)
        self.codigo = codigo
        self.cantidad_disponible = cantidad_disponible
        self.categoria = categoria

    def guardar(self):
        if self.id_producto:
            query = '''
                UPDATE productos SET nombre=?, descripcion=?, precio=?, codigo=?, cantidad_disponible=?, categoria=?
                WHERE id=?
            '''
            db.execute_query(query, (self.nombre, self.descripcion, float(self.precio), self.codigo, self.cantidad_disponible, self.categoria, self.id_producto))
        else:
            query = '''
                INSERT INTO productos (nombre, descripcion, precio, codigo, cantidad_disponible, categoria)
                VALUES (?, ?, ?, ?, ?, ?)
            '''
            cursor = db.execute_query(query, (self.nombre, self.descripcion, float(self.precio), self.codigo, self.cantidad_disponible, self.categoria))
            self.id_producto = cursor.lastrowid  # Obtenemos el id_producto generado

    @staticmethod
    def obtener_producto_por_codigo(codigo):
        query = 'SELECT * FROM productos WHERE codigo = ?'
        producto_data = db.fetchone(query, (codigo,))
        if producto_data:
            return Producto(*producto_data)
        return None

    @staticmethod
    def obtener_producto_por_id(id_producto):
        query = 'SELECT * FROM productos WHERE id = ?'
        producto_data = db.fetchone(query, (id_producto,))
        if producto_data:
            return Producto(*producto_data)
        return None

    @staticmethod
    def obtener_todos():
        query = 'SELECT * FROM productos'
        productos_data = db.fetchall(query)
        return [Producto(*producto) for producto in productos_data]

class Emisor:
    def __init__(self, id_emisor=None, nombre=None, nit=None, direccion=None, telefono=None):
        self.id_emisor = id_emisor
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.telefono = telefono

    def obtener_informacion(self):
        return {
            'nombre': self.nombre,
            'nit': self.nit,
            'direccion': self.direccion,
            'telefono': self.telefono
        }

class GestionAutorizacion:
    def __init__(self):
        self.CUIS = self.generar_CUIS()
        self.CUFD = self.generar_CUFD()
        self.fecha_vencimiento_CUIS = datetime.now() + timedelta(days=365)
        self.fecha_vencimiento_CUFD = datetime.now() + timedelta(hours=24)

    def verificar_vigencia_CUIS(self):
        if datetime.now() >= self.fecha_vencimiento_CUIS:
            self.CUIS = self.generar_CUIS()
            self.fecha_vencimiento_CUIS = datetime.now() + timedelta(days=365)

    def verificar_vigencia_CUFD(self):
        if datetime.now() >= self.fecha_vencimiento_CUFD:
            self.CUFD = self.generar_CUFD()
            self.fecha_vencimiento_CUFD = datetime.now() + timedelta(hours=24)

    def generar_CUIS(self):
        return str(uuid.uuid4()).replace('-', '')[:16]

    def generar_CUFD(self):
        return str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '')

class Factura:
    def __init__(self, id_factura=None, emisor=None, cliente=None, id_vendedor=None, fecha_emision=None, total=Decimal('0.00'), impuestos=Decimal('0.00'), CUF=None, CUIS=None, CUFD=None, codigo_qr=None, detalles=None):
        self.id_factura = id_factura
        self.emisor = emisor
        self.cliente = cliente
        self.id_vendedor = id_vendedor
        self.fecha_emision = fecha_emision or datetime.now().isoformat()
        self.total = total
        self.impuestos = impuestos
        self.CUF = CUF or self.generar_CUF()
        self.CUIS = CUIS
        self.CUFD = CUFD
        self.codigo_qr = codigo_qr
        self.detalles = detalles or []

    def agregar_detalle(self, detalle):
        self.detalles.append(detalle)
        self.total += detalle.subtotal

    def calcular_impuestos(self):
        # Supongamos un impuesto del 13%
        self.impuestos = self.total * Decimal('0.13')

    def generar_CUF(self):
        # Generar CUF de 34 caracteres
        return str(uuid.uuid4()).replace('-', '')[:34]

    def generar_codigo_qr(self):
        data_qr = f"FacturaID:{self.id_factura}|CUF:{self.CUF}|Total:{self.total}|Fecha:{self.fecha_emision}"
        qr = qrcode.QRCode(version=1, box_size=10, border=2)
        qr.add_data(data_qr)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        self.codigo_qr = base64.b64encode(buffered.getvalue()).decode()

    def guardar(self):
        self.calcular_impuestos()
        gestion_autorizacion = GestionAutorizacion()
        self.CUIS = gestion_autorizacion.CUIS
        self.CUFD = gestion_autorizacion.CUFD
        # Generamos el QR después de obtener el id_factura
        query = '''
            INSERT INTO facturas (id_cliente, id_vendedor, fecha_emision, total, impuestos, CUF, CUIS, CUFD, codigo_qr)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        cursor = db.execute_query(query, (self.cliente.id_cliente, self.id_vendedor, self.fecha_emision, float(self.total), float(self.impuestos), self.CUF, self.CUIS, self.CUFD, ''))
        self.id_factura = cursor.lastrowid  # Obtenemos el id_factura generado
        self.generar_codigo_qr()
        # Actualizamos la factura con el código QR
        query_update = '''
            UPDATE facturas SET codigo_qr = ? WHERE id = ?
        '''
        db.execute_query(query_update, (self.codigo_qr, self.id_factura))

        for detalle in self.detalles:
            detalle.id_factura = self.id_factura
            detalle.guardar()

class DetalleFactura:
    def __init__(self, id_detalle=None, id_factura=None, producto=None, cantidad=None, precio_unitario=None, subtotal=None):
        self.id_detalle = id_detalle
        self.id_factura = id_factura
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = Decimal(precio_unitario)
        self.subtotal = subtotal or (self.cantidad * self.precio_unitario)

    def guardar(self):
        query = '''
            INSERT INTO detalles_factura (id_factura, id_producto, cantidad, precio_unitario, subtotal)
            VALUES (?, ?, ?, ?, ?)
        '''
        db.execute_query(query, (self.id_factura, self.producto.id_producto, self.cantidad, float(self.precio_unitario), float(self.subtotal)))
