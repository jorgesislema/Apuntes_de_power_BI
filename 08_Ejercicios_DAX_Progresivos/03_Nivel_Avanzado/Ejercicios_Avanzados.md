# Ejercicios DAX - Nivel Avanzado

## Introducción

En el nivel avanzado, el estudiante domina conceptos sofisticados de DAX incluyendo funciones de iteración complejas, manipulación avanzada de contextos, y técnicas de optimización. Se enfoca en resolver problemas de negocio complejos que requieren análisis multidimensional.

---

## Ejercicio 1: Análisis de Correlación y Tendencias

### Contexto
Se necesita implementar análisis estadísticos avanzados para identificar correlaciones entre variables y detectar tendencias en los datos.

### Objetivo
Crear medidas que permitan:
- Calcular correlaciones entre métricas
- Identificar tendencias automáticamente
- Realizar análisis de regresión básica

### Datos Necesarios
- Tabla `Ventas` con datos históricos
- Tabla `Calendario` para análisis temporal
- Múltiples métricas para correlacionar

### Solución Paso a Paso

#### Paso 1: Cálculo de Correlación
```dax
Correlacion_Ventas_Publicidad = 
VAR TablaBase = 
    SUMMARIZE(
        FILTER(
            ALL(Calendario),
            Calendario[Fecha] >= DATE(2023, 1, 1)
        ),
        Calendario[AñoMes],
        "Ventas", CALCULATE(SUM(Ventas[Monto])),
        "Publicidad", CALCULATE(SUM(Marketing[Inversion]))
    )
VAR N = COUNTROWS(TablaBase)
VAR PromedioVentas = AVERAGEX(TablaBase, [Ventas])
VAR PromedioPublicidad = AVERAGEX(TablaBase, [Publicidad])
VAR Numerador = 
    SUMX(
        TablaBase,
        ([Ventas] - PromedioVentas) * ([Publicidad] - PromedioPublicidad)
    )
VAR DenominadorVentas = 
    SUMX(
        TablaBase,
        ([Ventas] - PromedioVentas) ^ 2
    )
VAR DenominadorPublicidad = 
    SUMX(
        TablaBase,
        ([Publicidad] - PromedioPublicidad) ^ 2
    )
VAR Correlacion = 
    DIVIDE(
        Numerador,
        SQRT(DenominadorVentas * DenominadorPublicidad),
        0
    )
RETURN
Correlacion
```

**Explicación técnica:** Esta medida implementa el coeficiente de correlación de Pearson para medir la relación lineal entre ventas y inversión publicitaria. Utiliza una tabla virtual para organizar los datos por período y luego aplica la fórmula estadística estándar.

#### Paso 2: Detección de Tendencias
```dax
Tendencia_Ventas = 
VAR PeriodosAnalisis = 6
VAR TablaBase = 
    ADDCOLUMNS(
        TOPN(
            PeriodosAnalisis,
            ALL(Calendario[AñoMes]),
            Calendario[AñoMes],
            DESC
        ),
        "Ventas", CALCULATE(SUM(Ventas[Monto])),
        "Periodo", Calendario[AñoMes] - MIN(ALL(Calendario[AñoMes])) + 1
    )
VAR N = COUNTROWS(TablaBase)
VAR SumaX = SUMX(TablaBase, [Periodo])
VAR SumaY = SUMX(TablaBase, [Ventas])
VAR SumaXY = SUMX(TablaBase, [Periodo] * [Ventas])
VAR SumaX2 = SUMX(TablaBase, [Periodo] ^ 2)
VAR Pendiente = 
    DIVIDE(
        (N * SumaXY) - (SumaX * SumaY),
        (N * SumaX2) - (SumaX ^ 2),
        0
    )
VAR TipoTendencia = 
    SWITCH(
        TRUE(),
        Pendiente > 1000, "Crecimiento Fuerte",
        Pendiente > 0, "Crecimiento Moderado",
        Pendiente > -1000, "Decrecimiento Moderado",
        "Decrecimiento Fuerte"
    )
RETURN
TipoTendencia
```

**Explicación técnica:** Esta medida calcula la pendiente de una línea de tendencia usando regresión lineal simple sobre los últimos períodos. La pendiente indica si las ventas están aumentando o disminuyendo y a qué velocidad.

---

## Ejercicio 2: Análisis de Cohorte Básico

### Contexto
Se requiere implementar un análisis de cohorte para estudiar el comportamiento de retención de clientes a lo largo del tiempo.

### Objetivo
Desarrollar medidas que:
- Identifiquen cohortes de clientes
- Calculen tasas de retención por cohorte
- Analicen el comportamiento a lo largo del tiempo

### Solución Paso a Paso

#### Paso 1: Identificación de Cohorte
```dax
Mes_Cohorte = 
VAR ClienteActual = SELECTEDVALUE(Clientes[ClienteID])
VAR PrimeraCompra = 
    CALCULATE(
        MIN(Ventas[Fecha]),
        Ventas[ClienteID] = ClienteActual
    )
VAR MesCohorte = 
    YEAR(PrimeraCompra) * 100 + MONTH(PrimeraCompra)
RETURN
MesCohorte
```

**Explicación técnica:** Esta medida identifica el mes de la primera compra de cada cliente, que define su cohorte. Se expresa como AAAALL para facilitar agrupaciones.

#### Paso 2: Período Relativo de Actividad
```dax
Periodo_Actividad = 
VAR ClienteActual = SELECTEDVALUE(Clientes[ClienteID])
VAR PrimeraCompra = 
    CALCULATE(
        MIN(Ventas[Fecha]),
        Ventas[ClienteID] = ClienteActual
    )
VAR FechaAnalisis = MAX(Calendario[Fecha])
VAR MesesDiferencia = 
    (YEAR(FechaAnalisis) - YEAR(PrimeraCompra)) * 12 + 
    (MONTH(FechaAnalisis) - MONTH(PrimeraCompra))
RETURN
MesesDiferencia
```

**Explicación técnica:** Calcula cuántos meses han transcurrido desde la primera compra del cliente hasta el período de análisis. Esto permite analizar la retención en diferentes momentos del ciclo de vida.

#### Paso 3: Tasa de Retención por Cohorte
```dax
Tasa_Retencion = 
VAR CohorteActual = [Mes_Cohorte]
VAR PeriodoActual = [Periodo_Actividad]
VAR ClientesCohorte = 
    CALCULATE(
        DISTINCTCOUNT(Clientes[ClienteID]),
        FILTER(
            ALL(Clientes),
            [Mes_Cohorte] = CohorteActual
        )
    )
VAR ClientesActivos = 
    CALCULATE(
        DISTINCTCOUNT(Ventas[ClienteID]),
        FILTER(
            ALL(Clientes),
            [Mes_Cohorte] = CohorteActual && [Periodo_Actividad] = PeriodoActual
        )
    )
RETURN
DIVIDE(ClientesActivos, ClientesCohorte, 0)
```

**Explicación técnica:** Calcula qué porcentaje de clientes de una cohorte específica siguen activos en un período determinado, permitiendo analizar patrones de retención.

---

## Ejercicio 3: Análisis ABC/XYZ Multidimensional

### Contexto
Se necesita implementar una clasificación ABC/XYZ que considere múltiples dimensiones para una segmentación sofisticada de productos.

### Objetivo
Crear medidas que:
- Clasifiquen productos por valor (ABC)
- Clasifiquen productos por variabilidad (XYZ)
- Combinen ambas clasificaciones

### Solución Paso a Paso

#### Paso 1: Clasificación ABC por Valor
```dax
Clasificacion_ABC = 
VAR ProductoActual = SELECTEDVALUE(Productos[ProductoID])
VAR VentasProducto = 
    CALCULATE(
        SUM(Ventas[Monto]),
        Productos[ProductoID] = ProductoActual
    )
VAR TablaProductos = 
    ADDCOLUMNS(
        ALL(Productos[ProductoID]),
        "VentasProducto", 
        CALCULATE(SUM(Ventas[Monto]))
    )
VAR TablaOrdenada = 
    ADDCOLUMNS(
        TablaProductos,
        "VentasAcumuladas",
        VAR ProductoAnalisis = [ProductoID]
        VAR VentasProductoAnalisis = [VentasProducto]
        RETURN
        SUMX(
            FILTER(
                TablaProductos,
                [VentasProducto] >= VentasProductoAnalisis
            ),
            [VentasProducto]
        )
    )
VAR VentasTotales = SUMX(TablaOrdenada, [VentasProducto])
VAR PorcentajeAcumulado = 
    DIVIDE(
        LOOKUPVALUE(
            TablaOrdenada[VentasAcumuladas],
            TablaOrdenada[ProductoID], ProductoActual
        ),
        VentasTotales
    )
VAR ClasificacionABC = 
    SWITCH(
        TRUE(),
        PorcentajeAcumulado <= 0.8, "A",
        PorcentajeAcumulado <= 0.95, "B",
        "C"
    )
RETURN
ClasificacionABC
```

**Explicación técnica:** Implementa la clasificación ABC tradicional basada en el principio de Pareto, donde los productos A representan el 80% de las ventas, B el siguiente 15%, y C el 5% restante.

#### Paso 2: Clasificación XYZ por Variabilidad
```dax
Clasificacion_XYZ = 
VAR ProductoActual = SELECTEDVALUE(Productos[ProductoID])
VAR TablaVentasMensuales = 
    SUMMARIZE(
        FILTER(
            Ventas,
            Productos[ProductoID] = ProductoActual
        ),
        Calendario[AñoMes],
        "VentasMes", SUM(Ventas[Monto])
    )
VAR PromedioVentas = AVERAGEX(TablaVentasMensuales, [VentasMes])
VAR DesviacionEstandar = 
    SQRT(
        AVERAGEX(
            TablaVentasMensuales,
            ([VentasMes] - PromedioVentas) ^ 2
        )
    )
VAR CoeficienteVariacion = 
    DIVIDE(DesviacionEstandar, PromedioVentas, 0)
VAR ClasificacionXYZ = 
    SWITCH(
        TRUE(),
        CoeficienteVariacion <= 0.5, "X",
        CoeficienteVariacion <= 1.0, "Y",
        "Z"
    )
RETURN
ClasificacionXYZ
```

**Explicación técnica:** La clasificación XYZ se basa en el coeficiente de variación de las ventas mensuales. X indica baja variabilidad (predecible), Y variabilidad media, y Z alta variabilidad (impredecible).

#### Paso 3: Matriz ABC/XYZ Combinada
```dax
Estrategia_ABC_XYZ = 
VAR ClasifABC = [Clasificacion_ABC]
VAR ClasifXYZ = [Clasificacion_XYZ]
VAR Estrategia = 
    SWITCH(
        ClasifABC & ClasifXYZ,
        "AX", "Gestión Intensiva - Stock Alto",
        "AY", "Monitoreo Continuo - Stock Medio",
        "AZ", "Análisis Especial - Stock Variable",
        "BX", "Gestión Rutinaria - Stock Medio",
        "BY", "Revisión Periódica - Stock Bajo",
        "BZ", "Gestión Flexible - Stock Mínimo",
        "CX", "Gestión Básica - Stock Bajo",
        "CY", "Revisión Ocasional - Stock Mínimo",
        "CZ", "Gestión Pasiva - Bajo Demanda",
        "Sin Clasificar"
    )
RETURN
Estrategia
```

**Explicación técnica:** Combina ambas clasificaciones para generar una estrategia de gestión específica para cada producto, considerando tanto su importancia económica como su predictibilidad.

---

## Ejercicio 4: Análisis de Canasta de Mercado

### Contexto
Se requiere implementar análisis de asociación para identificar productos que se compran juntos frecuentemente.

### Objetivo
Desarrollar medidas que:
- Calculen soporte de productos individuales
- Determinen confianza entre productos
- Identifiquen reglas de asociación

### Solución Paso a Paso

#### Paso 1: Soporte de Producto
```dax
Soporte_Producto = 
VAR ProductoActual = SELECTEDVALUE(Productos[ProductoID])
VAR TransaccionesConProducto = 
    CALCULATE(
        DISTINCTCOUNT(Ventas[VentaID]),
        Productos[ProductoID] = ProductoActual
    )
VAR TotalTransacciones = DISTINCTCOUNT(Ventas[VentaID])
RETURN
DIVIDE(TransaccionesConProducto, TotalTransacciones, 0)
```

**Explicación técnica:** El soporte mide qué tan frecuentemente aparece un producto en todas las transacciones. Es la base para calcular métricas de asociación más complejas.

#### Paso 2: Productos Frecuentemente Comprados Juntos
```dax
Productos_Asociados = 
VAR ProductoBase = SELECTEDVALUE(Productos[ProductoID])
VAR TransaccionesConBase = 
    CALCULATETABLE(
        VALUES(Ventas[VentaID]),
        Productos[ProductoID] = ProductoBase
    )
VAR TablaAsociaciones = 
    ADDCOLUMNS(
        FILTER(
            ALL(Productos[ProductoID]),
            Productos[ProductoID] <> ProductoBase
        ),
        "Producto", Productos[ProductoID],
        "NombreProducto", RELATED(Productos[NombreProducto]),
        "Confianza",
        VAR ProductoAsociado = Productos[ProductoID]
        VAR TransaccionesJuntos = 
            CALCULATE(
                DISTINCTCOUNT(Ventas[VentaID]),
                Productos[ProductoID] = ProductoAsociado,
                Ventas[VentaID] IN TransaccionesConBase
            )
        VAR TransaccionesBase = COUNTROWS(TransaccionesConBase)
        RETURN DIVIDE(TransaccionesJuntos, TransaccionesBase, 0)
    )
VAR Top3Asociados = 
    TOPN(
        3,
        TablaAsociaciones,
        [Confianza],
        DESC
    )
RETURN
CONCATENATEX(
    Top3Asociados,
    [NombreProducto] & " (" & FORMAT([Confianza], "0%") & ")",
    ", "
)
```

**Explicación técnica:** Esta medida identifica los productos que más frecuentemente se compran junto con el producto seleccionado, calculando la confianza de la regla de asociación.

---

## Ejercicio 5: Optimización de Precios Dinámicos

### Contexto
Se necesita implementar un modelo de optimización de precios que considere elasticidad, competencia y margen objetivo.

### Objetivo
Crear medidas que:
- Calculen elasticidad precio-demanda
- Determinen precios óptimos
- Simulen impacto de cambios de precio

### Solución Paso a Paso

#### Paso 1: Elasticidad de Precio
```dax
Elasticidad_Precio = 
VAR ProductoActual = SELECTEDVALUE(Productos[ProductoID])
VAR DatosPrecio = 
    ADDCOLUMNS(
        FILTER(
            SUMMARIZE(
                Ventas,
                Calendario[AñoMes],
                "PrecioPromedio", AVERAGE(Ventas[PrecioUnitario]),
                "CantidadVendida", SUM(Ventas[Cantidad])
            ),
            [CantidadVendida] > 0
        ),
        "LogPrecio", LN([PrecioPromedio]),
        "LogCantidad", LN([CantidadVendida])
    )
VAR N = COUNTROWS(DatosPrecio)
VAR PromedioLogPrecio = AVERAGEX(DatosPrecio, [LogPrecio])
VAR PromedioLogCantidad = AVERAGEX(DatosPrecio, [LogCantidad])
VAR Numerador = 
    SUMX(
        DatosPrecio,
        ([LogPrecio] - PromedioLogPrecio) * ([LogCantidad] - PromedioLogCantidad)
    )
VAR Denominador = 
    SUMX(
        DatosPrecio,
        ([LogPrecio] - PromedioLogPrecio) ^ 2
    )
VAR Elasticidad = DIVIDE(Numerador, Denominador, 0)
RETURN
Elasticidad
```

**Explicación técnica:** Calcula la elasticidad precio-demanda usando regresión logarítmica, que es más apropiada para modelos de elasticidad ya que los coeficientes representan directamente las elasticidades.

#### Paso 2: Precio Óptimo Sugerido
```dax
Precio_Optimo = 
VAR ElasticidadActual = [Elasticidad_Precio]
VAR CostoUnitario = SELECTEDVALUE(Productos[CostoUnitario])
VAR MargenObjetivo = 0.4  // 40% margen objetivo
VAR PrecioBaseCosto = DIVIDE(CostoUnitario, (1 - MargenObjetivo))
VAR PrecioActual = SELECTEDVALUE(Productos[Precio])
VAR FactorElasticidad = 
    IF(
        ElasticidadActual < -1,  // Elástico
        0.95,  // Reducir precio ligeramente
        1.05   // Aumentar precio ligeramente
    )
VAR PrecioSugerido = PrecioActual * FactorElasticidad
VAR PrecioFinal = 
    MAX(
        PrecioBaseCosto,  // No menos que precio base con margen
        MIN(
            PrecioSugerido,
            PrecioActual * 1.2  // No más de 20% de aumento
        )
    )
RETURN
PrecioFinal
```

**Explicación técnica:** Combina múltiples factores para sugerir un precio óptimo: elasticidad calculada, margen objetivo, y restricciones de cambio máximo para evitar shocks de precio.

---

## Ejercicio 6: Pronóstico de Demanda Simple

### Contexto
Se requiere implementar un modelo básico de pronóstico que combine tendencia estacional con suavizado exponencial.

### Objetivo
Desarrollar medidas que:
- Detecten patrones estacionales
- Calculen tendencias
- Generen pronósticos a corto plazo

### Solución Paso a Paso

#### Paso 1: Índice Estacional
```dax
Indice_Estacional = 
VAR MesActual = MONTH(MAX(Calendario[Fecha]))
VAR PromedioGeneral = 
    CALCULATE(
        AVERAGE(SUM(Ventas[Monto])),
        ALL(Calendario[Fecha])
    )
VAR PromedioMes = 
    CALCULATE(
        AVERAGE(SUM(Ventas[Monto])),
        ALL(Calendario[Fecha]),
        MONTH(Calendario[Fecha]) = MesActual
    )
RETURN
DIVIDE(PromedioMes, PromedioGeneral, 1)
```

**Explicación técnica:** El índice estacional compara las ventas promedio de cada mes con el promedio general anual, identificando meses de alta y baja demanda.

#### Paso 2: Tendencia Linear
```dax
Tendencia_Linear = 
VAR UltimosMeses = 12
VAR TablaBase = 
    ADDCOLUMNS(
        TOPN(
            UltimosMeses,
            SUMMARIZE(
                Ventas,
                Calendario[AñoMes],
                "Ventas", SUM(Ventas[Monto])
            ),
            Calendario[AñoMes],
            DESC
        ),
        "Periodo", 
        RANKX(
            TOPN(
                UltimosMeses,
                SUMMARIZE(
                    Ventas,
                    Calendario[AñoMes],
                    "Ventas", SUM(Ventas[Monto])
                ),
                Calendario[AñoMes],
                DESC
            ),
            Calendario[AñoMes],
            ASC
        )
    )
VAR N = COUNTROWS(TablaBase)
VAR SumaX = SUMX(TablaBase, [Periodo])
VAR SumaY = SUMX(TablaBase, [Ventas])
VAR SumaXY = SUMX(TablaBase, [Periodo] * [Ventas])
VAR SumaX2 = SUMX(TablaBase, [Periodo] ^ 2)
VAR Pendiente = 
    DIVIDE(
        (N * SumaXY) - (SumaX * SumaY),
        (N * SumaX2) - (SumaX ^ 2),
        0
    )
RETURN
Pendiente
```

**Explicación técnica:** Calcula la pendiente de la tendencia usando regresión lineal sobre los últimos 12 meses, proporcionando la tasa de crecimiento o decrecimiento mensual.

---

## Ejercicios Prácticos para el Estudiante

### Ejercicio A: Customer Lifetime Value Avanzado
Implementar un modelo CLV que incluya:
1. Probabilidad de retención por segmento
2. Valor presente neto de flujos futuros
3. Análisis de sensibilidad por variables

### Ejercicio B: Análisis de Atribución Multicanal
Desarrollar medidas para:
1. Atribución de primer y último toque
2. Modelos de atribución ponderada
3. Análisis de journey del cliente

### Ejercicio C: Optimización de Inventario
Crear medidas que:
1. Calculen puntos de reorden dinámicos
2. Optimicen niveles de stock por estacionalidad
3. Identifiquen productos obsoletos automáticamente

---

## Mejores Prácticas para Nivel Avanzado

### 1. Optimización de Rendimiento
- Usar variables para cálculos complejos repetitivos
- Minimizar el número de transiciones de contexto
- Evaluar alternativas de implementación

### 2. Manejo de Complejidad
- Dividir medidas complejas en componentes
- Documentar lógica de negocio detalladamente
- Validar resultados con múltiples escenarios

### 3. Escalabilidad
- Diseñar medidas que funcionen con volúmenes grandes
- Considerar impacto en memory y CPU
- Implementar validaciones automáticas

---

## Evaluación del Nivel Avanzado

Para completar exitosamente este nivel, el estudiante debe demostrar competencia en:

### Conceptos Expertos
- Análisis estadístico en DAX
- Optimización de contextos complejos
- Implementación de algoritmos de negocio

### Funciones Especializadas
- SUMX, AVERAGEX con lógica compleja
- Combinaciones avanzadas de funciones de tabla
- Manipulación sofisticada de contextos

### Habilidades de Resolución
- Traducir problemas de negocio complejos a DAX
- Optimizar soluciones para rendimiento
- Crear frameworks reutilizables

---

**"El nivel avanzado de DAX transforma al analista en un arquitecto de soluciones, capaz de construir sistemas de análisis sofisticados que resuelven problemas de negocio complejos."**
