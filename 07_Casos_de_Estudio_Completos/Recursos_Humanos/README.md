# Caso de Estudio: Análisis de Recursos Humanos - Rotación de Personal

## Descripción del Proyecto

Este caso de estudio aborda uno de los desafíos más críticos en la gestión de recursos humanos: el análisis y predicción de la rotación de personal. Implementa un modelo completo de People Analytics utilizando Power BI para identificar patrones, causas y factores predictivos de la rotación laboral.

## Contexto del Negocio

### Empresa Ficticia: TechCorp Solutions
- **Industria**: Tecnología y consultoría
- **Empleados**: 2,500 personas
- **Ubicaciones**: 15 oficinas en 8 países
- **Problema**: Rotación del 18% anual (objetivo: <12%)
- **Costo estimado**: €3.2M anuales en reclutamiento y training

### Desafíos Identificados
- **Alta rotación** en roles técnicos específicos
- **Diferencias regionales** significativas en retención
- **Falta de early warning** para identificar riesgo de salida
- **Decisiones de HR** basadas en intuición vs datos
- **Dificultad para medir** ROI de iniciativas de retención

## Objetivos del Análisis

### Objetivos Estratégicos
- **Reducir rotación** del 18% al 12% en 18 meses
- **Identificar factors de riesgo** para retención proactiva
- **Optimizar inversión** en programas de desarrollo
- **Mejorar experience del empleado** basado en insights
- **Establecer cultura** data-driven en HR

### Objetivos Analíticos
- Analizar patrones históricos de rotación
- Identificar segmentos de alto riesgo
- Crear modelo predictivo de propensión a salir
- Medir efectividad de programas de retención
- Desarrollar alertas tempranas automáticas

## Estructura de Datos

### Fuentes de Datos Integradas

#### 1. Sistema HRIS (Workday)
```
Tablas principales:
├── Empleados (Master Data)
│   ├── EmpleadoID (PK)
│   ├── NumeroEmpleado
│   ├── Nombre, Apellidos
│   ├── Email, Telefono
│   ├── FechaNacimiento
│   ├── Genero, EstadoCivil
│   ├── FechaIngreso
│   ├── FechaSalida (si aplica)
│   ├── EstadoEmpleado
│   └── MotivoSalida
│
├── Posiciones (Job Data)
│   ├── PosicionID (PK)
│   ├── EmpleadoID (FK)
│   ├── TituloTrabajo
│   ├── DepartamentoID (FK)
│   ├── UbicacionID (FK)
│   ├── ManagerID (FK)
│   ├── Nivel, Banda
│   ├── SalarioBase
│   ├── FechaInicioPos
│   └── FechaFinPos
│
├── Evaluaciones (Performance)
│   ├── EvaluacionID (PK)
│   ├── EmpleadoID (FK)
│   ├── Periodo
│   ├── Rating
│   ├── Objetivos
│   └── ComentariosManager
│
└── Capacitaciones (Learning)
    ├── CapacitacionID (PK)
    ├── EmpleadoID (FK)
    ├── CursoID (FK)
    ├── FechaCompletado
    ├── Calificacion
    └── HorasInvertidas
```

#### 2. Encuestas de Employee Engagement
- Satisfaction surveys trimestrales
- Exit interviews estructuradas
- Pulse surveys mensuales
- Feedback 360 degrees

#### 3. Sistemas Adicionales
- **Timesheet data** (horas trabajadas, overtime)
- **Benefits utilization** (uso de beneficios)
- **Internal mobility** (movimientos internos)
- **Recognition programs** (premios y reconocimientos)

### Datos Externos
- **Benchmarks industriales** (Glassdoor, LinkedIn)
- **Datos económicos** regionales
- **Información salarial** de mercado
- **Trends de la industria** tech

## Modelo de Datos Implementado

### Esquema Estrella Especializado en HR
```
        DimFecha
           │
           │
DimEmpleado ─┼─ FactRotacion ─┼─ DimPosicion
           │                │
      DimManager        DimDepartamento
           │                │
    DimUbicacion      DimMotivoSalida
```

### Tablas de Dimensiones Clave

#### Dimensión Empleado Enriquecida
```dax
DimEmpleado = 
ADDCOLUMNS(
    Empleados,
    "EdadActual", 
        IF(
            ISBLANK(Empleados[FechaSalida]),
            DATEDIFF(Empleados[FechaNacimiento], TODAY(), YEAR),
            DATEDIFF(Empleados[FechaNacimiento], Empleados[FechaSalida], YEAR)
        ),
    "AntiguedadMeses",
        IF(
            ISBLANK(Empleados[FechaSalida]),
            DATEDIFF(Empleados[FechaIngreso], TODAY(), MONTH),
            DATEDIFF(Empleados[FechaIngreso], Empleados[FechaSalida], MONTH)
        ),
    "GeneracionLaboral",
        SWITCH(
            TRUE(),
            [EdadActual] <= 27, "Gen Z",
            [EdadActual] <= 42, "Millennial", 
            [EdadActual] <= 57, "Gen X",
            "Baby Boomer"
        )
)
```

#### Tabla de Hechos de Rotación
```dax
FactRotacion = 
VAR EmpleadosConSalida = 
    FILTER(
        Empleados,
        NOT ISBLANK(Empleados[FechaSalida])
    )
RETURN
    ADDCOLUMNS(
        EmpleadosConSalida,
        "AntiguedadAlSalir", 
            DATEDIFF([FechaIngreso], [FechaSalida], MONTH),
        "RotacionVoluntaria",
            IF([MotivoSalida] IN {"Renuncia", "Mejor Oportunidad"}, 1, 0),
        "CostoRotacion",
            [SalarioAnual] * 1.5  // Estimación costo de reemplazo
    )
```

## Medidas DAX para People Analytics

### KPIs Fundamentales de Rotación

#### Tasas de Rotación
```dax
TasaRotacionGeneral = 
VAR EmpleadosIniciales = 
    CALCULATE(
        DISTINCTCOUNT(Empleados[EmpleadoID]),
        Empleados[FechaIngreso] <= MIN(DimFecha[Fecha])
    )
VAR SalidasPeriodo = 
    DISTINCTCOUNT(FactRotacion[EmpleadoID])
VAR EmpleadosPromedio = 
    (EmpleadosIniciales + [EmpleadosActivos]) / 2
RETURN
    DIVIDE(SalidasPeriodo, EmpleadosPromedio)

TasaRotacionVoluntaria = 
VAR SalidasVoluntarias = 
    CALCULATE(
        DISTINCTCOUNT(FactRotacion[EmpleadoID]),
        FactRotacion[RotacionVoluntaria] = 1
    )
VAR EmpleadosPromedio = [EmpleadosPromedio]
RETURN
    DIVIDE(SalidasVoluntarias, EmpleadosPromedio)

TasaRetencion = 1 - [TasaRotacionGeneral]
```

#### Análisis de Supervivencia
```dax
SupervivenciaLaboral = 
VAR MesesAntiguedad = MAX(DimEmpleado[AntiguedadMeses])
VAR EmpleadosEnPeriodo = 
    CALCULATE(
        DISTINCTCOUNT(Empleados[EmpleadoID]),
        DimEmpleado[AntiguedadMeses] >= MesesAntiguedad
    )
VAR EmpleadosQuePermanenecen = 
    CALCULATE(
        DISTINCTCOUNT(Empleados[EmpleadoID]),
        DimEmpleado[AntiguedadMeses] >= MesesAntiguedad,
        ISBLANK(Empleados[FechaSalida])
    )
RETURN
    DIVIDE(EmpleadosQuePermanenecen, EmpleadosEnPeriodo)
```

### Análisis de Factores de Riesgo

#### Scoring de Riesgo de Rotación
```dax
RiesgoRotacion = 
VAR AntiguedadRiesgo = 
    SWITCH(
        TRUE(),
        [AntiguedadMeses] <= 6, 5,    // Muy alto
        [AntiguedadMeses] <= 18, 4,   // Alto
        [AntiguedadMeses] <= 36, 3,   // Medio
        [AntiguedadMeses] <= 60, 2,   // Bajo
        1                             // Muy bajo
    )
VAR PerformanceRiesgo = 
    VAR UltimoRating = 
        CALCULATE(
            MAX(Evaluaciones[Rating]),
            FILTER(
                Evaluaciones,
                Evaluaciones[EmpleadoID] = EARLIER(Empleados[EmpleadoID])
            )
        )
    RETURN
        SWITCH(
            TRUE(),
            UltimoRating <= 2, 5,     // Performance bajo = alto riesgo
            UltimoRating <= 3, 3,
            UltimoRating <= 4, 2,
            1
        )
VAR EngagementRiesgo = 
    // Basado en última encuesta de engagement
    VAR UltimoEngagement = [UltimoScoreEngagement]
    RETURN
        SWITCH(
            TRUE(),
            UltimoEngagement <= 2, 5,
            UltimoEngagement <= 3, 3,
            UltimoEngagement <= 4, 2,
            1
        )
RETURN
    (AntiguedadRiesgo + PerformanceRiesgo + EngagementRiesgo) / 3
```

#### Análisis de Manager Impact
```dax
RotacionPorManager = 
VAR RotacionEquipo = 
    CALCULATE(
        [TasaRotacionGeneral],
        RELATEDTABLE(Empleados)
    )
VAR RotacionCompania = 
    CALCULATE(
        [TasaRotacionGeneral],
        ALL(Empleados)
    )
RETURN
    RotacionEquipo - RotacionCompania

ManagerRiesgo = 
IF(
    [RotacionPorManager] > 0.05,  // 5% por encima del promedio
    "Alto",
    IF([RotacionPorManager] > 0.02, "Medio", "Bajo")
)
```

### Time Intelligence para HR

#### Análisis de Tendencias
```dax
RotacionTendencia12M = 
CALCULATE(
    [TasaRotacionGeneral],
    DATESINPERIOD(
        DimFecha[Fecha],
        LASTDATE(DimFecha[Fecha]),
        -12,
        MONTH
    )
)

PrediccionRotacion = 
VAR TendenciaActual = [RotacionTendencia12M]
VAR FactorEstacional = [FactorEstacionalRotacion]
RETURN
    TendenciaActual * FactorEstacional
```

#### Análisis de Cohorts de Contratación
```dax
RetencionCohorte = 
VAR CohorteContratacion = 
    FORMAT(MIN(Empleados[FechaIngreso]), "YYYY-MM")
VAR EmpleadosCohorte = 
    CALCULATE(
        DISTINCTCOUNT(Empleados[EmpleadoID]),
        FORMAT(Empleados[FechaIngreso], "YYYY-MM") = CohorteContratacion
    )
VAR EmpleadosActivos = 
    CALCULATE(
        DISTINCTCOUNT(Empleados[EmpleadoID]),
        FORMAT(Empleados[FechaIngreso], "YYYY-MM") = CohorteContratacion,
        ISBLANK(Empleados[FechaSalida])
    )
RETURN
    DIVIDE(EmpleadosActivos, EmpleadosCohorte)
```

## Análisis Avanzados Implementados

### 1. Employee Journey Analytics
```dax
FasesDelViaje = 
VAR Antiguedad = [AntiguedadMeses]
RETURN
    SWITCH(
        TRUE(),
        Antiguedad <= 3, "Onboarding",
        Antiguedad <= 12, "Early Career",
        Antiguedad <= 36, "Development",
        Antiguedad <= 60, "Growth",
        "Expertise"
    )

RiesgoEnFase = 
CALCULATE(
    [TasaRotacionGeneral],
    FILTER(
        ALL(DimEmpleado[FasesDelViaje]),
        DimEmpleado[FasesDelViaje] = MAX(DimEmpleado[FasesDelViaje])
    )
)
```

### 2. Análisis de Compensation Equity
```dax
BrechaCompaRatio = 
VAR SalarioPromedioPosicion = 
    CALCULATE(
        AVERAGE(Empleados[SalarioBase]),
        ALLEXCEPT(
            Empleados,
            Empleados[TituloTrabajo],
            Empleados[Ubicacion]
        )
    )
VAR SalarioEmpleado = MAX(Empleados[SalarioBase])
RETURN
    DIVIDE(SalarioEmpleado, SalarioPromedioPosicion) - 1

RiesgoCompensacion = 
IF(
    [BrechaCompaRatio] < -0.15,  // 15% por debajo del promedio
    "Alto",
    IF([BrechaCompaRatio] < -0.05, "Medio", "Bajo")
)
```

### 3. Network Analysis
```dax
ConectividadInterna = 
VAR ProyectosColaborativos = 
    COUNTROWS(
        FILTER(
            ProyectosEquipo,
            ProyectosEquipo[EmpleadoID] = MAX(Empleados[EmpleadoID])
        )
    )
VAR EquiposUnicos = 
    DISTINCTCOUNT(
        FILTER(
            ProyectosEquipo,
            ProyectosEquipo[EmpleadoID] = MAX(Empleados[EmpleadoID])
        )[EquipoID]
    )
RETURN
    ProyectosColaborativos * EquiposUnicos
```

## Dashboards y Visualizaciones

### 1. Executive Dashboard - People KPIs
**Audiencia**: CHRO, C-Level
**Contenido**:
- KPIs de rotación vs objetivos
- Trends y forecasts de retention
- Cost of turnover analysis
- Benchmark vs industria
- ROI de programas de retención

### 2. Manager Dashboard - Team Health
**Audiencia**: Managers, Team Leads
**Contenido**:
- Team retention metrics
- Individual risk scores
- Performance vs retention correlation
- Action items recomendados
- Peer manager benchmarking

### 3. HR Operational Dashboard
**Audiencia**: HR Business Partners, Recruiters
**Contenido**:
- Pipeline de rotación predicha
- Exit interview insights
- Segmentación detallada de riesgo
- Intervention tracking
- Workload y capacity planning

### 4. Employee Self-Service Analytics
**Audiencia**: Empleados individuales
**Contenido**:
- Career progression paths
- Skill gap analysis
- Internal opportunities
- Peer benchmarking (anónimo)
- Development recommendations

## Insights y Hallazgos Clave

### Patrones de Rotación Identificados

#### Por Demografía
- **Gen Z**: 28% rotación (vs 18% promedio)
- **Mujeres en tech**: 22% rotación (gap de género)
- **Remote workers**: 12% rotación (mejor retención)
- **Nuevos managers**: 31% rotación en primer año

#### Por Timing
- **Pico estacional**: Enero-Febrero (+40% salidas)
- **Critical period**: Meses 8-14 de antigüedad
- **Performance review cycle**: +25% salidas post-evaluación
- **Promotion cycles**: Spike de salidas en no-promovidos

#### Por Ubicación
- **San Francisco**: 24% rotación (mercado competitivo)
- **Madrid**: 14% rotación (mercado estable)
- **Bangalore**: 31% rotación (growth market)

### Factores Predictivos Top 10
1. **Manager relationship** (R² = 0.67)
2. **Compensation vs market** (R² = 0.54)
3. **Career advancement clarity** (R² = 0.51)
4. **Work-life balance score** (R² = 0.47)
5. **Learning opportunity access** (R² = 0.43)
6. **Peer recognition frequency** (R² = 0.39)
7. **Commute time** (R² = 0.35)
8. **Project autonomy level** (R² = 0.32)
9. **Cross-team collaboration** (R² = 0.29)
10. **Benefits utilization** (R² = 0.26)

## Modelo Predictivo Implementado

### Risk Scoring Algorithm
```dax
EmpleadoEnRiesgo = 
VAR RiskScore = 
    ([ManagerRiskScore] * 0.3) +
    ([CompensationRiskScore] * 0.25) +
    ([EngagementRiskScore] * 0.2) +
    ([CareerRiskScore] * 0.15) +
    ([WorkLifeBalanceRiskScore] * 0.1)
RETURN
    SWITCH(
        TRUE(),
        RiskScore >= 4, "Crítico",
        RiskScore >= 3, "Alto", 
        RiskScore >= 2, "Medio",
        "Bajo"
    )
```

### Early Warning System
- **Alertas automáticas** para managers con empleados en riesgo crítico
- **Escalation workflow** para HR intervention
- **Success tracking** de acciones de retención
- **Predictive pipeline** para workforce planning

## Programa de Retención Basado en Datos

### Intervenciones Diseñadas
1. **High Performer Retention Program**
   - Identificación automática de top performers en riesgo
   - Fast-track career conversations
   - Retention bonuses targeted

2. **Manager Excellence Initiative**
   - Training para managers con alta rotación
   - Monthly check-ins estructurados
   - 360 feedback continuo

3. **Compensation Equity Review**
   - Análisis automated de pay gaps
   - Market adjustment recommendations
   - Transparent compensation bands

4. **Career Pathway Clarification**
   - Individual development plans data-driven
   - Skills gap analysis automático
   - Internal mobility recommendations

## Resultados e Impacto

### Mejoras Cuantificables
- **Rotación general**: 18% → 13.2% (-4.8pp)
- **Rotación alta performance**: 25% → 11% (-14pp)
- **Time to fill**: 45 → 32 días (-29%)
- **Employee satisfaction**: 6.2 → 7.8 (+1.6pts)
- **Manager effectiveness**: 68% → 84% (+16pp)

### Valor Económico
- **Costo de rotación evitado**: €1.8M anuales
- **ROI del programa**: 340% en 18 meses
- **Productividad mejorada**: 12% (por mayor retención)
- **Recruitment cost reduction**: 35%

### Adopción Organizacional
- **87% managers** usando dashboard regularmente
- **92% HR BPs** reportan mejor decision-making
- **76% empleados** engaged con self-service analytics
- **C-Level buy-in**: Full sponsorship y investment

## Próximos Pasos y Roadmap

### Expansiones Analíticas
- **Predictive hiring** success models
- **Skills demand forecasting**
- **Succession planning** automation
- **Culture measurement** through network analysis

### Integraciones Técnicas
- **Microsoft Viva** integration para employee experience
- **AI/ML models** en Azure para prediction accuracy
- **Real-time streaming** de engagement data
- **Natural language processing** de exit interviews

### Escalabilidad Global
- **Multi-tenant model** para diferentes BUs
- **Localization** de factores por región
- **Compliance** con regulaciones locales (GDPR, etc.)
- **Cross-cultural adaptation** de modelos

---

**Nota**: Este caso de estudio utiliza datos simulados pero representa patrones reales observados en organizaciones tecnológicas. Los modelos y métricas están disponibles en la carpeta `data/` para práctica educativa.
