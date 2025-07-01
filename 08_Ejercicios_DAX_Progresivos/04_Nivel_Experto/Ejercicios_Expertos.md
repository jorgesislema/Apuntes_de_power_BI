# Ejercicios DAX - Nivel Experto

## Introducción

En este nivel experto, el estudiante domina las técnicas más avanzadas de DAX. Se enfoca en optimización de rendimiento, patrones complejos, virtual tables, funciones iterativas avanzadas y arquitecturas escalables para soluciones empresariales.

Los ejercicios requieren un entendimiento profundo del motor de cálculo de DAX, optimización de consultas y patrones de diseño para modelos de datos complejos.

---

## Ejercicio 1: Optimización de Consultas y Performance Tuning

### Contexto Empresarial
Una empresa multinacional necesita un dashboard ejecutivo que procese millones de registros con sub-segundo de respuesta.

### Teoría: Optimización del Motor Vertipaq
El motor Vertipaq de Power BI utiliza compresión columnar y técnicas de optimización específicas:

1. **Eliminación de Contexto**: Minimizar evaluaciones innecesarias
2. **Materialización**: Pre-calcular resultados complejos
3. **Paralelización**: Aprovechar el procesamiento paralelo
4. **Cache Management**: Gestión eficiente de memoria

### Desafío 1.1: Medida de Ventas Optimizada

**Problema**: Crear una medida que calcule ventas del año actual vs año anterior con máximo rendimiento.

```dax
// Versión No Optimizada (Evitar)
Ventas YoY Malo = 
VAR VentasActual = 
    CALCULATE(
        SUM(Ventas[Importe]),
        YEAR(Ventas[Fecha]) = YEAR(TODAY())
    )
VAR VentasAnterior = 
    CALCULATE(
        SUM(Ventas[Importe]),
        YEAR(Ventas[Fecha]) = YEAR(TODAY()) - 1
    )
RETURN
    DIVIDE(VentasActual - VentasAnterior, VentasAnterior)
```

**Explicación del Problema**:
1. Usa TODAY() que no es optimizable
2. Funciones de fecha en cada iteración
3. No aprovecha relaciones del modelo

```dax
// Versión Optimizada
Ventas YoY Optimizada = 
VAR FechaMaxima = MAX(Calendario[Fecha])
VAR AñoActual = YEAR(FechaMaxima)
VAR VentasActual = 
    CALCULATE(
        [Total Ventas],
        Calendario[Año] = AñoActual
    )
VAR VentasAnterior = 
    CALCULATE(
        [Total Ventas],
        Calendario[Año] = AñoActual - 1
    )
RETURN
    DIVIDE(VentasActual - VentasAnterior, VentasAnterior, 0)
```

**Explicación de la Optimización**:
1. **Deterministic Context**: FechaMaxima es constante por contexto
2. **Relationship Leverage**: Usa relaciones predefinidas
3. **Measure Reuse**: Reutiliza [Total Ventas] optimizada
4. **Single Evaluation**: AñoActual se calcula una vez

---

## Ejercicio 2: Virtual Tables y Técnicas de Materialización

### Contexto Empresarial
Análisis de cohortes de clientes para retención y valor de vida del cliente (CLV).

### Teoría: Virtual Tables en DAX
Las virtual tables permiten crear conjuntos de datos temporales en memoria para cálculos complejos:

1. **SUMMARIZE**: Agrupación con medidas
2. **ADDCOLUMNS**: Extensión de tablas
3. **FILTER**: Filtrado dinámico
4. **TOPN**: Ranking y selección

### Desafío 2.1: Análisis de Cohortes Avanzado

```dax
Cohort Analysis = 
VAR CohorteBase = 
    ADDCOLUMNS(
        SUMMARIZE(
            Ventas,
            Clientes[ID_Cliente],
            "PrimeraCompra", MIN(Ventas[Fecha])
        ),
        "MesPrimera", EOMONTH([PrimeraCompra], 0),
        "AñoPrimero", YEAR([PrimeraCompra])
    )

VAR CohorteConActividad = 
    ADDCOLUMNS(
        CohorteBase,
        "ComprasSubsecuentes", 
        VAR ClienteActual = [ID_Cliente]
        VAR FechaPrimera = [PrimeraCompra]
        RETURN
            CALCULATE(
                COUNTROWS(Ventas),
                Ventas[ID_Cliente] = ClienteActual,
                Ventas[Fecha] > FechaPrimera
            )
    )

VAR ResultadoFinal = 
    ADDCOLUMNS(
        FILTER(
            CohorteConActividad,
            [ComprasSubsecuentes] > 0
        ),
        "TasaRetencion", 
        DIVIDE([ComprasSubsecuentes], 
               CALCULATE(COUNTROWS(Ventas), 
                        Ventas[ID_Cliente] = [ID_Cliente]))
    )

RETURN
    AVERAGEX(ResultadoFinal, [TasaRetencion])
```

**Explicación del Proceso**:
1. **CohorteBase**: Identifica primera compra por cliente
2. **Materialización**: Calcula mes y año de primera compra
3. **CohorteConActividad**: Cuenta compras posteriores por cliente
4. **Filtrado**: Solo clientes con actividad subsecuente
5. **Agregación Final**: Promedio de tasas de retención

---

## Ejercicio 3: Funciones Iterativas Avanzadas y Patrones de Escalabilidad

### Contexto Empresarial
Sistema de scoring dinámico para evaluación de riesgo crediticio con múltiples variables.

### Teoría: Iteración Avanzada en DAX
Las funciones X permiten iteraciones complejas con evaluación por fila:

1. **SUMX**: Suma con expresión por fila
2. **AVERAGEX**: Promedio con lógica compleja
3. **MAXX/MINX**: Extremos con evaluación
4. **RANKX**: Ranking dinámico

### Desafío 3.1: Credit Scoring Dinámico

```dax
Credit Score Avanzado = 
VAR ParametrosScoring = 
    ROW(
        "PesoIngreso", 0.35,
        "PesoHistorial", 0.25,
        "PesoDeuda", 0.20,
        "PesoAntiguedad", 0.15,
        "PesoGarantias", 0.05
    )

VAR ClientesConScore = 
    ADDCOLUMNS(
        Clientes,
        "ScoreIngreso", 
        VAR IngresoCliente = Clientes[Ingreso_Mensual]
        VAR PercentilIngreso = 
            DIVIDE(
                RANKX(ALL(Clientes), Clientes[Ingreso_Mensual], , ASC),
                COUNTROWS(ALL(Clientes))
            )
        RETURN PercentilIngreso * 100,
        
        "ScoreHistorial",
        VAR MesesHistorial = Clientes[Meses_Historial_Crediticio]
        VAR MaxHistorial = MAXX(ALL(Clientes), Clientes[Meses_Historial_Crediticio])
        RETURN DIVIDE(MesesHistorial, MaxHistorial) * 100,
        
        "ScoreDeuda",
        VAR RatioDeuda = DIVIDE(Clientes[Deuda_Total], Clientes[Ingreso_Mensual] * 12)
        VAR DeudaSegura = 0.3  // 30% ratio considerado seguro
        RETURN IF(RatioDeuda <= DeudaSegura, 100, (1 - RatioDeuda) * 100),
        
        "ScoreAntiguedad",
        VAR AñosEmpleo = Clientes[Años_Empleo_Actual]
        VAR MaxAños = MAXX(ALL(Clientes), Clientes[Años_Empleo_Actual])
        RETURN DIVIDE(AñosEmpleo, MaxAños) * 100,
        
        "ScoreGarantias",
        VAR TieneGarantias = IF(Clientes[Valor_Garantias] > 0, 100, 20)
        RETURN TieneGarantias
    )

VAR ScoreFinal = 
    ADDCOLUMNS(
        ClientesConScore,
        "Score_Final",
        [ScoreIngreso] * [PesoIngreso] +
        [ScoreHistorial] * [PesoHistorial] +
        [ScoreDeuda] * [PesoDeuda] +
        [ScoreAntiguedad] * [PesoPesoAntiguedad] +
        [ScoreGarantias] * [PesoGarantias],
        
        "Categoria_Riesgo",
        VAR Score = [Score_Final]
        RETURN
            SWITCH(
                TRUE(),
                Score >= 80, "Bajo Riesgo",
                Score >= 60, "Riesgo Moderado",
                Score >= 40, "Riesgo Alto",
                "Riesgo Crítico"
            )
    )

RETURN
    AVERAGEX(ScoreFinal, [Score_Final])
```

**Proceso de Evaluación**:
1. **Parametrización**: Pesos configurables por componente
2. **Normalización**: Scores en escala 0-100
3. **Percentiles**: Ranking relativo por criterio
4. **Ponderación**: Combinación weighted de factores
5. **Categorización**: Clasificación final de riesgo

---

## Ejercicio 4: Patrones de Time Intelligence Avanzados

### Contexto Empresarial
Dashboard ejecutivo con métricas de tendencia, estacionalidad y forecasting básico.

### Teoría: Time Intelligence Personalizada
Más allá de las funciones estándar, creamos patrones temporales complejos:

1. **Rolling Averages**: Promedios móviles personalizados
2. **Seasonal Patterns**: Detección de estacionalidad
3. **Growth Rates**: Tasas de crecimiento compuestas
4. **Trend Analysis**: Análisis de tendencias

### Desafío 4.1: Sistema de Métricas Temporales Avanzadas

```dax
// Promedio Móvil Adaptativo
Promedio Movil Adaptativo = 
VAR FechaActual = MAX(Calendario[Fecha])
VAR PeriodoAnalisis = 90  // días
VAR DatosHistoricos = 
    FILTER(
        ALL(Calendario),
        Calendario[Fecha] <= FechaActual &&
        Calendario[Fecha] > FechaActual - PeriodoAnalisis
    )

VAR PromedioBase = 
    CALCULATE(
        [Total Ventas],
        DatosHistoricos
    ) / PeriodoAnalisis

VAR VolatilidadPeriodo = 
    VAR MediaVentas = [Total Ventas]
    VAR DesviacionesCuadradas = 
        SUMX(
            DatosHistoricos,
            VAR VentasDia = CALCULATE([Total Ventas], Calendario[Fecha] = EARLIER(Calendario[Fecha]))
            VAR Desviacion = VentasDia - MediaVentas
            RETURN Desviacion * Desviacion
        )
    RETURN SQRT(DIVIDE(DesviacionesCuadradas, PeriodoAnalisis))

VAR FactorAdaptacion = 
    IF(VolatilidadPeriodo > PromedioBase * 0.2, 30, 90)  // Período más corto si alta volatilidad

RETURN
    CALCULATE(
        [Total Ventas],
        FILTER(
            ALL(Calendario),
            Calendario[Fecha] <= FechaActual &&
            Calendario[Fecha] > FechaActual - FactorAdaptacion
        )
    ) / FactorAdaptacion
```

### Desafío 4.2: Detección de Estacionalidad

```dax
Indice Estacionalidad = 
VAR AñoActual = YEAR(MAX(Calendario[Fecha]))
VAR MesActual = MONTH(MAX(Calendario[Fecha]))

VAR VentasMesActual = [Total Ventas]

VAR PromedioHistoricoMes = 
    VAR AñosHistoricos = 
        FILTER(
            ALL(Calendario),
            YEAR(Calendario[Fecha]) < AñoActual &&
            MONTH(Calendario[Fecha]) = MesActual
        )
    RETURN
        CALCULATE([Total Ventas], AñosHistoricos) / 
        DISTINCTCOUNT(YEAR(AñosHistoricos[Fecha]))

VAR PromedioAnualHistorico = 
    VAR AñosCompletos = 
        FILTER(
            ALL(Calendario),
            YEAR(Calendario[Fecha]) < AñoActual
        )
    RETURN
        CALCULATE([Total Ventas], AñosCompletos) / 
        (DISTINCTCOUNT(YEAR(AñosCompletos[Fecha])) * 12)

VAR IndiceEstacional = 
    DIVIDE(PromedioHistoricoMes, PromedioAnualHistorico, 1)

RETURN IndiceEstacional
```

**Interpretación del Índice**:
- **> 1.2**: Estacionalidad alta positiva
- **0.8 - 1.2**: Comportamiento normal
- **< 0.8**: Estacionalidad baja/negativa

---

## Ejercicio 5: Arquitectura Escalable y Governance

### Contexto Empresarial
Sistema de métricas empresariales con governance, versionado y auditabilidad.

### Teoría: Patterns de Escalabilidad
Para soluciones empresariales robustas:

1. **Medidas Base**: Componentes reutilizables
2. **Metadata Management**: Gestión de metadatos
3. **Error Handling**: Manejo de errores
4. **Performance Monitoring**: Monitoreo de rendimiento

### Desafío 5.1: Framework de Métricas Empresariales

```dax
// Medida Base con Metadata y Error Handling
[BASE] Total Ventas = 
VAR Resultado = 
    TRY(
        SUM(Ventas[Importe]),
        BLANK()
    )
VAR MetadataValidation = 
    IF(
        HASONEVALUE(Calendario[Fecha]) || 
        ISFILTERED(Calendario[Fecha]),
        TRUE,
        FALSE
    )
RETURN
    IF(
        MetadataValidation,
        Resultado,
        ERROR("Contexto temporal requerido para cálculo de ventas")
    )

// Medida Derivada con Auditabilidad
Total Ventas (Auditada) = 
VAR ResultadoBase = [BASE] Total Ventas
VAR ContextoActual = 
    CONCATENATEX(
        FILTERS(Calendario),
        "Calendario[" & Calendario[Fecha] & "]",
        "; "
    )
VAR TimestampCalculo = NOW()
VAR MetricaAuditoria = 
    "Cálculo: " & TimestampCalculo & 
    " | Contexto: " & ContextoActual &
    " | Resultado: " & ResultadoBase

// Log para auditoría (conceptual - requiere tabla de logs)
VAR LogEntry = 
    ROW(
        "Timestamp", TimestampCalculo,
        "Medida", "Total Ventas",
        "Contexto", ContextoActual,
        "Resultado", ResultadoBase,
        "Usuario", USERNAME()
    )

RETURN ResultadoBase
```

### Desafío 5.2: Sistema de Alertas y Monitoreo

```dax
Sistema Alertas Avanzado = 
VAR ConfiguracionAlertas = 
    DATATABLE(
        "Metrica", STRING,
        "Umbral_Critico", DOUBLE,
        "Umbral_Advertencia", DOUBLE,
        "Tipo_Comparacion", STRING,
        {
            {"Ventas", 1000000, 800000, "Mayor_Que"},
            {"Margen", 0.15, 0.20, "Mayor_Que"},
            {"Rotacion_Inventario", 12, 8, "Mayor_Que"}
        }
    )

VAR EvaluacionAlertas = 
    ADDCOLUMNS(
        ConfiguracionAlertas,
        "Valor_Actual",
        VAR MetricaEvaluar = [Metrica]
        RETURN
            SWITCH(
                MetricaEvaluar,
                "Ventas", [Total Ventas],
                "Margen", [Margen Porcentual],
                "Rotacion_Inventario", [Rotacion Inventario],
                BLANK()
            ),
        "Estado_Alerta",
        VAR ValorActual = [Valor_Actual]
        VAR Critico = [Umbral_Critico]
        VAR Advertencia = [Umbral_Advertencia]
        VAR TipoComp = [Tipo_Comparacion]
        RETURN
            SWITCH(
                TRUE(),
                TipoComp = "Mayor_Que" && ValorActual < Critico, "CRÍTICO",
                TipoComp = "Mayor_Que" && ValorActual < Advertencia, "ADVERTENCIA",
                TipoComp = "Menor_Que" && ValorActual > Critico, "CRÍTICO",
                TipoComp = "Menor_Que" && ValorActual > Advertencia, "ADVERTENCIA",
                "NORMAL"
            )
    )

VAR AlertasCriticas = 
    FILTER(EvaluacionAlertas, [Estado_Alerta] = "CRÍTICO")

VAR ConteoAlertas = COUNTROWS(AlertasCriticas)

RETURN
    IF(
        ConteoAlertas > 0,
        "⚠️ " & ConteoAlertas & " alertas críticas detectadas",
        "✅ Todos los indicadores dentro de rangos normales"
    )
```

---

## Ejercicio 6: Optimización de Modelos Complejos

### Contexto Final
Revisión y optimización de un modelo empresarial completo con millones de registros.

### Checklist de Optimización Experta

#### 1. **Diseño del Modelo**
```dax
// Verificación de Cardinalidades
Analisis Cardinalidades = 
VAR TablasFact = 
    DATATABLE(
        "Tabla", STRING,
        "Registros", INTEGER,
        {
            {"Ventas", COUNTROWS(Ventas)},
            {"Inventario", COUNTROWS(Inventario)},
            {"Presupuesto", COUNTROWS(Presupuesto)}
        }
    )

VAR TablasDimension = 
    DATATABLE(
        "Tabla", STRING,
        "Registros", INTEGER,
        {
            {"Productos", COUNTROWS(Productos)},
            {"Clientes", COUNTROWS(Clientes)},
            {"Calendario", COUNTROWS(Calendario)}
        }
    )

RETURN
    "Fact Tables: " & SUMX(TablasFact, [Registros]) &
    " | Dim Tables: " & SUMX(TablasDimension, [Registros])
```

#### 2. **Performance Metrics**
```dax
Performance Monitor = 
VAR InicioCalculo = NOW()
VAR ResultadoComplejo = 
    SUMX(
        Ventas,
        VAR ProductoActual = Ventas[ID_Producto]
        VAR ClienteActual = Ventas[ID_Cliente]
        RETURN
            Ventas[Cantidad] * 
            RELATED(Productos[Precio_Unitario]) *
            (1 - RELATED(Clientes[Descuento_Categoria]))
    )
VAR FinCalculo = NOW()
VAR TiempoEjecucion = FinCalculo - InicioCalculo

RETURN
    "Resultado: " & ResultadoComplejo & 
    " | Tiempo: " & TiempoEjecucion & " segundos"
```

---

## Ejercicios de Práctica Adicionales

### Ejercicio A: Machine Learning Integration
Implementar un sistema de clustering de clientes usando técnicas estadísticas en DAX.

### Ejercicio B: Real-time Analytics
Crear métricas que se actualicen en tiempo real para dashboards ejecutivos.

### Ejercicio C: Multi-tenancy Support
Diseñar un modelo que soporte múltiples organizaciones con segregación de datos.

### Ejercicio D: Advanced Security
Implementar Row-Level Security dinámico basado en jerarquías organizacionales complejas.

---

## Recursos Avanzados y Siguientes Pasos

### Herramientas de Profiling
- **DAX Studio**: Análisis de consultas y optimización
- **Tabular Editor**: Gestión avanzada de modelos
- **Performance Analyzer**: Monitoreo en Power BI Desktop

### Patrones de Arquitectura
- **Medallion Architecture**: Bronze, Silver, Gold layers
- **Data Mesh**: Arquitectura descentralizada
- **Real-time + Batch**: Arquitecturas híbridas

### Certificaciones Recomendadas
- **Microsoft Certified: Data Analyst Associate**
- **Microsoft Certified: Azure Data Engineer Associate**
- **Power BI Specialist Certifications**

El dominio del nivel experto requiere práctica continua, comprensión profunda del motor de cálculo y experiencia en proyectos empresariales reales. Estos ejercicios proporcionan la base para convertirse en un arquitecto de soluciones Power BI de nivel empresarial.
