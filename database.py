import sqlite3

class Database:
    def __init__(self, db_name='sistema_facturacion.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()

        # Tabla de usuarios (clientes y vendedores)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                rol TEXT NOT NULL
            )
        ''')

        # Tabla de clientes
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER UNIQUE,
                nombre TEXT NOT NULL,
                nit TEXT NOT NULL,
                direccion TEXT,
                telefono TEXT,
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
            )
        ''')

        # Tabla de productos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                precio REAL NOT NULL,
                codigo TEXT UNIQUE NOT NULL,
                cantidad_disponible INTEGER NOT NULL,
                categoria TEXT
            )
        ''')

        # Tabla de facturas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS facturas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_cliente INTEGER,
                id_vendedor INTEGER,
                fecha_emision TEXT NOT NULL,
                total REAL NOT NULL,
                impuestos REAL NOT NULL,
                CUF TEXT NOT NULL,
                CUIS TEXT NOT NULL,
                CUFD TEXT NOT NULL,
                codigo_qr TEXT,
                FOREIGN KEY (id_cliente) REFERENCES clientes(id),
                FOREIGN KEY (id_vendedor) REFERENCES usuarios(id)
            )
        ''')

        # Tabla de detalles de factura
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS detalles_factura (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_factura INTEGER NOT NULL,
                id_producto INTEGER NOT NULL,
                cantidad INTEGER NOT NULL,
                precio_unitario REAL NOT NULL,
                subtotal REAL NOT NULL,
                FOREIGN KEY (id_factura) REFERENCES facturas(id),
                FOREIGN KEY (id_producto) REFERENCES productos(id)
            )
        ''')

        self.conn.commit()

    def execute_query(self, query, params=()):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        return cursor  # Devolvemos el cursor para acceder a lastrowid si es necesario

    def fetchone(self, query, params=()):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()

    def fetchall(self, query, params=()):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
