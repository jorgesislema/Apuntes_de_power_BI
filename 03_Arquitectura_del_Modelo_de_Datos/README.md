# Módulo 03: Arquitectura del Modelo de Datos

## Descripción

Un modelo de datos bien diseñado es la base de cualquier solución Power BI exitosa. Este módulo cubre los principios del modelado dimensional, tipos de relaciones y estrategias de optimización.

## Objetivos de Aprendizaje

Al finalizar este módulo serás capaz de:

- Diseñar modelos dimensionales eficientes
- Configurar relaciones y cardinalidades correctas
- Distinguir entre esquema estrella y copo de nieve
- Optimizar el rendimiento del modelo

## Contenido del Módulo

| # | Archivo | Tema | Tiempo |
|:-:|---------|------|:------:|
| 3.1 | [Fundamentos del Modelado Dimensional](3.1_Fundamentos_del_Modelado_Dimensional.md) | Tablas de hechos, dimensiones, granularidad | 70 min |
| 3.2 | [Relaciones y Cardinalidades](3.2_Relaciones_y_Cardinalidades.md) | Tipos, comportamientos, activación | 65 min |
| 3.3 | [Esquemas Estrella y Copo de Nieve](3.3_Esquemas_Estrella_y_Copo_de_Nieve.md) | Comparación, ventajas, cuándo usar cada uno | 50 min |
| 3.4 | [Optimización y Agregaciones](3.4_Optimizacion_y_Agregaciones.md) | Rendimiento, tablas resumen, almacenamiento | 60 min |

## Tipos de Modelos

```mermaid
flowchart TD
    subgraph Estrella["Esquema Estrella"]
        E1[Dim Tiempo] --> H1[Hecho Ventas]
        E2[Dim Producto] --> H1
        E3[Dim Cliente] --> H1
        E4[Dim Tienda] --> H1
    end
    
    subgraph Copo["Esquema Copo de Nieve"]
        C1[Dim Tiempo] --> H2[Hecho Ventas]
        C2[Dim Producto] --> C2A[Dim Categoría]
        C2A --> H2
        C3[Dim Cliente] --> C3A[Dim Ciudad]
        C3A --> H2
    end
    
    style Estrella fill:#e8f5e9,stroke:#2e7d32
    style Copo fill:#fff3e0,stroke:#e65100
```

## Diagrama de Relaciones

```mermaid
flowchart LR
    subgraph Tablas["Modelo Dimensional"]
        A[Dim Calendario] -->|1:M| D[Hecho Ventas]
        B[Dim Producto] -->|1:M| D
        C[Dim Cliente] -->|1:M| D
        E[Dim Tienda] -->|1:M| D
    end
    
    subgraph Cardinalidad["Cardinalidades"]
        D -->|1:1| A
        D -->|1:1| B
        D -->|1:1| C
        D -->|1:1| E
    end
    
    style Tablas fill:#e3f2fd,stroke:#1565c0
```

## Prerrequisitos

- Completar [Módulo 02: DAX](../02_El_Corazon_del_Modelo_DAX/)

## Siguiente Módulo → [04: Visualización](../04_Visualizacion_y_Storytelling_con_Datos/)
