# Técnicas Avanzadas DAX - Nivel Experto

## Introducción a las Técnicas Avanzadas

Este documento explora las técnicas más sofisticadas de DAX, enfocándose en patrones de optimización, arquitecturas escalables y metodologías para soluciones empresariales de alto rendimiento.

---

## 1. Optimización del Motor de Cálculo

### 1.1 Comprensión del Motor Vertipaq

El motor Vertipaq utiliza técnicas específicas para optimizar el procesamiento:

#### Estrategias de Compresión
```dax
// Análisis de Cardinalidad para Optimización
Analisis Cardinalidad = 
VAR TablasAnalisis = 
    DATATABLE(
        "Tabla", STRING,
        "Columna", STRING,
        {
            {"Ventas", "ID_Producto"},
            {"Ventas", "ID_Cliente"},
            {"Ventas", "Fecha"},
            {"Productos", "Categoria"},
            {"Clientes", "Segmento"}
        }
    )

VAR ResultadoAnalisis = 
    ADDCOLUMNS(
        TablasAnalisis,
        "Cardinalidad",
        VAR TablaActual = [Tabla]
        VAR ColumnaActual = [Columna]
        RETURN
            SWITCH(
                TablaActual,
                "Ventas", 
                    SWITCH(
                        ColumnaActual,
                        "ID_Producto", DISTINCTCOUNT(Ventas[ID_Producto]),
                        "ID_Cliente", DISTINCTCOUNT(Ventas[ID_Cliente]),
                        "Fecha", DISTINCTCOUNT(Ventas[Fecha])
                    ),
                "Productos",
                    SWITCH(
                        ColumnaActual,
                        "Categoria", DISTINCTCOUNT(Productos[Categoria])
                    ),
                "Clientes",
                    SWITCH(
                        ColumnaActual,
                        "Segmento", DISTINCTCOUNT(Clientes[Segmento])
                    )
            ),
        "Compresion_Estimada",
        VAR Cardinalidad = [Cardinalidad]
        VAR TotalRegistros = 
            SWITCH([Tabla],
                "Ventas", COUNTROWS(Ventas),
                "Productos", COUNTROWS(Productos),
                "Clientes", COUNTROWS(Clientes)
            )
        RETURN DIVIDE(Cardinalidad, TotalRegistros)
    )

RETURN ResultadoAnalisis
```

### 1.2 Técnicas de Context Transition

#### Context Transition Optimization
```dax
// Técnica: Minimize Context Transitions
Ventas Optimizadas = 
VAR ContextoFiltrado = 
    CALCULATETABLE(
        Ventas,
        // Pre-filtrar en lugar de múltiples CALCULATE
        KEEPFILTERS(Productos[Categoria] = "Electrónicos")
    )

VAR ResultadoOptimizado = 
    SUMX(
        ContextoFiltrado,
        Ventas[Cantidad] * RELATED(Productos[Precio])
    )

RETURN ResultadoOptimizado

// Comparar con versión no optimizada:
Ventas No Optimizadas = 
SUMX(
    Ventas,
    IF(
        RELATED(Productos[Categoria]) = "Electrónicos",
        Ventas[Cantidad] * RELATED(Productos[Precio]),
        0
    )
)
```

---

## 2. Patrones de Arquitectura Escalable

### 2.1 Patrón Factory para Medidas

#### Base Factory Pattern
```dax
// Medida Factory - Configuración Centralizada
[CONFIG] Parametros = 
DATATABLE(
    "Parametro", STRING,
    "Valor", DOUBLE,
    {
        {"Margen_Objetivo", 0.25},
        {"Descuento_Maximo", 0.15},
        {"Umbral_Stock_Critico", 10},
        {"Factor_Estacionalidad", 1.2}
    }
)

// Factory Method para obtener parámetros
[FACTORY] Get Parameter = 
FUNCTION(ParameterName AS STRING)
VAR ParameterValue = 
    MAXX(
        FILTER([CONFIG] Parametros, [Parametro] = ParameterName),
        [Valor]
    )
RETURN IF(ISBLANK(ParameterValue), 0, ParameterValue)

// Uso del Factory Pattern
Margen Dinamico = 
VAR ObjetivoMargen = [FACTORY] Get Parameter("Margen_Objetivo")
VAR MargenActual = DIVIDE([Total Ventas] - [Total Costos], [Total Ventas])
VAR VariacionMargen = MargenActual - ObjetivoMargen

RETURN 
    SWITCH(
        TRUE(),
        VariacionMargen > 0.05, "Excelente",
        VariacionMargen > 0, "Bueno",
        VariacionMargen > -0.05, "Aceptable",
        "Crítico"
    )
```

### 2.2 Patrón Template para Time Intelligence

#### Time Intelligence Template
```dax
// Template Base para Time Intelligence
[TEMPLATE] Time Intelligence Base = 
FUNCTION(
    MeasureExpression AS VARIANT,
    PeriodOffset AS INTEGER,
    PeriodType AS STRING
)
VAR BaseMeasure = MeasureExpression
VAR CurrentDate = MAX(Calendario[Fecha])
VAR ComparisonPeriod = 
    SWITCH(
        PeriodType,
        "MONTH", EDATE(CurrentDate, PeriodOffset),
        "QUARTER", EDATE(CurrentDate, PeriodOffset * 3),
        "YEAR", EDATE(CurrentDate, PeriodOffset * 12),
        CurrentDate
    )

VAR FilteredPeriod = 
    FILTER(
        ALL(Calendario),
        SWITCH(
            PeriodType,
            "MONTH", 
                YEAR(Calendario[Fecha]) = YEAR(ComparisonPeriod) &&
                MONTH(Calendario[Fecha]) = MONTH(ComparisonPeriod),
            "QUARTER",
                YEAR(Calendario[Fecha]) = YEAR(ComparisonPeriod) &&
                QUARTER(Calendario[Fecha]) = QUARTER(ComparisonPeriod),
            "YEAR",
                YEAR(Calendario[Fecha]) = YEAR(ComparisonPeriod)
        )
    )

RETURN CALCULATE(BaseMeasure, FilteredPeriod)

// Implementaciones específicas usando el template
Ventas Mes Anterior = [TEMPLATE] Time Intelligence Base([Total Ventas], -1, "MONTH")
Ventas Año Anterior = [TEMPLATE] Time Intelligence Base([Total Ventas], -1, "YEAR")
Ventas Trimestre Anterior = [TEMPLATE] Time Intelligence Base([Total Ventas], -1, "QUARTER")
```

---

## 3. Técnicas de Performance Monitoring

### 3.1 Profiler de Rendimiento Integrado

```dax
// Performance Profiler para Medidas
[PERFORMANCE] Measure Profiler = 
VAR StartTime = NOW()
VAR MeasureResult = [Medida a Evaluar]
VAR EndTime = NOW()
VAR ExecutionTime = EndTime - StartTime
VAR MemoryContext = 
    CONCATENATEX(
        FILTERS(ALL()),
        "[" & [Tabla] & "]" & [Columna],
        " | "
    )

VAR PerformanceMetrics = 
    "Resultado: " & MeasureResult & 
    " | Tiempo: " & FORMAT(ExecutionTime, "hh:mm:ss.000") &
    " | Contexto: " & MemoryContext

RETURN PerformanceMetrics
```

### 3.2 Query Plan Analysis

```dax
// Análisis de Plan de Consulta Simulado
Query Plan Analyzer = 
VAR QueryComplexity = 
    COUNTROWS(FILTERS(ALL())) +  // Filtros activos
    COUNTROWS(VALUES(Productos)) +  // Cardinalidad productos
    COUNTROWS(VALUES(Clientes)) +   // Cardinalidad clientes
    COUNTROWS(VALUES(Calendario))   // Cardinalidad temporal

VAR EstimatedCost = 
    SWITCH(
        TRUE(),
        QueryComplexity < 1000, "Bajo",
        QueryComplexity < 10000, "Medio",
        QueryComplexity < 100000, "Alto",
        "Crítico"
    )

VAR OptimizationSuggestions = 
    SWITCH(
        EstimatedCost,
        "Bajo", "Sin optimización requerida",
        "Medio", "Considerar agregaciones pre-calculadas",
        "Alto", "Implementar particionado y agregaciones",
        "Crítico", "Reestructurar modelo y consultas"
    )

RETURN 
    "Complejidad: " & QueryComplexity & 
    " | Costo: " & EstimatedCost &
    " | Recomendación: " & OptimizationSuggestions
```

---

## 4. Patrones de Seguridad Avanzada

### 4.1 Dynamic Row Level Security

```dax
// RLS Dinámico Basado en Jerarquías
[SECURITY] Dynamic RLS = 
VAR CurrentUser = USERNAME()
VAR UserHierarchy = 
    LOOKUPVALUE(
        Seguridad_Usuarios[Nivel_Acceso],
        Seguridad_Usuarios[Usuario], CurrentUser
    )

VAR AccessibleClients = 
    SWITCH(
        UserHierarchy,
        "CEO", ALL(Clientes),
        "Director_Regional", 
            FILTER(
                Clientes,
                Clientes[Region] IN 
                VALUES(
                    FILTER(
                        Seguridad_Usuarios,
                        Seguridad_Usuarios[Usuario] = CurrentUser
                    )[Regiones_Permitidas]
                )
            ),
        "Gerente_Sucursal",
            FILTER(
                Clientes,
                Clientes[Sucursal] IN 
                VALUES(
                    FILTER(
                        Seguridad_Usuarios,
                        Seguridad_Usuarios[Usuario] = CurrentUser
                    )[Sucursales_Permitidas]
                )
            ),
        FILTER(Clientes, FALSE())  // Sin acceso por defecto
    )

RETURN AccessibleClients
```

### 4.2 Data Masking Dinámico

```dax
// Enmascaramiento de Datos Sensibles
Cliente Nombre Seguro = 
VAR CurrentUser = USERNAME()
VAR UserClearance = 
    LOOKUPVALUE(
        Seguridad_Usuarios[Nivel_Clearance],
        Seguridad_Usuarios[Usuario], CurrentUser
    )

VAR MaskedName = 
    VAR OriginalName = Clientes[Nombre_Completo]
    VAR FirstName = LEFT(OriginalName, SEARCH(" ", OriginalName) - 1)
    VAR LastNameInitial = LEFT(MID(OriginalName, SEARCH(" ", OriginalName) + 1, 100), 1)
    RETURN FirstName & " " & LastNameInitial & "."

RETURN 
    IF(
        UserClearance >= 3,  // Nivel 3+ puede ver nombres completos
        Clientes[Nombre_Completo],
        MaskedName
    )
```

---

## 5. Técnicas de Machine Learning Integration

### 5.1 Clustering Estadístico en DAX

```dax
// K-Means Clustering Simplificado
[ML] Customer Clustering = 
VAR CustomerMetrics = 
    ADDCOLUMNS(
        SUMMARIZE(
            Ventas,
            Clientes[ID_Cliente],
            Clientes[Nombre]
        ),
        "Total_Compras", CALCULATE([Total Ventas]),
        "Frecuencia_Compras", CALCULATE(DISTINCTCOUNT(Ventas[Fecha])),
        "Ticket_Promedio", DIVIDE(CALCULATE([Total Ventas]), CALCULATE(DISTINCTCOUNT(Ventas[Fecha]))),
        "Dias_Ultima_Compra", DATEDIFF(MAX(Ventas[Fecha]), TODAY(), DAY)
    )

VAR NormalizedMetrics = 
    ADDCOLUMNS(
        CustomerMetrics,
        "Total_Norm", 
        VAR MaxTotal = MAXX(CustomerMetrics, [Total_Compras])
        VAR MinTotal = MINX(CustomerMetrics, [Total_Compras])
        RETURN DIVIDE([Total_Compras] - MinTotal, MaxTotal - MinTotal),
        
        "Frecuencia_Norm",
        VAR MaxFreq = MAXX(CustomerMetrics, [Frecuencia_Compras])
        VAR MinFreq = MINX(CustomerMetrics, [Frecuencia_Compras])
        RETURN DIVIDE([Frecuencia_Compras] - MinFreq, MaxFreq - MinFreq),
        
        "Ticket_Norm",
        VAR MaxTicket = MAXX(CustomerMetrics, [Ticket_Promedio])
        VAR MinTicket = MINX(CustomerMetrics, [Ticket_Promedio])
        RETURN DIVIDE([Ticket_Promedio] - MinTicket, MaxTicket - MinTicket),
        
        "Recencia_Norm",
        VAR MaxDias = MAXX(CustomerMetrics, [Dias_Ultima_Compra])
        VAR MinDias = MINX(CustomerMetrics, [Dias_Ultima_Compra])
        RETURN 1 - DIVIDE([Dias_Ultima_Compra] - MinDias, MaxDias - MinDias)  // Invertido: menos días = mejor
    )

VAR ClusteredCustomers = 
    ADDCOLUMNS(
        NormalizedMetrics,
        "RFM_Score",
        ([Frecuencia_Norm] + [Total_Norm] + [Recencia_Norm]) / 3,
        "Segment",
        VAR Score = ([Frecuencia_Norm] + [Total_Norm] + [Recencia_Norm]) / 3
        RETURN
            SWITCH(
                TRUE(),
                Score >= 0.8, "Champions",
                Score >= 0.6, "Loyal Customers",
                Score >= 0.4, "Potential Loyalists",
                Score >= 0.2, "At Risk",
                "Lost Customers"
            )
    )

RETURN ClusteredCustomers
```

### 5.2 Forecasting Básico con Regresión Linear

```dax
// Simple Linear Regression para Forecasting
[ML] Sales Forecast = 
VAR HistoricalData = 
    ADDCOLUMNS(
        FILTER(
            ALL(Calendario),
            Calendario[Fecha] <= TODAY() - 30  // Datos hasta hace 30 días
        ),
        "Ventas", CALCULATE([Total Ventas]),
        "X", DATEDIFF(DATE(2020,1,1), Calendario[Fecha], DAY)  // Variable independiente
    )

VAR N = COUNTROWS(HistoricalData)
VAR SumX = SUMX(HistoricalData, [X])
VAR SumY = SUMX(HistoricalData, [Ventas])
VAR SumXY = SUMX(HistoricalData, [X] * [Ventas])
VAR SumX2 = SUMX(HistoricalData, [X] * [X])

VAR Slope = DIVIDE((N * SumXY) - (SumX * SumY), (N * SumX2) - (SumX * SumX))
VAR Intercept = DIVIDE(SumY - (Slope * SumX), N)

VAR ForecastDate = MAX(Calendario[Fecha])
VAR X_Forecast = DATEDIFF(DATE(2020,1,1), ForecastDate, DAY)
VAR ForecastValue = Intercept + (Slope * X_Forecast)

VAR ConfidenceInterval = 
    VAR Residuals = 
        SUMX(
            HistoricalData,
            VAR Predicted = Intercept + (Slope * [X])
            VAR Actual = [Ventas]
            RETURN (Actual - Predicted) ^ 2
        )
    VAR MSE = DIVIDE(Residuals, N - 2)
    VAR StandardError = SQRT(MSE)
    RETURN StandardError * 1.96  // 95% confidence

RETURN 
    "Forecast: " & FORMAT(ForecastValue, "Currency") &
    " ± " & FORMAT(ConfidenceInterval, "Currency")
```

---

## 6. Técnicas de Memoria y Cache Management

### 6.1 Cache Strategy Implementation

```dax
// Estrategia de Cache para Medidas Costosas
[CACHE] Expensive Calculation = 
VAR CacheKey = 
    CONCATENATEX(
        FILTERS(ALL()),
        [Table] & "|" & [Column] & "|" & [Value],
        ";"
    )

VAR CachedResult = 
    LOOKUPVALUE(
        Cache_Table[Result],
        Cache_Table[CacheKey], CacheKey,
        Cache_Table[Timestamp], MAX(Cache_Table[Timestamp])
    )

VAR CacheAge = 
    DATEDIFF(
        LOOKUPVALUE(
            Cache_Table[Timestamp],
            Cache_Table[CacheKey], CacheKey
        ),
        NOW(),
        MINUTE
    )

VAR UseCache = NOT ISBLANK(CachedResult) && CacheAge < 60  // Cache válido por 60 minutos

VAR FreshCalculation = 
    // Cálculo costoso aquí
    SUMX(
        CROSSJOIN(Ventas, Productos),
        Ventas[Cantidad] * Productos[Precio] * Productos[Factor_Complejidad]
    )

RETURN 
    IF(UseCache, CachedResult, FreshCalculation)
```

### 6.2 Memory Pressure Detection

```dax
// Detector de Presión de Memoria
Memory Pressure Monitor = 
VAR ActiveTables = 
    DATATABLE(
        "Table", STRING,
        "EstimatedRows", INTEGER,
        {
            {"Ventas", COUNTROWS(Ventas)},
            {"Productos", COUNTROWS(Productos)},
            {"Clientes", COUNTROWS(Clientes)},
            {"Calendario", COUNTROWS(Calendario)}
        }
    )

VAR TotalRows = SUMX(ActiveTables, [EstimatedRows])
VAR ActiveFilters = COUNTROWS(FILTERS(ALL()))
VAR MemoryPressure = TotalRows * ActiveFilters * 0.001  // Estimación simplificada

VAR PressureLevel = 
    SWITCH(
        TRUE(),
        MemoryPressure < 1000, "Low",
        MemoryPressure < 10000, "Medium",
        MemoryPressure < 100000, "High",
        "Critical"
    )

VAR Recommendations = 
    SWITCH(
        PressureLevel,
        "Low", "Rendimiento óptimo",
        "Medium", "Considerar agregaciones",
        "High", "Implementar particionado",
        "Critical", "Reducir granularidad del modelo"
    )

RETURN 
    "Presión: " & PressureLevel & 
    " (" & FORMAT(MemoryPressure, "#,##0") & " units)" &
    " | " & Recommendations
```

---

## 7. Técnicas de Testing y Validación

### 7.1 Unit Testing Framework para DAX

```dax
// Framework de Testing para Medidas DAX
[TEST] Unit Test Framework = 
VAR TestCases = 
    DATATABLE(
        "TestName", STRING,
        "Expected", DOUBLE,
        "TestCondition", STRING,
        {
            {"Total_Ventas_2023", 1000000, "YEAR(Calendario[Fecha]) = 2023"},
            {"Margen_Electronica", 0.25, "Productos[Categoria] = 'Electrónicos'"},
            {"Clientes_Premium", 100, "Clientes[Segmento] = 'Premium'"}
        }
    )

VAR TestResults = 
    ADDCOLUMNS(
        TestCases,
        "Actual",
        VAR TestName = [TestName]
        VAR Condition = [TestCondition]
        RETURN
            SWITCH(
                TestName,
                "Total_Ventas_2023", CALCULATE([Total Ventas], YEAR(Calendario[Fecha]) = 2023),
                "Margen_Electronica", CALCULATE([Margen Porcentual], Productos[Categoria] = "Electrónicos"),
                "Clientes_Premium", CALCULATE(DISTINCTCOUNT(Clientes[ID_Cliente]), Clientes[Segmento] = "Premium"),
                0
            ),
        "Status",
        VAR Expected = [Expected]
        VAR Actual = [Actual]
        VAR Tolerance = 0.01  // 1% tolerance
        VAR Difference = ABS(Expected - Actual)
        VAR PercentDifference = DIVIDE(Difference, Expected)
        RETURN
            IF(
                PercentDifference <= Tolerance,
                "PASS",
                "FAIL (" & FORMAT(PercentDifference, "0.00%") & " difference)"
            )
    )

VAR PassedTests = COUNTROWS(FILTER(TestResults, [Status] = "PASS"))
VAR TotalTests = COUNTROWS(TestResults)
VAR PassRate = DIVIDE(PassedTests, TotalTests)

RETURN 
    "Tests: " & PassedTests & "/" & TotalTests & 
    " (" & FORMAT(PassRate, "0.00%") & " pass rate)"
```

### 7.2 Data Quality Validation

```dax
// Validador de Calidad de Datos
[QUALITY] Data Validation = 
VAR ValidationRules = 
    DATATABLE(
        "Rule", STRING,
        "Description", STRING,
        "Severity", STRING,
        {
            {"No_Null_Ventas", "Ventas sin valores nulos", "Critical"},
            {"Positive_Amounts", "Importes positivos", "Critical"},
            {"Valid_Dates", "Fechas válidas", "High"},
            {"Referential_Integrity", "Integridad referencial", "Medium"}
        }
    )

VAR ValidationResults = 
    ADDCOLUMNS(
        ValidationRules,
        "Issues_Found",
        VAR Rule = [Rule]
        RETURN
            SWITCH(
                Rule,
                "No_Null_Ventas", COUNTROWS(FILTER(Ventas, ISBLANK(Ventas[Importe]))),
                "Positive_Amounts", COUNTROWS(FILTER(Ventas, Ventas[Importe] <= 0)),
                "Valid_Dates", COUNTROWS(FILTER(Ventas, Ventas[Fecha] < DATE(2000,1,1) || Ventas[Fecha] > TODAY() + 365)),
                "Referential_Integrity", COUNTROWS(FILTER(Ventas, ISBLANK(RELATED(Productos[Nombre])))),
                0
            ),
        "Status",
        VAR Issues = [Issues_Found]
        VAR Severity = [Severity]
        RETURN
            IF(
                Issues = 0,
                "OK",
                IF(
                    Severity = "Critical",
                    "CRITICAL: " & Issues & " issues",
                    IF(
                        Severity = "High",
                        "HIGH: " & Issues & " issues",
                        "MEDIUM: " & Issues & " issues"
                    )
                )
            )
    )

VAR CriticalIssues = COUNTROWS(FILTER(ValidationResults, LEFT([Status], 8) = "CRITICAL"))
VAR HighIssues = COUNTROWS(FILTER(ValidationResults, LEFT([Status], 4) = "HIGH"))

RETURN 
    IF(
        CriticalIssues > 0,
        "BLOCKED: " & CriticalIssues & " critical data quality issues",
        IF(
            HighIssues > 0,
            "WARNING: " & HighIssues & " high priority issues",
            "HEALTHY: Data quality validated"
        )
    )
```

---

## Conclusión

Estas técnicas avanzadas representan el nivel más alto de expertise en DAX y Power BI. Su implementación requiere:

1. **Comprensión Profunda**: Del motor de cálculo y optimización
2. **Experiencia Práctica**: En proyectos empresariales complejos
3. **Pensamiento Arquitectónico**: Para soluciones escalables
4. **Metodología Rigurosa**: Testing, validación y governance

El dominio de estas técnicas convierte al profesional en un arquitecto de soluciones de Business Intelligence capaz de diseñar e implementar sistemas de nivel empresarial que escalen efectivamente y proporcionen valor de negocio sostenible.
