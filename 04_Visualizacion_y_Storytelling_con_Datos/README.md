# Módulo 04: Visualización y Storytelling con Datos

## Descripción

La visualización efectiva transforma datos complejos en historias comprensibles. Este módulo cubre los principios de diseño, técnicas de storytelling y buenas prácticas para crear dashboards impactantes.

## Objetivos de Aprendizaje

Al finalizar este módulo serás capaz de:

- Aplicar principios de diseño visual basados en evidencia
- Seleccionar el tipo de gráfico adecuado para cada dato
- Construir narrativas visuales coherentes
- Diseñar dashboards profesionales y accesibles

## Contenido del Módulo

| # | Archivo | Tema | Tiempo |
|:-:|---------|------|:------:|
| 4.1 | [Principios de Visualización Efectiva](4.1_Principios_de_Visualizacion_Efectiva.md) | Gestalt, color, pre-atención, layouts | 80 min |
| 4.2 | [Construcción de Narrativas con Datos](4.2_Construccion_de_Narrativas_con_Datos.md) | Storytelling, estructura, flujo | 60 min |
| 4.3 | [Diseño de Dashboards Profesionales](4.3_Diseno_de_Dashboards_Profesionales.md) | Layout, consistencia, responsive | 70 min |
| 4.4 | [Accesibilidad en Visualización](4.4_Accesibilidad_en_Visualizacion.md) | WCAG, daltonismo, alternativas | 45 min |

## Tipos de Gráficos y Uso Recomendado

```mermaid
flowchart TD
    A[Tipo de Dato] --> B{¿Qué quieres mostrar?}
    
    B -->|Comparar valores| C[Gráfico de Barras]
    B -->|Mostrar tendencia| D[Gráfico de Líneas]
    B -->|Mostrar proporción| E[Gráfico Circular]
    B -->|Mostrar distribución| F[Histograma]
    B -->|Mostrar relación| G[Gráfico de Dispersión]
    B -->|Mostrar jerarquía| H[Treemap]
    B -->|Mostrar geografía| I[Mapa]
    
    C --> C1[Barras simples]
    C --> C2[Barras agrupadas]
    C --> C3[Barras apiladas]
    
    D --> D1[Línea simple]
    D --> D2[Líneas múltiples]
    D --> D3[Área]
    
    E --> E1[Pastel]
    E --> E2[Donut]
    
    style A fill:#2196f3,stroke:#1565c0,color:#fff
    style B fill:#ff9800,stroke:#e65100,color:#fff
    style C fill:#4caf50,stroke:#2e7d32,color:#fff
    style D fill:#4caf50,stroke:#2e7d32,color:#fff
    style E fill:#4caf50,stroke:#2e7d32,color:#fff
    style F fill:#4caf50,stroke:#2e7d32,color:#fff
    style G fill:#4caf50,stroke:#2e7d32,color:#fff
    style H fill:#4caf50,stroke:#2e7d32,color:#fff
    style I fill:#4caf50,stroke:#2e7d32,color:#fff
```

## Flujo de Storytelling

```mermaid
flowchart LR
    A[Contexto] --> B[Tensión]
    B --> C[Resolución]
    C --> D[Acción]
    
    A --> A1["¿Quiénes somos?"]
    A --> A2["¿Cuál es el problema?"]
    
    B --> B1["Los datos muestran..."]
    B --> B2["Esto es preocupante porque..."]
    
    C --> C1["La raíz es..."]
    C --> C2["Podemos mejorar con..."]
    
    D --> D1["Recomendación 1"]
    D --> D2["Recomendación 2"]
    
    style A fill:#1976d2,stroke:#0d47a1,color:#fff
    style B fill:#f57c00,stroke:#e65100,color:#fff
    style C fill:#388e3c,stroke:#1b5e20,color:#fff
    style D fill:#7b1fa2,stroke:#4a148c,color:#fff
```

## Paleta de Colores Recomendada

| Uso | Color Hex | Nombre | Aplicación |
|-----|:---------:|--------|------------|
| Primario | `#1976d2` | Azul | Títulos, elementos principales |
| Secundario | `#4caf50` | Verde | Valores positivos |
| Terciario | `#ff9800` | Naranja | Advertencias, tendencias |
| Alerta | `#f44336` | Rojo | Valores negativos, errores |
| Neutro | `#757575` | Gris | Texto secundario, bordes |
| Fondo | `#fafafa` | Gris claro | Fondos de paneles |

## Prerrequisitos

- Completar [Módulo 03: Modelo de Datos](../03_Arquitectura_del_Modelo_de_Datos/)

## Siguiente Módulo → [05: Power BI Service](../05_Power_BI_Service_y_Colaboracion/)
