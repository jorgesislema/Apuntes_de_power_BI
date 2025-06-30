# Caso de Estudio: Análisis de Ventas Retail

## Descripción del Proyecto

Este caso de estudio presenta un análisis completo de ventas para una cadena de retail ficticia, implementando las mejores prácticas de Power BI desde la modelización de datos hasta la creación de dashboards ejecutivos.

## Objetivos del Análisis

### Objetivos de Negocio
- **Optimizar performance de ventas** por región y categoría de producto
- **Identificar tendencias estacionales** para mejorar planning de inventario
- **Analizar comportamiento del cliente** para estrategias de retención
- **Monitorear KPIs operacionales** en tiempo real
- **Facilitar toma de decisiones** basada en datos

### Objetivos Técnicos
- Demostrar modelado dimensional efectivo
- Implementar medidas DAX avanzadas
- Crear visualizaciones interactivas profesionales
- Establecer governance de datos apropiada
- Optimizar rendimiento del modelo

## Estructura de Datos

### Fuentes de Datos Simuladas

#### 1. Sistema ERP (SQL Server)
```
Tablas principales:
├── Ventas (Fact Table)
│   ├── VentaID (PK)
│   ├── FechaVenta  
│   ├── ProductoID (FK)
│   ├── ClienteID (FK)
│   ├── SucursalID (FK)
│   ├── EmpleadoID (FK)
│   ├── Cantidad
│   ├── PrecioUnitario
│   ├── Descuento
│   └── ImporteTotal
│
├── Productos (Dimension)
│   ├── ProductoID (PK)
│   ├── NombreProducto
│   ├── CategoriaID (FK)
│   ├── MarcaID (FK)
│   ├── Costo
│   ├── PrecioSugerido
│   └── FechaLanzamiento
│
├── Clientes (Dimension)
│   ├── ClienteID (PK)
│   ├── NombreCliente
│   ├── Email
│   ├── FechaNacimiento
│   ├── Genero
│   ├── Ciudad
│   ├── CodigoPostal
│   └── FechaRegistro
│
└── Sucursales (Dimension)
    ├── SucursalID (PK)
    ├── NombreSucursal
    ├── RegionID (FK)
    ├── Ciudad
    ├── Gerente
    ├── FechaApertura
    └── MetrosCuadrados
```

#### 2. Sistema CRM (Salesforce)
- Datos de interacciones con clientes
- Campañas de marketing
- Leads y oportunidades
- Satisfacción del cliente

#### 3. Datos Externos
- Información demográfica del INE
- Datos económicos (inflación, desempleo)
- Información de competencia
- Datos meteorológicos

## Modelo de Datos Implementado

### Esquema Estrella
```
          DimFecha
              │
              │
DimProducto ──┼── FactVentas ──┼── DimCliente  
              │               │
         DimSucursal     DimEmpleado
```

### Tablas de Dimensiones

#### Dimensión Fecha (Calculada)
```dax
DimFecha = 
ADDCOLUMNS(
    CALENDAR(DATE(2020,1,1), DATE(2025,12,31)),
    "Año", YEAR([Date]),
    "Mes", MONTH([Date]),
    "NombreMes", FORMAT([Date], "MMMM"),
    "Trimestre", "T" & ROUNDUP(MONTH([Date])/3, 0),
    "DiaSemana", WEEKDAY([Date]),
    "EsFinSemana", WEEKDAY([Date]) IN {1,7},
    "AñoMes", FORMAT([Date], "YYYY-MM")
)
```

#### Jerarquías Implementadas
- **Tiempo**: Año → Trimestre → Mes → Día
- **Producto**: Categoría → Subcategoría → Marca → Producto
- **Geografía**: Región → Ciudad → Sucursal
- **Cliente**: Segmento → Género → Rango Edad

## Medidas DAX Implementadas

### KPIs Fundamentales

#### Ventas
```dax
VentasTotales = SUM(FactVentas[ImporteTotal])

VentasAñoAnterior = 
CALCULATE(
    [VentasTotales],
    SAMEPERIODLASTYEAR(DimFecha[Fecha])
)

CrecimientoVentas = 
DIVIDE(
    [VentasTotales] - [VentasAñoAnterior],
    [VentasAñoAnterior]
)
```

#### Margen y Rentabilidad
```dax
CostoTotal = 
SUMX(
    FactVentas,
    FactVentas[Cantidad] * RELATED(DimProducto[Costo])
)

MargenBruto = [VentasTotales] - [CostoTotal]

PorcentajeMargen = DIVIDE([MargenBruto], [VentasTotales])
```

#### Análisis de Clientes
```dax
ClientesActivos = 
DISTINCTCOUNT(FactVentas[ClienteID])

TicketPromedio = 
DIVIDE([VentasTotales], [ClientesActivos])

FrecuenciaCompra = 
DIVIDE(
    COUNTROWS(FactVentas),
    [ClientesActivos]
)
```

### Medidas de Time Intelligence

#### Análisis Temporal Avanzado
```dax
VentasAcumuladas = 
TOTALYTD([VentasTotales], DimFecha[Fecha])

VentasTrimestresMovil = 
CALCULATE(
    [VentasTotales],
    DATESINPERIOD(
        DimFecha[Fecha],
        LASTDATE(DimFecha[Fecha]),
        -3,
        QUARTER
    )
)

TendenciaCrecimiento = 
VAR VentasActuales = [VentasTotales]
VAR VentasTresMesesAtras = 
    CALCULATE(
        [VentasTotales],
        DATEADD(DimFecha[Fecha], -3, MONTH)
    )
RETURN
    DIVIDE(VentasActuales - VentasTresMesesAtras, VentasTresMesesAtras)
```

### Análisis Avanzado

#### Segmentación RFM
```dax
RecencyScore = 
VAR UltimaCompraCliente = 
    CALCULATE(
        MAX(FactVentas[FechaVenta]),
        ALLEXCEPT(FactVentas, FactVentas[ClienteID])
    )
VAR DiasDesdeUltimaCompra = 
    DATEDIFF(UltimaCompraCliente, TODAY(), DAY)
RETURN
    SWITCH(
        TRUE(),
        DiasDesdeUltimaCompra <= 30, 5,
        DiasDesdeUltimaCompra <= 60, 4,
        DiasDesdeUltimaCompra <= 90, 3,
        DiasDesdeUltimaCompra <= 180, 2,
        1
    )
```

#### Análisis de Cohorts
```dax
RetencionMensual = 
VAR PrimerMesCliente = 
    CALCULATE(
        MIN(FactVentas[FechaVenta]),
        ALLEXCEPT(FactVentas, FactVentas[ClienteID])
    )
VAR MesActual = MAX(DimFecha[Fecha])
VAR ClientesCohorte = 
    CALCULATE(
        DISTINCTCOUNT(FactVentas[ClienteID]),
        FILTER(
            ALL(FactVentas),
            FORMAT(FactVentas[FechaVenta], "YYYY-MM") = 
            FORMAT(PrimerMesCliente, "YYYY-MM")
        )
    )
VAR ClientesActivos = 
    DISTINCTCOUNT(FactVentas[ClienteID])
RETURN
    DIVIDE(ClientesActivos, ClientesCohorte)
```

## Dashboards Implementados

### 1. Dashboard Ejecutivo
**Audiencia**: C-Level, Directores
**Actualización**: Diaria
**Contenido**:
- KPIs principales con variación vs objetivo
- Tendencias de ventas y margen
- Top 10 productos y regiones
- Alertas automáticas de performance

### 2. Dashboard Operacional
**Audiencia**: Gerentes regionales, Jefes de tienda
**Actualización**: Tiempo real
**Contenido**:
- Performance diaria vs objetivo
- Inventario y rotación de productos
- Productividad de empleados
- Satisfacción del cliente

### 3. Dashboard Analítico
**Audiencia**: Analistas, Marketing
**Actualización**: Semanal
**Contenido**:
- Análisis de cohorts y retención
- Segmentación de clientes
- Análisis de canasta de mercado
- Efectividad de campañas

## Aspectos Técnicos Destacados

### Optimizaciones Implementadas

#### Modelo de Datos
- **Agregaciones automáticas** para queries comunes
- **Incremental refresh** en tabla de hechos
- **Particionamiento** por año para performance
- **Compresión optimizada** con tipos de datos apropiados

#### DAX Optimization
```dax
// Uso de variables para optimización
VentasOptimizadas = 
VAR VentasBase = SUM(FactVentas[ImporteTotal])
VAR FactorCambio = 1.21  // IVA
RETURN
    VentasBase * FactorCambio
```

#### Query Folding
- Transformaciones optimizadas en Power Query
- Filtros aplicados en fuente de datos
- Agregaciones pre-calculadas en views

### Gobernanza Implementada

#### Seguridad
```dax
// Row-Level Security por región
[Region] = USERNAME()
```

#### Documentación
- Descripción de cada medida y columna
- Lineage de datos documentado
- Glosario de términos de negocio
- Procedimientos de actualización

## Resultados y Beneficios

### Impacto en el Negocio
- **15% mejora** en identificación de oportunidades de venta
- **25% reducción** en tiempo de preparación de reportes
- **30% mejor** precisión en forecasting de inventario
- **Decisiones más rápidas** basadas en datos en tiempo real

### Adopción del Usuario
- **85% adopción** en primeros 3 meses
- **Reducción 70%** en solicitudes de reportes ad-hoc
- **Mejora significativa** en satisfacción del usuario
- **Training exitoso** de equipos regionales

## Lecciones Aprendidas

### Éxitos
1. **Modelado incremental** permitió escalabilidad
2. **Colaboración estrecha** con negocio aseguró adopción
3. **Documentación extensa** facilitó mantenimiento
4. **Testing riguroso** previno errores en producción

### Desafíos Superados
1. **Performance inicial** mejorada con agregaciones
2. **Calidad de datos** mejorada con validaciones
3. **Cambios de requerimientos** manejados con arquitectura flexible
4. **Adopción del usuario** lograda con training y soporte

## Próximos Pasos

### Roadmap Técnico
- Integración con Microsoft Fabric
- Implementación de Machine Learning
- Real-time analytics con streaming datasets
- Automatización avanzada con Power Automate

### Expansión Funcional
- Análisis predictivo de demanda
- Optimización de precios dinámicos
- Análisis de sentiment de clientes
- Integración con IoT de tiendas

---

**Nota**: Este caso de estudio está diseñado como material educativo y utiliza datos simulados. Los archivos de datos y el modelo .pbix están incluidos en la carpeta `data/` para práctica y referencia.
