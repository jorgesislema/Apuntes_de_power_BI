# Módulo 01: Alquimia de Datos con Power Query

## Descripción

Power Query es el motor de Extracción, Transformación y Carga (ETL) integrado en Power BI. Este módulo te enseña a conectar, transformar y preparar datos desde cualquier fuente para su análisis.

## Objetivos de Aprendizaje

Al finalizar este módulo serás capaz de:

- Navegar por el editor de Power Query
- Conectar a múltiples fuentes de datos
- Aplicar transformaciones comunes y avanzadas
- Crear funciones M personalizadas
- Entender los modos de almacenamiento (Import vs DirectQuery)

## Contenido del Módulo

| # | Archivo | Tema | Tiempo |
|:-:|---------|------|:------:|
| 1.1 | [Anatomía del Editor de Power Query](1.1_Anatomia_del_Editor_de_Power_Query.md) | Interfaz, flujo de trabajo, preview | 60 min |
| 1.2 | [Conectores y Modos de Almacenamiento](1.2_Conectores_de_Datos_y_Modos_de_Almacenamiento.md) | Conectores, Import, DirectQuery, Composite | 70 min |
| 1.3 | [Transformaciones Comunes](1.3_Transformaciones_Comunes.md) | Filtrar, agrupar, pivotar, unir | 80 min |
| 1.4 | [Funciones M Personalizadas](1.4_Funciones_M_Personalizadas.md) | Lenguaje M, funciones, parámetros | 90 min |

## Glosario

| [Glosario del Módulo](01_Glosario_Power_Query.md) |
|:--------------------------------------------------:|
| Definiciones de todos los términos técnicos del módulo |

## Diagrama de Flujo ETL

```mermaid
flowchart LR
    subgraph EXTRACCION["1. EXTRACCIÓN"]
        A[Excel] --> D[Power Query]
        B[SQL Server] --> D
        C[API REST] --> D
        E[CSV] --> D
    end
    
    subgraph TRANSFORMACION["2. TRANSFORMACIÓN"]
        D --> F[Limpiar datos]
        F --> G[Tipos de datos]
        G --> H[Columnas calculadas]
        H --> I[Agrupaciones]
        I --> J[Uniones/Merges]
    end
    
    subgraph CARGA["3. CARGA"]
        J --> K[Modelo Tabular]
        K --> L[Power BI Service]
    end
    
    style EXTRACCION fill:#e3f2fd,stroke:#1565c0
    style TRANSFORMACION fill:#fff3e0,stroke:#e65100
    style CARGA fill:#e8f5e9,stroke:#2e7d32
```

## Esquema del Editor

```mermaid
flowchart TD
    subgraph Editor["Editor de Power Query"]
        A[Panel Consultas] --> B[Barra de Fórmulas]
        B --> C[Vista Previa]
        C --> D[Pasos Aplicados]
    end
    
    A --> A1[Consultas en curso]
    A --> A2[Consultas aplicadas]
    
    D --> D1[Paso 1: Fuente]
    D --> D2[Paso 2: Encabezados]
    D --> D3[Paso 3: Tipos]
    D --> D4[Paso N: Resultado]
    
    style Editor fill:#f5f5f5,stroke:#616161
```

## Prerrequisitos

- Completar [Módulo 00: Fundamentos Esenciales](../00_Fundamentos_Esenciales/)

## Siguiente Módulo → [02: DAX](../02_El_Corazon_del_Modelo_DAX/)
