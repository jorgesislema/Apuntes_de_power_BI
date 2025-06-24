# Glosario de Power Query

## A

**Applied Steps (Pasos Aplicados)**
Secuencia de transformaciones que se aplican a los datos en orden cronológico, cada una construyendo sobre la anterior.

**Anonymous Function (Función Anónima)**
Función sin nombre definida inline usando la sintaxis `(parámetros) => expresión` en lenguaje M.

## B

**Blank**
Valor especial en Power Query que representa la ausencia de datos, diferente de null o cero.

**Binary**
Tipo de datos que representa archivos o contenido binario, como imágenes o documentos.

## C

**Connector (Conector)**
Componente que permite a Power Query conectarse a fuentes de datos específicas con configuraciones optimizadas.

**Custom Column (Columna Personalizada)**
Nueva columna creada usando fórmulas M personalizadas para calcular valores basados en otras columnas.

**Custom Function (Función Personalizada)**
Función reutilizable definida por el usuario que puede ser invocada desde múltiples consultas.

## D

**Data Privacy Levels (Niveles de Privacidad de Datos)**
Configuración de seguridad que controla cómo Power Query puede combinar datos de diferentes fuentes.

**Data Profiling (Perfilado de Datos)**
Análisis automático de la calidad, distribución y características de los datos en las columnas.

**Data Types (Tipos de Datos)**
Clasificación de datos en categorías como texto, número, fecha, booleano, etc., que determina las operaciones disponibles.

**DirectQuery**
Modo de conectividad que consulta datos directamente en la fuente sin importarlos al modelo de Power BI.

## E

**Each**
Palabra clave en M que representa el registro actual en operaciones de iteración sobre tablas.

**Error Handling (Manejo de Errores)**
Técnicas para detectar, capturar y manejar errores que pueden ocurrir durante las transformaciones de datos.

**ETL (Extract, Transform, Load)**
Proceso de extracción, transformación y carga de datos que Power Query facilita con su interfaz visual.

## F

**Function (Función)**
Bloque de código reutilizable que acepta parámetros y retorna un valor, fundamental en el lenguaje M.

**Fuzzy Matching (Coincidencia Difusa)**
Técnica para encontrar coincidencias aproximadas entre texto, útil para combinar datos con pequeñas variaciones.

## G

**Gateway**
Componente que actúa como puente entre Power BI Service y fuentes de datos on-premises.

**Group By (Agrupar Por)**
Operación que organiza filas en grupos basados en valores comunes y permite aplicar agregaciones.

## I

**Import Mode (Modo Importación)**
Modo de almacenamiento donde los datos se cargan completamente en el modelo de Power BI.

**Incremental Refresh (Actualización Incremental)**
Técnica para actualizar solo los datos nuevos o modificados, mejorando el rendimiento de las actualizaciones.

## J

**Join**
Operación para combinar datos de dos tablas basado en columnas relacionadas.

**JSON (JavaScript Object Notation)**
Formato de intercambio de datos basado en texto que Power Query puede parsear y transformar.

## K

**Key (Clave)**
Columna o conjunto de columnas que identifican únicamente cada fila en una tabla.

## L

**Let Expression (Expresión Let)**
Estructura fundamental del lenguaje M que permite definir variables locales y construir consultas paso a paso.

**List**
Tipo de datos en M que representa una secuencia ordenada de valores del mismo tipo.

## M

**M Language (Lenguaje M)**
Lenguaje funcional de fórmulas utilizado por Power Query para definir transformaciones de datos.

**Merge**
Operación para combinar tablas basada en columnas relacionadas, similar a JOIN en SQL.

**Metadata (Metadatos)**
Información sobre la estructura, tipos y propiedades de los datos, mantenida por Power Query.

## N

**Null**
Valor que representa la ausencia de datos o un valor desconocido en Power Query.

**Native Query (Consulta Nativa)**
Consulta en el lenguaje específico de la fuente de datos (como SQL) que se puede ejecutar directamente.

## O

**OData**
Protocolo estándar para crear y consumir APIs REST que Power Query soporta nativamente.

## P

**Parameter (Parámetro)**
Variable configurable que permite personalizar el comportamiento de consultas y funciones.

**Pivot/Unpivot**
Operaciones para transformar la estructura de datos entre formato ancho y largo.

**Preview (Vista Previa)**
Muestra limitada de datos que Power Query utiliza para mostrar resultados durante el desarrollo.

## Q

**Query**
Conjunto de pasos de transformación que definen cómo obtener y procesar datos de una fuente.

**Query Diagnostics (Diagnósticos de Consulta)**
Herramienta para analizar el rendimiento y comportamiento de las consultas de Power Query.

**Query Folding**
Optimización donde Power Query traduce transformaciones al lenguaje nativo de la fuente de datos.

## R

**Record**
Tipo de datos en M que representa una colección de campos con nombre, similar a una fila en una tabla.

**Refresh (Actualización)**
Proceso de volver a ejecutar las consultas para obtener datos actualizados de las fuentes.

**Reference (Referencia)**
Tipo de consulta que apunta a otra consulta existente, creando una dependencia.

## S

**Schema**
Estructura que define los nombres de columnas, tipos de datos y metadatos de una tabla.

**Source (Origen)**
Primer paso en cualquier consulta que define la conexión a la fuente de datos original.

**Split Column (Dividir Columna)**
Operación para separar una columna en múltiples columnas basado en delimitadores o posiciones.

## T

**Table**
Tipo de datos fundamental en Power Query que representa datos estructurados en filas y columnas.

**Transform (Transformar)**
Proceso de modificar la estructura, formato o contenido de los datos.

**Type System (Sistema de Tipos)**
Marco que define y maneja los diferentes tipos de datos disponibles en Power Query.

## U

**Union**
Operación para combinar filas de múltiples tablas con estructura similar.

**Unpivot**
Transformación que convierte columnas en filas, cambiando de formato ancho a formato largo.

## V

**Value**
Unidad fundamental de datos en M que puede ser de cualquier tipo soportado.

**Variable**
Nombre que almacena un valor o resultado intermedio en una expresión let.

## W

**Web API**
Interfaz de programación de aplicaciones accesible vía web que Power Query puede consumir.

**Worksheet**
Hoja individual dentro de un libro de Excel que puede ser referenciada como fuente de datos.

## X

**XML (eXtensible Markup Language)**
Formato de marcado que Power Query puede parsear y transformar en datos tabulares.

---

## Convenciones del Lenguaje M

### Sintaxis Básica
```m
// Comentario de línea
/* Comentario de bloque */

// Identificadores
Variable1
'Nombre con espacios'
#"Nombre con caracteres especiales"

// Literales
"texto"          // Text
123              // Number  
true             // Logical
#date(2024,1,15) // Date
null             // Null
```

### Operadores Comunes
```m
+   // Suma/concatenación
-   // Resta
*   // Multiplicación  
/   // División
&   // Concatenación de texto
=   // Igualdad
<>  // Desigualdad
<   // Menor que
>   // Mayor que
and // Y lógico
or  // O lógico
not // No lógico
```

### Funciones Frecuentes
- **Table.SelectColumns()**: Seleccionar columnas específicas
- **Table.FilterRows()**: Filtrar filas
- **Table.TransformColumns()**: Transformar columnas
- **Table.AddColumn()**: Agregar nueva columna
- **Text.Split()**: Dividir texto
- **Date.Year()**: Extraer año de fecha
- **Number.Round()**: Redondear números

---

**Nota:** Este glosario se actualiza periódicamente para incluir nuevos términos que emergen con las actualizaciones de Power Query y el ecosistema de Microsoft Power Platform.
