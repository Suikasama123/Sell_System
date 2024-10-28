# Sistema de Facturación Electrónica

[![Sistema de Facturación Electrónica](https://via.placeholder.com/800x200.png?text=Sistema+de+Facturación+Electrónica)](https://github.com/Suikasama123/Sell_System)

## Tabla de Contenidos

- [Descripción General](#descripción-general)
- [Características Principales](#características-principales)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación y Ejecución](#instalación-y-ejecución)
- [Uso del Sistema](#uso-del-sistema)
  - [Inicio de Sesión y Registro](#inicio-de-sesión-y-registro)
  - [Funciones para Vendedores](#funciones-para-vendedores)
  - [Funciones para Clientes](#funciones-para-clientes)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Desafíos y Aprendizajes](#desafíos-y-aprendizajes)
  - [Desafíos](#desafíos)
  - [Aprendizajes](#aprendizajes)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)
- [Contacto](#contacto)
- [Capturas de Pantalla](#capturas-de-pantalla)
- [Futuras Mejoras](#futuras-mejoras)
- [Cómo Reportar Errores](#cómo-reportar-errores)
- [Agradecimientos](#agradecimientos)
- [Recursos y Referencias](#recursos-y-referencias)

---

## Descripción General

El **Sistema de Facturación Electrónica** es una aplicación desarrollada en Python que permite gestionar ventas y compras, generar facturas electrónicas con códigos QR y mantener un registro de usuarios, productos y clientes. Este proyecto tiene como objetivo facilitar el proceso de facturación y gestión de inventario para pequeñas y medianas empresas.

> **Nota:** Este proyecto fue desarrollado íntegramente por **Carlos Daniel Ochoa Molina** debido a problemas en la implementación de la metodología **Scrum** y la disolución del grupo de trabajo original.

**Repositorio del Proyecto:** [https://github.com/Suikasama123/Sell_System](https://github.com/Suikasama123/Sell_System)

## Características Principales

- **Gestión de Usuarios**: Registro e inicio de sesión para vendedores y clientes.
- **Gestión de Productos**: Los vendedores pueden agregar, editar y visualizar productos disponibles.
- **Proceso de Venta y Compra**: Vendedores y clientes pueden realizar ventas y compras respectivamente, agregando productos a un carrito y generando facturas.
- **Generación de Facturas Electrónicas**: Creación de facturas detalladas con información del emisor, cliente, productos, totales, impuestos y códigos QR.
- **Código QR**: Las facturas incluyen un código QR que contiene información relevante de la transacción.
- **Base de Datos Integrada**: Uso de SQLite para almacenar información de usuarios, productos, clientes y facturas.

## Tecnologías Utilizadas

- **Python 3.x**
- **Tkinter**: Para la interfaz gráfica de usuario.
- **SQLite**: Base de datos ligera para almacenamiento de información.
- **Pillow (PIL)**: Manejo y manipulación de imágenes.
- **QRCode**: Generación de códigos QR.
- **Decimal**: Manejo preciso de valores monetarios.

## Instalación y Ejecución

### Requisitos Previos

- **Python 3.x** instalado en el sistema.
- **Pip** para la gestión de paquetes de Python.

### Pasos de Instalación

1. **Clonar el Repositorio**

   ```bash
   git clone https://github.com/Suikasama123/Sell_System.git
   cd Sell_System
