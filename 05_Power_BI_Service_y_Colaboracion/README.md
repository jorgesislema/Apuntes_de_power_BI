# Módulo 05: Power BI Service y Colaboración

## Descripción

Power BI Service es la plataforma en la nube que permite publicar, compartir y colaborar en reportes. Este módulo cubre deployment, workspaces, seguridad y administración empresarial.

## Objetivos de Aprendizaje

Al finalizar este módulo serás capaz de:

- Publicar y distribuir reportes en Power BI Service
- Gestionar workspaces y permisos
- Implementar seguridad a nivel de fila (RLS)
- Configurar data gateways para datos locales

## Contenido del Módulo

| # | Archivo | Tema | Tiempo |
|:-:|---------|------|:------:|
| 5.1 | [Deployment y Publicación](5.1_Deployment_y_Publicacion.md) | Publish, actualización, distribución | 60 min |
| 5.2 | [Colaboración y Workspaces](5.2_Colaboracion_y_Gestion_de_Workspaces.md) | Espacios de trabajo, permisos, packs | 55 min |
| 5.3 | [Seguridad y Administración](5.3_Seguridad_y_Administracion.md) | RLS, audit, cumplimiento | 65 min |
| 5.4 | [Data Gateways](5.4_Data_Gateways.md) | Puente local, configuración, modos | 50 min |
| 5.5 | [Pipelines y Desarrollo](5.5_Pipelines_y_Desarrollo.md) | CI/CD, ambientes, despliegue | 55 min |

## Arquitectura de Power BI Service

```mermaid
flowchart TB
    subgraph Local["Entorno Local"]
        A[Power BI Desktop] -->|Publish| B[Power BI Service]
        C[Data Gateway] -->|Conexión| D[Datasets]
    end
    
    subgraph Service["Power BI Service"]
        B --> E[Workspaces]
        E --> F[Dashboards]
        E --> G[Reportes]
        E --> H[Datasets]
        
        I[Seguridad RLS] --> H
        J[Actualización] --> H
    end
    
    subgraph Consumo["Consumo"]
        F --> K[Usuarios]
        G --> K
        H --> L[Apps]
        H --> M[Embedding]
    end
    
    style Local fill:#e3f2fd,stroke:#1565c0
    style Service fill:#fff3e0,stroke:#e65100
    style Consumo fill:#e8f5e9,stroke:#2e7d32
```

## Flujo de Deployment

```mermaid
flowchart LR
    A[Desarrollo] -->|Publish| B[Test]
    B -->|Aprobación| C[Producción]
    
    A --> A1[Power BI Desktop]
    A --> A2[Workspace Dev]
    
    B --> B1[Workspace Test]
    B --> B2[Validación]
    
    C --> C1[Workspace Prod]
    C --> C2[Monitoreo]
    
    style A fill:#2196f3,stroke:#1565c0,color:#fff
    style B fill:#ff9800,stroke:#e65100,color:#fff
    style C fill:#4caf50,stroke:#2e7d32,color:#fff
```

## Prerrequisitos

- Completar [Módulo 04: Visualización](../04_Visualizacion_y_Storytelling_con_Datos/)
- Cuenta de Power BI Service (gratuita o premium)

## Siguiente Módulo → [06: Gobernanza](../06_Gobernanza_y_Escalabilidad_Empresarial/)
