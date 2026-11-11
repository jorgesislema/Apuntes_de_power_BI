# Módulo 07: Casos de Estudio Completos

## Descripción

Este módulo presenta implementaciones completas de Power BI en escenarios empresariales reales. Cada caso incluye modelo de datos, medidas DAX, diseño de dashboard y lecciones aprendidas.

---

## Casos de Estudio Disponibles

| Caso | Industria | Nivel | Tiempo | Complejidad |
|------|-----------|:-----:|:------:|:-----------:|
| [Ventas Retail](Ventas_Retail/) | Comercio Minorista | Intermedio-Avanzado | 4 h | ⭐⭐⭐ |
| [Recursos Humanos](Recursos_Humanos/) | Gestión de Talento | Intermedio | 3 h | ⭐⭐ |
| [Compras y Cadena de Suministro](Compras_Cadena_Suministro/) | Manufactura / Distribución | Intermedio-Avanzado | 6 h | ⭐⭐⭐⭐ |
| [Mantenimiento Industrial](Mantenimiento_Industrial/) | Manufactura / Producción | Avanzado | 8 h | ⭐⭐⭐⭐⭐ |
| [Seguridad Industrial](Seguridad_Industrial/) | Manufactura / Construcción | Intermedio-Avanzado | 6 h | ⭐⭐⭐⭐ |
| [Power BI + IA + MCP](PowerBI_IA_MCP/) | Tecnología / Desarrollo | Avanzado-Experto | 10 h | ⭐⭐⭐⭐⭐ |

---

## Mapa de Casos por Industria

```mermaid
flowchart TB
    subgraph Casos["Casos de Estudio"]
        A[Ventas Retail]
        B[Recursos Humanos]
        C[Compras y Suministro]
        D[Mantenimiento Industrial]
        E[Seguridad Industrial]
        F[Power BI + IA]
    end
    
    subgraph Industrias["Sectores Industriales"]
        G[Comercio Minorista]
        H[Gestión de Talento]
        I[Manufactura]
        J[Tecnología]
    end
    
    A --> G
    B --> H
    C --> I
    D --> I
    E --> I
    F --> J
    
    style Casos fill:#1976d2,stroke:#0d47a1,color:#fff
    style Industrias fill:#4caf50,stroke:#2e7d32,color:#fff
```

---

## Caso 1: Ventas Retail

```mermaid
erDiagram
    DIM_CALENDARIO {
        date FechaPK PK
        int Anio
        int Mes
        string Trimestre
        string NombreMes
    }
    
    DIM_TIENDA {
        int TiendaID PK
        string Nombre
        string Region
        string Ciudad
        string Gerente
    }
    
    DIM_PRODUCTO {
        int ProductoID PK
        string Nombre
        string Categoria
        string SubCategoria
        decimal PrecioUnitario
    }
    
    DIM_CLIENTE {
        int ClienteID PK
        string Nombre
        string Tipo
        string Ciudad
    }
    
    HECHO_VENTAS {
        int VentaID PK
        date FechaFK FK
        int TiendaFK FK
        int ProductoFK FK
        int ClienteFK FK
        int Cantidad
        decimal MontoTotal
        decimal Descuento
        decimal Ganancia
    }
    
    DIM_CALENDARIO ||--o{ HECHO_VENTAS : "tiene"
    DIM_TIENDA ||--o{ HECHO_VENTAS : "realiza"
    DIM_PRODUCTO ||--o{ HECHO_VENTAS : "incluye"
    DIM_CLIENTE ||--o{ HECHO_VENTAS : "compra"
```

### Métricas Clave

| Métrica | Fórmula DAX | Descripción |
|---------|-------------|-------------|
| Ventas Brutas | `SUM(Hecho[MontoTotal])` | Total de ventas antes de descuentos |
| Ventas Netas | `[Brutas] - SUM(Hecho[Descuento])` | Ventas después de descuentos |
| Margen % | `DIVIDE([Ganancia], [Netas])` | Porcentaje de ganancia |
| Ticket Promedio | `DIVIDE([Netas], Clientes)` | Gasto promedio por cliente |
| Crecimiento YoY | `DIVIDE([Act]-[Ant], [Ant])` | Variación interanual |

---

## Caso 2: Recursos Humanos

```mermaid
erDiagram
    DIM_EMPLEADO {
        int EmpleadoID PK
        string Nombre
        string Departamento
        string Cargo
        date FechaIngreso
    }
    
    DIM_TIEMPO {
        date FechaPK PK
        int Anio
        int Mes
        int Trimestre
    }
    
    HECHO_NOMINA {
        int NominaID PK
        int EmpleadoID FK
        date FechaPK FK
        decimal SalarioBase
        decimal Bonificaciones
        decimal Deducciones
        decimal Neto
    }
    
    DIM_EMPLEADO ||--o{ HECHO_NOMINA : "recibe"
    DIM_TIEMPO ||--o{ HECHO_NOMINA : "corresponde a"
```

### Métricas Clave

| Métrica | Fórmula DAX | Descripción |
|---------|-------------|-------------|
| Nómina Total | `SUM(Nomina[Neto])` | Total de pagos netos |
| Costo por Departamento | `SUM(Nomina[Neto]) GROUP BY Depto` | Gasto por área |
| Rotación de Personal | `ConteoSalidas / PromedioEmpleados` | Tasa de rotación |
| Antigüedad Promedio | `AVG(DATEDIFF(Hoy, Ingreso))` | Años promedio en la empresa |

---

## Caso 3: Compras y Cadena de Suministro

```mermaid
flowchart TB
    subgraph Cadena["Cadena de Suministro"]
        A[Proveedores] --> B[Compras]
        B --> C[Almacén]
        C --> D[Producción]
        D --> D[ Distribución]
    end
    
    subgraph KPIs["KPIs Principales"]
        E[Fill Rate >95%]
        F[Lead Time <7 días]
        G[Inventario Obsoleto <5%]
        H[Costos -15%]
    end
    
    style Cadena fill:#1976d2,stroke:#0d47a1,color:#fff
    style KPIs fill:#4caf50,stroke:#2e7d32,color:#fff
```

### Métricas Clave

| Métrica | Fórmula DAX | Meta |
|---------|-------------|:----:|
| Fill Rate | `DIVIDE(CantRecibida, CantOrdenada)` | >95% |
| Lead Time Promedio | `AVG(DiasEntrega)` | <7 días |
| Score Proveedor | `Calidad x 0.4 + Tiempo x 0.35 + Costo x 0.25` | >4.0 |
| Días de Stock | `StockActual / ConsumoDiario` | 15-30 días |

---

## Caso 4: Mantenimiento Industrial

```mermaid
flowchart TB
    subgraph Mantenimiento["Estrategia de Mantenimiento"]
        A[Correctivo] --> B[Reparar cuando falla]
        C[Preventivo] --> D[Reparar en intervalos]
        E[Preditivo] --> F[Reparar según condición]
        G[Prescriptivo] --> H[IA recomienda acción]
    end
    
    subgraph KPIs["KPIs Principales"]
        I[OEE >85%]
        J[MTBF >720 h]
        K[MTTR <4 h]
        L[Disponibilidad >95%]
    end
    
    style Mantenimiento fill:#ff9800,stroke:#e65100,color:#fff
    style KPIs fill:#4caf50,stroke:#2e7d32,color:#fff
```

### Métricas Clave

| Métrica | Fórmula DAX | Meta |
|---------|-------------|:----:|
| OEE | `Disponibilidad x Rendimiento x Calidad` | >85% |
| MTBF | `TiempoTotal / #Fallas` | >720 h |
| MTTR | `SUM(TiempoReparación) / #Reparaciones` | <4 h |
| Disponibilidad | `TiempoOperación / TiempoTotal` | >95% |

---

## Caso 5: Seguridad Industrial

```mermaid
flowchart TB
    subgraph Seguridad["Sistema de Seguridad"]
        A[Prevención] --> B[Detección]
        B --> C[Respuesta]
        C --> D[Análisis]
        D --> E[Mejora]
    end
    
    subgraph Normas["Marco Normativo"]
        F[ISO 45001]
        G[OSHA]
        H[NOM-004-STPS]
    end
    
    subgraph KPIs["KPIs Principales"]
        I[TRIR <1.0]
        J[DART <0.5]
        K[Frecuencia <5.0]
        L[Capacitación >95%]
    end
    
    style Seguridad fill:#1976d2,stroke:#0d47a1,color:#fff
    style Normas fill:#ff9800,stroke:#e65100,color:#fff
    style KPIs fill:#4caf50,stroke:#2e7d32,color:#fff
```

### Métricas Clave

| Métrica | Fórmula DAX | Meta |
|---------|-------------|:----:|
| TRIR | `(Incidentes x 200K) / HorasTrabajadas` | <1.0 |
| DART | `(DíasPerdidos x 200K) / HorasTrabajadas` | <0.5 |
| Frecuencia | `(Incidentes x 1M) / HorasTrabajadas` | <5.0 |
| Cumplimiento Capacitación | `HorasRealizadas / HorasPlaneadas` | >95% |

---

## Caso 6: Power BI + IA + MCP

```mermaid
flowchart TB
    subgraph Stack["Stack Tecnológico"]
        A[Power BI] --> B[IA Generativa]
        B --> C[MCP Server]
        C --> D[VS Code]
    end
    
    subgraph Casos["Casos de Uso"]
        E[Generación automática de DAX]
        F[Documentación automática]
        G[Análisis de datos con IA]
        H[Desarrollo asistido]
    end
    
    Stack --> Casos
    
    style Stack fill:#9c27b0,stroke:#6a1b9a,color:#fff
    style Casos fill:#4caf50,stroke:#2e7d32,color:#fff
```

### Componentes

| Componente | Función | Herramienta |
|------------|---------|-------------|
| **IA Generativa** | Generar código DAX | GitHub Copilot, ChatGPT |
| **MCP Server** | Integración IA-Power BI | Custom MCP Server |
| **VS Code** | IDE de desarrollo | Visual Studio Code |
| **Python** | Automatización | Scripts personalizados |

---

## Tabla Comparativa de Casos

| Característica | Retail | RRHH | Compras | Mantenimiento | Seguridad | IA+MCP |
|----------------|:------:|:----:|:-------:|:-------------:|:---------:|:------:|
| **Volumen datos** | Medio | Bajo | Alto | Alto | Medio | Variable |
| **Complejidad DAX** | Media | Baja | Alta | Muy Alta | Media | Muy Alta |
| **Modelo dimensional** | Estrella | simple | Estrella | Estrella | Estrella | Flexible |
| **Time Intelligence** | Sí | Sí | Parcial | Sí | Parcial | Sí |
| **IoT/Sensores** | No | No | No | Sí | Sí | No |
| **IA/ML** | No | No | No | Parcial | No | Sí |
| **Costo implementación** | Bajo | Bajo | Medio | Alto | Medio | Variable |

---

## Lecciones Aprendidas

| Lección | Aplicación |
|---------|------------|
| El modelo dimensional es fundamental | Usar esquema estrella siempre que sea posible |
| Las medidas deben ser reutilizables | Crear medidas base y medidas calculadas separadas |
| La granularidad debe ser consistente | Definir la granularidad antes de diseñar el modelo |
| Los datos de ejemplo agilizan el desarrollo | Generar datos de prueba representativos |
| La industria-specific knowledge es clave | Entender el dominio antes de modelar |
| La IA potencia la productividad | Usar herramientas de IA para tareas repetitivas |

---

## Prerrequisitos

- Completar los Módulos 00-06
- Cuenta de Power BI Desktop instalada
- Para Caso 6: Python, VS Code, cuenta GitHub

---

## Siguiente Módulo → [08: Ejercicios DAX](../08_Ejercicios_DAX_Progresivos/)
