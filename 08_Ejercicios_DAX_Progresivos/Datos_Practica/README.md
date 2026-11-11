# Datos de Práctica

## Descripción
Archivos CSV generados para ejercicios DAX del repositorio.

## Archivos Generados

| Archivo | Registros | Descripción |
|---------|:---------:|-------------|
| `clientes.csv` | 500 | Clientes con nombre, email, ciudad y tipo |
| `productos.csv` | 50 | Productos con categoría, precio y stock |
| `vendedores.csv` | 25 | Vendedores por región con comisión |
| `ventas.csv` | 5,000 | Transacciones de 2022-2024 |

## Generar Datos

```bash
python generar_datos_practica.py
```

## Estructura de Archivos

### clientes.csv
```
ClienteID, Nombre, Apellido, Email, Ciudad, TipoCliente, FechaRegistro
1, Juan, García, juan.garcia1@email.com, Madrid, Regular, 2022-03-15
```

### productos.csv
```
ProductoID, Nombre, Categoria, SubCategoria, PrecioUnitario, CostoUnitario, Stock
1, Smartphone 1, Electrónica, Smartphone, 450.00, 225.00, 150
```

### ventas.csv
```
VentaID, Fecha, ClienteID, VendedorID, ProductoID, Cantidad, DescuentoPorcentaje, MontoTotal, Estado
1, 2022-05-20, 142, 8, 23, 3, 10, 1215.00, Completada
```

## Distribución de Datos

### Clientes por Ciudad
- Madrid: ~15%
- Barcelona: ~12%
- Valencia: ~11%
- Otras ciudades: ~62%

### Tipo de Cliente
- Regular: 70%
- Premium: 25%
- VIP: 5%

### Estados de Venta
- Completada: 66.7%
- Cancelada: 16.7%
- Pendiente: 16.7%
