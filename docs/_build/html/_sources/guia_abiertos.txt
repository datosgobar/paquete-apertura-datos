# Guía para la publicación de datos en formatos abiertos

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

## Indice

- [Introducción](#introduccion)
- [Objetivo de la guía](#objetivo-de-la-guia)
- [Formatos abiertos de archivos](#formatos-abiertos-de-archivos)
  - [CSV](#csv)
  - [JSON](#json)
- [Fragmentación de archivos](#fragmentacion-de-archivos)
- [Nomenclatura de archivos](#nomenclatura-de-archivos)
- [Codificación](#codificacion)
- [Estructura y características de los datos tabulares](#estructura-y-caracteristicas-de-los-datos-tabulares)
  - [Recomendaciones generales](#recomendaciones-generales)
    - [Nomenclatura de los campos (nombres de las columnas)](#nomenclatura-de-los-campos-nombres-de-las-columnas)
    - [Nivel de granularidad de los datos](#nivel-de-granularidad-de-los-datos)
    - [Usar orientación vertical en lugar de horizontal](#usar-orientacion-vertical-en-lugar-de-horizontal)
    - [Incluir sólo un atributo por campo](#incluir-solo-un-atributo-por-campo)
    - [Valores nulos, desconocidos o en blanco en campos numéricos](#valores-nulos-desconocidos-o-en-blanco-en-campos-numericos)
  - [Recomendaciones para estructurar planillas de cálculo](#recomendaciones-para-estructurar-planillas-de-calculo)
    - [Usar celdas simples](#usar-celdas-simples)
    - [Fila de encabezado](#fila-de-encabezado)
    - [Celdas vacías en filas para agrupar conceptos](#celdas-vacias-en-filas-para-agrupar-conceptos)
    - [Formato de celdas](#formato-de-celdas)
  - [Exportación a CSV](#exportacion-a-csv)
- [Estándares según el tipo de Datos](#estandares-segun-el-tipo-de-datos)
  - [Texto](#texto)
    - [Entidades](#entidades)
    - [Nombres propios](#nombres-propios)
    - [Siglas](#siglas)
  - [Número](#numero)
    - [Moneda](#moneda)
    - [Números telefónicos](#numeros-telefonicos)
    - [Coordenadas](#coordenadas)
  - [Tiempo](#tiempo)
    - [Rangos horarios](#rangos-horarios)
  - [Booleano](#booleano)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Introducción

Esta guía busca ayudar a los organismos a instrumentar la Política de Datos Abiertos impulsada desde el Gobierno de la Nación Argentina, a través del Decreto N° 117/2016 del 12 de enero de 2016.

## Objetivo de la guía

Esta es **una guía de buenas prácticas para la publicación de datos en formatos abiertos.**

Estas recomendaciones se basan en:

* Estándares usados a nivel nacional e internacional.

* La experiencia de trabajo del equipo de la Dirección Nacional de Datos e Información Pública del Ministerio de Modernización de la Nación.

Esta es **una guía colaborativa y en progreso**. Valoramos, y alentamos, a organizaciones y ciudadanos a plantear ideas, sugerencias, y comentarios que nos ayuden a crear un mejor documento.

El documento se estructura así:

**Formatos abiertos de archivos:** cuáles son los formatos más usuales en los que se publican datos y cuáles son los más recomendables.

* **Fragmentación de archivos**: cuáles son los criterios para decidir que un archivo es demasiado grande (y hay que fragmentarlo) o demasiado chico (y hay que juntarlo con otros).

* **Nomenclatura de archivos**: cómo nombrar adecuadamente un archivo.

* **Codificación**: cuál es la codificación en que se debe guardar un archivo.

* **Estructura y características de los datos tabulares**

    * Recomendaciones generales: aplican a todos los casos.

    * Recomendaciones para estructurar planillas de cálculo: aplican exclusivamente al trabajo en planillas de cálculo.

    * Exportación a CSV: cómo exportar adecuadamente planillas de cálculo a un archivo de formato abierto.

* **Estándares según el tipo de datos**: cuáles son los estándares recomendados para manejar distintos tipos de datos.

Estos son los primeros aspectos importantes para la estandarización de datos.

Para una discusión sobre los estándares recomendados en el manejo de datos básicos y fundamentales, transversales a distintas áreas temáticas, se puede consultar la **Guía para la identificación y uso de entidades interoperables**.

## Formatos abiertos de archivos

Hay una gran variedad de tecnologías disponibles para producir y almacenar datos. Como ser: planillas de cálculo, bases de datos, software estadístico más específico y más. Esto genera una enorme diversidad de formatos, a veces caótica.

Algunos de estos formatos, no siempre se adecuan a los niveles de apertura deseados. Te ofrecemos algunas pautas y recomendaciones que facilitan la adaptación y/o transformación de estos formatos hacia otros más abiertos y fácilmente reutilizables.

En este cuadro consideramos algunos de los formatos más usados y evaluamos su nivel de apertura:

<table>
  <colgroup>
    <col style="width:17%">
    <col style="width:49%">
    <col style="width:17%">
    <col style="width:17%">
  </colgroup>
<tbody>
  <tr>
    <td>Formato</td>
    <td>Descripción breve</td>
    <td>Tipo de datos</td>
    <td>Nivel de apertura</td>
  </tr>
  <tr>
    <td>XLS</td>
    <td>Los XLS son archivos de planilla de cálculo. Es un formato propietario de MS Office.</td>
    <td>Tabulares</td>
    <td>Baja</td>
  </tr>
  <tr>
    <td>XLSX</td>
    <td>Los XLSX son archivos con la estructura de un XML. Es un formato abierto basado en Office Open XML (ISO/IEC 29500:2008). Popularizado por ser el formato por defecto del procesador de planillas de cálculo desde MS Office 2007.</td>
    <td>Tabulares</td>
    <td>Media</td>
  </tr>
  <tr>
    <td>ODS</td>
    <td>Los ODS son archivos con la estructura de un XML. Es un formato abierto basado en OASIS OpenDocument Format (ISO/IEC 26300) . Es el formato por defecto del procesador de planillas de cálculo Open Office.</td>
    <td>Tabulares</td>
    <td>Media</td>
  </tr>
  <tr>
    <td>CSV</td>
    <td>Los archivos CSV son archivos de texto plano donde las columnas se separan por comas y las filas por saltos de línea.
Es un formato abierto.</td>
    <td>Tabulares</td>
    <td>Alta</td>
  </tr>
  <tr>
    <td>JSON</td>
    <td>Es un formato para el intercambio de datos. En mayor medida que los formatos anteriores, JSON es especialmente útil para datos entre máquinas. Es un formato abierto basado en la especificación RFC 7159. </td>
    <td style="font-size: 12px" >Estructurados</td>
    <td>Alta</td>
  </tr>
</tbody>
</table>

Antes de seguir, introduciremos dos conceptos que se usarán a lo largo de toda la guía:

* **Distribución o Recurso:** Una distribución o recurso es la unidad mínima en la que se publican datos. Se trata de los archivos que pueden ser descargados y re-utilizados por un usuario. Los recursos pueden tener diversos formatos (.csv, .shp, etc.).

* **Dataset:** Un conjunto de datos o dataset agrupa recursos referidos a un mismo tema que respetan una estructura de la información. Los mismos podrían diferir en el formato en que se los presenta (Ej. .csv, .json, .xls, etc.), la fecha a la que se refieren, el área geográfica cubierta o estar separados bajo algún otro criterio.

Un recurso en formato tabular es un archivo plano que se ajusta a un esquema predefinido de columnas, incluyendo el nombre de la columna y el tipo de datos.

En la mayoría de los casos, corresponde a datos que llegan de bases de datos, reportes y planillas de cálculo en general. A diferencia de los formatos tabulares, los archivos JSON siguen una estructura diferente donde se definen listas de objetos con pares "clave" - “valor”.

**Recomendamos con énfasis la publicación de los datos en formato CSV y/o JSON**. En caso de utilizar formatos propietarios o aún no estandarizados, es útil indicar software, versión y aplicación que permite procesar esos formatos.


### CSV

El CSV es un formato de archivo de texto plano donde las campos (columnas) se separan por comas; y los registros (filas), por saltos de línea. Algunas versiones alternativas de esta forma de publicar datos usan otros separadores como punto y coma (";") o pipe (“|”).

Las recomendaciones, siguiendo lo indicado por la especificación [RFC4180](http://tools.ietf.org/html/rfc4180) y las pautas de la [W3C](https://www.w3.org/TR/tabular-data-model/), para la publicación de archivos en formato CSV son:

* Las filas deben finalizar con los caracteres de "retorno de carro" (\r) y "salto de línea" (\n) unidos (\r\n). Esta forma de separar las líneas se denomina usualmente CRLF ("Carriage Return Line Feed").

* La primera fila siempre contiene los nombres de los campos.

* No se deben repetir nombres entre los campos.

* No se debe colocar espacios al principio ni al final del nombre de un campo, o de un valor.

* Tanto los campos como los valores deben estar separados por comas (",").


* En el caso de que un valor contenga el caracter separador (",") o cualquiera de los caracteres que separan las líneas ("\r", "\n" o "\r\n"), el valor completo debe ser encerrado entre comillas dobles "". Esto indica que el caracter no cumple el rol de separar columnas o filas, sino que es parte de un valor.

Ejemplo:

```
col1,col2\r\n
"La tasa de Juan, está vacía",La tasa de Pablo está llena\r\n
"La tasa de Juan\nestá vacía",La tasa de Pablo está llena\r\n
"La tasa de Juan\r\nestá vacía",La tasa de Pablo está llena\r\n
```


* En el caso de que un valor contenga el caracter comilla doble ("), el valor debe ser encerrado entre comillas dobles como en el caso anterior ("") y, además, los caracteres comilla doble que se encuentren dentro del valor deben escribirse dos veces ("").

Ejemplo:

```
col1,col2\r\n
"La tasa de ""Juan"" está vacía",La tasa de Pablo está llena\r\n
```

* Para todos los tipos de datos se considera válido el valor indefinido. Este se expresará con la ausencia de todo caracter y no con un caracter o string especial como podrían ser ".", "null", "none", "nan", etc.

Ejemplo:

```
col1,col2,col3\r\n
a,,b\r\n
a,"",b\r\n
```

### JSON

JSON es un formato de texto popular para el intercambio de datos, es un acrónimo de  JavaScript Object Notation. Por su característica de ser un formato de tipo estructurado es especialmente útil para el intercambio de datos entre máquina (*machine - readable format*).

El formato JSON ha sido definido por la especificación [RFC 7159](https://tools.ietf.org/html/rfc7159) y, tal como CSV, también es un estándar abierto.

## Fragmentación de archivos

Para garantizar la accesibilidad a los datos, **es necesario fragmentar los archivos  excesivamente grandes**, que superen el millón de filas.

Para esto, recomendamos usar conceptos simples, fragmentando:

(a) **por períodos** en caso de tratarse de información temporal (Ej. Años, semestres, trimestres, meses, semanas, días),

(b) **por zonas** en caso de tratarse de información geográfica (Ej. provincias, municipios, barrios, secciones, o manzanas) o

(c) **por dimensiones temáticas** propias del dominio particular de la información.

Sin embargo, siempre que se decida fragmentar un archivo para garantizar su accesibilidad,  recomendamos publicar también una versión no fragmentada que contenga el conjunto de datos completo (aunque sea muy grande), a los fines de evitar la tarea de consolidación.

Para eso, sugerimos usar protocolos de compresión, en especial para archivos muy grandes, y altamente compresibles. De hacerlo, aconsejamos protocolos sin pérdida, y abiertos.

## Nomenclatura de archivos

Recomendamos estas convenciones para nombrar archivos:

* Usar palabras siempre en minúsculas.
* No usar artículos.
* Usar únicamente letras y números ASCII, siempre en minúsculas, comprendidos en el rango "a-z" y “0-9”.
* Separar las palabras con guión medio "-".
* En caso de corresponder, ubicar la referencia temporal o del atributo de fragmentación siempre al final.

Ejemplos:

* *acceso-informacion-publica.csv*: Versión completa del recurso.

* *acceso-informacion-publica-2013.csv*: Versión del recurso fragmentada por año.

* *acceso-informacion-publica-201302.csv*: Versión del recurso fragmentada por mes.

* *acceso-informacion-publica-caba.csv*: Versión del recurso fragmentada por división político-territorial (provincia o caba).

* *acceso-informacion-publica-caba-2013.csv*: Versión del recurso fragmentada por división político-territorial (provincia o caba) y año.

* *acceso-informacion-publica-jujuy-20130208.csv*:  Versión del recurso fragmentada por división político-territorial (provincia o caba) y fecha.

Para la fragmentación temporal, recomendamos el estándar de los ejemplos, ya que es compacto y ordena los recursos por tiempo: YYYYMMDD. Por favor, recordá mantener siempre dos dígitos para el mes y el día, incluso si el número es menor a 10.

Para la fragmentación por zonas, consultá la **Guía para la identificación y  uso de entidades interoperables**, y mirá cómo nombrarlas adecuadamente.

En el caso de usar dimensiones temáticas propias del dominio particular de la información, podés ver esa guía o usar el mejor estándar identificado para esa temática particular.

## Codificación

Todos los recursos de datos, incluyendo los geográficos, deben publicarse usando la codificación UTF-8 siguiendo las  [recomendaciones de la W3C](https://www.w3.org/TR/tabular-data-model/#h-encoding).

Una de las principales razones es que UTF-8 soporta una gran variedad de lenguajes, [según la W3C](https://www.w3.org/International/questions/qa-choosing-encodings) es un *"estándar en el que se definen todos los caracteres necesarios para la escritura de la mayoría de los idiomas hablados en la actualidad. Su objetivo es ser, y, en gran medida, ya lo ha logrado, un superconjunto de todos los sets de caracteres que se hayan codificado"*.

## Estructura y características de los datos tabulares

En esta sección veremos:

(a) Recomendaciones generales para el trabajo con datos, y

(b) Recomendaciones para el trabajo con planillas de cálculo, orientadas tanto a facilitar su exportación a formatos abiertos, como a su propia usabilidad en el contexto de cualquier aplicación de planillas de cálculo.

### Recomendaciones generales

Estas son recomendaciones generales para el trabajo con datos tabulares. Sugerimos adoptarlas sea cual sea la tecnología usada.

Muchas de las las recomendaciones aquí presentadas se encuadran en los principios de [Tidy Data](https://www.jstatsoft.org/article/view/v059i10/v59i10.pdf) delineados por [Hadley Wickham](http://hadley.nz/). Éstos establecen, por ejemplo, que en una tabla de datos *"cada variable es una columna, cada observacion es una fila, y cada tipo de unidad observacional es una tabla"*. Sugerimos complementar la lectura de esta guía con la del trabajo que mencionamos.


#### Nomenclatura de los campos (nombres de las columnas)

La "nomenclatura de los campos" es el nombre de las columnas en los datos de estructura tabular. Estas recomendaciones aplican a la generalidad de los casos, pero cuando haya convenciones particulares según la temática o rubro de datos de que se trate y éstas entren en conflicto, puede ser conveniente privilegiar primero la convención de la temática específica y luego la convención general.

Los nombres de los campos deben:

* Estar en español.

* Ser lo más explícitos, descriptivos y declarativos como sea posible.

    * Es preferible que el nombre de un campo sea claro antes que corto, pero se recomienda no superar los 50 caracteres.

    * No usar abreviaturas si no es estrictamente necesario o recomendado por una convención ampliamente difundida. En caso de usarlas, incluirlas en el diccionario de datos.

* Estar en minúsculas, no incluir caracteres especiales, ni estar subrayados.

    * Usar palabras compuestas únicamente de caracteres en minúsculas comprendidos en el rango a-z (letras sin tildes) y en el rango 0-9 (dígitos).

    * Las palabras deben unirse con guión bajo " _ ".

    * No contener espacios.

    * Las palabras deben separarse siempre con " _ ", en lugar de no tener separación alguna: fecha_audiencia_solicitada en lugar de fechaaudienciasolicitada

* Referirse a un sólo atributo de los datos, indivisible en más de un campo.

    * Los campos deben separar los atributos de los datos en la forma más desagregada que sea posible. 

    * Se debe evitar definir campos que contengan más de un tipo de información (por ejemplo: e-mail y sitio web, número de teléfono, etc bajo "datos_de_contacto").

* Si existe una entidad que engloba varias características separadas en campos diferentes, comenzar nombrando los campos con esa entidad y luego con los atributos más específicos (de lo más general a lo más específico). 

    * Ej.: solicitante y solicitante_documento son entidades más generales que se repiten en varios campos, que corresponden a atributos más específicos.

* solicitante_nombre

* solicitante_cargo

* solicitante_documento_tipo

* solicitante_documento_numero

    * Resulta más fácil  identificar qué campos están relacionados entre sí porque configuran atributos de una misma entidad, en lugar de parecer campos conceptualmente independientes.  Además, el ordenamiento alfabético de los campos los dejaría automáticamente agrupados por su pertenencia a una entidad más importante.

    * Incluso cuando la entidad de un atributo parezca evidente (ej.: un dataset llamado "audiencias" donde todos los campos son atributos de la entidad “audiencia”), se recomienda nombrar el campo incluyendo la entidad a la que hace referencia el atributo.

* <span class="no-recomendado">**No recomendado**</span>: “fecha_hora”
* <span class="recomendado">**Recomendado**</span>: "audiencia_id", “audiencia_fecha_hora”.

Los campos que sean identificadores o códigos, deberán incluir el sufijo "_id" en el nombre del campo, salvo casos excepcionales donde un nombre alternativo sea más conveniente porque ofrece información sobre el sistema de identificación usado.

* En cuanto a los campos que contengan la descripción de ese identificador, se recomienda que incluyan el sufijo "_desc" (por "descripción") en caso de que no exista una forma más conveniente de nombrar el campo.

<span class="recomendado">**Recomendado**</span>

<table>
<tbody>
    <td>sucursal_id</td>
    <td>sucursal_desc</td>
  </tr>
  <tr>
    <td>1</td>
    <td>Nueva Pompeya</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Barracas</td>
  </tr>
  <tr>
    <td>3</td>
    <td>La Quiaca</td>
  </tr>
</tbody>
</table>


#### Nivel de granularidad de los datos

Por favor, no incluir totales, subtotales ni agrupamientos de datos. Un dataset debe ser consistente en el nivel de granularidad de los datos que contiene. Está bien tener un dataset con la cantidad de convenios firmados por provincia y está bien tener un dataset con la cantidad de convenios firmados por municipio. No está bien tener un dataset que mezcle ambos. 

Dicho esto, el dato agregado "convenios firmados por provincia" siempre se puede calcular a partir de un proceso del dataset más desagregado, pero esto no es así a la inversa (es imposible recuperar los datos a nivel de municipio desde el dataset provincial).

<span class="no-recomendado">**No recomendado**</span> - datos con subtotales y/o totales incluidos (diferentes niveles de granularidad)

<table>
  <colgroup>
    <col style="width:21%">
    <col style="width:21%">
    <col style="width:28%">
    <col style="width:30%">
  </colgroup>
<tbody>
  <tr>
    <td style="font-size: 11px">provincia_nombre</td>
    <td style="font-size: 11px">municipio_nombre</td>
    <td style="font-size: 11px">convenios_firmados_anio</td>
    <td style="font-size: 11px">convenios_firmados_numero</td>
  </tr>
  <tr>
    <td> </td>
    <td>Provincia X</td>
    <td>Municipio W</td>
    <td>2011</td>
  </tr>
  <tr>
    <td>Provincia X</td>
    <td>Municipio X</td>
    <td>2011</td>
    <td>15</td>
  </tr>
  <tr>
    <td>Provincia X</td>
    <td>Subtotal</td>
    <td>2011</td>
    <td>25</td>
  </tr>
  <tr>
    <td>Provincia Y</td>
    <td>Municipio Z</td>
    <td>2011</td>
    <td>5</td>
  </tr>
  <tr>
    <td>Provincia Y</td>
    <td>Subtotal</td>
    <td>2011</td>
    <td>5</td>
  </tr>
  <tr>
    <td></td>
    <td>TOTAL</td>
    <td>2011</td>
    <td>30</td>
  </tr>
</tbody>
</table>


<span class="recomendado">**Recomendado**</span> - datos de un mismo nivel de granularidad

<table>
  <colgroup>
    <col style="width:21%">
    <col style="width:21%">
    <col style="width:28%">
    <col style="width:30%">
  </colgroup>
<tbody>
  <tr>
    <td style="font-size: 11px">provincia_nombre</td>
    <td style="font-size: 11px">municipio_nombre</td>
    <td style="font-size: 11px">convenios_firmados_anio</td>
    <td style="font-size: 11px">convenios_firmados_numero</td>
  </tr>
  <tr>
    <td>Provincia X</td>
    <td>Municipio W</td>
    <td>2011</td>
    <td>10</td>
  </tr>
  <tr>
    <td>Provincia X</td>
    <td>Municipio X</td>
    <td>2011</td>
    <td>15</td>
  </tr>
  <tr>
    <td>Provincia Y</td>
    <td>Municipio Z</td>
    <td>2011</td>
    <td>5</td>
  </tr>
</tbody>
</table>


#### Usar orientación vertical en lugar de horizontal

Es preferible que la orientación de los datos sea "vertical" en lugar de “horizontal” en los casos en que esto sea posible. La principal razón es que los datos orientados de manera vertical facilitan el tratamiento y análisis de los datos.

<span class="no-recomendado">**No recomendado**</span> - Orientación horizontal

<table>
  <colgroup>
    <col style="width:19%">
    <col style="width:17%">
    <col style="width:27%">
    <col style="width:28%">
  </colgroup>
<tbody>
  <tr>
    <td style="font-size: 11px">municipio_nombre</td>
    <td style="font-size: 11px">solicitudes_anio</td>
    <td style="font-size:11px;">solicitudes_poda_y_arbolado_numero</td>
    <td style="font-size:11px;">solicitudes_recoleccion_residuos_numero</td>
  </tr>
  <tr>
    <td>Municipalidad X</td>
    <td>2015</td>
    <td>340</td>
    <td>198</td>
</tbody>
</table>


<span class="recomendado">**Recomendado**</span> - Orientación vertical

<table>
  <colgroup>
    <col style="width:19%">
    <col style="width:17%">
    <col style="width:27%">
    <col style="width:28%">
  </colgroup>

<tbody>
  <tr>
    <td style="font-size: 11px">municipio_nombre</td>
    <td style="font-size: 11px">solicitudes_anio</td>
    <td style="font-size:11px;">solicitudes_categoria</td>
    <td style="font-size:11px;">solicitudes_numero</td>
  </tr>
  <tr>
    <td>Municipalidad X</td>
    <td>2015</td>
    <td>Poda y arbolado</td>
    <td>340</td>
  </tr>
  <tr>
    <td>Municipalidad X</td>
    <td>2015</td>
    <td>Recolección de residuos</td>
    <td>198</td>
  </tr>
</tbody>
</table>


#### Incluir sólo un atributo por campo

Se recomienda definir los campos de forma atómica de modo de incluir un sólo atributo por elemento, en lugar de datos múltiples, generando campos adicionales de ser necesario.

<span class="no-recomendado">**No recomendado**</span> - múltiples datos en una celda

<table>
<tbody>
  <tr>
    <td>municipio_nombre</td>
    <td>solicitudes_anio</td>
    <td style="font-size:11px;">categoria_solicitudes_numero_y_tipo</td>
  </tr>
  <tr>
    <td>Municipalidad X</td>
    <td>2015</td>
    <td>Poda y arbolado - 340
Recolección de residuos - 198</td>
</tbody>
</table>


<span class="recomendado">**Recomendado**</span> - un dato por celda

<table>
<tbody>
  <tr>
    <td>municipio_nombre</td>
    <td>solicitudes_anio</td>
    <td>solicitudes_categoria</td>
    <td>solicitudes_numero</td>
  </tr>
  <tr>
    <td>Municipalidad X</td>
    <td>2015</td>
    <td>Poda y arbolado</td>
    <td>340</td>
  </tr>
  <tr>
    <td>Municipalidad X</td>
    <td>2015</td>
    <td>Recolección de residuos</td>
    <td>198</td>
  </tr>
</tbody>
</table>


#### Valores nulos, desconocidos o en blanco en campos numéricos

Los valores de los datos deben ser siempre explícitos y respetando el tipo de datos del campo de que se trate. Los elementos o celdas en blanco se interpretarán siempre como "valor ausente". 

Si existen distintas interpretaciones posibles de un "valor ausente", éstas deben ser explicitadas en un campo aparte. Si sólo hay “valores ausentes” (no hay distintas interpretaciones, es siempre un “valor ausente”) no es necesario agregar una columna adicional.

Es importante destacar, por ejemplo, que cuando un valor numérico sea "0" siempre debe ponerse un “0” como dato (y no un valor nulo, en blanco o vacío).

<span class="no-recomendado">**No recomendado**</span> - texto presente en campos numéricos

<table id="una-columna">
<tbody>
  <tr>
    <td>solicitudes_numero</td>
  </tr>
  <tr>
    <td>34</td>
  </tr>
  <tr>
    <td>NA</td>
  </tr>
  <tr>
  </tr>
  <tr>
    <td>...</td>
  </tr>
  <tr>
    <td></td>
  </tr>
  <tr>
    <td></td>
  </tr>
  <tr>
    <td>567</td>
  </tr>
</tbody>
</table>


<span class="recomendado">**Recomendado**</span> - texto excluido de campos numéricos

<table>
<tbody>
  <tr>
    <td>solicitudes_numero</td>
    <td>solicitudes_numero_missing_desc</td>
  </tr>
  <tr>
    <td>34</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>No disponible</td>
  </tr>
  <tr>
    <td></td>
    <td>No sabe / No contesta</td>
  </tr>
  <tr>
    <td></td>
    <td>Valor ausente</td>
  </tr>
  <tr>
    <td></td>
    <td>Valor ausente</td>
  </tr>
  <tr>
    <td>0</td>
    <td></td>
  </tr>
  <tr>
    <td>567</td>
    <td></td>
  </tr>
</tbody>
</table>


### Recomendaciones para estructurar planillas de cálculo

Las recomendaciones de esta sección aplican exclusivamente al trabajo sobre planillas de cálculo.

#### Usar celdas simples

Recomendamos usar celdas simples y, en ningún caso, combinar celdas.

<span class="no-recomendado">**No recomendado**</span> - celdas combinadas

<table>
<tbody>
  <tr>
    <td>proveedor_nombre</td>
    <td colspan="2">contacto_datos</td>
  </tr>
  <tr>
    <td></td>
    <td>correo_electronico</td>
    <td>telefono</td>
  </tr>
    <td>Ejemplo Sociedad Anónima</td>
    <td>ejemplo@ejemplo.com.ar</td>
    <td>1143XXXXXX</td>
  </tr>
</tbody>
</table>


<span class="recomendado">**Recomendado**</span> - celdas simples, sin combinar

<table>
<tbody>
  <tr>
    <td>proveedor_nombre</td>
    <td>contacto_correo_electronico</td>
    <td>contacto_telefono</td>
  </tr>
  <tr>
    <td>Ejemplo Sociedad Anónima</td>
    <td>ejemplo@ejemplo.com.ar</td>
    <td>1143XXXXXX</td>
  </tr>
</tbody>
</table>


#### Fila de encabezado

Los datos deben contener sólo una fila de encabezado. Desde la segunda fila en adelante, sólo debe haber datos, pero nunca un encabezado.

<span class="no-recomendado">**No recomendado**</span> - múltiples filas de encabezado

<table>
<tbody>
  <tr>
    <td>Nombre del</td>
    <td>Dirección de correo</td>
    <td>Teléfono de</td>
  </tr>
  <tr>
    <td>proveedor</td>
    <td>electrónico de contacto</td>
    <td>contacto</td>
  </tr>
    <td>Ejemplo Sociedad Anónima</td>
    <td>ejemplo@ejemplo.com.ar</td>
    <td>1143XXXXXX</td>
  </tr>
</tbody>
</table>


<span class="recomendado">**Recomendado**</span> - encabezado de una única fila

<table>
<tbody>
  <tr>
    <td>proveedor_nombre</td>
    <td>contacto_correo_electronico</td>
    <td>contacto_telefono</td>
  </tr>
  <tr>
    <td>Ejemplo Sociedad Anónima</td>
    <td>ejemplo@ejemplo.com.ar</td>
    <td>1143XXXXXX</td>
  </tr>
</tbody>
</table>


#### Celdas vacías en filas para agrupar conceptos

Recomendamos no dejar celdas vacías en filas bajo la presunción de que valores en blanco posteriores a un valor positivo contienen implícitamente a ese mismo valor en una suerte de "agrupamiento conceptual".

Este error es muy común en la construcción de planillas de cálculo y suele generar problemas graves cuando cambia el orden original de las filas. Además, impide el uso de tablas dinámicas y otras formas de analizar los datos.

<span class="no-recomendado">**No recomendado**</span> - primera celda de la segunda fila vacía

<table>
<tbody>
  <tr>
    <td>municipio_nombre</td>
    <td>solicitudes_anio</td>
    <td>solicitudes_categoria</td>
    <td>solicitudes_numero</td>
  </tr>
  <tr>
    <td>Municipalidad X</td>
    <td>2015</td>
    <td>Poda y arbolado</td>
    <td> </td>
  </tr>
  <tr>
    <td></td>
    <td>2015</td>
    <td>Recolección de residuos</td>
    <td>198</td>
  </tr>
</tbody>
</table>


<span class="recomendado">**Recomendado**</span> - primera celda de la segunda fila completa

<table>
<tbody>
  <tr>
    <td>municipio_nombre</td>
    <td>solicitudes_anio</td>
    <td>solicitudes_categoria</td>
    <td>solicitudes_numero</td>
  </tr>
  <tr>
    <td>Municipalidad X</td>
    <td>2015</td>
    <td>Poda y arbolado</td>
    <td>340</td>
  </tr>
  <tr>
    <td>Municipalidad X</td>
    <td>2015</td>
    <td>Recolección de residuos</td>
    <td>198</td>
  </tr>
</tbody>
</table>


#### Formato de celdas

Las celdas de una planilla de cálculo deben estar formateadas acorde al tipo de datos de que se trate. Específicamente, **los números** siempre deben estar en celdas de formato/tipo "número", **los campos de tipo textual** deben estar en celdas de formato/tipo “texto” y **los campos de tipo fecha** deben estar en celdas de formato/tipo “fecha”.

<table>
  <colgroup>
    <col style="width:30%">
    <col style="width:40%">
    <col style="width:30%">
  </colgroup>
<tbody>
  <tr>
    <td>audiencia_fecha_hora</td>
    <td>audiencia_sujeto_obligado_nombre</td>
    <td>audiencia_numero</td>
  </tr>
  <tr>
    <td>1/3/16</td>
    <td>Juan</td>
    <td>3456</td>
  </tr>
  <tr>
    <td>(Fecha)</td>
    <td>(Texto)</td>
    <td>(Número)</td>
  </tr>
</tbody>
</table>


Mantener el formato correcto de las celdas según el tipo de datos que contengan:

* Mejora las las probabilidades de que una exportación a otro formato salga correctamente.

* Hace que los datos sean más operables en la propia planilla de cálculo, aprovechando mejor sus funcionalidades.

### Exportación a CSV

Insistimos: CSV es el formato más recomendado para la publicación de archivos tabulares. A la hora de exportar una planilla de cálculo a CSV hay 3 parámetros que deben ser especificados durante la exportación, independientemente del software de que se use:

* **Codificación** (encoding, en inglés): siempre debe ser UTF-8.

* **Caracter separador** (separator character, en inglés): siempre debe ser "," (coma).

* **Caracter calificador** (quote character o enclosing character, en inglés): siempre debe ser " “ “ (comillas dobles).

## Estándares según el tipo de Datos

El formato recomendado para los distintos tipos de datos está mayormente basado en las especificaciones de la [W3C](https://www.w3.org/TR/tabular-data-model/). En los otros casos, las recomendaciones surgen de la experiencia de trabajo del equipo de la Dirección Nacional de Datos e Información Pública y del esfuerzo realizado en la búsqueda de estándares más adecuados.

### Texto

* Los campos de texto no deben contener espacios en blanco innecesarios al principio ni al final.

#### Entidades

Las entidades que aparezcan entre los datos de un campo textual deben tener una descripción única. Es decir, toda mención que se realice a una entidad dada debe hacerse usando exactamente la misma cadena de caracteres cada vez:

* **Las descripciones de entidades** deberían elegirse siempre de forma tal que cumplan con el estándar específico que las describe, en caso de que este exista.

* **Cuando este estándar no existe** y hay dudas respecto del criterio a adoptar para elegir la descripción única de una entidad, debe **privilegiarse siempre aquella que sea lo más explícita**, descriptiva y declarativa posible.



<span class="no-recomendado">**No recomendado**</span>

<table id="una-columna">
<tbody>
  <tr>
    <td>localidad_nombre</td>
  </tr>
  <tr>
    <td>Ciudad Autónoma de Buenos Aires</td>
  </tr>
  <tr>
    <td>CABA</td>
  </tr>
  <tr>
    <td>Capital Federal</td>
  <tr>
    <td>Ciudad de Buenos Aires</td>
  </tr>
</tbody>
</table>


<span class="recomendado">**Recomendado**</span> 

<table  id="una-columna">
<tbody>
  <tr>
    <td>localidad_nombre</td>
  </tr>
  <tr>
    <td>Ciudad Autónoma de Buenos Aires</td>
  </tr>
  <tr>
    <td>Ciudad Autónoma de Buenos Aires</td>
  </tr>
  <tr>
    <td>Ciudad Autónoma de Buenos Aires</td>
  </tr>
  <tr>
    <td>Ciudad Autónoma de Buenos Aires</td>
  </tr>
</tbody>
</table>


En el ejemplo anterior, los cuatro valores de texto refieren a la misma entidad. Debe elegirse una única forma de referirse a la misma y usarla en todos los casos.

Siempre que sea posible, la elección deberá fundamentarse en el estándar establecido para ese tipo de entidad (para más información ver la **Guía para la identificación y uso de entidades interoperables**). En el caso de no existir un estándar, deberá adecuarse a las pautas generales contexto del dataset de que se trate.

#### Nombres propios

**Se capitalizan** (primera letra de cada palabra es mayúscula, el resto de las letras son minúsculas) **todas las palabras significativas**, salvo las siglas. Las palabras significativas son aquellas que no cumplen la función de artículos o preposiciones.

#### Siglas

Todas las siglas se escriben en mayúsculas, sin usar puntos ni espacios intermedios.


### Número

* El separador decimal debe ser el caracter ".".
* No se usará separador de miles.
* No se deberán usar espacios en blanco.
* Para los números negativos debe incluirse el símbolo menos "-” inmediatamente antes del número, sin espacio en blanco intermedio.

#### Moneda

Los valores numéricos que sean además valores monetarios se consideran números y, por lo tanto, valen las mismas recomendaciones que para ellos. Además, agregamos las siguientes recomendaciones:

* La cantidad de decimales debe limitarse a dos, salvo que el uso de una mayor cantidad de decimales sea significativo para el caso particular.

* En ningún caso se incluirán símbolos o letras en el campo numérico -ya sea "$", “DOL”, “USD”, etc.

Si en el recurso los valores monetarios están expresados en diferentes monedas, se recomienda indicarlo en un campo aparte (que puede llamarse "moneda_id") usando los códigos alfabéticos definidos en la [ISO 4127](http://www.iso.org/iso/home/standards/currency_codes.htm).

Ejemplo:

* ARS, para el peso argentino.
* USD, para el dólar estadounidense.

#### Números telefónicos

En este apartado, proponemos una solución para incluir números telefónicos nacionales en los recursos de datos.

A nivel internacional, el estándar para los números telefónicos fue desarrollado por el "Sector de Normalización de las Telecomunicaciones de la Unión Internacional de Telecomunicaciones" (ITU Telecommunication Standardization Sector) bajo la recomendación [E.164](https://www.itu.int/rec/T-REC-E.164/es).

Para el caso de los números nacionales, el ENACOM tiene la competencia sobre el sistema de numeración telefónica. Este organismo determina que el número nacional de abonado debe estar compuesto por 10 dígitos. Estos 10 dígitos están conformados por un indicativo interurbano más un número de abonado. Pudiendo el indicativo interurbano tener entre 2 y 4 dígitos, y el número de abonado entre 6 y 8 dígitos.

<table>
<tbody>
  <tr>
    <td>Indicativo interurbano (ámbito geográfico al que corresponde)</td>
    <td>Número de abonado</td>
    <td>Número Nacional interurbano = Indicativo interurbano + Número de abonado</td>
  </tr>
  <tr>
    <td>11 (AMBA)</td>
    <td>4343XXXX</td>
    <td>114343XXXX</td>
  </tr>
  <tr>
    <td>351 (Ciudad de Córdoba)</td>
    <td>434XXXX</td>
    <td>351434XXXX</td>
  </tr>
  <tr>
    <td>3837 (Tinogasta)</td>
    <td>43XXXX</td>
    <td>383743XXXX</td>
  </tr>
</tbody>
</table>


Esta numeración es válida para los teléfonos móviles, pero dado que para llamar a un móvil desde un teléfono fijo es necesario anteponer "15" al número de abonado, es necesario que el registro del número telefónico especifique de alguna manera si se trata de un móvil o de un teléfono fijo.

Al no existir estándares nacionales para la inclusión de números telefónicos en recursos de datos, los números telefónicos suelen indicarse de múltiples maneras. Por ejemplo:

<span class="no-recomendado">**No recomendado**</span> - Múltiples formas de indicar un número telefónico

<table>
<tbody>
  <tr>
    <td>proveedor_nombre</td>
    <td>contacto_correo_electronico</td>
    <td>contacto_telefono</td>
  </tr>
  <tr>
    <td>Ejemplo Sociedad Anónima</td>
    <td>ejemplo@ejemplo.com.ar</td>
    <td>01143XXXXXX</td>
  </tr>
    <td>Ejemplo2 Sociedad Anónima</td>
    <td>ejemplo2@ejemplo2.com.ar</td>
    <td>011-45XXXXXX</td>
  </tr>
  <tr>
    <td>Ejemplo3 Sociedad Anónima</td>
    <td>ejemplo3@ejemplo3.com.ar</td>
    <td>351 434-XXXX</td>
  </tr>
  <tr>
    <td>Ejemplo4 Sociedad Anónima</td>
    <td>ejemplo4@ejemplo4.com.ar</td>
    <td>011 15 6344-XXXX</td>
  </tr>
</tbody>
</table>


Para los recursos que contengan números telefónicos nacionales recomendamos como mínimo:

* Respetar el estándar definido por el Número Nacional Interurbano utilizando la conformación de números mediante 10 dígitos.
* Asegurarse de indicar si el teléfono es móvil o fijo.
* Omitir el agregado de dígitos adicionales en el indicativo interurbano. Recomendamos no indicar cero inicial antes del código de área.

Con las salvedades que comentaremos al final de este apartado, un posible abordaje sería el de la tabla a continuación:

<span class="recomendado">**Recomendado**</span> - adecuado al estándar del Número Nacional Interurbano

<table>
  <colgroup>
    <col style="width:16%">
    <col style="width:22%">
    <col style="width:18%">
    <col style="width:26%">
    <col style="width:18%">
      </colgroup>
<tbody>
  <tr>
    <td >proveedor_nombre</td>
    <td >contacto_correo_electronico</td>
    <td >tipo_numero_telefono</td>
    <td >contacto_telefono_indicativo_interurbano</td>
    <td >contacto_telefono_numero_abonado</td>
  </tr>
  <tr>
    <td>Ejemplo Sociedad Anónima</td>
    <td  style="font-size:11px;">ejemplo@ejemplo.com.ar</td>
    <td>Fijo</td>
    <td>11</td>
    <td>43XXXXXX</td>
  </tr>
  <tr>
    <td>Ejemplo2 Sociedad Anónima</td>
    <td style="font-size:11px;">ejemplo2@ejemplo2.com.ar</td>
    <td>Fijo</td>
    <td>11</td>
    <td>45XXXXXX</td>
  </tr>
  <tr>
    <td>Ejemplo3 Sociedad Anónima</td>
    <td style="font-size:11px;">ejemplo3@ejemplo3.com.ar</td>
    <td>Fijo</td>
    <td>351</td>
    <td>434XXXX</td>
  </tr>
  <tr>
    <td>Ejemplo4 Sociedad Anónima</td>
    <td style="font-size:11px;">ejemplo4@ejemplo4.com.ar</td>
    <td>Móvil</td>
    <td>11</td>
    <td>6344XXXX</td>
  </tr>
</tbody>
</table>


Esta recomendación no contempla estos casos específicos:

* No será aplicable a números de uso público, ejemplo: 100, Bomberos; 911, Policía Federal; etc.
* Para casos que requieran la inclusión de más de un número telefónico. Deberán agregarse campos o modificar la estructura de la base de datos.
* Para teléfonos que requieran la inclusión de un número de interno, y al estar éste definido por la persona u organización específica, deberá considerarse la inclusión de otro campo de tipo texto. Ya que los números de interno pueden incluir texto. Ejemplo: "*86", “#36”, etc.
* Para el casos de números internacionales recomendamos contemplar el estándar internacional  [E.164](https://www.itu.int/rec/T-REC-E.164/es).

#### Coordenadas

Para registrar datos de coordenadas geográficas de puntos, usamos números decimales. Los campos deberán llamarse "latitud" y “longitud”. Cuando sea conveniente especificar el nombre de la entidad de la cual se consignan las coordenadas, se usarán los sufijos “_latitud” y “_longitud”.

<span class="no-recomendado">**No recomendado**</span>

<table>
<tbody>
  <tr>
    <td>latitud</td>
    <td>longitud</td>
  </tr>
  <tr>
    <td>34º 11' 30''</td>
    <td>58º 43' 20''</td>
  </tr>
</tbody>
</table>


<span class="recomendado">**Recomendado**</span>

<table>
<tbody>
  <tr>
    <td>latitud</td>
    <td>longitud</td>
  </tr>
  <tr>
    <td>-34.6043222</td>
    <td>-58.4134862</td>
  </tr>
</tbody>
</table>


### Tiempo

Se usará el estándar [ISO 8601](https://es.wikipedia.org/wiki/ISO_8601) (YYYY-MM-DDTHH:MM:SS[.mmmmmm][+HH:MM]). A menos que se indique lo contrario, se asumirá que la zona horaria es UTC-03:00 (Argentina).

* Fecha: YYYY-MM-DD
* Hora: HH:MM:SS[.mmmmmm][+HH:MM]
* Fecha y Hora: YYYY-MM-DDTHH:MM:SS[.mmmmmm][+HH:MM]
* Duración: YYYY-MM-DDTHH:MM:SS[.mmmmmm]

#### Rangos horarios

* Los rangos estarán divididos en dos partes separadas por un doble guión bajo "__", la primera indica el día y la segunda, la hora.

* Se puede omitir la parte del día o bien de la hora pero nunca ambas.

* Si se omite la parte que indica el día se asumirá que el rango abarca todo el horario indicado.

* Si se omite la parte que indica el horario se asumirá que el rango abarca todo el día indicado.

* El día se puede indicar tanto mediante rangos separando los días con guiones medios "-" o bien como particulares con el guión bajo "_".

Ejemplos de formatos válidos para días:

```
DAY: Un solo día
DAY1-DAY2: Entre entre DAY1 y DAY2
DAY1_DAY2: DAY1 y DAY2
DAY1-DAY2_DAY3: DAY1 a DAY2 y DAY3
```

* La hora se indica mediante rangos, separando los horarios con guiones medios ("-"). También se pueden indicar varios horarios con el guión bajo "_".

Ejemplos de formatos válidos para horas:

```
HH:MM-HH:MM : Rango simple
HH:MM-HH:MM_HH:MM-HH:MM : Dos rangos
```

Más ejemplos de formatos válidos completos:

```
HH:MM-HH:MM para indicar un rango que ocurre todos los días.
DAY para indicar que el rango ocupa todo el día DAY.
DAY__HH:MM-HH:MM para indicar un rango que ocurre los días DAY entre HH:MM y HH:MM.
DAY__HH:MM-HH:MM_HH:MM-HH:MM para indicar mas un rango horario en el mismo día
DAY1-DAY2__HH:MM-HH:MM para indicar un rango que ocurre los días DAY1 a DAY2 entre HH:MM y HH:MM
DAY1-DAY2__HH:MM-HH:MM_HH:MM-HH:MM para indicar mas un rango horario en el mismo rango de días
```

* En caso de que se necesite cubrir más de una franja horaria y esta sintaxis sea insuficiente, se pueden incluir varias separadas por espacios.

* Los días se indicarán con sus iniciales en castellano: LUN, MAR, MIE, JUE, VIE, SAB y DOM

Ejemplos:

```
24hs -> "00:00-23:59" 
Jueves 24hs -> "JUE" 
Jueves de 14:30 a 17 hs -> "JUE__14:30-17:00" 
Jueves de 8 a 12 hs y de 16 a 20 hs -> "JUE__08:12-17:00_16:00-20:00" 
Jueves de 8 a 15 hs y Viernes de 8 a 15 hs -> "JUE__08:00-15:00 VIE_08:00-15:00" 
Lunes a Viernes 7:30 a 17 hs y Sábados 8 a 12 hs -> "LUN-VIE__07:30-17:00 SAB__08:00-12:00" 
Lunes a Viernes 8 a 11 y 14 a 18 hs -> "LUN-VIE__08:00-11:00_14:00-18:00" 
Lunes y Miercoles 8 a 11 y 14 a 18 hs -> "LUN_MIE__08:00-11:00_14:00-18:00" 
Lunes a Miercoles y Viernes 8 a 11 y 14 a 18 hs -> "LUN-MIE_VIE__08:00-11:00_14:00-18:00"
Lunes a Miercoles 8 a 11 y de Viernes a Domingo 9 a 10 -> "LUN-MIE__08:00-11:00 VIE-DOM__09:00-10:00"
```

### Booleano

* A menos que se indique lo contrario, se identificarán con los valores *true* o *false*.

    * Esta convención puede variar en algunos rubros específicos de datos, pero en caso de no existir una convención clara y definida aplicable al rubro o contexto del dataset, se recomienda utilizar *true* o *false*.

* Este campo puede contener "valores ausentes". En ese caso, el campo deberá estar totalmente vacío, no conteniendo ningún caracter.

* Si existe la posibilidad de que haya otro valor que no sea *true*, *false* o "valor ausente" significa que se eligió un tipo de datos incorrecto: este no es booleano, el tipo de dato booleano es binario y sólo admite 2 valores de verdad (aparte del caso del “valor ausente”).

