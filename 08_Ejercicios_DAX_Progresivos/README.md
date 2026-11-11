# Módulo 08: Ejercicios DAX Progresivos

## Descripción

Ejercicios prácticos de DAX organizados por nivel de dificultad. Cada ejercicio incluye contexto de negocio, modelo de datos, desafío y solución detallada.

## Estructura de Ejercicios

```mermaid
flowchart TD
    A[Nivel Básico] -->|Dominar| B[Nivel Intermedio]
    B -->|Dominar| C[Nivel Avanzado]
    C -->|Dominar| D[Nivel Experto]
    
    A --> A1[SUM, COUNT, AVERAGE]
    A --> A2[FILTER básico]
    A --> A3[Medidas simples]
    
    B --> B1[CALCULATE]
    B --> B2[Time Intelligence]
    B --> B3[Relaciones]
    
    C --> C1[Variables VAR]
    C --> C2[Iteradores]
    C --> C3[Patrones complejos]
    
    D --> D1[Optimización]
    D --> D2[Dynamic Segmentation]
    D --> D3[Medidas dinámicas]
    
    style A fill:#4caf50,stroke:#2e7d32,color:#fff
    style B fill:#ff9800,stroke:#e65100,color:#fff
    style C fill:#f44336,stroke:#c62828,color:#fff
    style D fill:#9c27b0,stroke:#6a1b9a,color:#fff
```

## Niveles de Dificultad

| Nivel | Archivo | Temas Cubiertos | Ejercicios | Tiempo |
|:-----:|---------|-----------------|:----------:|:------:|
| Básico | [Ejercicios Básicos](01_Nivel_Basico/Ejercicios_Basicos.md) | SUM, COUNT, AVERAGE, MIN, MAX | 10 | 2 h |
| Intermedio | [Ejercicios Intermedios](02_Nivel_Intermedio/Ejercicios_Intermedios.md) | CALCULATE, FILTER, ALL | 8 | 3 h |
| Avanzado | [Ejercicios Avanzados](03_Nivel_Avanzado/Ejercicios_Avanzados.md) | VAR, iteradores, time intelligence | 6 | 4 h |
| Experto | [Ejercicios Expertos](04_Nivel_Experto/Ejercicios_Expertos.md) | Patrones, optimización, dinámicos | 5 | 3 h |

## Datos de Práctica

| Archivo | Registros | Descripción |
|---------|:---------:|-------------|
| `clientes.csv` | 500 | Clientes con nombre, email, ciudad y tipo |
| `productos.csv` | 50 | Productos con categoría, precio y stock |
| `vendedores.csv` | 25 | Vendedores por región con comisión |
| `ventas.csv` | 5,000 | Transacciones de 2022-2024 |

### Generar Datos

```bash
cd Datos_Practica
python generar_datos_practica.py
```

## Esquema de Datos

```mermaid
erDiagram
    CLIENTES {
        int ClienteID PK
        string Nombre
        string Apellido
        string Email
        string Ciudad
        string TipoCliente
        date FechaRegistro
    }
    
    PRODUCTOS {
        int ProductoID PK
        string Nombre
        string Categoria
        string SubCategoria
        decimal PrecioUnitario
        decimal CostoUnitario
        int Stock
    }
    
    VENDEDORES {
        int VendedorID PK
        string Nombre
        string Region
        date FechaIngreso
        decimal ComisionPorcentaje
    }
    
    VENTAS {
        int VentaID PK
        date Fecha
        int ClienteID FK
        int VendedorID FK
        int ProductoID FK
        int Cantidad
        int DescuentoPorcentaje
        decimal MontoTotal
        string Estado
    }
    
    CLIENTES ||--o{ VENTAS : "realiza"
    PRODUCTOS ||--o{ VENTAS : "incluye"
    VENDEDORES ||--o{ VENTAS : "atiende"
```

## Cómo Usar Este Módulo

1. **Lee el contexto del negocio** — Entiende el escenario
2. **Revisa el modelo de datos** — Identifica tablas y relaciones
3. **Intenta resolver el ejercicio** — Sin ver la solución
4. **Compara con la solución** — Verifica tu enfoque
5. **Experimenta** — Modifica la solución para aprender más

## Prerrequisitos

- Completar [Módulo 02: DAX](../02_El_Corazon_del_Modelo_DAX/)
- Generar datos de práctica (ver arriba)

## Módulos Relacionados

- [02. DAX - Motor de Cálculo](../02_El_Corazon_del_Modelo_DAX/)
- [07. Casos de Estudio](../07_Casos_de_Estudio_Completos/)
