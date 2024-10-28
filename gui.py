import tkinter as tk
from tkinter import ttk, messagebox
from models import Usuario, Producto, Factura, DetalleFactura, Cliente, Emisor
from utils import validar_campo_vacio
from decimal import Decimal
import base64
from PIL import Image, ImageTk
import io

class SistemaFacturacionGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Facturación Electrónica")
        self.root.geometry("800x600")
        self.usuario_actual = None
        self.carrito = []
        self.emisor = Emisor(nombre="Mi Empresa", nit="123456789", direccion="Av. Ejemplo #123", telefono="555-1234")

        self.mostrar_pantalla_login()
    def mostrar_pantalla_login(self):
        self.limpiar_ventana()

        self.root.configure(bg="#f0f0f0")  # Color de fondo

        # Crear un frame para organizar los widgets
        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        tk.Label(frame, text="Iniciar Sesión", font=("Arial", 24), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(frame, text="Nombre de Usuario:", font=("Arial", 14), bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_username = tk.Entry(frame, font=("Arial", 14))
        self.entry_username.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Contraseña:", font=("Arial", 14), bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.entry_password = tk.Entry(frame, show='*', font=("Arial", 14))
        self.entry_password.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(frame, text="Iniciar Sesión", font=("Arial", 14), width=15, command=self.login).grid(row=3, column=0, columnspan=2, pady=20)
        tk.Button(frame, text="Registrarse", font=("Arial", 12), command=self.mostrar_pantalla_registro).grid(row=4, column=0, columnspan=2, pady=5)

    def mostrar_pantalla_registro(self):
        self.limpiar_ventana()

        self.root.configure(bg="#f0f0f0")

        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        tk.Label(frame, text="Registrarse", font=("Arial", 24), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(frame, text="Nombre Completo:", font=("Arial", 14), bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_nombre = tk.Entry(frame, font=("Arial", 14))
        self.entry_nombre.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Nombre de Usuario:", font=("Arial", 14), bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.entry_username = tk.Entry(frame, font=("Arial", 14))
        self.entry_username.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="Contraseña:", font=("Arial", 14), bg="#f0f0f0").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.entry_password = tk.Entry(frame, show='*', font=("Arial", 14))
        self.entry_password.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(frame, text="Rol:", font=("Arial", 14), bg="#f0f0f0").grid(row=4, column=0, sticky="e", padx=5, pady=5)
        self.entry_rol = ttk.Combobox(frame, values=["Cliente", "Vendedor"], font=("Arial", 14))
        self.entry_rol.grid(row=4, column=1, padx=5, pady=5)
        self.entry_rol.current(0)

        tk.Button(frame, text="Registrarse", font=("Arial", 14), width=15, command=self.registrarse).grid(row=5, column=0, columnspan=2, pady=20)
        tk.Button(frame, text="Volver", font=("Arial", 12), command=self.mostrar_pantalla_login).grid(row=6, column=0, columnspan=2, pady=5)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if validar_campo_vacio(username, password):
            usuario = Usuario(username=username, password=password)
            if usuario.autenticar():
                self.usuario_actual = usuario
                if usuario.rol.lower() == 'vendedor':
                    self.mostrar_menu_vendedor()
                elif usuario.rol.lower() == 'cliente':
                    self.mostrar_menu_cliente()
                else:
                    messagebox.showerror("Error", "Rol no reconocido.")
            else:
                messagebox.showerror("Error", "Credenciales incorrectas.")
        else:
            messagebox.showerror("Error", "Complete todos los campos.")

    def registrarse(self):
        nombre = self.entry_nombre.get()
        username = self.entry_username.get()
        password = self.entry_password.get()
        rol = self.entry_rol.get()

        if validar_campo_vacio(nombre, username, password, rol):
            usuario = Usuario(nombre=nombre, username=username, password=password, rol=rol)
            try:
                usuario.registrar()
                messagebox.showinfo("Registro Exitoso", "Usuario registrado correctamente.")
                self.mostrar_pantalla_login()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Complete todos los campos.")

    def mostrar_menu_vendedor(self):
        self.limpiar_ventana()

        self.root.configure(bg="#f0f0f0")

        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(expand=True)

        tk.Label(frame, text=f"Bienvenido Vendedor: {self.usuario_actual.nombre}", font=("Arial", 20), bg="#f0f0f0").pack(pady=20)

        btn_frame = tk.Frame(frame, bg="#f0f0f0")
        btn_frame.pack()

        tk.Button(btn_frame, text="Gestionar Productos", font=("Arial", 16), width=20, command=self.gestionar_productos).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(btn_frame, text="Registrar Venta", font=("Arial", 16), width=20, command=self.registrar_venta_vendedor).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(btn_frame, text="Cerrar Sesión", font=("Arial", 14), width=20, command=self.cerrar_sesion).grid(row=1, column=0, columnspan=2, pady=20)

    def mostrar_menu_cliente(self):
        self.limpiar_ventana()

        self.root.configure(bg="#f0f0f0")

        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(expand=True)

        tk.Label(frame, text=f"Bienvenido Cliente: {self.usuario_actual.nombre}", font=("Arial", 20), bg="#f0f0f0").pack(pady=20)

        btn_frame = tk.Frame(frame, bg="#f0f0f0")
        btn_frame.pack()

        tk.Button(btn_frame, text="Comprar Productos", font=("Arial", 16), width=20, command=self.comprar_productos).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(btn_frame, text="Cerrar Sesión", font=("Arial", 14), width=20, command=self.cerrar_sesion).grid(row=1, column=0, pady=20)

    def gestionar_productos(self):
        self.limpiar_ventana()

        self.root.configure(bg="#f0f0f0")

        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Gestionar Productos", font=("Arial", 20), bg="#f0f0f0").pack(pady=20)

        btn_frame = tk.Frame(frame, bg="#f0f0f0")
        btn_frame.pack()

        tk.Button(btn_frame, text="Agregar Producto", font=("Arial", 16), width=20, command=self.agregar_producto).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(btn_frame, text="Ver Productos", font=("Arial", 16), width=20, command=self.ver_productos).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(btn_frame, text="Volver", font=("Arial", 14), width=20, command=self.mostrar_menu_vendedor).grid(row=1, column=0, columnspan=2, pady=20)

    def agregar_producto(self):
        self.limpiar_ventana()

        self.root.configure(bg="#f0f0f0")

        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(expand=True)

        tk.Label(frame, text="Agregar Producto", font=("Arial", 20), bg="#f0f0f0").pack(pady=20)

        form_frame = tk.Frame(frame, bg="#f0f0f0")
        form_frame.pack()

        tk.Label(form_frame, text="Nombre del Producto:", font=("Arial", 14), bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.entry_nombre_producto = tk.Entry(form_frame, font=("Arial", 14))
        self.entry_nombre_producto.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Descripción:", font=("Arial", 14), bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_descripcion_producto = tk.Entry(form_frame, font=("Arial", 14))
        self.entry_descripcion_producto.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Precio:", font=("Arial", 14), bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.entry_precio_producto = tk.Entry(form_frame, font=("Arial", 14))
        self.entry_precio_producto.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Código:", font=("Arial", 14), bg="#f0f0f0").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.entry_codigo_producto = tk.Entry(form_frame, font=("Arial", 14))
        self.entry_codigo_producto.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Cantidad Disponible:", font=("Arial", 14), bg="#f0f0f0").grid(row=4, column=0, sticky="e", padx=5, pady=5)
        self.entry_cantidad_producto = tk.Entry(form_frame, font=("Arial", 14))
        self.entry_cantidad_producto.grid(row=4, column=1, padx=5, pady=5)

        btn_frame = tk.Frame(frame, bg="#f0f0f0")
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="Guardar", font=("Arial", 14), width=15, command=self.guardar_producto).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Volver", font=("Arial", 14), width=15, command=self.gestionar_productos).grid(row=0, column=1, padx=10)

    def guardar_producto(self):
        nombre = self.entry_nombre_producto.get()
        descripcion = self.entry_descripcion_producto.get()
        precio = self.entry_precio_producto.get()
        codigo = self.entry_codigo_producto.get()
        cantidad = self.entry_cantidad_producto.get()

        if validar_campo_vacio(nombre, precio, codigo, cantidad):
            try:
                precio = float(precio)
                cantidad = int(cantidad)
                producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio, codigo=codigo, cantidad_disponible=cantidad)
                producto.guardar()
                messagebox.showinfo("Éxito", "Producto guardado correctamente.")
                self.gestionar_productos()
            except ValueError:
                messagebox.showerror("Error", "Precio y Cantidad deben ser numéricos.")
        else:
            messagebox.showerror("Error", "Complete todos los campos obligatorios.")

    def ver_productos(self):
        self.limpiar_ventana()

        self.root.configure(bg="#f0f0f0")

        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Lista de Productos", font=("Arial", 20), bg="#f0f0f0").pack(pady=20)

        productos = Producto.obtener_todos()

        tree = ttk.Treeview(frame, columns=("ID", "Nombre", "Precio", "Cantidad"), show='headings', height=15)
        tree.column("ID", width=50, anchor='center')
        tree.column("Nombre", width=200, anchor='center')
        tree.column("Precio", width=100, anchor='center')
        tree.column("Cantidad", width=100, anchor='center')

        tree.heading("ID", text="ID")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Precio", text="Precio")
        tree.heading("Cantidad", text="Cantidad")

        for producto in productos:
            tree.insert('', tk.END, values=(producto.id_producto, producto.nombre, producto.precio, producto.cantidad_disponible))

        tree.pack(pady=10)

        tk.Button(frame, text="Volver", font=("Arial", 14), width=15, command=self.gestionar_productos).pack(pady=20)

    def registrar_venta_vendedor(self):
        self.limpiar_ventana()

        self.root.configure(bg="#f0f0f0")

        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Registrar Venta", font=("Arial", 20), bg="#f0f0f0").pack(pady=20)

        form_frame = tk.Frame(frame, bg="#f0f0f0")
        form_frame.pack()

        tk.Label(form_frame, text="ID Cliente:", font=("Arial", 14), bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.entry_id_cliente = tk.Entry(form_frame, font=("Arial", 14))
        self.entry_id_cliente.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Cantidad a Comprar:", font=("Arial", 14), bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5)
        self.entry_cantidad = tk.Entry(form_frame, font=("Arial", 14))
        self.entry_cantidad.grid(row=1, column=1, padx=5, pady=5)

        # Mostrar lista de productos disponibles
        productos = Producto.obtener_todos()

        self.tree_productos = ttk.Treeview(frame, columns=("ID", "Nombre", "Precio", "Cantidad"), show='headings', height=10)
        self.tree_productos.column("ID", width=50, anchor='center')
        self.tree_productos.column("Nombre", width=200, anchor='center')
        self.tree_productos.column("Precio", width=100, anchor='center')
        self.tree_productos.column("Cantidad", width=100, anchor='center')

        self.tree_productos.heading("ID", text="ID")
        self.tree_productos.heading("Nombre", text="Nombre")
        self.tree_productos.heading("Precio", text="Precio")
        self.tree_productos.heading("Cantidad", text="Cantidad")

        for producto in productos:
            self.tree_productos.insert('', tk.END, values=(producto.id_producto, producto.nombre, producto.precio, producto.cantidad_disponible))

        self.tree_productos.pack(pady=10)

        btn_frame = tk.Frame(frame, bg="#f0f0f0")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Agregar al Carrito", font=("Arial", 14), width=20, command=self.agregar_al_carrito_vendedor).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(btn_frame, text="Finalizar Venta", font=("Arial", 14), width=20, command=self.finalizar_venta).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(btn_frame, text="Volver", font=("Arial", 14), width=20, command=self.mostrar_menu_vendedor).grid(row=1, column=0, columnspan=2, pady=20)

        # Carrito de compras
        tk.Label(frame, text="Carrito de Compras", font=("Arial", 18), bg="#f0f0f0").pack(pady=10)

        self.carrito_frame = tk.Frame(frame, bg="#f0f0f0")
        self.carrito_frame.pack()

        self.actualizar_carrito()

    def agregar_al_carrito_vendedor(self):
        selected_item = self.tree_productos.focus()
        if selected_item:
            producto_values = self.tree_productos.item(selected_item, 'values')
            producto_id = producto_values[0]
            cantidad = self.entry_cantidad.get()

            if validar_campo_vacio(cantidad):
                try:
                    cantidad = int(cantidad)
                    producto = Producto.obtener_producto_por_id(producto_id)
                    if producto:
                        if cantidad <= producto.cantidad_disponible:
                            self.carrito.append({'producto': producto, 'cantidad': cantidad})
                            messagebox.showinfo("Éxito", f"Producto {producto.nombre} agregado al carrito.")
                            self.actualizar_carrito()
                        else:
                            messagebox.showerror("Error", "Cantidad no disponible en stock.")
                    else:
                        messagebox.showerror("Error", "Producto no encontrado.")
                except ValueError:
                    messagebox.showerror("Error", "La cantidad debe ser un número entero.")
            else:
                messagebox.showerror("Error", "Ingrese la cantidad a comprar.")
        else:
            messagebox.showerror("Error", "Seleccione un producto de la lista.")

    def actualizar_carrito(self):
        for widget in self.carrito_frame.winfo_children():
            widget.destroy()

        tree = ttk.Treeview(self.carrito_frame, columns=("Nombre", "Cantidad", "Subtotal"), show='headings', height=10)
        tree.column("Nombre", width=200, anchor='center')
        tree.column("Cantidad", width=100, anchor='center')
        tree.column("Subtotal", width=100, anchor='center')

        tree.heading("Nombre", text="Nombre")
        tree.heading("Cantidad", text="Cantidad")
        tree.heading("Subtotal", text="Subtotal")

        total = 0
        for item in self.carrito:
            subtotal = item['producto'].precio * item['cantidad']
            total += subtotal
            tree.insert('', tk.END, values=(item['producto'].nombre, item['cantidad'], f"{subtotal:.2f}"))

        tree.pack()

        tk.Label(self.carrito_frame, text=f"Total: {total:.2f}", font=("Arial", 16), bg="#f0f0f0").pack(pady=10)

    def finalizar_venta(self):
        id_cliente = self.entry_id_cliente.get()

        if validar_campo_vacio(id_cliente):
            if self.carrito:
                cliente = Cliente.obtener_cliente_por_id(id_cliente)
                if not cliente:
                    messagebox.showerror("Error", "Cliente no encontrado.")
                    return
                factura = Factura(emisor=self.emisor, cliente=cliente, id_vendedor=self.usuario_actual.id_usuario)
                for item in self.carrito:
                    producto = item['producto']
                    cantidad = item['cantidad']
                    detalle = DetalleFactura(producto=producto, cantidad=cantidad, precio_unitario=producto.precio)
                    factura.agregar_detalle(detalle)
                    producto.cantidad_disponible -= cantidad
                    producto.guardar()
                factura.guardar()
                self.mostrar_factura(factura)
                self.carrito = []
                self.registrar_venta_vendedor()
            else:
                messagebox.showerror("Error", "El carrito está vacío.")
        else:
            messagebox.showerror("Error", "Complete todos los campos.")

    def comprar_productos(self):
        self.limpiar_ventana()

        self.root.configure(bg="#f0f0f0")

        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Comprar Productos", font=("Arial", 20), bg="#f0f0f0").pack(pady=20)

        # Mostrar lista de productos disponibles
        productos = Producto.obtener_todos()

        self.tree_productos = ttk.Treeview(frame, columns=("ID", "Nombre", "Precio", "Cantidad"), show='headings', height=10)
        self.tree_productos.column("ID", width=50, anchor='center')
        self.tree_productos.column("Nombre", width=200, anchor='center')
        self.tree_productos.column("Precio", width=100, anchor='center')
        self.tree_productos.column("Cantidad", width=100, anchor='center')

        self.tree_productos.heading("ID", text="ID")
        self.tree_productos.heading("Nombre", text="Nombre")
        self.tree_productos.heading("Precio", text="Precio")
        self.tree_productos.heading("Cantidad", text="Cantidad")

        for producto in productos:
            self.tree_productos.insert('', tk.END, values=(producto.id_producto, producto.nombre, producto.precio, producto.cantidad_disponible))

        self.tree_productos.pack(pady=10)

        # Entrada para la cantidad
        form_frame = tk.Frame(frame, bg="#f0f0f0")
        form_frame.pack()

        tk.Label(form_frame, text="Cantidad a Comprar:", font=("Arial", 14), bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5)
        self.entry_cantidad = tk.Entry(form_frame, font=("Arial", 14))
        self.entry_cantidad.grid(row=0, column=1, padx=5, pady=5)

        btn_frame = tk.Frame(frame, bg="#f0f0f0")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Agregar al Carrito", font=("Arial", 14), width=20, command=self.agregar_al_carrito_cliente).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(btn_frame, text="Finalizar Compra", font=("Arial", 14), width=20, command=self.finalizar_compra_cliente).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(btn_frame, text="Volver", font=("Arial", 14), width=20, command=self.mostrar_menu_cliente).grid(row=1, column=0, columnspan=2, pady=20)

        # Carrito de compras
        tk.Label(frame, text="Carrito de Compras", font=("Arial", 18), bg="#f0f0f0").pack(pady=10)

        self.carrito_frame = tk.Frame(frame, bg="#f0f0f0")
        self.carrito_frame.pack()

        self.actualizar_carrito_cliente()

    def agregar_al_carrito_cliente(self):
        selected_item = self.tree_productos.focus()
        if selected_item:
            producto_values = self.tree_productos.item(selected_item, 'values')
            producto_id = producto_values[0]
            cantidad = self.entry_cantidad.get()

            if validar_campo_vacio(cantidad):
                try:
                    cantidad = int(cantidad)
                    producto = Producto.obtener_producto_por_id(producto_id)
                    if producto:
                        if cantidad <= producto.cantidad_disponible:
                            self.carrito.append({'producto': producto, 'cantidad': cantidad})
                            messagebox.showinfo("Éxito", f"Producto {producto.nombre} agregado al carrito.")
                            self.actualizar_carrito_cliente()
                        else:
                            messagebox.showerror("Error", "Cantidad no disponible en stock.")
                    else:
                        messagebox.showerror("Error", "Producto no encontrado.")
                except ValueError:
                    messagebox.showerror("Error", "La cantidad debe ser un número entero.")
            else:
                messagebox.showerror("Error", "Ingrese la cantidad a comprar.")
        else:
            messagebox.showerror("Error", "Seleccione un producto de la lista.")

    def actualizar_carrito_cliente(self):
        for widget in self.carrito_frame.winfo_children():
            widget.destroy()

        tree = ttk.Treeview(self.carrito_frame, columns=("Nombre", "Cantidad", "Subtotal"), show='headings', height=10)
        tree.column("Nombre", width=200, anchor='center')
        tree.column("Cantidad", width=100, anchor='center')
        tree.column("Subtotal", width=100, anchor='center')

        tree.heading("Nombre", text="Nombre")
        tree.heading("Cantidad", text="Cantidad")
        tree.heading("Subtotal", text="Subtotal")

        total = 0
        for item in self.carrito:
            subtotal = item['producto'].precio * item['cantidad']
            total += subtotal
            tree.insert('', tk.END, values=(item['producto'].nombre, item['cantidad'], f"{subtotal:.2f}"))

        tree.pack()

        tk.Label(self.carrito_frame, text=f"Total: {total:.2f}", font=("Arial", 16), bg="#f0f0f0").pack(pady=10)

    def finalizar_compra_cliente(self):
        if self.carrito:
            # Verificar si el usuario actual es un cliente registrado
            cliente = Cliente.obtener_cliente_por_usuario(self.usuario_actual.id_usuario)
            if not cliente:
                # Solicitar datos adicionales del cliente
                self.solicitar_datos_cliente()
                return  # Esperamos a que el usuario ingrese los datos
            factura = Factura(emisor=self.emisor, cliente=cliente, id_vendedor=None)
            for item in self.carrito:
                producto = item['producto']
                cantidad = item['cantidad']
                detalle = DetalleFactura(producto=producto, cantidad=cantidad, precio_unitario=producto.precio)
                factura.agregar_detalle(detalle)
                producto.cantidad_disponible -= cantidad
                producto.guardar()
            factura.guardar()
            self.mostrar_factura(factura)
            self.carrito = []
            self.comprar_productos()
        else:
            messagebox.showerror("Error", "El carrito está vacío.")

    def solicitar_datos_cliente(self):
        ventana_cliente = tk.Toplevel(self.root)
        ventana_cliente.title("Registrar Datos del Cliente")
        ventana_cliente.geometry("400x300")

        tk.Label(ventana_cliente, text="Complete sus datos para continuar", font=("Arial", 14)).pack(pady=10)

        frame = tk.Frame(ventana_cliente)
        frame.pack(pady=10)

        tk.Label(frame, text="Nombre:", font=("Arial", 12)).grid(row=0, column=0, sticky="e", padx=5, pady=5)
        entry_nombre = tk.Entry(frame, font=("Arial", 12))
        entry_nombre.grid(row=0, column=1, padx=5, pady=5)
        entry_nombre.insert(0, self.usuario_actual.nombre)

        tk.Label(frame, text="NIT/CI:", font=("Arial", 12)).grid(row=1, column=0, sticky="e", padx=5, pady=5)
        entry_nit = tk.Entry(frame, font=("Arial", 12))
        entry_nit.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Dirección:", font=("Arial", 12)).grid(row=2, column=0, sticky="e", padx=5, pady=5)
        entry_direccion = tk.Entry(frame, font=("Arial", 12))
        entry_direccion.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="Teléfono:", font=("Arial", 12)).grid(row=3, column=0, sticky="e", padx=5, pady=5)
        entry_telefono = tk.Entry(frame, font=("Arial", 12))
        entry_telefono.grid(row=3, column=1, padx=5, pady=5)

        def guardar_datos_cliente():
            nombre = entry_nombre.get()
            nit = entry_nit.get()
            direccion = entry_direccion.get()
            telefono = entry_telefono.get()

            if validar_campo_vacio(nombre, nit):
                cliente = Cliente(id_usuario=self.usuario_actual.id_usuario, nombre=nombre, nit=nit, direccion=direccion, telefono=telefono)
                cliente.guardar()
                ventana_cliente.destroy()
                self.finalizar_compra_cliente()  # Continuamos con la compra
            else:
                messagebox.showerror("Error", "Nombre y NIT/CI son obligatorios.")

        tk.Button(ventana_cliente, text="Guardar", font=("Arial", 12), command=guardar_datos_cliente).pack(pady=10)

    def mostrar_factura(self, factura):
        ventana_factura = tk.Toplevel(self.root)
        ventana_factura.title(f"Factura N° {factura.id_factura}")
        ventana_factura.geometry("600x700")

        # Información del emisor
        tk.Label(ventana_factura, text=factura.emisor.nombre, font=("Arial", 14, "bold")).pack()
        tk.Label(ventana_factura, text=f"NIT: {factura.emisor.nit}").pack()
        tk.Label(ventana_factura, text=f"Dirección: {factura.emisor.direccion}").pack()
        tk.Label(ventana_factura, text=f"Teléfono: {factura.emisor.telefono}").pack()
        tk.Label(ventana_factura, text="").pack()

        # Información del cliente
        tk.Label(ventana_factura, text="Datos del Cliente", font=("Arial", 12, "bold")).pack()
        tk.Label(ventana_factura, text=f"Nombre: {factura.cliente.nombre}").pack()
        tk.Label(ventana_factura, text=f"NIT/CI: {factura.cliente.nit}").pack()
        tk.Label(ventana_factura, text="").pack()

        # Detalles de la factura
        tk.Label(ventana_factura, text="Detalle de la Factura", font=("Arial", 12, "bold")).pack()

        tree = ttk.Treeview(ventana_factura, columns=("Producto", "Cantidad", "P.Unitario", "Subtotal"), show='headings')
        tree.column("Producto", width=200)
        tree.column("Cantidad", width=80, anchor='center')
        tree.column("P.Unitario", width=100, anchor='center')
        tree.column("Subtotal", width=100, anchor='center')

        tree.heading("Producto", text="Producto")
        tree.heading("Cantidad", text="Cantidad")
        tree.heading("P.Unitario", text="P. Unitario")
        tree.heading("Subtotal", text="Subtotal")

        for detalle in factura.detalles:
            tree.insert('', tk.END, values=(detalle.producto.nombre, detalle.cantidad, f"{detalle.precio_unitario:.2f}", f"{detalle.subtotal:.2f}"))

        tree.pack(pady=10)

        # Totales
        tk.Label(ventana_factura, text=f"Total: {factura.total:.2f} Bs.").pack()
        tk.Label(ventana_factura, text=f"Impuestos (13%): {factura.impuestos:.2f} Bs.").pack()
        tk.Label(ventana_factura, text=f"Total a Pagar: {(factura.total + factura.impuestos):.2f} Bs.", font=("Arial", 12, "bold")).pack()
        tk.Label(ventana_factura, text="").pack()

        # Códigos y QR
        tk.Label(ventana_factura, text=f"CUF: {factura.CUF}").pack()
        tk.Label(ventana_factura, text=f"CUFD: {factura.CUFD}").pack()
        tk.Label(ventana_factura, text=f"CUIS: {factura.CUIS}").pack()

        # Mostrar código QR
        qr_image_data = base64.b64decode(factura.codigo_qr)
        qr_image = Image.open(io.BytesIO(qr_image_data))
        qr_photo = ImageTk.PhotoImage(qr_image)

        tk.Label(ventana_factura, image=qr_photo).pack()
        tk.Label(ventana_factura, text="Este documento es la Representación Gráfica de un Documento Fiscal Digital emitido en una modalidad de facturación en línea.", font=("Arial", 8), wraplength=500, justify="center").pack()

        ventana_factura.mainloop()

    def cerrar_sesion(self):
        self.usuario_actual = None
        self.carrito = []
        self.mostrar_pantalla_login()

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def run(self):
        self.root.mainloop()
