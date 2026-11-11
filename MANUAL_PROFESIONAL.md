# MANUAL PROFESIONAL: Repositorio de Power BI
## De Cero a PhD — Guía Completa de Estándares y Mejoras

---

**Versión:** 1.0  
**Fecha:** 18 de Septiembre, 2026  
**Autor:** Jorge Sislema  
**Licencia:** MIT

---

## TABLA DE CONTENIDOS

1. [Análisis del Estado Actual](#1-análisis-del-estado-actual)
2. [Estructura de Repositorio Profesional](#2-estructura-de-repositorio-profesional)
3. [Estándares de Código y Documentación](#3-estándares-de-código-y-documentación)
4. [Guía de Mejoras por Fase](#4-guía-de-mejoras-por-fase)
5. [Plantillas de Archivos](#5-plantillas-de-archivos)
6. [Gestión de Datos de Ejemplo](#6-gestión-de-datos-de-ejemplo)
7. [Automatización y CI/CD](#7-automatización-y-cicd)
8. [Glosario Profesional](#8-glosario-profesional)
9. [Ejemplos Prácticos](#9-ejemplos-prácticos)
10. [Checklist de Calidad](#10-checklist-de-calidad)

---

## 1. ANÁLISIS DEL ESTADO ACTUAL

### 1.1 Puntuación General

| Criterio | Puntuación | Estado |
|----------|:----------:|--------|
| Estructura de carpetas | 8/10 | ✅ Excelente |
| Contenido técnico markdown | 9/10 | ✅ Excelente |
| README principal | 2/10 | 🔴 Crítico |
| .gitignore | 0/10 | 🔴 Ausente |
| Archivos vacíos/irrelevantes | -3 | 🔴 Problema serio |
| Casos de estudio | 4/10 | 🟡 Parcial |
| Consistencia visual | 6/10 | 🟡 Aceptable |
| Gobernanza del repo | 3/10 | 🔴 Deficiente |
| Documentación de uso | 2/10 | 🔴 Crítico |

**Puntuación global: 4.3/10 — Fase inicial de desarrollo**

### 1.2 Problemas Críticos Identificados

#### PROBLEMA 1: Ausencia total de `.gitignore`
```
CONSECUENCIA:
- Carpeta .mypy_cache/ trackeada (caché de Python, nunca debe ir al repo)
- Carpeta .qodo/ trackeada (herramienta de IA vacía)
- Futuros archivos temporales serán committeados accidentalmente
```

#### PROBLEMA 2: Archivo irrelevante `eje.py`
```
CONTENIDO REAL:
- Script de simulación bancaria usando librería `simpy`
- Simula colas de espera en un banco
- NO tiene relación alguna con Power BI
- Contiene función `calcular_satisfaccion` referenciada pero no definida

ACCIÓN: ELIMINAR COMPLETAMENTE
```

#### PROBLEMA 3: Archivos vacíos
```
ARCHIVOS VACÍOS (0 bytes):
├── 08_Ejercicios_DAX_Progresivos/README.md
├── 08_Ejercicios_DAX_Progresivos/Datos_Practica/README.md
├── 08_Ejercicios_DAX_Progresivos/Datos_Practica/generar_datos_practica.py
├── 08_Ejercicios_DAX_Progresivos/Datos_Practica/Clientes.csv
├── 08_Ejercicios_DAX_Progresivos/Datos_Practica/Productos.csv
├── 08_Ejercicios_DAX_Progresivos/Datos_Practica/Vendedores.csv
└── 08_Ejercicios_DAX_Progresivos/Datos_Practica/Ventas.csv
```

#### PROBLEMA 4: README.md insuficiente
```
CONTENIDO ACTUAL (2 líneas):
# Apuntes_de_power_BI
Colección de apuntes de Power BI para estudiar y repasar

PROBLEMAS:
- Sin tabla de contenidos
- Sin badges de licencia/estado
- Sin descripción del proyecto
- Sin instrucciones de uso
- Sin guía de navegación
- "Power BI" con tipografía inconsistente
```

#### PROBLEMA 5: Casos de estudio sin datos
```
CARPETAS data/ VACÍAS:
├── 07_Casos_de_Estudio_Completos/Ventas_Retail/data/
└── 07_Casos_de_Estudio_Completos/Recursos_Humanos/data/

Los READMEs mencionan archivos .pbix y datos que NO EXISTEN
```

### 1.3 Fortalezas Existentes

| Fortaleza | Detalle |
|-----------|---------|
| Esquema numerado | Secuencia lógica `00→08` bien estructurada |
| Contenido markdown | Nivel experto, bien formateado, con ejemplos |
| Glosarios | Excelentes glosarios alfabéticos en carpetas 00 y 01 |
| CONTRIBUTING.md | Guía completa de contribución (51 líneas) |
| Licencia | MIT License correcta y completa |
| Ejercicios DAX | Progresión pedagógica clara (básico→experto) |

---

## 2. ESTRUCTURA DE REPOSITORIO PROFESIONAL

### 2.1 Árbol de Directorios Objetivo

```
Apuntes_de_power_BI/
│
├── .github/                          ← NUEVO: Configuración GitHub
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       └── markdown-lint.yml
│
├── .gitignore                        ← NUEVO: Obligatorio
├── README.md                         ← REESCRIBIR: Profesional
├── LICENSE                           ← MANTENER: Correcto
├── CONTRIBUTING.md                   ← MANTENER: Correcto
├── CHANGELOG.md                      ← NUEVO: Historial de cambios
├── CODE_OF_CONDUCT.md                ← NUEVO: Código de conducta
│
├── assets/                           ← NUEVO: Recursos compartidos
│   ├── images/                       ← Capturas de pantalla
│   │   ├── power_bi_desktop/
│   │   ├── power_bi_service/
│   │   └── diagrams/
│   ├── data/                         ← Datos de ejemplo compartidos
│   │   ├── retail/
│   │   ├── hr/
│   │   └── sample/
│   └── templates/                    ← Plantillas reutilizables
│       ├── measure_template.dax
│       └── report_template.md
│
├── 00_Fundamentos_Esenciales/        ← MANTENER
│   ├── README.md                     ← NUEVO: Índice de la sección
│   ├── 0.1_Que_es_Business_Intelligence.md
│   ├── 0.2_Anatomia_del_Ecosistema_Power_BI.md
│   ├── 0.3_Instalacion_y_Configuracion.md
│   ├── 0.4_Recorrido_por_la_Interfaz_de_PBI_Desktop.md
│   └── 00_Glosario_Fundamentos.md
│
├── 01_Alquimia_de_Datos_con_Power_Query/
│   ├── README.md                     ← NUEVO
│   ├── 1.1_Anatomia_del_Editor_de_Power_Query.md
│   ├── 1.2_Conectores_de_Datos_y_Modos_de_Almacenamiento.md
│   ├── 1.3_Transformaciones_Comunes.md           ← NUEVO
│   ├── 1.4_Funciones_M_Personalizadas.md         ← NUEVO
│   └── 01_Glosario_Power_Query.md
│
├── 02_El_Corazon_del_Modelo_DAX/
│   ├── README.md                     ← NUEVO
│   ├── 2.1_Conceptos_Fundamentales/
│   │   ├── 2.1.1_Contexto_de_Filtro.md
│   │   ├── 2.1.2_Contexto_de_Fila.md
│   │   └── 2.1.3_Transicion_de_Contexto.md
│   ├── 2.2_Funciones_DAX_Esenciales/             ← NUEVO
│   │   ├── 2.2.1_Funciones_de_Filtrado.md
│   │   ├── 2.2.2_Funciones_de_Time_Intelligence.md
│   │   └── 2.2.3_Funciones_de_Texto_y_Fechas.md
│   ├── 2.3_Patrones_DAX_Avanzados/               ← NUEVO
│   │   ├── 2.3.1_Patron_Calendario.md
│   │   ├── 2.3.2_Patron_ABC_Analysis.md
│   │   └── 2.3.3_Patron_Dynamic_Segmentation.md
│   └── 02_Glosario_DAX.md                        ← NUEVO
│
├── 03_Arquitectura_del_Modelo_de_Datos/
│   ├── README.md                     ← NUEVO
│   ├── 3.1_Fundamentos_del_Modelado_Dimensional.md
│   ├── 3.2_Relaciones_y_Cardinalidades.md
│   ├── 3.3_Esquemas_Eny_Y.md                      ← NUEVO
│   ├── 3.4_Optimizacion_y_Agregaciones.md         ← NUEVO
│   └── 03_Glosario_Modelado.md                    ← NUEVO
│
├── 04_Visualizacion_y_Storytelling_con_Datos/
│   ├── README.md                     ← NUEVO
│   ├── 4.1_Principios_de_Visualizacion_Efectiva.md
│   ├── 4.2_Construccion_de_Narrativas_con_Datos.md
│   ├── 4.3_Diseno_de_Dashboards_Profesionales.md  ← NUEVO
│   ├── 4.4_Accesibilidad_en_Visualizacion.md      ← NUEVO
│   └── 04_Glosario_Visualizacion.md               ← NUEVO
│
├── 05_Power_BI_Service_y_Colaboracion/
│   ├── README.md                     ← NUEVO
│   ├── 5.1_Deployment_y_Publicacion.md
│   ├── 5.2_Colaboracion_y_Gestion_de_Workspaces.md
│   ├── 5.3_Seguridad_y_Administracion.md
│   ├── 5.4_Data_Gateways.md                       ← NUEVO
│   ├── 5.5_Pipelines_y_Desarrollo.md             ← NUEVO
│   └── 05_Glosario_Service.md                     ← NUEVO
│
├── 06_Gobernanza_y_Escalabilidad_Empresarial/
│   ├── README.md                     ← NUEVO
│   ├── 6.1_Estrategias_de_Gobernanza.md
│   ├── 6.2_Arquitectura_Escalable.md
│   ├── 6.3_Centro_de_Excelencia_COE.md
│   ├── 6.4_Lineamientos_de_Nomenclatura.md       ← NUEVO
│   ├── 6.5_Monitoreo_y_Optimizacion.md           ← NUEVO
│   └── 06_Glosario_Gobernanza.md                 ← NUEVO
│
├── 07_Casos_de_Estudio_Completos/
│   ├── README.md                     ← NUEVO: Índice general
│   ├── Ventas_Retail/
│   │   ├── README.md
│   │   ├── data/                     ← LLENAR con datos CSV
│   │   │   ├── productos.csv
│   │   │   ├── tiendas.csv
│   │   │   ├── ventas.csv
│   │   │   └── calendario.csv
│   │   ├── dax/                      ← NUEVO: Medidas DAX
│   │   │   ├── medidas_ventas.dax
│   │   │   └── medidas_inventario.dax
│   │   └── report/                   ← NUEVO: Especificación
│   │       └── dashboard_spec.md
│   └── Recursos_Humanos/
│       ├── README.md
│       ├── data/
│       │   ├── empleados.csv
│       │   ├── nomina.csv
│       │   └── calendario.csv
│       ├── dax/
│       │   └── medidas_rrhh.dax
│       └── report/
│           └── dashboard_spec.md
│
├── 08_Ejercicios_DAX_Progresivos/
│   ├── README.md                     ← REESCRIBIR
│   ├── 01_Nivel_Basico/
│   │   └── Ejercicios_Basicos.md
│   ├── 02_Nivel_Intermedio/
│   │   └── Ejercicios_Intermedios.md
│   ├── 03_Nivel_Avanzado/
│   │   └── Ejercicios_Avanzados.md
│   ├── 04_Nivel_Experto/
│   │   ├── Ejercicios_Expertos.md
│   │   └── Tecnicas_Avanzadas.md
│   └── Datos_Practica/
│       ├── README.md                 ← REESCRIBIR
│       ├── generar_datos.py          ← RENOMBRAR y LLENAR
│       ├── clientes.csv              ← LLENAR
│       ├── productos.csv             ← LLENAR
│       ├── vendedores.csv            ← LLENAR
│       └── ventas.csv                ← LLENAR
│
└── 09_Referencias_y_Recursos/                        ← NUEVO
    ├── README.md
    ├── libros_recomendados.md
    ├── certificaciones.md
    ├── comunidades_y_foros.md
    └── herramientas_complementarias.md
```

### 2.2 Convenciones de Nomenclatura

#### Carpetas
```
ESTANDAR: XX_Nombre_En_Title_Case_Con_Guiones_Bajos/
EJEMPLO:  01_Alquimia_de_Datos_con_Power_Query/

REGLAS:
1. Prefijo numérico de 2 dígitos (00-99)
2. Nombre descriptivo en español
3. Title Case (mayúscula inicial en palabras significativas)
4. Separador: guion bajo (_)
5. Sin espacios, tildes ni caracteres especiales
```

#### Archivos Markdown
```
ESTANDAR: X.Y_Nombre_Del_Tema.md
EJEMPLO:  2.1.1_Contexto_de_Filtro.md

REGLAS:
1. Numeración jerárquica (hasta 3 niveles)
2. Nombre descriptivo en Title Case
3. Extensión .md exclusivamente
4. Sin espacios en el nombre
```

#### Datos de Ejemplo
```
ESTANDAR: nombre_tabla.csv
EJEMPLO:  ventas.csv, productos.csv

REGLAS:
1. Nombre en minúsculas
2. Singular (no plural)
3. Formato CSV con UTF-8 encoding
4. Incluir encabezados en primera fila
```

---

## 3. ESTÁNDARES DE CÓDIGO Y DOCUMENTACIÓN

### 3.1 Plantilla de Archivo Markdown

Cada archivo de contenido DEBE seguir esta estructura:

```markdown
---
title: "Título del Tema"
description: "Descripción breve del contenido"
author: "Jorge Sislema"
date: YYYY-MM-DD
version: "1.0"
tags: [power-bi, dax, power-query, etc.]
difficulty: "básico|intermedio|avanzado|experto"
estimated_time: "XX minutos"
---

# Título del Tema

## Resumen Ejecutivo
<!-- Párrafo breve que explica qué aprenderá el lector -->

## Objetivos de Aprendizaje
<!-- Lista con viñetas de los objetivos específicos -->
- Objetivo 1
- Objetivo 2
- Objetivo 3

## Contenido

### Sección Principal
<!-- Desarrollo del tema con ejemplos prácticos -->

```dax
// Ejemplo de código DAX con comentarios
Measure = 
CALCULATE(
    SUM(Table[Column]),
    FilterExpression
)
```

### Ejemplo Práctico
<!-- Caso real empresarial -->

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| Columna 1 | Desc 1 | Ej 1 |

## Errores Comunes
<!-- Lista de errores frecuentes y cómo evitarlos -->

## Ejercicio Práctico
<!-- Actividad para reforzar el aprendizaje -->

## Glosario de la Sección
<!-- Definiciones de términos clave de ESTE archivo -->

## Referencias
<!-- Enlaces a documentación oficial, artículos, etc. -->

## Siguiente Tema
<!-- Enlace al siguiente archivo de la secuencia -->
```

### 3.2 Estándares de Código

#### Bloques de Código DAX
```
✅ BIEN:
```dax
Total Ventas = 
CALCULATE(
    SUM(Ventas[Monto]),
    Ventas[Estado] = "Completada"
)
```

❌ MAL:
```
Total Ventas = CALCULATE(SUM(Ventas[Monto]), Ventas[Estado] = "Completada")
```

REGLAS:
1. Siempre usar bloques de código con tag `dax`
2. Una instrucción por línea
3. Indentar con 4 espacios
4. Incluir comentarios explicativos
5. Usar nombres de columna descriptivos
```

#### Tablas Comparativas
```
ESTÁNDAR:
| Característica | Opción A | Opción B | Recomendado |
|----------------|----------|----------|:-----------:|
| Descripción    | Valor    | Valor    |     ✅      |

REGLAS:
1. Incluir encabezados claros
2. Columna "Recomendado" al final
3. Usar ✅ y ❌ para indicar preferencia
4. Alinear texto a la izquierda, center para iconos
```

### 3.3 Estándares de Imágenes

```
NOMENBRATURA: seccion_subseccion_descripcion.png
EJEMPLO:      02_01_contexto_filtro_diagrama.png

UBICACIÓN: assets/images/seccion_correspondiente/

TAMAÑO MÁXIMO: 1920x1080 px
FORMATO: PNG para diagramas, JPG para fotos
CALIDAD: Mínimo 72 DPI, recomendado 150 DPI

REGLAS:
1. Siempre incluir texto alternativo (alt text)
2. Comprimir imágenes antes de committear
3. Máximo 5 imágenes por archivo markdown
4. Incluir leyenda debajo de cada imagen
```

---

## 4. GUÍA DE MEJORAS POR FASE

### FASE 1: Infraestructura Básica (1-2 días)

#### Tarea 1.1: Crear `.gitignore`
```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
desktop.ini

# Power BI temp files
*.pbix.~
*.pbit.~

# Tools
.qodo/
.mypy_cache/
.pytest_cache/
```

#### Tarea 1.2: Reescribir `README.md`
```markdown
# 📊 Apuntes de Power BI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![Power BI](https://img.shields.io/badge/Power%20BI-Latest-blue.svg)](https://powerbi.microsoft.com)

> **Repositorio profesional de aprendizaje y referencia de Microsoft Power BI.**
> De fundamentos básicos hasta arquitectura empresarial nivel PhD.

---

## 📋 Tabla de Contenidos

### Fundamentos
| # | Módulo | Nivel | Tiempo Est. |
|:-:|--------|:-----:|:-----------:|
| 00 | [Fundamentos Esenciales](00_Fundamentos_Esenciales/) | Básico | 4 horas |
| 01 | [Power Query](01_Alquimia_de_Datos_con_Power_Query/) | Básico-Intermedio | 6 horas |

### Modelado y Análisis
| # | Módulo | Nivel | Tiempo Est. |
|:-:|--------|:-----:|:-----------:|
| 02 | [DAX - Motor de Cálculo](02_El_Corazon_del_Modelo_DAX/) | Intermedio-Avanzado | 10 horas |
| 03 | [Modelo de Datos](03_Arquitectura_del_Modelo_de_Datos/) | Intermedio | 5 horas |

### Visualización y Entrega
| # | Módulo | Nivel | Tiempo Est. |
|:-:|--------|:-----:|:-----------:|
| 04 | [Visualización y Storytelling](04_Visualizacion_y_Storytelling_con_Datos/) | Intermedio | 4 horas |
| 05 | [Power BI Service](05_Power_BI_Service_y_Colaboracion/) | Intermedio | 5 horas |

### Gobernanza y Estrategia
| # | Módulo | Nivel | Tiempo Est. |
|:-:|--------|:-----:|:-----------:|
| 06 | [Gobernanza Empresarial](06_Gobernanza_y_Escalabilidad_Empresarial/) | Avanzado | 6 horas |

### Práctica
| # | Módulo | Nivel | Tiempo Est. |
|:-:|--------|:-----:|:-----------:|
| 07 | [Casos de Estudio](07_Casos_de_Estudio_Completos/) | Todos | 8 horas |
| 08 | [Ejercicios DAX](08_Ejercicios_DAX_Progresivos/) | Progresivo | 12 horas |

---

## 🚀 Inicio Rápido

### Para Estudiantes
1. Clona este repositorio
2. Comienza con el [Módulo 00: Fundamentos](00_Fundamentos_Esenciales/)
3. Avanza secuencialmente循序渐进
4. Practica con los [ejercicios DAX](08_Ejercicios_DAX_Progresivos/)

### Para Profesionales
- Consulta los [casos de estudio](07_Casos_de_Estudio_Completos/) para implementaciones reales
- Revisa la [gobernanza](06_Gobernanza_y_Escalabilidad_Empresarial/) para arquitectura empresarial

---

## 📖 Cómo Usar Este Repositorio

### Estructura
Cada módulo contiene:
- **README.md**: Índice del módulo
- **Archivos numerados**: Contenido temático
- **Glosario**: Términos clave del módulo
- **Ejercicios**: Prácticas progresivas

### Niveles de Dificultad
- 🟢 **Básico**: Sin experiencia previa requerida
- 🟡 **Intermedio**: Conoce fundamentos de Power BI
- 🟠 **Avanzado**: Busca especialización
- 🔴 **Experto**: Nivel arquitecto/consultor

---

## 🤝 Contribuir

Lee las [guías de contribución](CONTRIBUTING.md) para:
- Reportar errores
- Sugerir mejoras
- Agregar ejercicios
- Corregir contenido

---

## 📄 Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).

---

## 📞 Contacto

**Jorge Sislema**
- GitHub: [@tu-usuario](https://github.com/tu-usuario)
- LinkedIn: [tu-linkedin](https://linkedin.com/tu-perfil)
```

#### Tarea 1.3: Eliminar `eje.py`
```bash
git rm eje.py
git commit -m "chore: remove irrelevant script (bank simulation)"
```

#### Tarea 1.4: Completar archivos vacíos
- Generar datos CSV reales para `Datos_Practica/`
- Completar `generar_datos_practica.py`
- Crear READMEs para carpetas vacías

---

### FASE 2: Contenido Faltante (1 semana)

#### Prioridad ALTA
| Archivo | Acción | Líneas Est. |
|---------|--------|:-----------:|
| `02.2_Funciones_DAX_Esenciales/` | Crear subcarpeta + 3 archivos | 600+ |
| `02.3_Patrones_DAX_Avanzados/` | Crear subcarpeta + 3 archivos | 600+ |
| `07_*/data/*.csv` | Generar datos de ejemplo | - |
| `08_*/Datos_Practica/*.csv` | Generar datos de ejemplo | - |

#### Prioridad MEDIA
| Archivo | Acción | Líneas Est. |
|---------|--------|:-----------:|
| `01.3_Transformaciones_Comunes.md` | Crear | 300+ |
| `01.4_Funciones_M_Personalizadas.md` | Crear | 350+ |
| `03.3_Esquemas_Eny_Y.md` | Crear | 250+ |
| `04.3_Diseno_de_Dashboards_Profesionales.md` | Crear | 400+ |
| `05.4_Data_Gateways.md` | Crear | 300+ |
| `09_Referencias_y_Recursos/` | Crear módulo completo | 400+ |

#### Prioridad BAJA
| Archivo | Acción | Líneas Est. |
|---------|--------|:-----------:|
| Glosarios por módulo (02-06) | Crear uno por módulo | 150 c/u |
| READMEs por módulo | Crear uno por módulo | 50 c/u |
| `CHANGELOG.md` | Crear | - |

---

### FASE 3: Contenido Visual (1 semana)

#### Tarea 3.1: Capturas de Pantalla
```
MÍNIMO REQUERIDO POR SECCIÓN:
├── 00_Fundamentos/
│   ├── interfaz_power_bi_desktop.png
│   └── paneles_principales.png
├── 01_Power_Query/
│   ├── editor_power_query.png
│   └── transformaciones_ejemplo.png
├── 02_DAX/
│   ├── calculated_column_vs_measure.png
│   └── context_transition_diagram.png
├── 03_Modelo_Datos/
│   ├── star_schema_diagram.png
│   └── relationship_view.png
├── 04_Visualizacion/
│   ├── chart_types_comparison.png
│   └── color_palette_examples.png
├── 05_Service/
│   ├── workspace_structure.png
│   └── deployment_pipeline.png
└── 06_Gobernanza/
    ├── governance_framework.png
    └── coe_structure.png
```

#### Tarea 3.2: Diagramas
```
CREAR CON draw.io O Mermaid:
1. Arquitectura del ecosistema Power BI
2. Flujo de datos ETL con Power Query
3. Modelo dimensional estrella vs. copo de nieve
4. Flujo de gobernanza empresarial
5. Pipeline de deployment
```

---

### FASE 4: Profesionalización Avanzada (2 semanas)

#### Tarea 4.1: CI/CD con GitHub Actions
```yaml
# .github/workflows/markdown-lint.yml
name: Markdown Lint

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: avto-dev/markdown-lint@v1
        with:
          args: './**/*.md'
```

#### Tarea 4.2: Issue Templates
```markdown
<!-- .github/ISSUE_TEMPLATE/bug_report.md -->
---
name: Reportar Error
about: Reportar un error en el contenido
title: '[ERROR] '
labels: bug
assignees: ''
---

**Sección afectada**
<!-- Ejemplo: 02.1.1_Contexto_de_Filtro.md -->

**Descripción del error**
<!-- Describe qué está mal -->

**Sugerencia de corrección**
<!-- Si tienes la corrección, ingrésala aquí -->
```

#### Tarea 4.3: CHANGELOG
```markdown
# Changelog

Todas las notas de cambio notables a este proyecto se documentarán en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/).

## [1.0.0] - 2026-09-18

### Added
- Estructura inicial del repositorio
- Módulo 00: Fundamentos Esenciales
- Módulo 01: Power Query
- Módulo 02: DAX (parcial)
- Módulo 03: Modelo de Datos
- Módulo 04: Visualización
- Módulo 05: Power BI Service
- Módulo 06: Gobernanza
- Módulo 07: Casos de Estudio
- Módulo 08: Ejercicios DAX
- Licencia MIT
- Guía de contribución

### Fixed
- N/A

### Changed
- N/A

### Removed
- Script irrelevante eje.py
```

---

## 5. PLANTILLAS DE ARCHIVOS

### 5.1 Plantilla de Glosario

```markdown
---
title: "Glosario: Nombre del Módulo"
description: "Definiciones de términos clave del módulo"
---

# Glosario del Módulo XX

> Glosario alfabético de términos técnicos utilizados en este módulo.

---

## A

### **Agregación (Aggregation)**
**Definición:** Proceso de consolidar datos granulares en un nivel superior de resumen.  
**Contexto Power BI:** Tablas de agregación que aceleran consultas al pre-calcular resultados.  
**Ejemplo:** Sumar ventas diarias para obtener ventas mensuales.  
**Ver también:** Tabla de agregación, Granularidad.

---

## B

### **BIs (Business Intelligence)**
**Definición:** Herramientas y procesos para transformar datos en información accionable.  
**Contexto Power BI:** El ecosistema Power BI es una plataforma de BI de Microsoft.  
**Ejemplo:** Dashboards que muestran KPIs de ventas en tiempo real.  
**Ver también:** BI Self-Service, BI Empresarial.

---

## C

### **Contexto de Filtro (Filter Context)**
**Definición:** El conjunto de filtros activos que determinan el resultado de una medida DAX.  
**Contexto Power BI:** Se establece por slicers, filtros de página/informe y relaciones.  
**Ejemplo:** Un slicer de "Año 2024" establece un contexto de filtro.  
**Ver también:** Contexto de fila, Transición de contexto.

---

*Continuar con todas las letras...*
```

### 5.2 Plantilla de Ejercicio DAX

```markdown
---
title: "Ejercicio DAX - Nivel Básico #01"
difficulty: "básico"
estimated_time: "15 minutos"
topic: "SUM, COUNT, AVERAGE"
---

# Ejercicio Dásico #01: Métricas de Ventas

## Contexto del Negocio
Eres analista en **Contoso Retail**. El gerente necesita un reporte de ventas
básico para la reunión trimestral.

## Modelo de Datos
```text
┌─────────────┐     ┌─────────────┐
│  Productos   │────<│    Ventas    │
│─────────────│     │─────────────│
│ ProductoID  │     │ VentaID     │
│ Nombre      │     │ ProductoID  │
│ Categoria   │     │ Fecha       │
│ PrecioUnit  │     │ Cantidad    │
└─────────────┘     │ MontoTotal  │
                    └─────────────┘
```

## Desafíos

### Nivel 1: Calcula el total de ventas
```dax
// Tu solución aquí
TotalVentas = 
```

<details>
<summary>💡 Solución</summary>

```dax
TotalVentas = 
SUM(Ventas[MontoTotal])
```

**Explicación:** `SUM` agrega todos los valores de la columna `MontoTotal`.
</details>

---

### Nivel 2: Cantidad de productos vendidos
```dax
// Tu solución aquí
ProductosVendidos = 
```

<details>
<summary>💡 Solución</summary>

```dax
ProductosVendidos = 
COUNTROWS(Ventas)
```

**Alternativa:**
```dax
ProductosVendidos = 
COUNT(Ventas[VentaID])
```
</details>

---

### Nivel 3: Ticket promedio
```dax
// Tu solución aquí
TicketPromedio = 
```

<details>
<summary>💡 Solución</summary>

```dax
TicketPromedio = 
AVERAGE(Ventas[MontoTotal])
```

**Variante con redondeo:**
```dax
TicketPromedio = 
ROUND(AVERAGE(Ventas[MontoTotal]), 2)
```
</details>

---

## Puntos Clave
- `SUM` agrega valores numéricos
- `COUNTROWS` cuenta filas de una tabla
- `AVERAGE` calcula el promedio aritmético
- Siempre usar `ROUND` para resultados monetarios

## Siguiente Ejercicio → [Ejercicio #02](01_Nivel_Basico/Ejercicio_02.md)
```

### 5.3 Plantilla de Caso de Estudio

```markdown
---
title: "Caso de Estudio: Ventas Retail"
description: "Implementación completa de modelo de datos para retail"
level: "intermedio-avanzado"
estimated_time: "4 horas"
---

# Caso de Estudio: Análisis de Ventas Retail

## 📋 Resumen Ejecutivo

| Campo | Detalle |
|-------|---------|
| **Industria** | Retail / Comercio Minorista |
| **Objetivo** | Dashboard de análisis de ventas multi-ámbito |
| **Datos** | 3 años de transacciones, 50 tiendas, 1,000 productos |
| **Herramientas** | Power BI Desktop + Power BI Service |
| **Nivel** | Intermedio-Avanzado |

---

## 🎯 Objetivos del Proyecto

1. Consolidar datos de ventas de múltiples tiendas
2. Crear modelo dimensional optimizado
3. Desarrollar 25+ medidas DAX de negocio
4. Diseñar dashboard ejecutivo con drill-through
5. Implementar seguridad a nivel de fila (RLS)

---

## 📊 Modelo de Datos

### Diagrama Estrella
```text
                    ┌─────────────────┐
                    │  Dim_Calendario  │
                    │─────────────────│
                    │ FechaPK (PK)    │
                    │ Año             │
                    │ Mes             │
                    │ Trimestre       │
                    │ DiaSemana       │
                    │ EsFinDeSemana   │
                    └────────┬────────┘
                             │
┌─────────────┐    ┌────────┴────────┐    ┌─────────────┐
│ Dim_Tiendas  │───<│  Hecho_Ventas   │>───│ Dim_Productos│
│─────────────│    │─────────────────│    │─────────────│
│ TiendaID(PK)│    │ VentaID (PK)    │    │ ProductoID  │
│ Nombre      │    │ FechaFK (FK)    │    │ Nombre      │
│ Region      │    │ TiendaFK (FK)   │    │ Categoria   │
│ Ciudad      │    │ ProductoFK (FK) │    │ SubCategoria│
│ Gerente     │    │ ClienteFK (FK)  │    │ PrecioUnit  │
└─────────────┘    │ Cantidad        │    │ CostoUnit   │
                   │ MontoTotal      │    └─────────────┘
                   │ CostoTotal      │
                   │ Descuento       │    ┌─────────────┐
                   │ Ganancia        │───<│ Dim_Clientes │
                   └─────────────────┘    │─────────────│
                                          │ ClienteID   │
                                          │ Nombre      │
                                          │ Tipo        │
                                          │ Ciudad      │
                                          └─────────────┘
```

---

## 📐 Especificación de Medidas DAX

### Medidas de Ventas

```dax
// 1. Total de Ventas Brutas
Ventas Brutas = 
SUM(Hecho_Ventas[MontoTotal])

// 2. Total de Descuentos
Total Descuentos = 
SUM(Hecho_Ventas[Descuento])

// 3. Ventas Netas
Ventas Netas = 
[Ventas Brutas] - [Total Descuentos]

// 4. Cantidad Total Vendida
Unidades Vendidas = 
SUM(Hecho_Ventas[Cantidad])

// 5. Ticket Promedio
Ticket Promedio = 
DIVIDE(
    [Ventas Netas],
    DISTINCTCOUNT(Hecho_Ventas[ClienteFK]),
    0
)
```

### Medidas de Rentabilidad

```dax
// 6. Costo Total
Costo Total = 
SUM(Hecho_Ventas[CostoTotal])

// 7. Ganancia Bruta
Ganancia Bruta = 
[Ventas Netas] - [Costo Total]

// 8. Margen de Ganancia %
Margen Ganancia = 
DIVIDE(
    [Ganancia Bruta],
    [Ventas Netas],
    0
)

// 9. ROI
ROI = 
DIVIDE(
    [Ganancia Bruta],
    [Costo Total],
    0
)
```

### Medidas de Time Intelligence

```dax
// 10. Ventas Año Actual (YTD)
Ventas YTD = 
TOTALYTD(
    [Ventas Netas],
    Dim_Calendario[Fecha]
)

// 11. Ventas Mismo Período Año Anterior (PY)
Ventas PY = 
SAMEPERIODLASTYEAR(
    Dim_Calendario[Fecha],
    [Ventas Netas]
)

// 12. Crecimiento YoY %
Crecimiento YoY = 
DIVIDE(
    [Ventas Netas] - [Ventas PY],
    [Ventas PY],
    0
)
```

---

## 📊 Especificación del Dashboard

### Página 1: Vista Ejecutiva
```
┌─────────────────────────────────────────────────────┐
│  📊 Dashboard Ejecutivo - Ventas Retail    [Filtros]│
├─────────────────┬─────────────────┬─────────────────┤
│  💰 Ventas Netas│  📈 Margen %   │  🏪 Tiendas     │
│   $12.5M        │    34.2%        │     48          │
│   ▲ 12% YoY    │    ▲ 2.1pp     │   ▲ 3 vs PY    │
├─────────────────┴─────────────────┴─────────────────┤
│                                                     │
│  ┌─────────────────────┐ ┌─────────────────────┐   │
│  │   Gráfico de Líneas │ │   Gráfico de Barras │   │
│  │   Ventas Mensuales  │ │   Ventas por Región │   │
│  │   vs PY             │ │                     │   │
│  └─────────────────────┘ └─────────────────────┘   │
│                                                     │
│  ┌─────────────────────────────────────────────┐   │
│  │           Tabla Detalle por Tienda           │   │
│  │  Tienda | Ventas | Margen | Crecimiento     │   │
│  └─────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

### Página 2: Análisis por Producto
### Página 3: Análisis por Cliente
### Página 4: Drill-through Tienda

---

## 🔐 Seguridad RLS

```dax
// Regla para Gerentes de Tienda
[EmpleadoID] = LOOKUPVALUE(
    Dim_Tiendas[GerenteID],
    Dim_Tiendas[TiendaID],
    MAX(Hecho_Ventas[TiendaFK])
)
```

---

## 📁 Estructura de Archivos

```
Ventas_Retail/
├── README.md                    ← Este archivo
├── data/
│   ├── dim_calendario.csv
│   ├── dim_tiendas.csv
│   ├── dim_productos.csv
│   ├── dim_clientes.csv
│   └── hecho_ventas.csv
├── dax/
│   ├── medidas_ventas.dax
│   ├── medidas_rentabilidad.dax
│   └── medidas_time_intelligence.dax
├── report/
│   ├── dashboard_spec.md
│   └── layout_mockup.png
└── pbix/
    └── retail_analysis.pbix    ← Archivo Power BI
```

---

## 🎓 Aprendizajes Clave

1. **Modelado dimensional** es fundamental para rendimiento
2. **DIVIDE** es más seguro que operador `/` para evitar división por cero
3. **Variables (VAR)** mejoran rendimiento y legibilidad
4. **RLS** permite seguridad a nivel de fila sin duplicar reportes
5. **Agregaciones** aceleran consultas en modelos grandes
```

---

## 6. GESTIÓN DE DATOS DE EJEMPLO

### 6.1 Generador de Datos de Práctica

```python
#!/usr/bin/env python3
"""
generar_datos_practica.py
Genera datos de ejemplo para ejercicios DAX del repositorio.

Uso: python generar_datos_practica.py
Salida: Archivos CSV en la carpeta Datos_Practica/
"""

import csv
import random
from datetime import datetime, timedelta

# Configuración
NUM_CLIENTES = 500
NUM_PRODUCTOS = 100
NUM_VENDEDORES = 25
NUM_VENTAS = 5000
FECHA_INICIO = datetime(2022, 1, 1)
FECHA_FIN = datetime(2024, 12, 31)

# Categorías de productos
CATEGORIAS = {
    "Electrónica": ["Smartphone", "Laptop", "Tablet", "Audífonos", "Monitor"],
    "Ropa": ["Camisa", "Pantalón", "Zapatos", "Chaqueta", "Gorra"],
    "Hogar": ["Sofá", "Mesa", "Silla", "Lámpara", "Alfombra"],
    "Deportes": ["Balón", "Raqueta", "Bicicleta", "Pesas", "Cinta"],
    "Alimentos": ["Café", "Chocolate", "Galletas", "Aceite", "Arroz"]
}

def generar_clientes():
    """Genera archivo clientes.csv"""
    nombres = ["Juan", "María", "Carlos", "Ana", "Pedro", "Laura", 
               "Miguel", "Sofía", "Antonio", "Isabel", "Francisco", "Carmen"]
    apellidos = ["García", "López", "Martínez", "González", "Rodríguez",
                 "Fernández", "Pérez", "Sánchez", "Ramírez", "Torres"]
    ciudades = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao",
                "Málaga", "Zaragoza", "Murcia", "Palma", "Las Palmas"]
    tipos = ["Regular", "Premium", "VIP"]
    
    with open('clientes.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ClienteID', 'Nombre', 'Apellido', 'Email', 
                         'Ciudad', 'TipoCliente', 'FechaRegistro'])
        
        for i in range(1, NUM_CLIENTES + 1):
            nombre = random.choice(nombres)
            apellido = random.choice(apellidos)
            email = f"{nombre.lower()}.{apellido.lower()}{i}@email.com"
            ciudad = random.choice(ciudades)
            tipo = random.choices(tipos, weights=[70, 25, 5])[0]
            fecha_reg = FECHA_INICIO + timedelta(days=random.randint(0, 365))
            
            writer.writerow([i, nombre, apellido, email, ciudad, 
                           tipo, fecha_reg.strftime('%Y-%m-%d')])
    
    print(f"✅ clientes.csv generado: {NUM_CLIENTES} registros")

def generar_productos():
    """Genera archivo productos.csv"""
    with open('productos.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ProductoID', 'Nombre', 'Categoria', 'SubCategoria',
                         'PrecioUnitario', 'CostoUnitario', 'Stock'])
        
        prod_id = 1
        for cat, subcats in CATEGORIAS.items():
            for subcat in subcats:
                for variant in range(1, 3):  # 2 variantes por subcategoría
                    precio = round(random.uniform(10, 500), 2)
                    costo = round(precio * random.uniform(0.4, 0.7), 2)
                    stock = random.randint(10, 500)
                    
                    writer.writerow([prod_id, f"{subcat} {variant}", cat, subcat,
                                   precio, costo, stock])
                    prod_id += 1
    
    print(f"✅ productos.csv generado: {prod_id - 1} registros")

def generar_vendedores():
    """Genera archivo vendedores.csv"""
    nombres = ["Roberto", "Elena", "Fernando", "Lucía", "Andrés",
               "Marta", "Javier", "Paula", "Diego", "Nuria"]
    apellidos = ["Álvarez", "Romero", "Navarro", "Domínguez", "Vidal",
                 "Castro", "Ortega", "Molina", "Reyes", "Serrano"]
    regiones = ["Norte", "Sur", "Este", "Oeste", "Centro"]
    
    with open('vendedores.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['VendedorID', 'Nombre', 'Apellido', 'Region',
                         'FechaIngreso', 'ComisionPorcentaje'])
        
        for i in range(1, NUM_VENDEDORES + 1):
            nombre = random.choice(nombres)
            apellido = random.choice(apellidos)
            region = random.choice(regiones)
            fecha_ing = FECHA_INICIO + timedelta(days=random.randint(0, 730))
            comision = round(random.uniform(0.05, 0.15), 2)
            
            writer.writerow([i, nombre, apellido, region,
                           fecha_ing.strftime('%Y-%m-%d'), comision])
    
    print(f"✅ vendedores.csv generado: {NUM_VENDEDORES} registros")

def generar_ventas():
    """Genera archivo ventas.csv"""
    with open('ventas.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['VentaID', 'Fecha', 'ClienteID', 'VendedorID',
                         'ProductoID', 'Cantidad', 'DescuentoPorcentaje',
                         'MontoTotal', 'Estado'])
        
        estados = ["Completada", "Completada", "Completada", "Completada",
                   "Cancelada", "Pendiente"]  # 66% completadas
        
        for i in range(1, NUM_VENTAS + 1):
            fecha = FECHA_INICIO + timedelta(days=random.randint(0, 1095))
            cliente = random.randint(1, NUM_CLIENTES)
            vendedor = random.randint(1, NUM_VENDEDORES)
            producto = random.randint(1, NUM_PRODUCTOS)
            cantidad = random.randint(1, 10)
            descuento = random.choices([0, 5, 10, 15, 20], 
                                       weights=[40, 25, 20, 10, 5])[0]
            monto_base = round(random.uniform(20, 2000), 2)
            monto_total = round(monto_base * cantidad * (1 - descuento/100), 2)
            estado = random.choice(estados)
            
            writer.writerow([i, fecha.strftime('%Y-%m-%d'), cliente, vendedor,
                           producto, cantidad, descuento, monto_total, estado])
    
    print(f"✅ ventas.csv generado: {NUM_VENTAS} registros")

if __name__ == "__main__":
    print("🚀 Generando datos de práctica...\n")
    random.seed(42)  # Reproducibilidad
    
    generar_clientes()
    generar_productos()
    generar_vendedores()
    generar_ventas()
    
    print(f"\n✨ ¡Datos generados exitosamente!")
    print(f"📁 Archivos creados en: {__file__.replace('generar_datos_practica.py', '')}")
```

### 6.2 Validación de Datos Generados

```python
#!/usr/bin/env python3
"""
validar_datos.py
Valida la integridad de los datos generados.
"""

import csv
import os

def validar_archivo(nombre_archivo, columnas_esperadas):
    """Valida que un archivo CSV tenga la estructura correcta."""
    print(f"\n📋 Validando {nombre_archivo}...")
    
    if not os.path.exists(nombre_archivo):
        print(f"  ❌ Archivo no encontrado")
        return False
    
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        
        # Validar columnas
        if headers != columnas_esperadas:
            print(f"  ❌ Columnas incorrectas")
            print(f"     Esperadas: {columnas_esperadas}")
            print(f"     Encontradas: {headers}")
            return False
        
        # Contar filas
        num_filas = sum(1 for _ in reader)
        
        # Validar no vacío
        if num_filas == 0:
            print(f"  ❌ Archivo vacío")
            return False
        
        print(f"  ✅ Válido: {num_filas} registros, {len(headers)} columnas")
        return True

if __name__ == "__main__":
    print("🔍 VALIDACIÓN DE DATOS DE PRÁCTICA\n")
    
    archivos = {
        'clientes.csv': ['ClienteID', 'Nombre', 'Apellido', 'Email',
                         'Ciudad', 'TipoCliente', 'FechaRegistro'],
        'productos.csv': ['ProductoID', 'Nombre', 'Categoria', 'SubCategoria',
                          'PrecioUnitario', 'CostoUnitario', 'Stock'],
        'vendedores.csv': ['VendedorID', 'Nombre', 'Apellido', 'Region',
                           'FechaIngreso', 'ComisionPorcentaje'],
        'ventas.csv': ['VentaID', 'Fecha', 'ClienteID', 'VendedorID',
                       'ProductoID', 'Cantidad', 'DescuentoPorcentaje',
                       'MontoTotal', 'Estado']
    }
    
    todos_validos = True
    for archivo, columnas in archivos.items():
        if not validar_archivo(archivo, columnas):
            todos_validos = False
    
    print("\n" + "="*50)
    if todos_validos:
        print("✨ ¡Todos los archivos son válidos!")
    else:
        print("⚠️  Algunos archivos tienen problemas")
```

---

## 7. AUTOMATIZACIÓN Y CICD

### 7.1 GitHub Actions - Markdown Lint

```yaml
# .github/workflows/markdown-lint.yml
name: Markdown Quality Check

on:
  push:
    branches: [main, develop]
    paths: ['**/*.md']
  pull_request:
    branches: [main]
    paths: ['**/*.md']

jobs:
  lint:
    name: Markdown Lint
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
      
      - name: Install markdownlint
        run: npm install -g markdownlint-cli
      
      - name: Run markdownlint
        run: markdownlint '**/*.md' --config .markdownlint.json
```

### 7.2 Configuración Markdownlint

```json
{
  "default": true,
  "MD013": { "line_length": 120 },
  "MD033": false,
  "MD041": false,
  "MD024": { "siblings_only": true }
}
```

### 7.3 GitHub Actions - Spell Check

```yaml
# .github/workflows/spell-check.yml
name: Spell Check

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  spell:
    name: Spell Check
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Check spelling
        uses: streetsidesoftware/cspell-action@v4
        with:
          files: '**/*.md'
          config: cspell.json
```

---

## 8. GLOSARIO PROFESIONAL

### Glosario General de Power BI

| Término | Definición | Contexto |
|---------|------------|----------|
| **Agregación** | Consolidación de datos granulares a un nivel superior | Tablas de agregación en Power BI |
| **BI (Business Intelligence)** | Tecnologías y prácticas para el análisis de datos | El dominio general de Power BI |
| **Cardinalidad** | Número de elementos en un conjunto de datos | Relaciones: one-to-one, one-to-many |
| **Calculation Group** | Grupo de elementos de cálculo reutilizables | Tabular Editor, TMDL |
| **Calculated Column** | Columna calculada con DAX en el modelo | Tabla, no medida |
| **COE (Center of Excellence)** | Centro de excelencia en datos | Gobernanza empresarial |
| **Contexto de Filtro** | Filtros activos que afectan el resultado de una medida | DAX fundamental |
| **Contexto de Fila** | Valores de la fila actual en una expresión DAX | Iteradores como SUMX |
| **DAX (Data Analysis Expressions)** | Lenguaje de fórmulas para análisis de datos | Motor de cálculo de Power BI |
| **Data Gateway** | Puente de conexión entre servicios locales y cloud | Power BI Service |
| **DirectQuery** | Modo de conexión en tiempo real sin importar datos | Optimización de rendimiento |
| **Drill-through** | Navegación de datos de resumen a detalle | Funcionalidad de informes |
| **Embedding** | Integración de reportes en aplicaciones | Power BI Embedded |
| **ETL (Extract, Transform, Load)** | Proceso de extracción y carga de datos | Power Query |
| **Frankenstein** | Modelo compuesto por múltiples orígenes | Composite models |
| **Itersum** | Funciones DAX que iteran fila por fila | SUMX, AVERAGEX, COUNTAX |
| **KPI (Key Performance Indicator)** | Indicador clave de rendimiento | Métricas de negocio |
| **Measure** | Cálculo DAX que se evalúa en tiempo de consulta | DAX |
| **M (Power Query)** | Lenguaje de programación de Power Query | ETL |
| **Metadata** | Datos sobre datos (estructura, tipos, etc.) | Modelo tabular |
| **MFA (Multi-Factor Auth)** | Autenticación de múltiples factores | Seguridad |
| **Natural Language Query** | Consulta en lenguaje natural (Q&A) | Power BI Service |
| **Optimización** | Mejora del rendimiento del modelo | Best practices |
| **Parquet** | Formato de almacenamiento columnar | Lakehouse, Data Lake |
| **Power BI Embedded** | Incorporación de reportes en aplicaciones | API REST |
| **Power Query** | Herramienta de ETL integrada en Power BI | Transformación de datos |
| **PPU (Premium Per User)** | Licencia Premium por usuario | Licensing |
| **Pro** | Licencia estándar de Power BI | Licensing |
| **Q&A** | Preguntas y respuestas en lenguaje natural | AI en Power BI |
| **RLS (Row-Level Security)** | Seguridad a nivel de fila | Seguridad |
| **Star Schema** | Esquema dimensional con tabla de hechos central | Modelado |
| **TMDL (Tabular Model Definition Language)** | Lenguaje de definición del modelo tabular | Nueva alternativa a .bim |
| **TMSL (Tabular Model Scripting Language)** | Lenguaje de scripting del modelo tabular | JSON-based |
| **VertiPaq** | Motor de almacenamiento columnar de Analysis Services | Compresión de datos |
| **What-If Parameter** | Parámetro de análisis hipotético | Simulación |
| **Workspace** | Área de trabajo en Power BI Service | Colaboración |
| **XMLA** | XML for Analysis, protocolo de acceso al modelo | Conectividad |

### Glosario de Funciones DAX

| Función | Categoría | Descripción |
|---------|-----------|-------------|
| `CALCULATE` | Filter | Evalúa una expresión en un contexto de filtro modificado |
| `FILTER` | Filter | Devuelve una tabla filtrada |
| `ALL` | Filter | Elimina filtros de un objeto |
| `ALLEXCEPT` | Filter | Elimina todos los filtros excepto los especificados |
| `SUM` | Aggregation | Suma una columna |
| `AVERAGE` | Aggregation | Promedio de una columna |
| `COUNTROWS` | Aggregation | Cuenta filas de una tabla |
| `DISTINCTCOUNT` | Aggregation | Cuenta valores únicos |
| `SUMX` | Iterator | Suma evaluando expresión fila por fila |
| `AVERAGEX` | Iterator | Promedio evaluando expresión fila por fila |
| `TOTALYTD` | Time Intelligence | Acumulado en el año |
| `SAMEPERIODLASTYEAR` | Time Intelligence | Mismo período año anterior |
| `DATESYTD` | Time Intelligence | Fechas del año actual |
| `CALCULATETABLE` | Filter | Devuelve tabla con filtro modificado |
| `RELATED` | Relation | Accede a columna de tabla relacionada |
| `RELATEDTABLE` | Relation | Devuelve tabla relacionada |
| `VALUES` | Table | Devuelve valores únicos de una columna |
| `DISTINCT` | Table | Valores únicos (sin duplicados) |
| `UNION` | Table | Combina tablas |
| `SELECTCOLUMNS` | Table | Selecciona y renombra columnas |
| `DIVIDE` | Math | División segura (maneja división por cero) |
| `ROUND` | Math | Redondea un número |
| `FORMAT` | Text | Formatea un valor como texto |
| `IF` | Logical | Evaluación condicional |
| `SWITCH` | Logical | Selección basada en valores |
| `VAR` | Variable | Define variables para cálculos complejos |
| `RETURN` | Variable | Retorna resultado de una expresión con VAR |

### Glosario de Power Query (M)

| Función | Categoría | Descripción |
|---------|-----------|-------------|
| `Table.AddColumn` | Tabla | Agrega nueva columna calculada |
| `Table.TransformColumns` | Tabla | Transforma columnas existentes |
| `Table.FilterRows` | Tabla | Filtra filas por condición |
| `Table.Group` | Tabla | Agrupa filas por columna(s) |
| `Table.Join` | Tabla | Une dos tablas (INNER, LEFT, etc.) |
| `Table.MergeQueries` | Tabla | Fusiona consultas |
| `Table.Pivot` | Tabla | Convierte filas en columnas |
| `Table.Unpivot` | Tabla | Convierte columnas en filas |
| `Table.Sort` | Tabla | Ordena filas |
| `Table.Distinct` | Tabla | Elimina duplicados |
| `Table.SelectColumns` | Tabla | Selecciona columnas específicas |
| `Table.RenameColumns` | Tabla | Renombra columnas |
| `Table.ReorderColumns` | Tabla | Reordena columnas |
| `Text.Trim` | Texto | Elimina espacios en blanco |
| `Text.Lower` | Texto | Convierte a minúsculas |
| `Text.Upper` | Texto | Convierte a mayúsculas |
| `Text.Proper` | Texto | Primera letra mayúscula |
| `Date.From` | Fecha | Convierte a fecha |
| `DateTime.LocalNow` | Fecha | Fecha y hora actual |
| `Number.Round` | Número | Redondea un número |
| `Number.IntegerDivide` | Número | División entera |
| `Record.Field` | Registro | Accede a campo de registro |
| `Record.HasFields` | Registro | Verifica existencia de campo |

---

## 9. EJEMPLOS PRÁCTICOS

### 9.1 Ejemplo: Medida DAX Completa

```dax
// ============================================================
// MEDIDA: Ventas Netas por Categoría (con manejo de errores)
// ============================================================
// Autor: Jorge Sislema
// Fecha: 2026-09-18
// Versión: 1.0
// Descripción: Calcula ventas netas agrupadas por categoría,
//              manejando división por cero y valores nulos.
// ============================================================

Ventas Netas por Categoria = 
VAR VentasBrutas = 
    CALCULATE(
        SUM(Hecho_Ventas[MontoTotal]),
        NOT ISBLANK(Hecho_Ventas[MontoTotal])
    )

VAR TotalDescuentos = 
    CALCULATE(
        SUM(Hecho_Ventas[Descuento]),
        NOT ISBLANK(Hecho_Ventas[Descuento])
    )

VAR VentasNetas = 
    VentasBrutas - TotalDescuentos

VAR Resultado = 
    IF(
        ISBLANK(VentasNetas),
        0,
        VentasNetas
    )

RETURN
    Resultado
```

### 9.2 Ejemplo: Transformación Power Query (M)

```m
// ============================================================
// TRANSFORMACIÓN: Limpieza y estandarización de datos de clientes
// ============================================================
// Propósito: Limpiar nombres, estandarizar ciudades y validar emails
// ============================================================

let
    // 1. Fuente de datos
    Fuente = Excel.Workbook(File.Contents("clientes.xlsx"), null, true),
    HojaClientes = Fuente{[Name="Clientes"]}[Data],
    
    // 2. Promover encabezados
    EncabezadosPromovidos = Table.PromoteHeaders(HojaClientes, [PromoteAllScalars=true]),
    
    // 3. Establecer tipos de datos
    TiposCambiados = Table.TransformColumnTypes(EncabezadosPromovidos, {
        {"ClienteID", Int64.Type},
        {"Nombre", type text},
        {"Apellido", type text},
        {"Email", type text},
        {"Ciudad", type text},
        {"FechaRegistro", type date}
    }),
    
    // 4. Limpiar nombres (trim + proper case)
    NombreLimpio = Table.TransformColumns(TiposCambiados, {
        {"Nombre", each Text.Proper(Text.Trim(_)), type text},
        {"Apellido", each Text.Proper(Text.Trim(_)), type text}
    }),
    
    // 5. Estandarizar ciudades
    CiudadEstandarizada = Table.TransformColumns(NombreLimpio, {
        {"Ciudad", each 
            let
                ciudadLimpia = Text.Trim(Text.Proper(_)),
                reemplazos = [
                    {"Madrd", "Madrid"},
                    {"Brcelona", "Barcelona"},
                    {"Valncia", "Valencia"}
                ]
            in
                List.Accumulate(reemplazos, ciudadLimpia, 
                    (estado, reemplazo) => Text.Replace(estado, reemplazo{0}, reemplazo{1}))
        , type text}
    }),
    
    // 6. Validar formato de email
    EmailValido = Table.AddColumn(CiudadEstandarizada, "EmailValido", each
        let
            email = [Email],
            tieneArroba = Text.Contains(email, "@"),
            tienePunto = Text.Contains(email, "."),
            longitudValida = Text.Length(email) > 5
        in
            tieneArroba and tienePunto and longitudValida,
        type logical
    ),
    
    // 7. Filtrar solo emails válidos
    Filtrados = Table.SelectRows(EmailValido, each [EmailValido] = true),
    
    // 8. Eliminar columna auxiliar
    Resultado = Table.RemoveColumns(Filtrados, {"EmailValido"})
in
    Resultado
```

### 9.3 Ejemplo: Script de Creación de Modelo

```bim
{
  "name": "Retail_Analysis",
  "compatibilityLevel": 1567,
  "model": {
    "culture": "es-ES",
    "tables": [
      {
        "name": "Dim_Calendario",
        "columns": [
          {
            "name": "FechaPK",
            "dataType": "dateTime",
            "isKey": true,
            "formatString": "dd/MM/yyyy"
          },
          {
            "name": "Año",
            "dataType": "int64"
          },
          {
            "name": "Mes",
            "dataType": "int64"
          },
          {
            "name": "NombreMes",
            "dataType": "string"
          },
          {
            "name": "Trimestre",
            "dataType": "string"
          }
        ]
      },
      {
        "name": "Hecho_Ventas",
        "columns": [
          {
            "name": "VentaID",
            "dataType": "int64",
            "isKey": true
          },
          {
            "name": "MontoTotal",
            "dataType": "decimal",
            "formatString": "#,##0.00 €"
          }
        ],
        "measures": [
          {
            "name": "Ventas Netas",
            "expression": "SUM(Hecho_Ventas[MontoTotal]) - SUM(Hecho_Ventas[Descuento])",
            "formatString": "#,##0.00 €"
          }
        ]
      }
    ],
    "relationships": [
      {
        "name": "Calendario_Ventas",
        "fromTable": "Dim_Calendario",
        "fromColumn": "FechaPK",
        "toTable": "Hecho_Ventas",
        "toColumn": "FechaFK",
        "cardinality": "oneToMany",
        "crossFilteringBehavior": "oneDirection"
      }
    ]
  }
}
```

---

## 10. CHECKLIST DE CALIDAD

### Checklist Pre-Commit

```markdown
## Checklist de Calidad - Antes de cada Commit

### Infraestructura
- [ ] .gitignore existe y está actualizado
- [ ] No hay archivos temporales (.tmp, .bak, .swp)
- [ ] No hay carpetas de caché (__pycache__, .mypy_cache)
- [ ] No hay archivos de IDE (.vscode, .idea)

### Contenido
- [ ] Markdown sin errores de ortografía
- [ ] Bloques de código con tag de lenguaje correcto
- [ ] Tablas bien formateadas y alineadas
- [ ] Imágenes con texto alternativo (alt text)
- [ ] Enlaces internos funcionales
- [ ] Numeración secuencial correcta

### Técnico
- [ ] Código DAX sintácticamente correcto
- [ ] Código M (Power Query) válido
- [ ] Datos de ejemplo coherentes y sin duplicados
- [ ] Scripts Python ejecutables sin errores

### Metadatos
- [ ] Frontmatter completo (title, description, date, tags)
- [ ] Fecha en formato YYYY-MM-DD
- [ ] Tags relevantes incluidos
- [ ] Nivel de dificultad especificado

### Profesionalismo
- [ ] Lenguaje técnico preciso
- [ ] Ejemplos contextualizados en negocio
- [ ] Glosario actualizado
- [ ] Referencias a documentación oficial
```

### Checklist de Pull Request

```markdown
## Checklist de Pull Request

### Contenido
- [ ] Nuevo archivo sigue la plantilla establecida
- [ ] Numeración correcta sin duplicados
- [ ] Glosario de la sección incluido
- [ ] Al menos un ejemplo práctico

### Calidad
- [ ] Sin errores de markdown (markdownlint pasa)
- [ ] Sin errores de ortografía (cspell pasa)
- [ ] Imágenes comprimidas (< 500KB c/u)
- [ ] Datos de ejemplo generados y validados

### Documentación
- [ ] README del módulo actualizado
- [ ] CHANGELOG actualizado si es cambio mayor
- [ ] Descripción clara del PR
```

---

## APÉNDICE A: Recursos Recomendados

### Documentación Oficial
- [Power BI Documentation](https://docs.microsoft.com/power-bi/)
- [DAX Reference](https://docs.microsoft.com/dax/)
- [Power Query M Reference](https://docs.microsoft.com/powerquery-m/)
- [Tabular Editor Documentation](https://docs.tabulareditor.com/)

### Comunidades
- [Power BI Community](https://community.powerbi.com/)
- [DAX Patterns](https://www.daxpatterns.com/)
- [SQLBI](https://www.sqlbi.com/)
- [Guy in a Cube](https://guyinacube.com/)

### Certificaciones
- **PL-300**: Microsoft Power BI Data Analyst Associate
- **DP-500**: Azure Enterprise Data Analyst Associate
- **PL-900**: Microsoft Power Platform Fundamentals

---

## APÉNDICE B: Comandos Útiles

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/Apuntes_de_power_BI.git

# Generar datos de práctica
cd Apuntes_de_power_BI/08_Ejercicios_DAX_Progresivos/Datos_Practica
python generar_datos_practica.py

# Validar datos generados
python validar_datos.py

# Ejecutar markdownlint
markdownlint '**/*.md'

# Ver estadísticas del repositorio
find . -name "*.md" | xargs wc -l | tail -1
```

---

**FIN DEL MANUAL**

*Este documento es vivo y debe actualizarse conforme evolucione el repositorio.*
*Última actualización: 18 de Septiembre, 2026*
