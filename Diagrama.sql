CREATE TABLE [usuarios] (
	[id] int NOT NULL,
	[nombre] nvarchar(max) NOT NULL,
	[username] nvarchar(max) NOT NULL UNIQUE,
	[password] nvarchar(max) NOT NULL,
	[rol] nvarchar(max) NOT NULL,
	PRIMARY KEY ([id])
);

CREATE TABLE [clientes] (
	[id] int NOT NULL,
	[id_usuario] int NOT NULL UNIQUE,
	[nombre] nvarchar(max) NOT NULL,
	[nit] nvarchar(max) NOT NULL,
	[direccion] nvarchar(max) NOT NULL,
	[telefono] nvarchar(max) NOT NULL,
	PRIMARY KEY ([id])
);

CREATE TABLE [vendedores] (
	[id] int NOT NULL,
	[id_usuario] int NOT NULL UNIQUE,
	[nombre] nvarchar(max) NOT NULL,
	PRIMARY KEY ([id])
);

CREATE TABLE [productos] (
	[id] int NOT NULL,
	[nombre] nvarchar(max) NOT NULL,
	[descripcion] nvarchar(max) NOT NULL,
	[precio] decimal(18,0) NOT NULL,
	[codigo] nvarchar(max) NOT NULL UNIQUE,
	[cantidad_disponible] int NOT NULL,
	[categoria] nvarchar(max) NOT NULL,
	[id_pedido] int NOT NULL,
	PRIMARY KEY ([id])
);

CREATE TABLE [certificados_digitales] (
	[id] int NOT NULL,
	[ruta_certificado] nvarchar(max) NOT NULL,
	[contrasena] nvarchar(max) NOT NULL,
	[fecha_emision] datetime NOT NULL,
	[fecha_expiracion] datetime NOT NULL,
	[id_factura] int NOT NULL,
	PRIMARY KEY ([id])
);

CREATE TABLE [contingencia] (
	[id] int NOT NULL,
	[estado_contingencia] bit NOT NULL,
	[descripcion] nvarchar(max) NOT NULL,
	[fecha_inicio] datetime NOT NULL,
	[fecha_fin] datetime NOT NULL,
	[id_certificado] int NOT NULL,
	PRIMARY KEY ([id])
);

CREATE TABLE [facturas] (
	[id] int NOT NULL,
	[id_cliente] int NOT NULL,
	[id_vendedor] int NOT NULL,
	[id_certificado] int NOT NULL,
	[fecha_emision] nvarchar(max) NOT NULL,
	[total] decimal(18,0) NOT NULL,
	[impuestos] decimal(18,0) NOT NULL,
	[cuf] nvarchar(max) NOT NULL,
	[cuis] nvarchar(max) NOT NULL,
	[cufd] nvarchar(max) NOT NULL,
	[codigo_qr] nvarchar(max) NOT NULL,
	[firma_digital] nvarchar(max) NOT NULL,
	PRIMARY KEY ([id])
);

CREATE TABLE [detalles_factura] (
	[id] int NOT NULL,
	[id_factura] int NOT NULL,
	[id_producto] int NOT NULL,
	[cantidad] int NOT NULL,
	[precio_unitario] decimal(18,0) NOT NULL,
	[subtotal] decimal(18,0) NOT NULL,
	PRIMARY KEY ([id])
);

CREATE TABLE [ventas] (
	[id] int NOT NULL,
	[id_vendedor] int NOT NULL,
	[id_cliente] int NOT NULL,
	[id_factura] int NOT NULL,
	[fecha] datetime NOT NULL,
	PRIMARY KEY ([id])
);

CREATE TABLE [pedidos] (
	[id] int NOT NULL,
	[id_cliente] int NOT NULL,
	[id_vendedor] int NOT NULL,
	[fecha] datetime NOT NULL,
	[estado] nvarchar(50) NOT NULL DEFAULT 'pendiente',
	[total] decimal(18,0) NOT NULL,
	PRIMARY KEY ([id])
);

CREATE TABLE [detalles_pedido] (
	[id] int NOT NULL,
	[id_pedido] int NOT NULL,
	[id_producto] int NOT NULL,
	[cantidad] int NOT NULL,
	[subtotal] decimal(18,0) NOT NULL,
	PRIMARY KEY ([id])
);

CREATE TABLE [notificaciones] (
	[id] int NOT NULL,
	[id_usuario] int NOT NULL,
	[id_factura] int NOT NULL,
	[mensaje_alerta] nvarchar(max) NOT NULL,
	[fecha_envio] datetime NOT NULL,
	[destinatarios] nvarchar(max) NOT NULL,
	PRIMARY KEY ([id])
);


ALTER TABLE [clientes] ADD CONSTRAINT [clientes_fk1] FOREIGN KEY ([id_usuario]) REFERENCES [usuarios]([id]);
ALTER TABLE [vendedores] ADD CONSTRAINT [vendedores_fk1] FOREIGN KEY ([id_usuario]) REFERENCES [usuarios]([id]);
ALTER TABLE [productos] ADD CONSTRAINT [productos_fk7] FOREIGN KEY ([id_pedido]) REFERENCES [pedidos]([id]);
ALTER TABLE [certificados_digitales] ADD CONSTRAINT [certificados_digitales_fk5] FOREIGN KEY ([id_factura]) REFERENCES [facturas]([id]);
ALTER TABLE [contingencia] ADD CONSTRAINT [contingencia_fk5] FOREIGN KEY ([id_certificado]) REFERENCES [certificados_digitales]([id]);
ALTER TABLE [facturas] ADD CONSTRAINT [facturas_fk1] FOREIGN KEY ([id_cliente]) REFERENCES [clientes]([id]);
ALTER TABLE [detalles_factura] ADD CONSTRAINT [detalles_factura_fk1] FOREIGN KEY ([id_factura]) REFERENCES [facturas]([id]);
ALTER TABLE [ventas] ADD CONSTRAINT [ventas_fk1] FOREIGN KEY ([id_vendedor]) REFERENCES [vendedores]([id]);
ALTER TABLE [pedidos] ADD CONSTRAINT [pedidos_fk1] FOREIGN KEY ([id_cliente]) REFERENCES [clientes]([id]);
ALTER TABLE [detalles_pedido] ADD CONSTRAINT [detalles_pedido_fk1] FOREIGN KEY ([id_pedido]) REFERENCES [pedidos]([id]);
ALTER TABLE [notificaciones] ADD CONSTRAINT [notificaciones_fk1] FOREIGN KEY ([id_usuario]) REFERENCES [usuarios]([id]);