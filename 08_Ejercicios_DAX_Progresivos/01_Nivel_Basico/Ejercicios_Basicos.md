# Ejercicios DAX - Nivel Básico

## Introducción

En este nivel básico, el estudiante aprende los fundamentos esenciales de DAX (Data Analysis Expressions). Se centra en la comprensión de conceptos fundamentales como medidas, columnas calculadas y funciones básicas de agregación.

---

## Ejercicio 1: Primeras Medidas Básicas

### Contexto Empresarial
Una empresa de retail necesita crear sus primeros KPIs básicos para monitorear las ventas diarias.

### Teoría: Conceptos Fundamentales
DAX (Data Analysis Expressions) es el lenguaje de fórmulas de Power BI. Los conceptos básicos incluyen:

1. **Medidas**: Cálculos dinámicos que se evalúan según el contexto
2. **Columnas Calculadas**: Valores calculados que se almacenan en el modelo
3. **Contexto de Filtro**: Las condiciones que afectan el cálculo
4. **Funciones de Agregación**: SUM, COUNT, AVERAGE, etc.

### Desafío 1.1: Medidas de Ventas Básicas

**Ejercicio**: Crear medidas básicas para análisis de ventas.

```dax
// Medida 1: Total de Ventas
Total Ventas = SUM(Ventas[Importe])
```

**Explicación del Proceso**:
1. **SUM**: Función de agregación que suma todos los valores
2. **Ventas[Importe]**: Referencia a la columna Importe de la tabla Ventas
3. **Contexto Automático**: La medida se calcula según los filtros aplicados

```dax
// Medida 2: Cantidad Total de Productos Vendidos
Cantidad Total = SUM(Ventas[Cantidad])
```

```dax
// Medida 3: Número de Transacciones
Numero Transacciones = COUNT(Ventas[ID_Venta])
```

**Por qué usar COUNT vs COUNTROWS**:
- **COUNT**: Cuenta valores no en blanco en una columna específica
- **COUNTROWS**: Cuenta filas en una tabla (incluye filas con valores en blanco)

### Desafío 1.2: Medidas de Clientes

```dax
// Medida 4: Número de Clientes Únicos
Clientes Unicos = DISTINCTCOUNT(Ventas[ID_Cliente])
```

**Explicación**:
- **DISTINCTCOUNT**: Cuenta valores únicos, eliminando duplicados
- Útil para contar entidades únicas como clientes, productos, etc.

```dax
// Medida 5: Ticket Promedio
Ticket Promedio = DIVIDE([Total Ventas], [Numero Transacciones])
```

**Concepto Clave - DIVIDE**:
- **DIVIDE**: Función segura para divisiones que maneja automáticamente la división por cero
- Sintaxis: DIVIDE(numerador, denominador, valor_si_error)

---

## Ejercicio 2: Columnas Calculadas vs Medidas

### Contexto Empresarial
El equipo de análisis necesita entender cuándo usar columnas calculadas versus medidas.

### Teoría: Diferencias Fundamentales

#### Columnas Calculadas
- Se calculan **una vez** durante la actualización de datos
- Ocupan **espacio en memoria**
- Útiles para **categorización** y **filtrado**
- Se pueden usar en **slicers** y **filtros**

#### Medidas
- Se calculan **dinámicamente** según el contexto
- **No ocupan** espacio adicional en memoria
- Útiles para **agregaciones** y **KPIs**
- Responden a **filtros** e **interacciones**

### Desafío 2.1: Columnas Calculadas Básicas

**Ejercicio**: Crear columnas para categorización.

```dax
// Columna Calculada 1: Categoría de Venta
Categoria Venta = 
IF(
    Ventas[Importe] >= 1000, 
    "Venta Alta",
    IF(
        Ventas[Importe] >= 500, 
        "Venta Media", 
        "Venta Baja"
    )
)
```

**Explicación del Proceso**:
1. **IF anidado**: Estructura condicional para crear categorías
2. **Evaluación por fila**: Se calcula para cada fila de la tabla
3. **Almacenamiento**: El resultado se guarda en el modelo

```dax
// Columna Calculada 2: Mes Nombre
Mes Nombre = FORMAT(Ventas[Fecha], "MMMM")
```

**Función FORMAT**:
- Convierte valores a texto con formato específico
- "MMMM" = nombre completo del mes
- "MMM" = nombre abreviado del mes

### Desafío 2.2: Cuándo Usar Cada Tipo

**Regla General**:
- **Columna Calculada**: Para categorización, agrupación, filtros
- **Medida**: Para cálculos que necesitan agregación dinámica

**Ejemplo Práctico**:
```dax
// CORRECTO: Columna para categorizar
Segmento Cliente = 
SWITCH(
    TRUE(),
    Clientes[Ventas_Anuales] >= 100000, "Premium",
    Clientes[Ventas_Anuales] >= 50000, "Gold",
    Clientes[Ventas_Anuales] >= 10000, "Silver",
    "Bronze"
)

// CORRECTO: Medida para agregar
Ventas Segmento Premium = 
CALCULATE(
    [Total Ventas],
    Clientes[Segmento] = "Premium"
)
```

---

## Ejercicio 3: Funciones de Agregación Avanzadas

### Contexto Empresarial
El departamento de ventas necesita análisis más detallados con diferentes tipos de agregaciones.

### Teoría: Funciones de Agregación en DAX

#### Funciones Numéricas
- **SUM**: Suma valores
- **AVERAGE**: Promedio aritmético
- **MIN/MAX**: Valores mínimo y máximo
- **COUNT**: Cuenta valores no en blanco
- **COUNTA**: Cuenta valores no vacíos (incluyendo texto)

#### Funciones de Conteo
- **COUNTROWS**: Cuenta filas
- **DISTINCTCOUNT**: Cuenta valores únicos
- **COUNTBLANK**: Cuenta valores en blanco

### Desafío 3.1: Análisis de Productos

```dax
// Medida 1: Precio Promedio de Productos
Precio Promedio = AVERAGE(Productos[Precio])
```

```dax
// Medida 2: Producto Más Caro
Precio Maximo = MAX(Productos[Precio])
```

```dax
// Medida 3: Producto Más Barato
Precio Minimo = MIN(Productos[Precio])
```

```dax
// Medida 4: Rango de Precios
Rango Precios = [Precio Maximo] - [Precio Minimo]
```

**Concepto de Reutilización**:
- Las medidas pueden referenciar otras medidas
- Esto facilita el mantenimiento y la consistencia
- Cambios en medidas base se propagan automáticamente

### Desafío 3.2: Análisis Temporal Básico

```dax
// Medida 5: Ventas del Año Actual
Ventas Año Actual = 
CALCULATE(
    [Total Ventas],
    YEAR(Ventas[Fecha]) = YEAR(TODAY())
)
```

**Introducción a CALCULATE**:
- **CALCULATE**: Función que modifica el contexto de filtro
- **YEAR(TODAY())**: Obtiene el año actual
- **Filtro dinámico**: Se actualiza automáticamente cada año

```dax
// Medida 6: Promedio de Ventas por Día
Promedio Ventas Diario = 
DIVIDE(
    [Total Ventas],
    DISTINCTCOUNT(Ventas[Fecha])
)
```

**Lógica del Cálculo**:
1. **Numerador**: Total de ventas en el periodo seleccionado
2. **Denominador**: Número de días únicos con ventas
3. **Resultado**: Promedio de ventas por día operativo

---

## Ejercicio 4: Introducción a Time Intelligence

### Contexto Empresarial
Los ejecutivos necesitan comparar el rendimiento actual con períodos anteriores.

### Teoría: Time Intelligence Básica
Time Intelligence permite crear cálculos basados en tiempo como:
- Año anterior
- Mes anterior
- Año hasta la fecha (YTD)
- Mes hasta la fecha (MTD)

### Desafío 4.1: Comparaciones Básicas de Tiempo

```dax
// Medida 1: Ventas Año Anterior
Ventas Año Anterior = 
CALCULATE(
    [Total Ventas],
    SAMEPERIODLASTYEAR(Calendario[Fecha])
)
```

**Función SAMEPERIODLASTYEAR**:
- Devuelve las fechas del mismo período del año anterior
- Requiere una tabla de calendario relacionada
- Mantiene el mismo nivel de granularidad (día, mes, trimestre)

```dax
// Medida 2: Crecimiento Año sobre Año
Crecimiento YoY = 
VAR VentasActual = [Total Ventas]
VAR VentasAnterior = [Ventas Año Anterior]
RETURN
    DIVIDE(VentasActual - VentasAnterior, VentasAnterior)
```

**Introducción a Variables (VAR)**:
- **VAR**: Declara una variable local
- **RETURN**: Especifica el valor a devolver
- **Beneficios**: Mejora legibilidad y performance

### Desafío 4.2: Acumulados (Year to Date)

```dax
// Medida 3: Ventas YTD (Year to Date)
Ventas YTD = 
CALCULATE(
    [Total Ventas],
    DATESYTD(Calendario[Fecha])
)
```

**Función DATESYTD**:
- Devuelve todas las fechas desde el inicio del año hasta la fecha actual
- Automáticamente considera el año del contexto actual
- Útil para análisis acumulativos

```dax
// Medida 4: Ventas YTD Año Anterior
Ventas YTD Año Anterior = 
CALCULATE(
    [Total Ventas],
    DATESYTD(SAMEPERIODLASTYEAR(Calendario[Fecha]))
)
```

**Combinación de Funciones**:
- Combina DATESYTD con SAMEPERIODLASTYEAR
- Calcula el acumulado del año anterior hasta la misma fecha
- Permite comparaciones justas entre períodos

---

## Ejercicio 5: Filtros Básicos con CALCULATE

### Contexto Empresarial
El equipo de análisis necesita crear KPIs segmentados por diferentes criterios.

### Teoría: CALCULATE - La Función Más Importante
CALCULATE modifica el contexto de filtro para un cálculo específico:
- Puede **agregar** filtros
- Puede **modificar** filtros existentes
- Puede **remover** filtros

### Desafío 5.1: Filtros por Categoría

```dax
// Medida 1: Ventas de Electrónicos
Ventas Electronicos = 
CALCULATE(
    [Total Ventas],
    Productos[Categoria] = "Electrónicos"
)
```

**Anatomía de CALCULATE**:
1. **Primera parte**: La medida base a calcular
2. **Segunda parte**: El filtro a aplicar
3. **Resultado**: La medida filtrada

```dax
// Medida 2: Ventas Múltiples Categorías
Ventas Tech = 
CALCULATE(
    [Total Ventas],
    OR(
        Productos[Categoria] = "Electrónicos",
        Productos[Categoria] = "Computación"
    )
)
```

**Operadores Lógicos**:
- **OR**: Al menos una condición debe ser verdadera
- **AND**: Todas las condiciones deben ser verdaderas
- Útil para filtros complejos

### Desafío 5.2: Filtros por Rango de Fechas

```dax
// Medida 3: Ventas Últimos 30 Días
Ventas Ultimos 30 Dias = 
CALCULATE(
    [Total Ventas],
    Ventas[Fecha] >= TODAY() - 30,
    Ventas[Fecha] <= TODAY()
)
```

**Filtros de Fecha**:
- **TODAY()**: Función que devuelve la fecha actual
- **Operadores de comparación**: >=, <=, =, <>
- **Aritmética de fechas**: TODAY() - 30 resta 30 días

```dax
// Medida 4: Ventas por Encima del Promedio
Ventas Alto Valor = 
VAR PromedioVenta = AVERAGE(Ventas[Importe])
RETURN
    CALCULATE(
        [Total Ventas],
        Ventas[Importe] > PromedioVenta
    )
```

**Filtro Dinámico**:
- El promedio se calcula según el contexto actual
- El filtro se ajusta automáticamente
- Concepto de "filtro inteligente"

---

## Ejercicio 6: Manejo de Errores y Valores Blank

### Contexto Empresarial
Los datos reales a menudo tienen inconsistencias que pueden causar errores en los cálculos.

### Teoría: Gestión de Errores en DAX
DAX puede encontrar diferentes tipos de problemas:
- **División por cero**
- **Valores BLANK**
- **Datos faltantes**
- **Tipos de datos incorrectos**

### Desafío 6.1: Funciones de Protección

```dax
// Medida 1: División Segura
Margen Porcentual = 
DIVIDE(
    [Total Ventas] - [Total Costos],
    [Total Ventas],
    0
)
```

**Función DIVIDE**:
- **Parámetro 1**: Numerador
- **Parámetro 2**: Denominador  
- **Parámetro 3**: Valor por defecto si hay error
- Previene automáticamente división por cero

```dax
// Medida 2: Verificación de Valores Blank
Ventas Con Validacion = 
IF(
    ISBLANK([Total Ventas]),
    "Sin Datos",
    FORMAT([Total Ventas], "Currency")
)
```

**Funciones de Verificación**:
- **ISBLANK**: Verifica si un valor está en blanco
- **ISERROR**: Verifica si hay error en el cálculo
- **FORMAT**: Convierte números a texto con formato

### Desafío 6.2: Manejo Avanzado de Errores

```dax
// Medida 3: Cálculo Robusto
Crecimiento Robusto = 
VAR VentasActual = [Total Ventas]
VAR VentasAnterior = [Ventas Año Anterior]
RETURN
    SWITCH(
        TRUE(),
        ISBLANK(VentasActual) || ISBLANK(VentasAnterior), BLANK(),
        VentasAnterior = 0, 1,
        DIVIDE(VentasActual - VentasAnterior, VentasAnterior)
    )
```

**Función SWITCH**:
- Evalúa múltiples condiciones en orden
- Más legible que IF anidados para múltiples casos
- TRUE() como primera expresión evalúa condiciones booleanas

**Lógica del Cálculo**:
1. Si cualquier valor es BLANK, devuelve BLANK
2. Si ventas anterior es 0, considera crecimiento del 100%
3. Si no, calcula el crecimiento normal

---

## Ejercicio 7: Primeros Pasos con Variables

### Contexto Empresarial
Los cálculos se vuelven más complejos y necesitan ser más legibles y eficientes.

### Teoría: Variables en DAX
Las variables ofrecen múltiples beneficios:
- **Legibilidad**: Código más claro y entendible
- **Performance**: Evita recálculos innecesarios
- **Mantenimiento**: Facilita modificaciones futuras
- **Debugging**: Permite verificar valores intermedios

### Desafío 7.1: Refactoring con Variables

```dax
// Versión SIN variables (difícil de leer)
ROI Sin Variables = 
DIVIDE(
    DIVIDE([Total Ventas] - [Total Costos], [Total Costos]),
    DIVIDE([Total Inversión Marketing], [Total Ventas]),
    0
)

// Versión CON variables (clara y eficiente)
ROI Con Variables = 
VAR Ventas = [Total Ventas]
VAR Costos = [Total Costos]
VAR InversionMarketing = [Total Inversión Marketing]
VAR Utilidad = Ventas - Costos
VAR MargenUtilidad = DIVIDE(Utilidad, Costos, 0)
VAR InversionRatio = DIVIDE(InversionMarketing, Ventas, 0)
VAR ROIFinal = DIVIDE(MargenUtilidad, InversionRatio, 0)
RETURN ROIFinal
```

**Beneficios de las Variables**:
1. **Claridad**: Cada paso del cálculo es evidente
2. **Eficiencia**: [Total Ventas] se evalúa solo una vez
3. **Debugging**: Puedes verificar cada variable
4. **Mantenimiento**: Fácil modificar la lógica

### Desafío 7.2: Variables para Lógica Compleja

```dax
// Medida: Análisis de Performance de Vendedor
Performance Vendedor = 
VAR VentasVendedor = [Total Ventas]
VAR PromedioEquipo = 
    CALCULATE(
        AVERAGE(Ventas[Importe]),
        ALL(Vendedores)
    )
VAR MetaVendedor = 
    LOOKUPVALUE(
        Vendedores[Meta_Mensual],
        Vendedores[ID_Vendedor], 
        MAX(Ventas[ID_Vendedor])
    )
VAR PerformanceVsMeta = DIVIDE(VentasVendedor, MetaVendedor, 0)
VAR PerformanceVsEquipo = DIVIDE(VentasVendedor, PromedioEquipo, 0)

VAR Clasificacion = 
    SWITCH(
        TRUE(),
        PerformanceVsMeta >= 1.2 && PerformanceVsEquipo >= 1.1, "Estrella",
        PerformanceVsMeta >= 1.0 && PerformanceVsEquipo >= 1.0, "Cumple",
        PerformanceVsMeta >= 0.8 || PerformanceVsEquipo >= 0.9, "En Desarrollo",
        "Necesita Apoyo"
    )

RETURN Clasificacion
```

**Conceptos Avanzados Introducidos**:
- **ALL**: Remueve filtros para cálculo global
- **LOOKUPVALUE**: Busca valores en otra tabla
- **MAX en contexto**: Obtiene el valor del vendedor actual
- **Lógica multi-criterio**: Combina múltiples condiciones

---

## Ejercicio 8: Práctica Integral

### Contexto Empresarial
Crear un dashboard completo con los conceptos aprendidos.

### Desafío Final: Dashboard de Ventas Integral

**Objetivo**: Crear un conjunto de medidas para un dashboard ejecutivo de ventas.

```dax
// 1. KPI Principal
Total Ventas = SUM(Ventas[Importe])

// 2. Comparación Temporal
Ventas Mes Anterior = 
CALCULATE(
    [Total Ventas],
    DATEADD(Calendario[Fecha], -1, MONTH)
)

// 3. Crecimiento
Crecimiento Mensual = 
VAR VentasActual = [Total Ventas]
VAR VentasAnterior = [Ventas Mes Anterior]
RETURN
    IF(
        ISBLANK(VentasAnterior) || VentasAnterior = 0,
        BLANK(),
        DIVIDE(VentasActual - VentasAnterior, VentasAnterior)
    )

// 4. Indicador Visual de Performance
Indicador Crecimiento = 
VAR Crecimiento = [Crecimiento Mensual]
RETURN
    SWITCH(
        TRUE(),
        ISBLANK(Crecimiento), "Sin Datos",
        Crecimiento >= 0.1, "Excelente",
        Crecimiento >= 0.05, "Bueno",
        Crecimiento >= 0, "Estable",
        Crecimiento >= -0.05, "Precaución",
        "Crítico"
    )

// 5. Meta Achievement
Cumplimiento Meta = 
VAR VentasActual = [Total Ventas]
VAR MetaPeriodo = [Meta Ventas Periodo]
RETURN
    DIVIDE(VentasActual, MetaPeriodo, 0)

// 6. Ventas por Segmento Top
Participacion Segmento = 
DIVIDE(
    [Total Ventas],
    CALCULATE([Total Ventas], ALL(Productos[Categoria]))
)
```

### Validación y Testing

**Checklist de Validación**:
1. **Sintaxis**: ¿La fórmula compila sin errores?
2. **Lógica**: ¿El resultado tiene sentido empresarial?
3. **Performance**: ¿La medida responde rápidamente?
4. **Casos Extremos**: ¿Maneja correctamente datos faltantes?
5. **Contexto**: ¿Funciona correctamente con filtros?

**Casos de Prueba**:
- Filtrar por un solo mes
- Filtrar por múltiples categorías
- Verificar con datos históricos
- Probar con períodos sin datos
- Validar cálculos manualmente

---

## Mejores Prácticas para Nivel Básico

### Naming Conventions
```dax
// BUENO: Nombres descriptivos y claros
Total Ventas Neto = SUM(Ventas[Importe]) - SUM(Ventas[Descuentos])

// MALO: Nombres ambiguos
Calc1 = SUM(Ventas[Importe]) - SUM(Ventas[Descuentos])
```

### Documentación
```dax
/*
Medida: Margen Contribución
Propósito: Calcula el margen de contribución por producto
Fórmula: (Ventas - Costos Variables) / Ventas
Autor: [Tu nombre]
Fecha: [Fecha de creación]
Modificado: [Última modificación]
*/
Margen Contribucion = 
DIVIDE(
    [Total Ventas] - [Costos Variables],
    [Total Ventas],
    0
)
```

### Gestión de Errores
```dax
// Siempre considera casos extremos
Medida Robusta = 
VAR Calculo = [Medida Base]
RETURN
    IF(
        ISBLANK(Calculo) || ISERROR(Calculo),
        0,  -- o BLANK() según necesidad del negocio
        Calculo
    )
```

## Conclusión del Nivel Básico

Al completar este nivel, el estudiante habrá dominado:

1. **Fundamentos de DAX**: Sintaxis básica y conceptos core
2. **Medidas vs Columnas**: Cuándo usar cada tipo
3. **Funciones de Agregación**: SUM, COUNT, AVERAGE, etc.
4. **CALCULATE básico**: Modificación simple de contextos
5. **Time Intelligence básica**: Comparaciones temporales
6. **Manejo de errores**: Protección contra errores comunes
7. **Variables básicas**: Mejora de legibilidad y performance
8. **Mejores prácticas**: Convenciones y documentación

El nivel básico proporciona la base sólida necesaria para avanzar a conceptos más complejos en los niveles intermedio y avanzado, donde se explorarán funciones más sofisticadas, patrones de diseño avanzados y optimizaciones de performance.

### Contexto
Se necesita crear medidas básicas para calcular totales de ventas y cantidades vendidas en un modelo de datos simple.

### Objetivo
Implementar medidas fundamentales que permitan:
- Calcular el total de ventas
- Obtener la cantidad total de productos vendidos
- Calcular el precio promedio de venta

### Datos Necesarios
- Tabla `Ventas` con columnas: `Monto`, `Cantidad`, `PrecioUnitario`

### Solución Paso a Paso

#### Paso 1: Crear Medida de Total de Ventas
```dax
Total_Ventas = SUM(Ventas[Monto])
```

**Explicación técnica:** La función SUM() suma todos los valores de la columna Monto en la tabla Ventas. Esta función respeta automáticamente cualquier filtro aplicado en el contexto actual, lo que significa que se adaptará a segmentaciones, filtros de fecha, etc.

#### Paso 2: Crear Medida de Cantidad Total
```dax
Cantidad_Total = SUM(Ventas[Cantidad])
```

**Explicación técnica:** Similar a la medida anterior, SUM() suma todos los valores de cantidad. Esta medida nos permite conocer el volumen total de productos vendidos.

#### Paso 3: Crear Medida de Precio Promedio
```dax
Precio_Promedio = AVERAGE(Ventas[PrecioUnitario])
```

**Explicación técnica:** La función AVERAGE() calcula el promedio aritmético de todos los valores en la columna PrecioUnitario. Es importante notar que esto calcula el promedio de los precios registrados, no necesariamente el precio promedio ponderado por cantidad.

---

## Ejercicio 2: Conteos y Funciones de Agregación

### Contexto
Se requiere analizar la diversidad de productos y clientes en las ventas, así como calcular estadísticas básicas.

### Objetivo
Crear medidas que permitan:
- Contar el número de transacciones
- Contar clientes únicos
- Contar productos únicos
- Obtener valores máximos y mínimos

### Solución Paso a Paso

#### Paso 1: Contar Transacciones
```dax
Numero_Transacciones = COUNTROWS(Ventas)
```

**Explicación técnica:** COUNTROWS() cuenta el número de filas en la tabla especificada. En este caso, cada fila representa una transacción, por lo que obtenemos el total de transacciones.

#### Paso 2: Contar Clientes Únicos
```dax
Clientes_Unicos = DISTINCTCOUNT(Ventas[ClienteID])
```

**Explicación técnica:** DISTINCTCOUNT() cuenta el número de valores únicos en una columna. Esto es útil para saber cuántos clientes diferentes han realizado compras, sin importar cuántas veces hayan comprado.

#### Paso 3: Contar Productos Únicos
```dax
Productos_Unicos = DISTINCTCOUNT(Ventas[ProductoID])
```

**Explicación técnica:** Similar a la medida anterior, cuenta cuántos productos diferentes se han vendido.

#### Paso 4: Venta Máxima y Mínima
```dax
Venta_Maxima = MAX(Ventas[Monto])

Venta_Minima = MIN(Ventas[Monto])
```

**Explicación técnica:** MAX() y MIN() devuelven respectivamente el valor máximo y mínimo de una columna. Estas funciones son útiles para identificar los extremos en los datos.

---

## Ejercicio 3: Columnas Calculadas Básicas

### Contexto
Se necesita enriquecer la tabla de ventas con cálculos que se realizan a nivel de fila.

### Objetivo
Crear columnas calculadas que:
- Calculen el monto con descuento aplicado
- Determinen el margen de ganancia
- Clasifiquen las ventas por tamaño

### Solución Paso a Paso

#### Paso 1: Monto con Descuento
```dax
Monto_Final = Ventas[Cantidad] * Ventas[PrecioUnitario] * (1 - Ventas[Descuento])
```

**Explicación técnica:** Esta columna calculada se evalúa para cada fila de la tabla Ventas. Multiplica la cantidad por el precio unitario y luego aplica el descuento. El resultado se almacena físicamente en el modelo.

#### Paso 2: Margen de Ganancia
```dax
Margen = Ventas[Monto_Final] - (Ventas[Cantidad] * RELATED(Productos[CostoUnitario]))
```

**Explicación técnica:** Calcula la diferencia entre el ingreso final y el costo total. RELATED() se usa para obtener el costo unitario de la tabla Productos relacionada.

#### Paso 3: Clasificación de Venta
```dax
Tamaño_Venta = 
IF(
    Ventas[Monto_Final] > 1000, "Grande",
    IF(
        Ventas[Monto_Final] > 500, "Mediana", "Pequeña"
    )
)
```

**Explicación técnica:** La función IF() permite crear lógica condicional. Esta columna clasifica cada venta en tres categorías basándose en el monto final.

---

## Ejercicio 4: Funciones de Texto y Fecha

### Contexto
Se requiere manipular datos de texto y fechas para crear categorías y análisis temporales básicos.

### Objetivo
Implementar funciones que:
- Extraigan información de fechas
- Manipulen texto
- Creen categorías temporales

### Solución Paso a Paso

#### Paso 1: Extraer Año y Mes
```dax
Año_Venta = YEAR(Ventas[Fecha])

Mes_Venta = MONTH(Ventas[Fecha])

Nombre_Mes = FORMAT(Ventas[Fecha], "MMMM")
```

**Explicación técnica:** YEAR() y MONTH() extraen componentes numéricos de una fecha. FORMAT() permite obtener representaciones de texto personalizadas, como el nombre completo del mes.

#### Paso 2: Día de la Semana
```dax
Dia_Semana = WEEKDAY(Ventas[Fecha], 2)

Nombre_Dia = 
SWITCH(
    WEEKDAY(Ventas[Fecha], 2),
    1, "Lunes",
    2, "Martes", 
    3, "Miércoles",
    4, "Jueves",
    5, "Viernes",
    6, "Sábado",
    7, "Domingo"
)
```

**Explicación técnica:** WEEKDAY() retorna un número que representa el día de la semana. El parámetro 2 hace que lunes sea 1. SWITCH() permite mapear estos números a nombres descriptivos.

#### Paso 3: Manipulación de Texto
```dax
Cliente_Inicial = LEFT(Clientes[Nombre], 1)

Nombre_Completo = Clientes[Nombre] & " " & Clientes[Apellido]

Email_Dominio = RIGHT(Clientes[Email], LEN(Clientes[Email]) - FIND("@", Clientes[Email]))
```

**Explicación técnica:** LEFT() extrae caracteres del inicio de un texto. El operador & concatena textos. RIGHT(), LEN() y FIND() se combinan para extraer el dominio de un email.

---

## Ejercicio 5: Medidas con Filtros Simples

### Contexto
Se necesita crear medidas que calculen valores específicos aplicando filtros básicos.

### Objetivo
Desarrollar medidas que:
- Filtren por categorías específicas
- Calculen porcentajes simples
- Comparen valores entre diferentes grupos

### Solución Paso a Paso

#### Paso 1: Ventas por Categoría
```dax
Ventas_Tecnologia = 
CALCULATE(
    SUM(Ventas[Monto]),
    Productos[Categoria] = "Tecnología"
)
```

**Explicación técnica:** CALCULATE() modifica el contexto de filtro. En este caso, suma las ventas solo para productos de la categoría "Tecnología", independientemente de otros filtros aplicados.

#### Paso 2: Porcentaje del Total
```dax
Porcentaje_Total = 
DIVIDE(
    SUM(Ventas[Monto]),
    CALCULATE(SUM(Ventas[Monto]), ALL(Productos)),
    0
)
```

**Explicación técnica:** ALL() elimina todos los filtros de la tabla especificada. DIVIDE() calcula el porcentaje de manera segura, retornando 0 si el denominador es cero.

#### Paso 3: Comparación con Promedio
```dax
Diferencia_Promedio = 
SUM(Ventas[Monto]) - 
CALCULATE(
    AVERAGE(Ventas[Monto]),
    ALL()
)
```

**Explicación técnica:** Esta medida compara las ventas actuales con el promedio general de todas las ventas, removiendo todos los filtros con ALL().

---

## Ejercicio 6: Validación y Manejo de Errores

### Contexto
Es importante crear medidas robustas que manejen casos especiales y errores potenciales.

### Objetivo
Implementar medidas que:
- Manejen divisiones por cero
- Validen datos faltantes
- Proporcionen valores por defecto

### Solución Paso a Paso

#### Paso 1: División Segura
```dax
Ticket_Promedio = 
VAR TotalVentas = SUM(Ventas[Monto])
VAR NumeroTransacciones = COUNTROWS(Ventas)
RETURN
IF(
    NumeroTransacciones > 0,
    DIVIDE(TotalVentas, NumeroTransacciones),
    0
)
```

**Explicación técnica:** Las variables (VAR) almacenan cálculos intermedios. IF() verifica que existan transacciones antes de realizar la división, evitando errores.

#### Paso 2: Validación de Datos
```dax
Ventas_Validas = 
SUMX(
    Ventas,
    IF(
        AND(
            NOT(ISBLANK(Ventas[Monto])),
            Ventas[Monto] > 0
        ),
        Ventas[Monto],
        0
    )
)
```

**Explicación técnica:** SUMX() itera sobre cada fila de la tabla. AND() e ISBLANK() validan que el monto no esté en blanco y sea positivo antes de incluirlo en la suma.

#### Paso 3: Medida con Valor por Defecto
```dax
Descuento_Aplicado = 
IF(
    ISBLANK(Ventas[Descuento]),
    0,
    Ventas[Descuento]
)
```

**Explicación técnica:** Esta medida proporciona un valor por defecto (0) cuando el descuento está en blanco, asegurando cálculos consistentes.

---

## Ejercicios Prácticos para el Estudiante

### Ejercicio A: Análisis de Vendedores
Crear medidas que calculen:
1. Total de ventas por vendedor
2. Número de clientes únicos atendidos por vendedor
3. Promedio de venta por vendedor

### Ejercicio B: Análisis Temporal
Implementar medidas que:
1. Calculen ventas del mes actual
2. Identifiquen el día con mayor venta
3. Determinen si las ventas están por encima del promedio mensual

### Ejercicio C: Análisis de Productos
Desarrollar medidas para:
1. Identificar el producto más vendido
2. Calcular el margen promedio por categoría
3. Determinar qué productos no han tenido ventas

---

## Mejores Prácticas para Nivel Básico

### 1. Nomenclatura Clara
- Usar nombres descriptivos para medidas
- Seguir convenciones de nomenclatura consistentes
- Documentar medidas complejas

### 2. Validación de Datos
- Siempre verificar divisiones por cero
- Manejar valores en blanco apropiadamente
- Validar rangos de datos esperados

### 3. Eficiencia Básica
- Usar funciones agregadas cuando sea posible
- Evitar cálculos innecesarios en columnas calculadas
- Preferir medidas sobre columnas calculadas cuando sea apropiado

---

## Evaluación del Nivel Básico

Para completar exitosamente este nivel, el estudiante debe demostrar competencia en:

### Conceptos Fundamentales
- Diferencia entre medidas y columnas calculadas
- Comprensión del contexto de filtro básico
- Uso apropiado de funciones de agregación

### Funciones Esenciales
- SUM, AVERAGE, COUNT, DISTINCTCOUNT
- MAX, MIN, IF, SWITCH
- CALCULATE con filtros simples
- Funciones de fecha y texto básicas

### Habilidades Prácticas
- Crear medidas que respondan preguntas de negocio específicas
- Validar y manejar errores en cálculos
- Implementar lógica condicional simple

---

**"El dominio de DAX comienza con la comprensión sólida de los fundamentos. Cada función avanzada se construye sobre estos conceptos básicos."**
