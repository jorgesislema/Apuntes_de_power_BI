#!/usr/bin/env python3
"""
generar_datos_practica.py
Genera datos de ejemplo para ejercicios DAX del repositorio.

Uso: python generar_datos_practica.py
Salida: Archivos CSV en la carpeta Datos_Practica/
"""

import csv
import random
from datetime import datetime, timedelta

# Configuración
NUM_CLIENTES = 500
NUM_PRODUCTOS = 100
NUM_VENDEDORES = 25
NUM_VENTAS = 5000
FECHA_INICIO = datetime(2022, 1, 1)
FECHA_FIN = datetime(2024, 12, 31)

# Categorías de productos
CATEGORIAS = {
    "Electrónica": ["Smartphone", "Laptop", "Tablet", "Audífonos", "Monitor"],
    "Ropa": ["Camisa", "Pantalón", "Zapatos", "Chaqueta", "Gorra"],
    "Hogar": ["Sofá", "Mesa", "Silla", "Lámpara", "Alfombra"],
    "Deportes": ["Balón", "Raqueta", "Bicicleta", "Pesas", "Cinta"],
    "Alimentos": ["Café", "Chocolate", "Galletas", "Aceite", "Arroz"]
}

def generar_clientes():
    """Genera archivo clientes.csv"""
    nombres = ["Juan", "María", "Carlos", "Ana", "Pedro", "Laura", 
               "Miguel", "Sofía", "Antonio", "Isabel", "Francisco", "Carmen"]
    apellidos = ["García", "López", "Martínez", "González", "Rodríguez",
                 "Fernández", "Pérez", "Sánchez", "Ramírez", "Torres"]
    ciudades = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao",
                "Málaga", "Zaragoza", "Murcia", "Palma", "Las Palmas"]
    tipos = ["Regular", "Premium", "VIP"]
    
    with open('clientes.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ClienteID', 'Nombre', 'Apellido', 'Email', 
                         'Ciudad', 'TipoCliente', 'FechaRegistro'])
        
        for i in range(1, NUM_CLIENTES + 1):
            nombre = random.choice(nombres)
            apellido = random.choice(apellidos)
            email = f"{nombre.lower()}.{apellido.lower()}{i}@email.com"
            ciudad = random.choice(ciudades)
            tipo = random.choices(tipos, weights=[70, 25, 5])[0]
            fecha_reg = FECHA_INICIO + timedelta(days=random.randint(0, 365))
            
            writer.writerow([i, nombre, apellido, email, ciudad, 
                           tipo, fecha_reg.strftime('%Y-%m-%d')])
    
    print(f"[OK] clientes.csv generado: {NUM_CLIENTES} registros")

def generar_productos():
    """Genera archivo productos.csv"""
    with open('productos.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ProductoID', 'Nombre', 'Categoria', 'SubCategoria',
                         'PrecioUnitario', 'CostoUnitario', 'Stock'])
        
        prod_id = 1
        for cat, subcats in CATEGORIAS.items():
            for subcat in subcats:
                for variant in range(1, 3):  # 2 variantes por subcategoría
                    precio = round(random.uniform(10, 500), 2)
                    costo = round(precio * random.uniform(0.4, 0.7), 2)
                    stock = random.randint(10, 500)
                    
                    writer.writerow([prod_id, f"{subcat} {variant}", cat, subcat,
                                   precio, costo, stock])
                    prod_id += 1
    
    print(f"[OK] productos.csv generado: {prod_id - 1} registros")

def generar_vendedores():
    """Genera archivo vendedores.csv"""
    nombres = ["Roberto", "Elena", "Fernando", "Lucía", "Andrés",
               "Marta", "Javier", "Paula", "Diego", "Nuria"]
    apellidos = ["Álvarez", "Romero", "Navarro", "Domínguez", "Vidal",
                 "Castro", "Ortega", "Molina", "Reyes", "Serrano"]
    regiones = ["Norte", "Sur", "Este", "Oeste", "Centro"]
    
    with open('vendedores.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['VendedorID', 'Nombre', 'Apellido', 'Region',
                         'FechaIngreso', 'ComisionPorcentaje'])
        
        for i in range(1, NUM_VENDEDORES + 1):
            nombre = random.choice(nombres)
            apellido = random.choice(apellidos)
            region = random.choice(regiones)
            fecha_ing = FECHA_INICIO + timedelta(days=random.randint(0, 730))
            comision = round(random.uniform(0.05, 0.15), 2)
            
            writer.writerow([i, nombre, apellido, region,
                           fecha_ing.strftime('%Y-%m-%d'), comision])
    
    print(f"[OK] vendedores.csv generado: {NUM_VENDEDORES} registros")

def generar_ventas():
    """Genera archivo ventas.csv"""
    with open('ventas.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['VentaID', 'Fecha', 'ClienteID', 'VendedorID',
                         'ProductoID', 'Cantidad', 'DescuentoPorcentaje',
                         'MontoTotal', 'Estado'])
        
        estados = ["Completada", "Completada", "Completada", "Completada",
                   "Cancelada", "Pendiente"]  # 66% completadas
        
        for i in range(1, NUM_VENTAS + 1):
            fecha = FECHA_INICIO + timedelta(days=random.randint(0, 1095))
            cliente = random.randint(1, NUM_CLIENTES)
            vendedor = random.randint(1, NUM_VENDEDORES)
            producto = random.randint(1, NUM_PRODUCTOS)
            cantidad = random.randint(1, 10)
            descuento = random.choices([0, 5, 10, 15, 20], 
                                       weights=[40, 25, 20, 10, 5])[0]
            monto_base = round(random.uniform(20, 2000), 2)
            monto_total = round(monto_base * cantidad * (1 - descuento/100), 2)
            estado = random.choice(estados)
            
            writer.writerow([i, fecha.strftime('%Y-%m-%d'), cliente, vendedor,
                           producto, cantidad, descuento, monto_total, estado])
    
    print(f"[OK] ventas.csv generado: {NUM_VENTAS} registros")

if __name__ == "__main__":
    import sys
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    print("Generando datos de practica...\n")
    random.seed(42)  # Reproducibilidad
    
    generar_clientes()
    generar_productos()
    generar_vendedores()
    generar_ventas()
    
    print(f"\nDatos generados exitosamente!")
