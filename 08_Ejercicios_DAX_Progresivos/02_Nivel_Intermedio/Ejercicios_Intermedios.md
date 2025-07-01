# Ejercicios DAX - Nivel Intermedio

## Introducción

En el nivel intermedio, el estudiante profundiza en conceptos más avanzados de DAX como Time Intelligence, funciones de tabla, y el uso de variables. Se enfoca en crear análisis temporales y cálculos más sofisticados que requieren comprensión del contexto de evaluación.

---

## Ejercicio 1: Time Intelligence Fundamental

### Contexto
Se necesita implementar análisis comparativos temporales para entender la evolución de las ventas a lo largo del tiempo.

### Objetivo
Crear medidas que permitan:
- Comparar ventas con períodos anteriores
- Calcular crecimientos y variaciones
- Analizar tendencias temporales

### Datos Necesarios
- Tabla `Calendario` con fechas continuas
- Tabla `Ventas` relacionada por fecha
- Relación activa entre ambas tablas

### Solución Paso a Paso

#### Paso 1: Ventas del Año Anterior
```dax
Ventas_Año_Anterior = 
CALCULATE(
    SUM(Ventas[Monto]),
    SAMEPERIODLASTYEAR(Calendario[Fecha])
)
```

**Explicación técnica:** SAMEPERIODLASTYEAR() desplaza el contexto de fecha exactamente un año hacia atrás. La función respeta automáticamente los filtros existentes y los aplica al período anterior correspondiente.

#### Paso 2: Crecimiento Anual
```dax
Crecimiento_Anual = 
VAR VentasActuales = SUM(Ventas[Monto])
VAR VentasAñoAnterior = [Ventas_Año_Anterior]
RETURN
IF(
    NOT(ISBLANK(VentasAñoAnterior)) && VentasAñoAnterior <> 0,
    DIVIDE(VentasActuales - VentasAñoAnterior, VentasAñoAnterior),
    BLANK()
)
```

**Explicación técnica:** Las variables (VAR) almacenan cálculos intermedios, mejorando la legibilidad y eficiencia. La validación asegura que no se calculen crecimientos cuando no hay datos de comparación.

#### Paso 3: Acumulado del Año
```dax
Ventas_YTD = 
CALCULATE(
    SUM(Ventas[Monto]),
    DATESYTD(Calendario[Fecha])
)
```

**Explicación técnica:** DATESYTD() (Year To Date) retorna todas las fechas desde el inicio del año hasta la fecha actual en contexto. Esto permite calcular totales acumulados del año en curso.

#### Paso 4: Mes Anterior
```dax
Ventas_Mes_Anterior = 
CALCULATE(
    SUM(Ventas[Monto]),
    PREVIOUSMONTH(Calendario[Fecha])
)
```

**Explicación técnica:** PREVIOUSMONTH() desplaza el contexto al mes inmediatamente anterior. Es útil para comparaciones mes a mes en análisis de tendencias.

---

## Ejercicio 2: Funciones de Variables y Cálculos Complejos

### Contexto
Se requiere crear medidas complejas que realicen múltiples cálculos interrelacionados de manera eficiente.

### Objetivo
Implementar medidas que:
- Utilicen variables para mejorar rendimiento
- Realicen cálculos condicionales complejos
- Combinen múltiples fuentes de datos

### Solución Paso a Paso

#### Paso 1: Análisis de Rendimiento de Vendedores
```dax
Performance_Vendedor = 
VAR VentasVendedor = SUM(Ventas[Monto])
VAR MetaVendedor = MAX(Vendedores[Meta])
VAR PorcentajeMeta = DIVIDE(VentasVendedor, MetaVendedor, 0)
VAR ClasificacionBase = 
    SWITCH(
        TRUE(),
        PorcentajeMeta >= 1.20, "Excepcional",
        PorcentajeMeta >= 1.00, "Cumple Meta",
        PorcentajeMeta >= 0.80, "Cerca de Meta",
        "Por Debajo de Meta"
    )
RETURN
ClasificacionBase & " (" & FORMAT(PorcentajeMeta, "0%") & ")"
```

**Explicación técnica:** Las variables permiten reutilizar cálculos complejos sin recalcularlos. SWITCH con TRUE() evalúa condiciones en orden hasta encontrar la primera verdadera.

#### Paso 2: Cálculo de Comisiones Variables
```dax
Comision_Calculada = 
VAR VentasTotales = SUM(Ventas[Monto])
VAR TasaBase = MAX(Vendedores[Comision])
VAR Bonificacion = 
    SWITCH(
        TRUE(),
        VentasTotales > 100000, 0.02,
        VentasTotales > 50000, 0.01,
        0
    )
VAR TasaFinal = TasaBase + Bonificacion
RETURN
VentasTotales * TasaFinal
```

**Explicación técnica:** Este cálculo implementa una estructura de comisiones escalonada donde la tasa aumenta según el volumen de ventas. Las variables hacen el código más legible y eficiente.

---

## Ejercicio 3: Funciones de Tabla y SUMMARIZE

### Contexto
Se necesita crear análisis que requieran manipulación de tablas virtuales para obtener insights específicos.

### Objetivo
Desarrollar medidas que:
- Trabajen con tablas virtuales
- Realicen agrupaciones dinámicas
- Calculen rankings y percentiles

### Solución Paso a Paso

#### Paso 1: Top 5 Productos por Ventas
```dax
Top_5_Productos = 
VAR TablaProductos = 
    SUMMARIZE(
        Ventas,
        Productos[NombreProducto],
        "VentasProducto", SUM(Ventas[Monto])
    )
VAR TablaOrdenada = 
    TOPN(
        5,
        TablaProductos,
        [VentasProducto],
        DESC
    )
VAR ResultadoTexto = 
    CONCATENATEX(
        TablaOrdenada,
        Productos[NombreProducto] & ": " & FORMAT([VentasProducto], "#,##0"),
        UNICHAR(10)
    )
RETURN
ResultadoTexto
```

**Explicación técnica:** SUMMARIZE() crea una tabla virtual agrupando datos. TOPN() selecciona los mejores N registros. CONCATENATEX() combina múltiples valores en texto separado por líneas.

#### Paso 2: Análisis de Percentiles
```dax
Percentil_Ventas = 
VAR TablaVentas = 
    SUMMARIZE(
        Ventas,
        Ventas[VentaID],
        "MontoVenta", SUM(Ventas[Monto])
    )
VAR VentaActual = SUM(Ventas[Monto])
VAR Percentil = 
    DIVIDE(
        COUNTROWS(
            FILTER(
                TablaVentas,
                [MontoVenta] <= VentaActual
            )
        ),
        COUNTROWS(TablaVentas),
        0
    )
RETURN
FORMAT(Percentil, "0%")
```

**Explicación técnica:** Este cálculo determina en qué percentil se encuentra una venta específica comparada con todas las demás ventas en el contexto actual.

---

## Ejercicio 4: Filtros Avanzados y Contexto

### Contexto
Se requiere implementar medidas que manipulen el contexto de filtro de manera sofisticada para obtener comparaciones específicas.

### Objetivo
Crear medidas que:
- Modifiquen contextos de filtro específicos
- Realicen comparaciones cruzadas
- Implementen filtros condicionales

### Solución Paso a Paso

#### Paso 1: Participación en el Total General
```dax
Participacion_Total = 
VAR VentasSegmento = SUM(Ventas[Monto])
VAR VentasTotales = 
    CALCULATE(
        SUM(Ventas[Monto]),
        ALL(Clientes[Segmento])
    )
RETURN
DIVIDE(VentasSegmento, VentasTotales, 0)
```

**Explicación técnica:** ALL() remueve filtros específicos de una columna, permitiendo calcular el total general. Esto es útil para calcular participaciones relativas.

#### Paso 2: Comparación con Mejor Mes
```dax
vs_Mejor_Mes = 
VAR VentasMesActual = SUM(Ventas[Monto])
VAR MejorMes = 
    CALCULATE(
        MAX(SUM(Ventas[Monto])),
        ALL(Calendario[Fecha]),
        VALUES(Calendario[Año])
    )
VAR Diferencia = VentasMesActual - MejorMes
RETURN
IF(
    Diferencia >= 0,
    "+" & FORMAT(Diferencia, "#,##0"),
    FORMAT(Diferencia, "#,##0")
)
```

**Explicación técnica:** VALUES() preserva el filtro del año actual mientras ALL() remueve filtros de fecha. Esto permite comparar con el mejor mes del año actual.

#### Paso 3: Filtro Condicional por Rango
```dax
Ventas_Rango_Alto = 
CALCULATE(
    SUM(Ventas[Monto]),
    FILTER(
        Ventas,
        Ventas[Monto] > 
        CALCULATE(
            AVERAGE(Ventas[Monto]),
            ALL()
        )
    )
)
```

**Explicación técnica:** FILTER() permite aplicar condiciones dinámicas. En este caso, suma solo las ventas que están por encima del promedio general.

---

## Ejercicio 5: Medidas de Análisis de Clientes

### Contexto
Se necesita implementar análisis sofisticados de comportamiento de clientes y segmentación.

### Objetivo
Desarrollar medidas para:
- Analizar frecuencia de compra
- Calcular valor de vida del cliente básico
- Segmentar clientes por comportamiento

### Solución Paso a Paso

#### Paso 1: Frecuencia de Compra del Cliente
```dax
Frecuencia_Compra = 
VAR ClienteSeleccionado = SELECTEDVALUE(Clientes[ClienteID])
VAR PrimeraCompra = 
    CALCULATE(
        MIN(Ventas[Fecha]),
        Ventas[ClienteID] = ClienteSeleccionado
    )
VAR UltimaCompra = 
    CALCULATE(
        MAX(Ventas[Fecha]),
        Ventas[ClienteID] = ClienteSeleccionado
    )
VAR DiasActivo = UltimaCompra - PrimeraCompra + 1
VAR NumeroCompras = 
    CALCULATE(
        DISTINCTCOUNT(Ventas[VentaID]),
        Ventas[ClienteID] = ClienteSeleccionado
    )
RETURN
IF(
    DiasActivo > 0,
    DIVIDE(NumeroCompras, DiasActivo, 0) * 30,
    BLANK()
)
```

**Explicación técnica:** Esta medida calcula cuántas compras por mes realiza un cliente en promedio, considerando su período de actividad total.

#### Paso 2: Valor Promedio del Cliente
```dax
Valor_Promedio_Cliente = 
VAR ClienteSeleccionado = SELECTEDVALUE(Clientes[ClienteID])
VAR TotalGastado = 
    CALCULATE(
        SUM(Ventas[Monto]),
        Ventas[ClienteID] = ClienteSeleccionado
    )
VAR NumeroCompras = 
    CALCULATE(
        DISTINCTCOUNT(Ventas[VentaID]),
        Ventas[ClienteID] = ClienteSeleccionado
    )
RETURN
DIVIDE(TotalGastado, NumeroCompras, 0)
```

**Explicación técnica:** Calcula el ticket promedio por cliente dividiendo el gasto total entre el número de transacciones realizadas.

---

## Ejercicio 6: Medidas de Inventario y Stock

### Contexto
Se requiere implementar análisis de rotación de inventario y disponibilidad de productos.

### Objetivo
Crear medidas que:
- Calculen rotación de inventario
- Identifiquen productos de movimiento lento
- Analicen días de inventario

### Solución Paso a Paso

#### Paso 1: Rotación de Inventario
```dax
Rotacion_Inventario = 
VAR CostoVentasAnual = 
    CALCULATE(
        SUMX(
            Ventas,
            Ventas[Cantidad] * RELATED(Productos[CostoUnitario])
        ),
        DATESYTD(Calendario[Fecha])
    )
VAR InventarioPromedio = 
    CALCULATE(
        AVERAGE(Productos[Stock]) * AVERAGE(Productos[CostoUnitario])
    )
RETURN
DIVIDE(CostoVentasAnual, InventarioPromedio, 0)
```

**Explicación técnica:** La rotación de inventario mide cuántas veces se vendió el inventario promedio durante el año. Un valor alto indica gestión eficiente del inventario.

#### Paso 2: Días de Inventario
```dax
Dias_Inventario = 
VAR RotacionInventario = [Rotacion_Inventario]
RETURN
IF(
    RotacionInventario > 0,
    365 / RotacionInventario,
    BLANK()
)
```

**Explicación técnica:** Convierte la rotación de inventario en días, indicando cuántos días duraría el inventario actual al ritmo de ventas actual.

---

## Ejercicios Prácticos para el Estudiante

### Ejercicio A: Análisis Temporal Avanzado
Implementar medidas que calculen:
1. Crecimiento trimestre a trimestre
2. Promedio móvil de 3 meses
3. Identificación de tendencias ascendentes/descendentes

### Ejercicio B: Análisis de Rentabilidad
Desarrollar medidas para:
1. Margen de contribución por producto
2. Punto de equilibrio por categoría
3. Análisis de rentabilidad por canal de venta

### Ejercicio C: Segmentación Avanzada
Crear medidas que:
1. Clasifiquen clientes en quintiles por gasto
2. Identifiquen clientes en riesgo de abandono
3. Calculen el lifetime value básico

---

## Mejores Prácticas para Nivel Intermedio

### 1. Uso Eficiente de Variables
- Almacenar cálculos complejos en variables
- Reutilizar variables para mejorar rendimiento
- Documentar variables con nombres descriptivos

### 2. Manipulación de Contexto
- Entender cuándo usar ALL(), ALLEXCEPT(), VALUES()
- Combinar funciones de time intelligence apropiadamente
- Validar resultados en diferentes contextos de filtro

### 3. Funciones de Tabla
- Usar SUMMARIZE() para agrupaciones complejas
- Implementar TOPN() para rankings dinámicos
- Combinar tablas virtuales eficientemente

---

## Evaluación del Nivel Intermedio

Para completar exitosamente este nivel, el estudiante debe demostrar competencia en:

### Conceptos Avanzados
- Comprensión profunda del contexto de filtro
- Uso efectivo de time intelligence
- Manipulación de tablas virtuales

### Funciones Especializadas
- CALCULATE con múltiples filtros
- SUMMARIZE, TOPN, CONCATENATEX
- SAMEPERIODLASTYEAR, DATESYTD, PREVIOUSMONTH
- Variables y estructuras de control complejas

### Habilidades Analíticas
- Crear análisis temporales comparativos
- Implementar segmentación de clientes
- Desarrollar métricas de rendimiento personalizadas

---

**"En el nivel intermedio, DAX se convierte en una herramienta poderosa para descubrir insights ocultos en los datos a través del dominio del tiempo y el contexto."**
