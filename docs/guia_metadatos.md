# Guía para el uso y la publicación de metadatos

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

## Indice

- [Glosario](#glosario)
- [Introducción](#introduccion)
  - [Objetivo de esta guía](#objetivo-de-esta-guia)
  - [¿Qué son los metadatos?](#que-son-los-metadatos)
  - [¿Cómo se publican los metadatos?](#como-se-publican-los-metadatos)
  - [Público objetivo de esta guía](#publico-objetivo-de-esta-guia)
- [Portal Andino](#portal-andino)
  - [Catálogo](#catalogo)
  - [Dataset](#dataset)
  - [Distribución](#distribucion)
  - [Campo](#campo)
  - [Tema](#tema)
- [Otros catálogos](#otros-catalogos)
  - [Estándar usado](#estandar-usado)
  - [Campos del perfil](#campos-del-perfil)
    - [Catálogo](#catalogo-1)
    - [Dataset](#dataset-1)
    - [Distribución](#distribucion-1)
    - [Campo](#campo-1)
    - [Tema](#tema-1)
- [Anexo I - Taxonomía temática global de la APN para los datasets (tabla)](#anexo-i-taxonomia-tematica-global-de-la-apn-para-los-datasets-tabla)
- [Anexo II - Pautas para la selección de etiquetas](#anexo-ii-pautas-para-la-seleccion-de-etiquetas)
- [Anexo III - Especificación de frecuencias (según ISO-8601)](#anexo-iii-especificacion-de-frecuencias-segun-iso-8601)
- [Anexo IV - Ejemplo de data.json](#anexo-iv-ejemplo-de-datajson)
- [Anexo V - Taxonomía temática global de la APN para los datasets (JSON)](#anexo-v-taxonomia-tematica-global-de-la-apn-para-los-datasets-json)
- [Anexo VI - Ejemplo de metadatos como texto](#anexo-vi-ejemplo-de-metadatos-como-texto)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Glosario

**Activo de datos**

Es cualquier **colección de datos con valor informativo**, de propiedad de una entidad u organismo, que reflejan su actividad y son relevantes para el desarrollo de sus misiones y funciones, o para los actores de su ecosistema. Aunque puede designar piezas aisladas de información, suele emplearse para **identificar y tratar conjuntos de datos** que pueden ser comprendidos y tratados **como una única unidad a efectos de su gestión, uso, protección e intercambio**.

**Distribución o recurso**

**Es la unidad mínima de un catálogo de datos**. Se trata de los activos de datos que se publican allí y que pueden ser descargados y re-utilizados por un usuario como archivos. Los recursos **pueden tener diversos formatos** (.csv, .shp, etc.). Están acompañados de información contextual asociada ("metadata") que describe el tipo de información que se publica, el proceso por el cual se obtiene, la descripción de los campos del recurso y cualquier información extra que facilite su interpretación, procesamiento y lectura.

**Dataset**

**También llamado _conjunto de datos,_ es la pieza principal en todo catálogo**. Se trata de un activo de datos que agrupa recursos referidos a un mismo tema, que respetan una estructura de la información. Los recursos que lo componen pueden diferir en el formato en que se los presenta (por ejemplo: .csv, .json, .xls, etc.), la fecha a la que se refieren, el área geográfica cubierta o estar separados bajo algún otro criterio. 

**Catálogo de datos**

Es **un directorio de conjuntos de datos, que recopila y organiza metadatos descriptivos**, de los datos que produce una organización. Un portal de datos es un catálogo.

**Perfil de metadatos**

**Es un estándar para documentar los activos de datos de un catálogo**. En esta guía documentamos un perfil de metadatos que busca unificar el modo en el que estos se comparten desde la Administración Pública Nacional.

**Portal Andino**

Es el **portal empaquetado y distribuible desarrollado sobre la base de la plataforma CKAN** (portal de datos abiertos), diseñado para facilitar la apertura y federación de activos de datos en la Argentina.

**Paquete para la apertura de datos de la República Argentina**

Es un **conjunto de herramientas y guías** de buenas prácticas creadas para **hacer más fácil la publicación de datos abiertos** en la Argentina.

## Introducción

Esta guía busca ayudar a los organismos a instrumentar la Política de Datos Abiertos impulsada desde el Gobierno de la Nación Argentina, a través del Decreto N° 117/2016 del 12 de enero de 2016.

 

### Objetivo de esta guía

Esta es **una guía de recomendaciones y buenas prácticas, para el uso y la publicación de metadatos**.

Para hacer estas recomendaciones, nos basamos en estándares usados a nivel nacional e internacional y en la experiencia de trabajo del equipo de la Dirección Nacional de Datos e Información Pública del Ministerio de Modernización de la Nación.

Esta es **una guía colaborativa y en progreso**. Valoramos, y alentamos, a organizaciones y ciudadanos a plantear ideas, sugerencias, y comentarios que nos ayuden a crear un mejor documento.

Este documento se complementa con la **Guía para la publicación de datos en formatos abiertos** y la **Guía para la identificación y uso de entidades interoperables**. 

### ¿Qué son los metadatos?

**Los metadatos son los datos sobre los datos**. Es decir: **elementos descriptivos que dan contexto** a un conjunto de datos, y acercan al usuario la información necesaria para entenderlos y usarlos eficazmente.

Un **título** y una breve **descripción** son los metadatos básicos que cualquier conjunto de datos a publicar debería tener. Después, existen muchos otros elementos que ayudan al lector a hacer un buen uso de los datos. Por ejemplo:

* **Nombre, tipo de datos y descripción de los campos**: ¿qué significa cada campo? ¿qué datos puedo encontrar en esa columna? ¿qué dicen y qué *no* dicen esos datos, cómo debo leerlos?
* **Palabras clave**: clasifican a un dataset como perteneciente a un conjunto de tópicos.
* **Tema**: clasifican a un dataset como perteneciente a un determinado tema, dentro de una jerarquía temática.
* **Fecha de publicación**: ¿cuándo se publicó por primera vez este dataset?
* **Fecha de última modificación**: ¿cuándo se actualizó por última vez este dataset?
* **Frecuencia de actualización**: ¿cada cuánto se actualiza este dataset?
* **URL de descarga**: ¿cómo dispongo de los datos, desde dónde puedo descargarlos?

Una lista curada de campos de metadatos, junto con las instrucciones de cómo deben utilizarse, define un **perfil de metadatos**.

En esta guía describimos el **perfil de metadatos recomendado para los catálogos de la Administración Pública Nacional** y cómo publicarlo.

### ¿Cómo se publican los metadatos?

**La publicación de los metadatos puede ser muy diversa** en detalle, calidad y forma. **Una publicación muy elemental es un documento de texto** que ofrece una descripción del dataset y de cada uno de los recursos que lo componen. Es posible ver un [ejemplo textual](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/data.md) de los metadatos de un catálogo de datos en el **Anexo VI - Ejemplo de metadatos como texto**.

Sin embargo, **las computadoras no pueden leer fácilmente documentos de texto**. La organización sistemática de colecciones de datasets (es decir, la creación de un **catálogo** de datos) exige un nivel de complejidad mayor para facilitar su descubrimiento, indexación, y reutilización por parte de scripts y aplicaciones de todo tipo.

La potencial reutilización de los conjuntos de datos y la posibilidad de que los mismos sean correctamente federados desde el Portal Nacional de Datos Abiertos (datos.gob.ar) dependerá de la calidad de sus metadatos. Adoptar y/o desarrollar estándares y vocabularios controlados es importante para la lectura e interpretación de los conjuntos de datos por personas y por aplicaciones informáticas.

Para esto, **los catálogos de datos publican sus metadatos en un formato estructurado (JSON)** respetando un determinado perfil estandarizado. Recomendamos ver un [ejemplo en JSON](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/data.json) de los metadatos de un catálogo de datos en el **Anexo IV - Ejemplo de data.json**.

En el resto de este documento detallamos las características de los estándares y vocabularios controlados adoptados para catálogos de datos, datasets y distribuciones.

### Público objetivo de esta guía

Esta guía intenta ayudar a quienes:

* **Publican sus catálogos de datos mediante un adaptación del portal Andino**. Es decir,  del portal que el equipo de Datos de la Nación Argentina diseñó sobre la base de CKAN y que pueden adoptar las dependencias de la Administración Pública Nacional (así como también de otros niveles gubernamentales sub-nacionales o incluso entidades del público general) para gestionar la publicación centralizada de sus activos de datos.

El portal Andino incluye formularios web para la carga de datos y metadatos. **La publicación de metadatos mediante este portal cumple con el perfil de metadatos recomendado en esta guía**. El Portal debe publicarse en un dominio de la forma *http://datos.[entidad].gob.ar*. Esto asegura la publicación automática de los metadatos en formato data.json en *http://datos.[entidad].gob.ar/data.json*

Si estás dentro de este grupo, **recomendamos leer la sección "_Portal Andino_"**. Con ella, podrás comprender cómo completar cada campo en el formulario web del Portal Andino.

* **Publican sus catálogos de datos mediante otros medios**. Esto es, en forma directa en el dominio digital de la entidad responsable o de alguna forma alternativa en la red. Esas entidades deberán publicar su catálogo de datos en un archivo estructurado (JSON) llamado *data.json* alojado en un dominio de la forma *http://datos.[entidad].gob.ar/data.json* siguiendo las especificaciones del perfil de metadatos de esta guía.

En [entidad] recomendamos usar un nombre simple y breve que represente a la organización que publica el catálogo (por ejemplo: datos.jus.gob.ar, datos.tucuman.gob.ar, datos.pilar.gob.ar).

Si la apertura de tus datos se inscribe en esta modalidad, **te sugerimos leer la sección "_Otros catálogos_"**. Te ayudará a comprender cómo generar y publicar un archivo *data.json* que cumpla con el perfil de metadatos de la Administración Pública Nacional.

## Portal Andino

**El portal Andino** es una herramienta especialmente diseñada para facilitar la publicación y apertura de datos y **cumple con el perfil de metadatos de la Administración Pública Nacional**.

Al cargar datasets y distribuciones a través de sus formularios, se generan los metadatos del perfil y se publican en un archivo data.json en el formato correcto.

El archivo *data.json* de un Portal Andino puede encontrarse en el directorio raíz del portal: *http://datos.[entidad].gob.ar/data.json*.

### Catálogo

**El perfil de metadatos propuesto se conforma de tres componentes principales**:

* La información del catálogo.
* Los datasets.
* Las distribuciones.

El *data.json* de **quienes usen el portal Andino contará con los metadatos correspondientes a los datasets y distribuciones**.

**Los metadatos a nivel de catálogo deberán ser completados en una planilla de cálculo y publicados en formato CSV en el directorio raíz del portal**, quedando disponibles para su descarga en una URL como *http://datos.[entidad].gob.ar/*catalog.csv.

El resto de los metadatos generados al cargar o actualizar un dataset o una distribución en el portal, se generan a través de los formularios completados y se publican automáticamente en *http://datos.[entidad].gob.ar/data.json*.

Recomendamos ver un [ejemplo textual](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/data.md) de metadatos de un **catálogo**.

Estos son los metadatos necesarios para describir el catálogo:

<table>
<colgroup>
    <col style="width:18%">
    <col style="width:19%">
    <col style="width:38%">
    <col style="width:25%">
  </colgroup>
  <tr>
    <td>Nombre</td>
    <td>Requerido</td>
    <td>Descripción</td>
    <td>Ejemplo</td>
  </tr>
  <tr>
    <td>Nombre</td>
    <td>Sí</td>
    <td>Nombre dado al catálogo. Debe ser claro, breve y lo suficientemente abstracto como para abarcar la multiplicidad de datasets que contiene.</td>
    <td>Datos Argentina </td>
  </tr>
  <tr>
    <td>Descripción</td>
    <td>Sí</td>
    <td>Descripción del contenido del catálogo.</td>
    <td>Portal de Datos Abiertos del Gobierno de la República Argentina</td>
  </tr>
  <tr>
    <td>Autor</td>
    <td>Sí</td>
    <td>Responsable de la publicación del catálogo.</td>
    <td>Ministerio de Modernización</td>
  </tr>
  <tr>
    <td>Correo electrónico del autor</td>
    <td>Sí</td>
    <td>Correo electrónico de contacto del responsable de la publicación del catálogo.</td>
    <td>datos@modernizacion.gob.ar</td>
  </tr>
  <tr>
    <td>Fecha de creación o publicación</td>
    <td>Recomendado</td>
    <td>Fecha de creación o publicación del catálogo. Se escribe según el formato ISO-8601, tipeado como fecha simple o fecha con hora, con el mayor detalle posible que sea relevante para el dataset.</td>
    <td>"2016-04-14T19:48:05.433640" para especificar fecha y hora<br/><br/>
    "2016-04-14" para especificar fecha únicamente</td>
  </tr>
  <tr>
    <td>Fecha de última actualización/ modificación</td>
    <td>Recomendado</td>
    <td>Fecha de última actualización/modificación del catálogo. Se escribe según el formato ISO-8601, tipeado como fecha simple o fecha con hora, con el mayor detalle posible que sea relevante para el dataset.</td>
    <td>"2016-04-19T19:48:05.433640" para especificar fecha y hora<br/><br/> "2016-04-19" para especificar fecha únicamente</td>
  </tr>
  <tr>
    <td>Idioma(s)</td>
    <td>Recomendado</td>
    <td>Lenguaje para la descripción de los metadatos de los datasets contenidos en el catálogo. Hay dos estándares ISO que pueden ser usados para este campo:<br/>
    (a) ISO 639-1 (2 letras)<br/>
    (b) ISO 639-2/T (3 letras) es el más recomendado.<br/>
    Puede definirse uno o más lenguajes en una lista.
    <a href="https://www.loc.gov/standards/iso639-2/php/code_list.php">Link a los estándares ISO</a> </td>
    <td>["es"] para un lenguaje ISO 639-1<br/>["spa", "eng"] para dos lenguajes ISO 639-2</td>
  </tr>
  <tr>
    <td>Taxonomía temática global</td>
    <td>Sí</td>
    <td>Es el sistema de clasificación temática global de la Administración Pública Nacional. Compone una lista de temas globales y está publicada en 
    <a href="http://datos.gob.ar/superThemeTaxonomy.json">http://datos.gob.ar/superThemeTaxonomy.json</a> </td>
    <td>http://datos.gob.ar/superThemeTaxonomy.json</td>
  </tr>
  <tr>
    <td>Licencia</td>
    <td>Recomendado</td>
    <td>Indica la licencia bajo la cual todos los datasets y distribuciones del catálogo están disponibles mediante un enlace a la licencia o documento de la licencia seleccionada, o mediante el título textual de la licencia tal como aparece en la lista de <a href="http://opendefinition.org/licenses/">http://opendefinition.org/licenses/</a>. recomendamos usar la licencia "Open Database License (ODbL) v1.0". Un dataset o distribución que especifique una licencia diferente, sobreescribe a la licencia general del catálogo.</td>
    <td>"http://opendatacommons.org/licenses/dbcl/1-0/" si se utiliza un enlace<br/> "Open Database License (ODbL) v1.0" si se consigna el nombre de la licencia a utilizar</td>
  </tr>
  <tr>
    <td>Página web del catálogo</td>
    <td>Recomendado</td>
    <td>Dirección web de acceso a la página principal del catálogo. Enlace a la página principal del catálogo.</td>
    <td>http://datos.gob.ar</td>
  </tr>
  <tr>
    <td>Derechos sobre el catálogo</td>
    <td>No</td>
    <td>Información sobre derechos aplicables al catálogo en el caso que no se hayan especificado en la licencia. Los datasets y sus distribuciones heredan la información sobre derechos aplicables al catálogo, a menos que especifiquen unos derechos distintos.</td>
    <td> </td>
  </tr>
  <tr>
    <td>Cobertura geográfica</td>
    <td>No</td>
    <td>El área geográfica cubierta por el catálogo. Una región o un lugar determinado. Puede tomar valores:<br/>
    a) De países y, provincias y municipios argentinos, según las recomendaciones de la "Guía para la identificación y uso de entidades interoperables”.<br/>
    b) Un área de coordenadas representada por latitud/ longitud en el orden: mínima longitud, mínima latitud, máxima longitud, máxima latitud.<br/>
    c) Un punto geográfico representado por latitud/longitud.<br/>
    d) Si la referencia geográfico no está identificada en la “Guía para la identificación y uso de entidades interoperables” indicar la URIs según geonames.org; ej : http://sws.geonames.org/6255146</td>
    <td>"ARG" es el código para la República Argentina.<br/>"06007" es el código de un departamento<br/>[-58.111111, -35.111111, -57.111111, -33.111111] es un bounding box. <br/>[-58.111111, -35.111111] es un punto geográfico. <br/>"http://sws.geonames.org/6255146"</td>
  </tr>
</table>


### Dataset

Recomendamos ver un[ ejemplo textual](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/dataset.md) de metadatos de un **dataset**.

A continuación, describimos los metadatos que se deben completar para describir un dataset a la hora de su carga o actualización en el catálogo:

 
<table>
<colgroup>
    <col style="width:18%">
    <col style="width:19%">
    <col style="width:38%">
    <col style="width:25%">
  </colgroup>
   <tr>
    <td>Nombre</td>
    <td>Requerido</td>
    <td>Descripción</td>
    <td>Ejemplo</td>
  </tr>
  <tr>
    <td>Título del dataset</td>
    <td>Sí</td>
    <td>Nombre asignado al dataset tal como será publicado. Debe ser claro y lo suficientemente abstracto como para abarcar la multiplicidad de distribuciones que contiene. Se recomienda no exceder los 100 caracteres en la mayoría de los casos. En caso de que un título más largo se juzgue necesario o relevante, este no deberá exceder los 200 caracteres.</td>
    <td>Sistema de contrataciones electrónicas</td>
  </tr>
  <tr>
    <td>Descripción del dataset</td>
    <td>Sí</td>
    <td>Descripción del contenido del dataset de un modo claro y conciso. Se recomienda no exceder los 500 caracteres en la mayoría de los casos. En caso de que una descripción más larga se juzgue necesaria o relevante, ésta no deberá exceder los 1500 caracteres.</td>
    <td>Datos correspondiente al Sistema de Contrataciones Electrónicas (Argentina Compra)</td>
  </tr>
  <tr>
    <td>Responsable</td>
    <td>Sí</td>
    <td>Responsable de la publicación del dataset. En el caso de organizaciones, detallar la estructura jerárquica separada por puntos, de manera jerárquicamente descendiente. Si la organización es parte de la Administración Pública Nacional y está listada en el dataset llamado "Estructura Organica del Poder Ejecutivo Nacional" (<a href="http://datos.gob.ar/dataset/estructura-organica-pen">http://datos.gob.ar/dataset/estructura-organica-pen</a>), deberá utilizarse la denominación allí documentada.</td>
    <td>Ministerio de Modernización. Secretaría de Modernización Administrativa. Oficina Nacional de Contrataciones.</td>
  </tr>
  <tr>
    <td>E-mail del responsable</td>
    <td>Recomendado</td>
    <td>Correo electrónico de contacto del responsable de la publicación del dataset.</td>
    <td>onc@modernizacion.gob.ar</td>
  </tr>
  <tr>
    <td>Mantenedor</td>
    <td>Recomendado</td>
    <td>Área/persona de contacto que puede brindar información relevante sobre el dataset.</td>
    <td>Ministerio de Modernización. Secretaría de Modernización Administrativa. Oficina Nacional de Contrataciones. Dirección de Compras Electrónicas.</td>
  </tr>
  <tr>
    <td>E-mail del mantenedor</td>
    <td>Recomendado</td>
    <td>Correo electrónico del área/persona de contacto que puede brindar información relevante sobre el dataset.</td>
    <td>onc-compraselectronicas@modernizacion.gob.ar</td>
  </tr>
  <tr>
    <td>Temas globales</td>
    <td>Si</td>
    <td>Temática/s o categoría/s globales a la/s que se refiere el dataset al ser publicado. Un dataset puede pertenecer a más de una categoría global, de manera que el tipo de valor de este campo es una lista de categorías. La/s categoría/s o temática/s globales deben adoptarse según el campo "Código (authority code)" del Anexo "Taxonomía temática para los datasets", que contiene una lista predefinida de temática/s globales.</td>
    <td>["ECON"]</td>
  </tr>
  <tr>
    <td>Temas específicos</td>
    <td>Recomendado</td>
    <td>Temática/s o categoría/s específica/s a la/s que se refiere el dataset al ser publicado. Un dataset puede pertenecer a más de una categoría específica, de manera que el tipo de valor de este campo es una lista de categorías. La taxonomía a utilizar debe ser creada por la autoridad responsable del Catálogo.</td>
    <td>["Contrataciones", "Compras", "Macroeconomía"]</td>
  </tr>
  <tr>
    <td>Etiquetas</td>
    <td>Recomendado</td>
    <td>Palabras que describen el título o el contenido del recurso. Es necesario que las etiquetas se encuentren correctamente escritas, en plural y respetando la existencia de tags anteriores. Etiquetas que colaboran en la búsqueda de los usuarios. Cuanto más amplia y uniforme sea la lista de tags mayor será su eficiencia. A tales fines se recomienda ver el Anexo “Pautas para la selección de etiquetas”.</td>
    <td>["bienes", "compras","contrataciones"]</td>
  </tr>
  <tr>
    <td>Frecuencia de actualización</td>
    <td>Sí</td>
    <td>Frecuencia con la que se actualiza el dataset. Se recomienda especificar períodos normalizados con formato ISO-8601, agregando el campo “eventual” para datasets que se publican con una frecuencia eventual o no especificada. Anexo "Especificación de frecuencias según ISO-8601".</td>
    <td>“R/P1Y” para datasets que se actualizan anualmente</td>
  </tr>
  <tr>
    <td>Fecha de publicación</td>
    <td>Sí</td>
    <td>Fecha de publicación del dataset. Según el formato ISO-8601, tipeado como fecha simple o fecha con hora, con el mayor detalle posible que sea relevante para el dataset.</td>
    <td>"2016-04-14T19:48:05.433640" para especificar fecha y hora<br/> "2016-04-14" para especificar fecha únicamente</td>
  </tr>
  <tr>
    <td>Idioma</td>
    <td>No</td>
    <td>Lenguaje para la descripción de los metadatos del dataset. Hay dos estándares ISO que pueden ser utilizados para este campo:<br/>
    (a) ISO 639-1 (2 letras)
    (b) ISO 639-2/T (3 letras) es el más recomendado.<br/>
    Puede definirse uno o más lenguajes en una lista. Los lenguajes especificados para un dataset, sobreesriben a los del catálogo. Si este campo está vacío el dataset hereda los lenguajes del catálogo. <a href="https://www.loc.gov/standards/iso639-2/php/code_list.php">Link a los estándares ISO</a>
    </td>
    <td>
    ["es"] para un lenguaje ISO 639-1<br/>
    ["spa", ”eng"] para dos lenguajes ISO 639-2
    </td>
  </tr>
  <tr>
    <td>Cobertura geográfica</td>
    <td>No</td>
    <td>Una región o lugar determinado al que el dataset haga referencia.
    Una región o un lugar determinado. Puede tomar valores:<br/>
    a) De países y, provincias y municipios argentinos, según las recomendaciones de la “Guía para la identificación y uso de entidades interoperables”.<br/>
    b) Un área de coordenadas representada por latitud/ longitud en el orden: minima longitud, mínima latitud, máxima longitud, máxima latitud.<br/>
    c) Un punto geográfico representado por latitud/longitud.<br/>
    d) Si la referencia geográfica no está identificada en la “Guía para la identificación y uso de entidades interoperables” indicar la URIs según geonames.org; ej:
    http://sws.geonames.org/6255146"</td>
    <td>"ARG" es el código para la República Argentina.<br/>
    "06007" es el código de un departamento<br/>
    [-58.111111, -35.111111, -57.111111, -33.111111] es un bounding box<br/>
    [-58.111111, -35.111111] es un punto geográfico <br/>
"http://sws.geonames.org/6255146"</td>
  </tr>
  <tr>
    <td>Cobertura temporal</td>
    <td>Recomendado</td>
    <td>Período de tiempo cubierto por el dataset. El intervalo de tiempo está formado por una fecha de inicio y una de fin separadas por “/”, en formato ISO 8601, con el nivel de especificidad requerido por el dataset.</td>
    <td>2015-01-01/2015-12-31<br/>2015-01-01T00:45:00Z/2016-01-15T00:06:00Z
    </td>
  </tr>
  <tr>
    <td>Fuente</td>
    <td>No</td>
    <td>URL de una página web a través de la cual se puede acceder al dataset, sus recursos o información adicional sobre el mismo.</td>
    <td>http://datos.gob.ar/dataset/sistema-de-contrataciones-electronicas-argentina-compra</td>
  </tr>
  <tr>
    <td>Licencia</td>
    <td>Recomendado</td>
    <td>Indica la licencia bajo la cual el dataset y todas sus distribuciones están disponibles mediante un enlace a la licencia o documento de la licencia seleccionada, o mediante el título textual de la licencia tal como aparece en la lista de <a href="http://opendefinition.org/licenses/">http://opendefinition.org/licenses/</a>. Recomendamos usar  la licencia "Open Database License (ODbL) v1.0". Un dataset hereda por default la licencia general del catálogo salvo que se especifique una licencia diferente en este campo. Las distribuciones del dataset heredan esta licencia salvo que especifiquen una diferente.</td>
    <td>"http://opendatacommons.org/licenses/dbcl/1-0/" si se utiliza un enlace<br/> "Open Database License (ODbL) v1.0" si se consigna el nombre de la licencia a utilizar</td>
  </tr>
</table>


 

### Distribución

Recomendamos ver un[ ejemplo textual](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/distribution.md) de metadatos de una **distribución**.

Estos son los metadatos que se deben completar al cargar o actualizar una distribución de un dataset en el catálogo para describirla:

<table>
<colgroup>
    <col style="width:18%">
    <col style="width:19%">
    <col style="width:38%">
    <col style="width:25%">
  </colgroup>
    <tr>
    <td>Nombre</td>
    <td>Requerido</td>
    <td>Descripción</td>
    <td>Ejemplo</td>
  </tr>
  <tr>
    <td>Descripción del recurso</td>
    <td>Recomendado</td>
    <td>Breve descripción de la distribución. Se recomienda no escribir más de una línea. Toda información adicional puede ser incluida en la descripción del dataset.</td>
    <td>Listado de las convocatorias abiertas durante el año 2015 en el sistema de contrataciones electrónicas</td>
  </tr>
  <tr>
    <td>Formato</td>
    <td>Recomendado</td>
    <td>Indica el formato del archivo de la distribución. Si el tipo de la distribución está definido por IANA (<a href="http://www.iana.org/assignments/media-types/media-types.xml">http://www.iana.org/assignments/media-types/media-types.xml</a>) debe usarse esa definición. En caso contrario deberán ponerse los caracteres después del punto final del archivo, que determinan el formato (cuando no está definido por IANA).</td>
    <td>"text/csv" definición de IANA "csv" caracteres finales después del punto</td>
  </tr>
  <tr>
    <td>Título del recurso</td>
    <td>Si</td>
    <td>Nombre asignado a la distribución.</td>
    <td>Convocatorias abiertas durante el año 2015</td>
  </tr>
  <tr>
    <td>Licencia</td>
    <td>Recomendado</td>
    <td>Indica la licencia bajo la cual la distribución está disponible mediante un enlace a la licencia o documento de la licencia seleccionada, o mediante el título textual de la licencia tal como aparece en la lista de <a href="http://opendefinition.org/licenses/">http://opendefinition.org/licenses/</a>. Recomendamos usar la licencia "Open Database License (ODbL) v1.0". Una distribución hereda por default la licencia del dataset al que pertenece, salvo que se especifique una licencia diferente en este campo.</td>
    <td>"http://opendatacommons.org/licenses/dbcl/1-0/" si se utiliza un enlace<br/> "Open Database License (ODbL) v1.0" si se consigna el nombre de la licencia a utilizar</td>
  </tr>
  <tr>
    <td>Derechos sobre la distribución</td>
    <td>No</td>
    <td>Información sobre derechos aplicables a la distribución que no se hayan especificado en la licencia. Si se especifican, estos derechos sobreescriben a los del catálogo. En caso contrario, las distribuciones heredan los derechos especificados para el catálogo.</td>
    <td> </td>
  </tr>
  <tr>
    <td>Campos de la distribución</td>
    <td>Recomendado</td>
    <td>Lista de campos que contiene una distribución tabular (no aplica para aquellas distribuciones que no sean tablas) y sus metadatos. Cada campo se representa con un objeto ("{}") donde se describen los metadatos especificados para la clase "field" de este perfil de metadatos (como "nombre", "tipo" y "descripción").</td>
    <td>[{...}, {...}]</td>
  </tr>
</table>


 

### Campo

Como se ve en la tabla anterior, metadatos de una distribución, recomendamos que las distribuciones tabulares incluyan algunos metadatos que ayuden a entender la información que contiene cada campo. Estos metadatos se completan en el mismo formulario que se utiliza para cargar o actualizar una distribución.

Estos son los metadatos que el responsable de cargar o actualizar una distribución de un dataset en el catálogo debe completar para describir los campos, en caso de corresponder:

 

<table>
<colgroup>
    <col style="width:18%">
    <col style="width:19%">
    <col style="width:38%">
    <col style="width:25%">
  </colgroup>
  <tr>
    <td>Nombre</td>
    <td>Requerido</td>
    <td>Descripción</td>
    <td>Ejemplo</td>
  </tr>
  <tr>
    <td>Nombre</td>
    <td>Recomendado</td>
    <td>El nombre del campo tal como se denomina en el encabezado de la distribución. Recomendamos ver la "Guía para la publicación de datos en formatos abiertos" para una adecuada elección del nombre de un campo.</td>
    <td>Ejemplo para el cuarto campo de la distribución "Convocatorias abiertas durante el año 2015", valor para el nombre: "unidad_operativa_contrataciones_desc"</td>
  </tr>
  <tr>
    <td>Tipo</td>
    <td>Recomendado</td>
    <td>El tipo de dato contenido en el campo según la lista por la librería recline.js (<a href="http://okfnlabs.org/recline/docs/models.html#types">http://okfnlabs.org/recline/docs/models.html#types</a>).
    Los tipos incluidos en esta lista son:<br/>
    string (text): valores de texto.
    number (double, float, numeric): números que puedan no ser enteros (incluyen decimales).<br/>
    integer (int): números que siempre son enteros.<br/>
    date: fecha simple expresada según el estándar ISO 8601 incluyendo únicamente año, mes y día (YYYY-MM-DD) como en "2016-02-01".<br/>
    time: tiempo expresado según el estándar ISO 8601 incluyendo únicamente horas, minutos y segundos (hh:mm:ss) como en "10:05:00".<br/>
    date-time (datetime, timestamp): fecha completa expresada según el estándar ISO 8601 incluyendo año, mes, día, horas, minutos y segundos (YYYY-MM-DDThh:mm:ssZ) como en "2016-02-01T10:05:00+03:00"<br/>
    boolean (bool): valores verdadero/falso.<br/>
    binary: representación de datos binarios base64.<br/>
    geo_point: ver estructura en  <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/geo-point.html">https://www.elastic.co/guide/en/elasticsearch/reference/current/geo-point.html.</a><br/>
    geojson: ver en <a href="http://geojson.org/">http://geojson.org/</a><br/>
    array: lista de valores.<br/>
    object (json): objeto de JSON.<br/>
    any: campo que puede contener valores de cualquier tipo.</td>
    <td>Ejemplo para el campo "unidad_operativa_contrataciones_desc" de la distribución "Convocatorias abiertas durante el año 2015", valor para tipo: "string"</td>
  </tr>
  <tr>
    <td>Descripción</td>
    <td>Recomendado</td>
    <td>La descripción de la información que contiene el campo.</td>
    <td>Ejemplo para el campo "unidad_operativa_contrataciones_desc" de la distribución "Convocatorias abiertas durante el año 2015", valor para descripción: "Organismo que realiza la convocatoria. Organismo de máximo nivel jerárquico al que pertenece la unidad operativa de contrataciones."</td>
  </tr>
</table>


### Tema

Cada catálogo de datos puede tener su propia taxonomía temática que permite clasificar a los datasets como pertenecientes a una o más categorías temáticas. Recomendamos que los temas tengan algunos metadatos que ayuden a un usuario a entenderlos mejor.

Estos son metadatos que el responsable de cargar o actualizar la taxonomía temática de un catálogo debe completar para describir los temas de la misma:

<table>
<colgroup>
    <col style="width:20%">
    <col style="width:20%">
    <col style="width:30%">
    <col style="width:30%">
  </colgroup>
  <tr>
    <td>Nombre</td>
    <td>Requerido</td>
    <td>Descripción</td>
    <td>Ejemplo</td>
  </tr>
  <tr>
    <td>Código identificador del tema</td>
    <td>Recomendado</td>
    <td>El identificador del tema.</td>
    <td>AGRI</td>
  </tr>
  <tr>
    <td>Etiqueta o título del tema</td>
    <td>Recomendado</td>
    <td>La etiqueta o título de un tema.</td>
    <td>Agricultura, pesca, silvicultura y alimentación</td>
  </tr>
  <tr>
    <td>Descripción del tema</td>
    <td>Recomendado</td>
    <td>Una breve y concisa descripción del tema.</td>
    <td>Bajo este concepto se incluyen datasets que cubren dominios tales como agricultura, pesca, forestación o alimentos.</td>
  </tr>
</table>

## Otros catálogos

Los usuarios que opten por una solución alternativa al Portal Andino para publicar sus datos, deberán publicar los metadatos de su Catálogo en un archivo *data.json* en una URL como la siguiente: *http://datos.[entidad].gob.ar/data.json*.

Este archivo deberá estar construido tal como se puede ver en el ejemplo del **Anexo IV - Ejemplo de data.json**, respetando el perfil de metadatos de la Administración Pública Nacional tal como se lo describe más adelante en la sección "*Campos del perfil*".


### Estándar usado

**El perfil de metadatos recomendado en esta guía es una adaptación del estándar DCAT - AP**, usado por los países de la Unión Europea. DCAT es un vocabulario controlado definido por la W3C, ampliamente usado a nivel global para la descripción de catálogos de datos.

Según la W3C: "Mediante la utilización de DCAT para describir datasets en catálogos de datos, quienes publican aumentan la posibilidad de descubrimiento (*discoverability*) y permiten a aplicaciones informáticas consumir metadatos de manera simple desde múltiples catálogos. Además permite la publicación descentralizada de catálogos y favorece la búsqueda ‘federada’ de datasets a través de varios sitios."

El perfil de metadatos propuesto para la Administración Pública Nacional se compone de 3 clases principales (*Catalog, Dataset y Distribution*) y 2 auxiliares (*Field* y *Theme*) que se relacionan según el siguiente esquema:

<div id="perfil-de-metadatos">

![Perfil de Metadatos](assets/der_perfil_metadatos.png)

</div>

A continuación, describimos los metadatos que el *data.json* debe contener, para cada una de estas clases.


### Campos del perfil

#### Catálogo 

Recomendamos [ver un ejemplo de metadatos de un catálogo en JSON](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/data.json).

Estos son los metadatos que el *data.json* debe contener, a nivel de catálogo:

<table class="six-columns" >
<colgroup>
    <col style="width:13%">
    <col style="width:13%">
    <col style="width:28%">
    <col style="width:20%">
    <col style="width:13%">
    <col style="width:13%">
  </colgroup>
  <tr>
    <td>Nombre</td>
    <td>Requerido</td>
    <td>Descripción</td>
    <td>Ejemplo</td>
    <td>Variable (data.json)</td>
    <td>Tipo (data.json)</td>
  </tr>
  <tr>
    <td>Datasets</td>
    <td>Sí</td>
    <td>Contiene una lista de los datasets que forman parte del catálogo.</td>
    <td>[{...}, {...}]</td>
    <td>dataset</td>
    <td>Array</td>
  </tr>
  <tr>
    <td>Nombre</td>
    <td>Sí</td>
    <td>Nombre dado al catálogo. Debe ser claro, breve y lo suficientemente abstracto como para abarcar la multiplicidad de datasets que contiene.</td>
    <td>Datos Argentina</td>
    <td>title</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Descripción</td>
    <td>Sí</td>
    <td>Descripción del contenido del catálogo.</td>
    <td>Portal de Datos Abiertos del Gobierno de la República Argentina</td>
    <td>description</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Autor</td>
    <td>Sí</td>
    <td>Responsable de la publicación del catálogo.</td>
    <td>Ministerio de Modernización</td>
    <td>publisher -> name</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Correo electrónico del autor</td>
    <td>Sí</td>
    <td>Correo electrónico de contacto del responsable de la publicación del catálogo.</td>
    <td>datos@modernizacion.gob.ar</td>
    <td>publisher -> mbox</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Fecha de creación o publicación</td>
    <td>Recomendado</td>
    <td>Fecha de creación o publicación del catálogo. Se escribe según el formato ISO-8601, tipeado como fecha simple o fecha con hora, con el mayor detalle posible que sea relevante para el dataset.</td>
    <td>"2016-04-14T19:48:05.433640" para especificar fecha y hora<br/>"2016-04-14" para especificar fecha únicamente</td>
    <td>issued</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Fecha de última actualización/ modificación</td>
    <td>Recomendado</td>
    <td>Fecha de última actualización/modificación del catálogo. Se escribe según el formato ISO-8601, tipeado como fecha simple o fecha con hora, con el mayor detalle posible que sea relevante para el dataset.</td>
    <td>"2016-04-19T19:48:05.433640" para especificar fecha y hora<br/>"2016-04-19" para especificar fecha únicamente</td>
    <td>modified</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Idioma(s)</td>
    <td>Recomendado</td>
    <td>Lenguaje para la descripción de los metadatos de los datasets contenidos en el catálogo. Hay 2 estándares ISO que pueden ser utilizados para este campo:<br/>
    (a) ISO 639-1 (2 letras)<br/>
    (b) ISO 639-2/T (3 letras) es el más recomendado.<br/>
    Puede definirse 1 o más lenguajes en una lista. (<a href="https://www.loc.gov/standards/iso639-2/php/code_list.php">Link a los estándares ISO</a>)</td>
    <td>["es"] para un lenguaje ISO 639-1<br/>
    ["spa", "eng"] para dos lenguajes ISO 639-2</td>
    <td>language</td>
    <td>Array</td>
  </tr>
  <tr>
    <td>Taxonomía temática global</td>
    <td>Sí</td>
    <td>Es el sistema de clasificación temática global de la Administración Pública Nacional. Compone una lista de temas globales y está publicada en <a href="http://datos.gob.ar/superThemeTaxonomy.json">http://datos.gob.ar/superThemeTaxonomy.json</a>.</td>
    <td>http://datos.gob.ar/superThemeTaxonomy.json</td>
    <td>superThemeTaxonomy</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Taxonomía temática específica</td>
    <td>Recomendado</td>
    <td>Es el sistema de clasificación temática específica, creado por la organización responsable del catálogo. Compone una lista de temas específicos a los datasets del catálogo. Si se clasifica algún dataset del catálogo como perteneciente a uno o más temas, este campo es obligatorio ya que se debe explicitar una taxonomía temática para poder usar sus temas.</td>
    <td>[{...}, {...}]</td>
    <td>themeTaxonomy</td>
    <td>Array</td>
  </tr>
  <tr>
    <td>Licencia</td>
    <td>Recomendado</td>
    <td>Indica la licencia bajo la cual todos los datasets y distribuciones del catálogo están disponibles mediante un enlace a la licencia o documento de la licencia seleccionada, o mediante el título textual de la licencia tal como aparece en la lista de <a href="http://opendefinition.org/licenses/">http://opendefinition.org/licenses/</a> . recomendamos usar la licencia "Open Database License (ODbL) v1.0". Un dataset o distribución que especifique una licencia diferente, sobreescribe a la licencia general del catálogo.</td>
    <td>"http://opendatacommons.org/licenses/dbcl/1-0/" si se utiliza un enlace<br/>"Open Database License (ODbL) v1.0" si se consigna el nombre de la licencia a utilizar</td>
    <td>license</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Página web del catálogo</td>
    <td>Recomendado</td>
    <td>Dirección web de acceso a la página principal del catálogo. Enlace a la página principal del catálogo.</td>
    <td>http://datos.gob.ar</td>
    <td>homepage</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Derechos sobre el catálogo</td>
    <td>No</td>
    <td>Información sobre derechos aplicables al catálogo en el caso que no se hayan especificado en la licencia. Los datasets y sus distribuciones heredan la información sobre derechos aplicables al catálogo, a menos que especifiquen unos derechos distintos.</td>
    <td></td>
    <td>rights</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Cobertura geográfica</td>
    <td>No</td>
    <td>El área geográfica cubierta por el catálogo. Una región o un lugar determinado. Puede tomar valores:<br/>
    a) De países y, provincias y municipios argentinos, según las recomendaciones de la Guía para la identificación y uso de entidades interoperables.<br/>
    b) Un área de coordenadas representada por latitud/ longitud en el orden: minima longitud, mínima latitud, máxima longitud, máxima latitud.<br/>
    c) Un punto geográfico representado por latitud/longitud.<br/>
    d) Si la referencia geográfico no está identificada en la Guía para la identificación y uso de entidades interoperables indicar la URIs según geonames.org; ej : 
    http://sws.geonames.org/6255146</td>
    <td>"ARG" es el código para la República Argentina.<br/>
    "06007" es el código de un departamento<br/>
    [-58.111111, -35.111111, -57.111111, -33.111111] es un bounding box<br/>
    [-58.111111, -35.111111] es un punto geográfico<br/>"http://sws.geonames.org/6255146"</td>
    <td>spatial</td>
    <td>String or Array</td>
  </tr>
</table>

Es importante poner atención a los dos campos que contienen una lista de objetos: **dataset** y **themeTaxonomy**.

El **primero** contendrá una lista de objetos que describen (cada uno) los metadatos de los distintos datasets que componen el catálogo (en la próxima sección se describen los metadatos que debe contener cada uno de estos objetos).

El **segundo** también contiene una lista de objetos que, juntos, definen una taxonomía temática para el catálogo. Cada uno de estos objetos contiene los metadatos que describen a cada uno de los temas de esta taxonomía. Más adelante se describen estos metadatos en la sección Tema.

#### Dataset

Recomendamos [ver un ejemplo de metadatos de un dataset en JSON](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/dataset.json).

Detallamos los metadatos que el *data.json* debe contener, para describir a un dataset dentro de la lista contenida en el campo **dataset** del catálogo:

<table  class="six-columns">
<colgroup>
    <col style="width:13%">
    <col style="width:13%">
    <col style="width:28%">
    <col style="width:20%">
    <col style="width:13%">
    <col style="width:13%">
  </colgroup>
  <tr>
    <td>Nombre</td>
    <td>Requerido</td>
    <td>Descripción</td>
    <td>Ejemplo</td>
    <td>Variable (data.json)</td>
    <td>Tipo (data.json)</td>
  </tr>
  <tr>
    <td>Título</td>
    <td>Sí</td>
    <td>Nombre asignado al dataset tal como será publicado. Debe ser claro y lo suficientemente abstracto como para abarcar la multiplicidad de distribuciones que contiene. Se recomienda no exceder los 100 caracteres en la mayoría de los casos. En caso de que un título más largo se juzgue necesario o relevante, este no deberá exceder los 200 caracteres.</td>
    <td>Sistema de contrataciones electrónicas</td>
    <td>title</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Descripción</td>
    <td>Sí</td>
    <td>Descripción del contenido del dataset de un modo claro y conciso. Se recomienda no exceder los 500 caracteres en la mayoría de los casos. En caso de que una descripción más larga se juzgue necesaria o relevante, ésta no deberá exceder los 1500 caracteres.</td>
    <td>Datos correspondiente al Sistema de Contrataciones Electrónicas (Argentina Compra)</td>
    <td>description</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Autor</td>
    <td>Sí</td>
    <td>Responsable de la publicación del dataset. En el caso de organizaciones, detallar la estructura jerárquica separada por puntos, de manera jerárquicamente descendiente. Si la organización es parte de la Administración Pública Nacional y está listada en el dataset llamado "Estructura Organica del Poder Ejecutivo Nacional" (<a href="http://datos.gob.ar/dataset/estructura-organica-pen">http://datos.gob.ar/dataset/estructura-organica-pen</a>), deberá utilizarse la denominación allí documentada.</td>
    <td>Ministerio de Modernización. Secretaría de Modernización Administrativa. Oficina Nacional de Contrataciones.</td>
    <td>publisher -> name</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Correo electrónico del autor</td>
    <td>Recomendado</td>
    <td>Correo electrónico de contacto del responsable de la publicación del dataset.</td>
    <td>onc@modernizacion.gob.ar</td>
    <td>publisher -> mbox</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Área/Persona de contacto</td>
    <td>Recomendado</td>
    <td>Área/persona de contacto que puede brindar información relevante sobre el dataset.</td>
    <td>Ministerio de Modernización. Secretaría de Modernización Administrativa. Oficina Nacional de Contrataciones. Dirección de Compras Electrónicas.</td>
    <td>contactPoint -> fn</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Correo electrónico del área/persona de contacto</td>
    <td>Recomendado</td>
    <td>Correo electrónico del área/persona de contacto que puede brindar información relevante sobre el dataset.</td>
    <td>onc-compraselectronicas@modernizacion.gob.ar</td>
    <td>contactPoint -> hasEmail</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Temática(s) globales</td>
    <td>Sí</td>
    <td>Temática/s o categoría/s globales a la/s que se refiere el dataset al ser publicado. Un dataset puede pertenecer a más de una categoría global, de manera que el tipo de valor de este campo es una lista de categorías. La/s categoría/s o temática/s globales deben adoptarse según el campo "Código (authority code)" del Anexo "Taxonomía temática para los datasets", que contiene una lista predefinida de temática/s globales.</td>
    <td>["ECON"]</td>
    <td>superTheme</td>
    <td>Array</td>
  </tr>
  <tr>
    <td>Temática(s) específicas</td>
    <td>Recomendado</td>
    <td>Temática/s o categoría/s específica/s a la/s que se refiere el dataset al ser publicado. Un dataset puede pertenecer a más de una categoría específica, de manera que el tipo de valor de este campo es una lista de categorías. La taxonomía a utilizar debe ser creada por la autoridad responsable del Catálogo. Se deben usar los ids (ver campo "id" de la clase Theme) de los temas definidos en la taxonomía para componer la lista (no se deben usar las etiquetas ni las descripciones).</td>
    <td>["Contrataciones", "Compras", "Macroeconomía"]</td>
    <td>theme</td>
    <td>Array</td>
  </tr>
  <tr>
    <td>Etiqueta(s)</td>
    <td>Recomendado</td>
    <td>Palabras que describen el título o el contenido del recurso. Es necesario que las etiquetas se encuentren correctamente escritas, en plural y respetando la existencia de tags anteriores. Etiquetas que colaboran en la búsqueda de los usuarios. Cuanto más amplia y uniforme sea la lista de tags mayor será su eficiencia. A tales fines se recomienda ver el Anexo “Pautas para la selección de etiquetas”.</td>
    <td>["bienes", "compras","contrataciones"]</td>
    <td>keyword</td>
    <td>Array</td>
  </tr>
  <tr>
    <td>Distribuciones</td>
    <td>Sí</td>
    <td>Lista de distribuciones que pertenecen al dataset y sus metadatos. Cada distribución se representa con un objeto ("{}") donde se describen los metadatos especificados para la clase "distribution" de este perfil de metadatos.</td>
    <td>[{...}, {...}]</td>
    <td>distribution</td>
    <td>Array</td>
  </tr>
  <tr>
    <td>Frecuencia de actualización</td>
    <td>Sí</td>
    <td>Frecuencia con la que se actualiza el dataset. Recomendamos especificar períodos normalizados con formato ISO-8601, agregando el campo “eventual” para datasets que se publican con una frecuencia eventual o no especificada. Anexo "Especificación de frecuencias según ISO-8601".</td>
    <td>“R/P1Y” para datasets que se actualizan anualmente</td>
    <td>accrualPeriodicity</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Fecha de publicación</td>
    <td>Sí</td>
    <td>Fecha de publicación del dataset. Según el formato ISO-8601, tipeado como fecha simple o fecha con hora, con el mayor detalle posible que sea relevante para el dataset.</td>
    <td>"2016-04-14T19:48:05.433640" para especificar fecha y hora<br/>"2016-04-14" para especificar fecha únicamente</td>
    <td>issued</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Fecha de última actualización/ modificación</td>
    <td>Recomendado</td>
    <td>Fecha de última actualización/modificación del dataset (ya sea de sus datos o de sus metadatos). Según el formato ISO-8601, tipeado como fecha simple o fecha con hora, con el mayor detalle posible que sea relevante para el dataset.</td>
    <td>"2016-04-19T19:48:05.433640" para especificar fecha y hora<br/>"2016-04-19" para especificar fecha únicamente</td>
    <td>modified</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Identificador</td>
    <td>No</td>
    <td>Identificador único del dataset, este identificador debe ser único para todo el catálogo.</td>
    <td>Un identificador único para el dataset. La URI u otro identificador único en el contexto del catálogo, ejemplo:<br/>"dataset-ejemplo-35782”</td>
    <td>identifier</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Idioma(s)</td>
    <td>No</td>
    <td>Lenguaje para la descripción de los metadatos del dataset. Hay 2 estándares ISO que pueden ser utilizados para este campo:<br/>
    (a) ISO 639-1 (2 letras)<br/>
    (b) ISO 639-2/T (3 letras) es el más recomendado.<br/>
    Puede definirse 1 o más lenguajes en una lista. Los lenguajes especificados para un dataset, sobreesriben a los del catálogo. Si este campo está vacío el dataset hereda los lenguajes del catálogo. (<a href="https://www.loc.gov/standards/iso639-2/php/code_list.php">Link a los estándares ISO</a>)</td>
    <td>["es"] para un lenguaje ISO 639-1<br/>
    ["spa", ”eng"] para dos lenguajes ISO 639-2</td>
    <td>language</td>
    <td>Array</td>
  </tr>
  <tr>
    <td>Cobertura geográfica</td>
    <td>No</td>
    <td>Una región o lugar determinado al que el dataset haga referencia.Una región o un lugar determinado. Puede tomar valores:<br/>
    a) De países y, provincias y municipios argentinos, según las recomendaciones de la Guía para la identificación y uso de entidades interoperables.<br/>
    b) Un área de coordenadas representada por latitud/ longitud en el orden: minima longitud, minima latitud, maxima longitud, maxima latitud.<br/>
    c) Un punto geográfico representado por latitud/longitud.<br/>
    d) Si la referencia geográfico no está identificada en la Guía para la identificación y uso de entidades interoperables indicar la URIs según geonames.org; ej : http://sws.geonames.org/6255146"</td>
    <td>"ARG" es el código para la República Argentina.<br/>
    "06007" es el código de un departamento<br/>
    [-58.111111, -35.111111, -57.111111, -33.111111] es un bounding box<br/>[-58.111111, -35.111111] es un punto geográfico<br/>
    "http://sws.geonames.org/6255146"</td>
    <td>spatial</td>
    <td>Array or String</td>
  </tr>
  <tr>
    <td>Cobertura temporal</td>
    <td>Recomendado</td>
    <td>Período de tiempo cubierto por el dataset. El intervalo de tiempo está formado por una fecha de inicio y una de fin separadas por “/”, en formato ISO 8601, con el nivel de especificidad requerido por el dataset.</td>
    <td>2015-01-01/2015-12-31<br/>2015-01-01T00:45:00Z/2016-01-15T00:06:00Z</td>
    <td>temporal</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Página de referencias</td>
    <td>No</td>
    <td>URL de una página web a través de la cual se puede acceder al dataset, sus recursos o información adicional sobre el mismo.</td>
    <td>http://datos.gob.ar/dataset/sistema-de-contrataciones-electronicas-argentina-compra</td>
    <td>landingPage</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Licencia</td>
    <td>Recomendado</td>
    <td>Indica la licencia bajo la cual el dataset y todas sus distribuciones están disponibles mediante un enlace a la licencia o documento de la licencia seleccionada, o mediante el título textual de la licencia tal como aparece en la lista de <a href="http://opendefinition.org/licenses/">http://opendefinition.org/licenses/</a>. Recomendamos usar la licencia "Open Database License (ODbL) v1.0". Un dataset hereda por default la licencia general del catálogo salvo que se especifique una licencia diferente en este campo. Las distribuciones del dataset heredan esta licencia salvo que especifiquen una diferente.</td>
    <td>"http://opendatacommons.org/licenses/dbcl/1-0/" si se utiliza un enlace<br/>"Open Database License (ODbL) v1.0" si se consigna el nombre de la licencia a utilizar</td>
    <td>license</td>
    <td>String</td>
  </tr>
</table>


Es importante prestar atención al campo **_distribution_** que contiene una lista de objetos que describen los metadatos de cada una de las distribuciones del daset. En la próxima sección abordaremos estos metadatos.

#### Distribución

Recomendamos [ver un ejemplo de metadatos de una distribución en JSON](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/distribution.json).

Estos son los metadatos que el *data.json* debe contener, para describir a una distribución dentro de la lista contenida en el campo **_distribution_*** *de un dataset:

<table  class="six-columns">
<colgroup>
    <col style="width:13%">
    <col style="width:13%">
    <col style="width:28%">
    <col style="width:20%">
    <col style="width:13%">
    <col style="width:13%">
  </colgroup>
  <tr>
    <td>Nombre</td>
    <td>Requerido</td>
    <td>Descripción</td>
    <td>Ejemplo</td>
    <td>Variable (data.json)</td>
    <td>Tipo (data.json)</td>
  </tr>
  <tr>
    <td>URL de acceso</td>
    <td>Sí</td>
    <td>URL que permite el acceso a la distribución del dataset. Puede ser una página, feed u otro tipo de recurso que dé acceso indirecto a las distribuciones. Si las distribuciones son solo accesibles a través de la página de referencia del dataset, debe completarse el valor de la URL de acceso a la distribución con el mismo valor de la página de referencia del dataset.</td>
    <td>http://datos.gob.ar/dataset/sistema-de-contrataciones-electronicas-argentina-compra/archivo/fa3603b3-0af7-43cc-9da9-90a512217d8a</td>
    <td>accessURL</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Descripción</td>
    <td>Recomendado</td>
    <td>Breve descripción de la distribución. Recomendamos no escribir más de una línea. Toda información adicional puede ser incluida en la descripción del dataset.</td>
    <td>Listado de las convocatorias abiertas durante el año 2015 en el sistema de contrataciones electrónicas</td>
    <td>description</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Formato del archivo</td>
    <td>Recomendado</td>
    <td>Indica el formato del archivo de la distribución. Si el tipo de la distribución está definido por IANA (http://www.iana.org/assignments/media-types/media-types.xml), debe usarse esa definición. En caso contrario deberán ponerse los caracteres después del punto final del archivo, que determinan el formato (cuando no está definido por IANA).</td>
    <td>"text/csv" definición de IANA "csv" caracteres finales después del punto</td>
    <td>format</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Tipo de archivo</td>
    <td>No</td>
    <td>Indica el tipo de archivo de la distribución, sólo si este está definido por IANA (http://www.iana.org/assignments/media-types/media-types.xml). En caso contrario este campo permanece vacío.</td>
    <td>"text/csv" definición de IANA "" cuando el formato no tiene definición en IANA</td>
    <td>mediaType</td>
    <td>String</td>
  </tr>
  <tr>
    <td>URL de descarga</td>
    <td>Sí</td>
    <td>URL que permite la descarga directa de la distribución del dataset, vincula directamente a un archivo descargable en un formato dado.</td>
    <td>http://datos.gob.ar/dataset/becaceb2-dbd0-4879-93bd-5f02bd3b8ca2/resource/bf2f67f4-9ab3-479b-a881-56b43565125e/download/contratos-2015.csv</td>
    <td>downloadURL</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Título</td>
    <td>Sí</td>
    <td>Nombre asignado a la distribución.</td>
    <td>Convocatorias abiertas durante el año 2015</td>
    <td>title</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Licencia</td>
    <td>Recomendado</td>
    <td>Indica la licencia bajo la cual la distribución está disponible mediante un enlace a la licencia o documento de la licencia seleccionada, o mediante el título textual de la licencia tal como aparece en la lista de <a href="http://opendefinition.org/licenses/">http://opendefinition.org/licenses/</a>. Recomendamos usar la licencia "Open Database License (ODbL) v1.0". Una distribución hereda por default la licencia del dataset al que pertenece, salvo que se especifique una licencia diferente en este campo.</td>
    <td>"http://opendatacommons.org/licenses/dbcl/1-0/" si se utiliza un enlace<br/> "Open Database License (ODbL) v1.0" si se consigna el nombre de la licencia a utilizar</td>
    <td>license</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Tamaño</td>
    <td>No</td>
    <td>Tamaño de la distribución en bytes. El tamaño puede ser aproximado cuando no se conozca el tamaño exacto.</td>
    <td>Ejemplo para un archivo de 5Kb aproximadamente: "5120”</td>
    <td>byteSize</td>
    <td>Integer</td>
  </tr>
  <tr>
    <td>Fecha de publicación</td>
    <td>Sí</td>
    <td>Fecha de publicación de la distribución. Según el formato ISO-8601, tipeado como fecha simple o fecha con hora, con el mayor detalle posible que sea relevante para el dataset.</td>
    <td>"2016-04-14T19:48:05.433640" para especificar fecha y hora<br/>"2016-04-14" para especificar fecha únicamente</td>
    <td>issued</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Fecha de última actualización/ modificación</td>
    <td>Recomendado</td>
    <td>Fecha de última actualización/modificación de la distribución. Según el formato ISO-8601, tipeado como fecha simple o fecha con hora, con el mayor detalle posible que sea relevante para el dataset.</td>
    <td>"2016-04-19T19:48:05.433640" para especificar fecha y hora<br/>"2016-04-19" para especificar fecha únicamente</td>
    <td>modified</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Derechos sobre la distribución</td>
    <td>No</td>
    <td>Información sobre derechos aplicables a la distribución que no se hayan especificado en la licencia. Si se especifican, estos derechos sobreescriben a los del catálogo. En caso contrario, las distribuciones heredan los derechos especificados para el catálogo.</td>
    <td></td>
    <td>rights</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Campos de la distribución</td>
    <td>Recomendado</td>
    <td>Lista de campos que contiene una distribución tabular (no aplica para aquellas distribuciones que no sean tablas) y sus metadatos. Cada campo se representa con un objeto ("{}") donde se describen los metadatos especificados para la clase "field" de este perfil de metadatos (como "nombre", "tipo" y "descripción").</td>
    <td>[{...}, {...}]</td>
    <td>field</td>
    <td>Array</td>
  </tr>
</table>


Recomendamos poner atención al campo **_field_** que contiene una lista de objetos que describen los metadatos de cada uno de los campos de la distribución (en el caso de distribuciones tabulares, únicamente). En la próxima sección abordaremos estos metadatos.

#### Campo

Recomendamos [ver un ejemplo de metadatos de un campo en JSON](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/field.json).

Estos son los metadatos que el *data.json* debe contener para describir a un campo de una distribución tabular dentro de la lista contenida en el campo de metadatos **_field_** de una distribución:

<table  class="six-columns">
<colgroup>
    <col style="width:13%">
    <col style="width:13%">
    <col style="width:28%">
    <col style="width:20%">
    <col style="width:13%">
    <col style="width:13%">
  </colgroup>
  <tr>
    <td>Nombre</td>
    <td>Requerido</td>
    <td>Descripción</td>
    <td>Ejemplo</td>
    <td>Variable (data.json)</td>
    <td>Tipo (data.json)</td>
  </tr>
  <tr>
    <td>Nombre</td>
    <td>Recomendado</td>
    <td>El nombre del campo tal como se denomina en el encabezado de la distribución. Véase la Guía para la publicación de datos en formatos abiertos para una adecuada elección del nombre de un campo.</td>
    <td>Ejemplo para el cuarto campo de la distribución "Convocatorias abiertas durante el año 2015", valor para el nombre: "unidad_operativa_contrataciones_desc"</td>
    <td>title</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Tipo</td>
    <td>Recomendado</td>
    <td>El tipo de dato contenido en el campo según la lista utilizada por la librería recline.js (<a href="http://okfnlabs.org/recline/docs/models.html#types">http://okfnlabs.org/recline/docs/models.html#types</a>).
    Los tipos incluidos en esta lista son:<br/>
    string (text): Valores de texto.<br/>
    number (double, float, numeric): Números que puedan no ser enteros (incluyen decimales).<br/>
    integer (int): Números que siempre son enteros.<br/>
    date: Fecha simple expresada según el estándar ISO 8601 incluyendo únicamente año, mes y día (YYYY-MM-DD) como en "2016-02-01".<br/>
    time: Tiempo expresado según el estándar ISO 8601 incluyendo únicamente horas, minutos y segundos (hh:mm:ss) como en "10:05:00".<br/>
    date-time (datetime, timestamp): Fecha completa expresada según el estándar ISO 8601 incluyendo año, mes, día, horas, minutos y segundos (YYYY-MM-DDThh:mm:ssZ) como en "2016-02-01T10:05:00+03:00"<br/>
    boolean (bool): Valores verdadero/falso.<br/>
    binary: Representación de datos binarios base64.<br/>
    geo_point: Ver estructura en  <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/geo-point.html">https://www.elastic.co/guide/en/elasticsearch/reference/current/geo-point.html.</a><br/>
    geojson: ver en <a href="http://geojson.org/">http://geojson.org/</a><br/>
    array: Lista de valores.<br/>
    object (json): Objeto de JSON.<br/>
    any: Campo que puede contener valores de cualquier tipo.</td>
    <td>Ejemplo para el campo "unidad_operativa_contrataciones_desc" de la distribución "Convocatorias abiertas durante el año 2015", valor para tipo: "string"</td>
    <td>type</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Descripción</td>
    <td>Recomendado</td>
    <td>La descripción de la información que contiene el campo.</td>
    <td>Ejemplo para el campo "unidad_operativa_contrataciones_desc" de la distribución "Convocatorias abiertas durante el año 2015", valor para descripción: "Organismo que realiza la convocatoría. Organismo de máximo nivel jerárquico al que pertenece la unidad operativa de contrataciones."</td>
    <td>description</td>
    <td>String</td>
  </tr>
</table>


#### Tema

Recomendamos [ver un ejemplo de metadatos de un campo en JSON](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/theme.json).

Estos son los metadatos que el *data.json* debe contener, para describir a un tema de la taxonomía temática de un catálogo:

<table class="six-columns">
  <tr>
    <td>Nombre</td>
    <td>Requerido</td>
    <td>Descripción</td>
    <td>Ejemplo</td>
    <td>Variable (data.json)</td>
    <td>Tipo (data.json)</td>
  </tr>
  <tr>
    <td>Identificador</td>
    <td>Recomendado</td>
    <td>El identificador del tema.</td>
    <td>AGRI</td>
    <td>id</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Etiqueta</td>
    <td>Recomendado</td>
    <td>La etiqueta o título de un tema.</td>
    <td>Agricultura, pesca, silvicultura y alimentación</td>
    <td>label</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Descripción</td>
    <td>Recomendado</td>
    <td>Una breve y concisa descripción del tema.</td>
    <td>Bajo este concepto se incluyen datasets que cubren dominios tales como agricultura, pesca, forestación o alimentos.</td>
    <td>description</td>
    <td>String</td>
  </tr>
</table>


## Anexo I - Taxonomía temática global de la APN para los datasets (tabla)

El Portal Nacional de Datos usa la [taxonomía temática definida por la Unión Europea](http://publications.europa.eu/mdr/authority/data-theme/index.html).

**Cada catálogo de datos puede desarrollar su propia taxonomía**, cuyo uso se expresa en  los siguientes campos de metadatos (y sus equivalentes para el Portal Andino):

* **themeTaxonomy**: es un campo de metadatos del catálogo que define una lista de temas que se pueden usar para clasificar los datasets. Refiere al esquema completo de la taxonomía en sí, no a alguna de sus etiquetas en particular.

* **theme**: es un campo de metadatos de un Dataset. Refiere a la/s etiqueta/s en particular bajos la/s cuales un dataset es clasificado temáticamente. Sólo pueden usarse etiquetas que estén definidas en la taxonomía temática de *themeTaxonomy*.

Además del uso de una taxonomía propia de cada catálogo de datos, **recomendamos la clasificación de los datasets según la taxonomía del Portal Nacional de Datos.** Esta es una *súper taxonomía* a la que cada catálogo hace referencia mediante los siguientes campos de metadatos (y sus equivalentes para el Portal Andino):

* **superThemeTaxonomy**: es un campo de metadatos del catálogo que apunta a la URL donde el Portal Nacional de Datos documenta la taxonomía temática de la Administración Pública Nacional.

* **superTheme**: es un campo de metadatos de un dataset. Refiere a la/s etiqueta/s en particular bajos la/s cuales un dataset es clasificado temáticamente, según la *súper taxonomía* que es la de la Administración Pública Nacional. Sólo pueden usarse etiquetas que estén definidas en la taxonomía temática de *superThemeTaxonomy*.

**La ventaja de usar una súper taxonomía** temática es que** facilita la clasificación de datasets** por parte de un usuario según un conjunto de categorías temáticas más generales, que son interoperables con las usadas por otros países del mundo. Esto, a su vez, **facilita la clasificación de datasets cosechados por el Portal Nacional de Datos**.

<table>
  <colgroup>
    <col style="width:33%">
    <col style="width:33%">
    <col style="width:33%">
  </colgroup>
  <tbody>
    <tr>
      <td>Código (authority code)</td>
      <td>Etiqueta (label)</td>
      <td>Descripción (description)</td>
    </tr>
    <tr>
      <td>AGRI</td>
      <td>Agroganadería, pesca y forestación</td>
      <td>Por ejemplo: 'Lechería: precio pagado al productor' o 'Superficie forestada'.</td>
    </tr>
    <tr>
      <td>ECON</td>
      <td>Economía y finanzas</td>
      <td>Por ejemplo: 'Deuda pública'.</td>
    </tr>
    <tr>
      <td>EDUC</td>
      <td>Educación, cultura y deportes</td>
      <td>Por ejemplo: 'Registro de Establecimientos Educativos'.</td>
    </tr>
    <tr>
      <td>ENER</td>
      <td>Energía</td>
      <td>Por ejemplo: 'Productos mineros exportados' o 'Precios del GNC'.</td>
    </tr>
    <tr>
      <td>ENVI</td>
      <td>Medio ambiente</td>
      <td>Por ejemplo: 'Operadores de residuos peligrosos'.</td>
    </tr>
    <tr>
      <td>GOVE</td>
      <td>Gobierno y sector público</td>
      <td>Por ejemplo: 'Inmuebles del estado Nacional'.</td>
    </tr>
    <tr>
      <td>HEAL</td>
      <td>Salud</td>
      <td>Por ejemplo: 'Estadísticas nacionales de VIH/SIDA'.</td>
    </tr>
    <tr>
      <td>INTR</td>
      <td>Asuntos internacionales</td>
      <td>Por ejemplo: 'Representaciones argentinas en el exterior'.</td>
    </tr>
    <tr>
      <td>JUST</td>
      <td>Justicia, seguridad y legales</td>
      <td>Por ejemplo:'Censo penitenciario'.</td>
    </tr>
    <tr>
      <td>REGI</td>
      <td>Regiones y ciudades</td>
      <td>Por ejemplo: 'Departamentos de la provincia de Río Negro'.</td>
    </tr>
    <tr>
      <td>SOCI</td>
      <td>Población y sociedad</td>
      <td>Por ejemplo: 'Turistas residentes que viajan por Argentina'.</td>
    </tr>
    <tr>
      <td>TECH</td>
      <td>Ciencia y tecnología</td>
      <td>Por ejemplo: 'Recursos humanos en ciencia y tecnología'.</td>
    </tr>
    <tr>
      <td>TRAN</td>
      <td>Transporte</td>
      <td>Por ejemplo: 'Estadísticas viales'.</td>
    </tr>
    </tbody>
</table>

## Anexo II - Pautas para la selección de etiquetas

Elegir buenas etiquetas hace más fácil la búsqueda de datasets para los usuarios. Cuanto más amplia y uniforme sea la lista de etiquetas, mayor será su efectividad.

Estas son pautas para definir etiquetas aplicables a la propiedad *keyword* de la clase dataset:

* Escribir correctamente y en plural.

* Usar mayúsculas sólo donde corresponda.

* Identificar palabras claves.

* Respetar la existencia de etiquetas anteriores.

* Agregar sinónimos y emplear lenguaje natural.

* Usar una sóla palabra. Si es muy necesario, usar más de una. 

* Si la etiqueta tiene más de una palabra, debe estar separada por un espacio, ej: "declaraciones juradas".

Preguntas útiles a la hora de pensar los etiquetas:

* ¿Cuál es el tema?

* ¿Qué aspectos serán de interés para los usuarios?

* ¿De qué otro modo buscaría sobre esta información?

* ¿De qué tipo de información se trata?

* ¿Qué área la provee?

## Anexo III - Especificación de frecuencias (según ISO-8601)

<table>
  <tr>
    <td>Frecuencia</td>
    <td>Valor según ISO-8601</td>
  </tr>
  <tr>
    <td>Cada diez años</td>
    <td>R/P10Y</td>
  </tr>
  <tr>
    <td>Cada cuatro años</td>
    <td>R/P4Y</td>
  </tr>
  <tr>
    <td>Cada tres años</td>
    <td>R/P3Y</td>
  </tr>
  <tr>
    <td>Cada dos años</td>
    <td>R/P2Y</td>
  </tr>
  <tr>
    <td>Anualmente</td>
    <td>R/P1Y</td>
  </tr>
  <tr>
    <td>Cada medio año</td>
    <td>R/P6M</td>
  </tr>
  <tr>
    <td>Cuatrimestralmente</td>
    <td>R/P4M</td>
  </tr>
  <tr>
    <td>Trimestralmente</td>
    <td>R/P3M</td>
  </tr>
  <tr>
    <td>Bimestralmente</td>
    <td>R/P2M</td>
  </tr>
  <tr>
    <td>Mensualmente</td>
    <td>R/P1M</td>
  </tr>
  <tr>
    <td>Cada 15 días</td>
    <td>R/P0.5M</td>
  </tr>
  <tr>
    <td>Tres veces por mes</td>
    <td>R/P0.33M</td>
  </tr>
  <tr>
    <td>Semanalmente</td>
    <td>R/P1W</td>
  </tr>
  <tr>
    <td>Dos veces a la semana</td>
    <td>R/P0.5W</td>
  </tr>
  <tr>
    <td>Tres veces a la semana</td>
    <td>R/P0.33W</td>
  </tr>
  <tr>
    <td>Diariamente</td>
    <td>R/P1D</td>
  </tr>
  <tr>
    <td>Cada hora</td>
    <td>R/PT1H</td>
  </tr>
  <tr>
    <td>Continuamente actualizado</td>
    <td>R/PT1S</td>
  </tr>
  <tr>
    <td>Eventual</td>
    <td>eventual</td>
  </tr>
</table>


## Anexo IV - Ejemplo de data.json

Este es un [ejemplo de data.json](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/data.json):

```json
{
  "title": "Datos Argentina",
  "description": "Portal de Datos Abiertos del Gobierno de la República Argentina",
  "publisher": {
    "name": "Ministerio de Modernización",
    "mbox": "datos@modernizacion.gob.ar"
  },
  "issued": "2016-04-14T19:48:05.433640-03:00",
  "modified": "2016-04-19T19:48:05.433640-03:00",
  "language": [
    "spa"
  ],
  "superThemeTaxonomy": "http://datos.gob.ar/superThemeTaxonomy.json",
  "themeTaxonomy": [
    {
      "id": "convocatorias",
      "label": "Convocatorias",
      "description": "Datasets sobre licitaciones en estado de convocatoria."
    },
    {
      "id": "compras",
      "label": "Compras",
      "description": "Datasets sobre compras realizadas."
    },
    {
      "id": "contrataciones",
      "label": "Contrataciones",
      "description": "Datasets sobre contrataciones."
    },
    {
      "id": "adjudicaciones",
      "label": "Adjudicaciones",
      "description": "Datasets sobre licitaciones adjudicadas."
    },
    {
      "id": "normativa",
      "label": "Normativa",
      "description": "Datasets sobre normativa para compras y contrataciones."
    },
    {
      "id": "proveedores",
      "label": "Proveedores",
      "description": "Datasets sobre proveedores del Estado."
    }
  ],
  "license": "Open Data Commons Open Database License 1.0",
  "homepage": "http://datos.gob.ar",
  "rights": "Derechos especificados en la licencia.",
  "spatial": "ARG",
  "dataset": [
    {
      "title": "Sistema de contrataciones electrónicas",
      "description": "Datos correspondientes al Sistema de Contrataciones Electrónicas (Argentina Compra)",
      "publisher": {
        "name": "Ministerio de Modernización. Secretaría de Modernización Administrativa. Oficina Nacional de Contrataciones",
        "mbox": "onc@modernizacion.gob.ar"
      },
      "contactPoint": {
        "fn": "Ministerio de Modernización. Secretaría de Modernización Administrativa. Oficina Nacional de Contrataciones. Dirección de Compras Electrónicas.",
        "hasEmail": "onc-compraselectronicas@modernizacion.gob.ar"
      },
      "superTheme": [
        "ECON"
      ],
      "theme": [
        "contrataciones",
        "compras",
        "convocatorias"
      ],
      "keyword": [
        "bienes",
        "compras",
        "contrataciones"
      ],
      "accrualPeriodicity": "R/P1Y",
      "issued": "2016-04-14T19:48:05.433640-03:00",
      "modified": "2016-04-19T19:48:05.433640-03:00",
      "identifier": "99db6631-d1c9-470b-a73e-c62daa32c420",
      "language": [
        "spa"
      ],
      "spatial": "ARG",
      "temporal": "2015-01-01/2015-12-31",
      "landingPage": "http://datos.gob.ar/dataset/sistema-de-contrataciones-electronicas-argentina-compra",
      "license": "Open Data Commons Open Database License 1.0",
      "distribution": [
        {
          "accessURL": "http://datos.gob.ar/dataset/sistema-de-contrataciones-electronicas-argentina-compra/archivo/fa3603b3-0af7-43cc-9da9-90a512217d8a",
          "description": "Listado de las convocatorias abiertas durante el año 2015 en el sistema de contrataciones electrónicas",
          "format": "CSV",
          "mediaType": "text/csv",
          "downloadURL": "http://186.33.211.253/dataset/99db6631-d1c9-470b-a73e-c62daa32c420/resource/4b7447cb-31ff-4352-96c3-589d212e1cc9/download/convocatorias-abiertas-anio-2015.csv",
          "title": "Convocatorias abiertas durante el año 2015",
          "license": "Open Data Commons Open Database License 1.0",
          "byteSize": "5120",
          "issued": "2016-04-14T19:48:05.433640-03:00",
          "modified": "2016-04-19T19:48:05.433640-03:00",
          "rights": "Derechos especificados en la licencia.",
          "field": [
            {
              "title": "procedimiento_id",
              "type": "integer",
              "description": "Identificador único del procedimiento de contratación"
            },
            {
              "title": "organismo_unidad_operativa_contrataciones_id",
              "type": "integer",
              "description": "Identificador único del organismo que realiza la convocatoria. Organismo de máximo nivel jerárquico al que pertenece la unidad operativa de contrataciones."
            },
            {
              "title": "unidad_operativa_contrataciones_id",
              "type": "integer",
              "description": "Identificador único de la unidad operativa de contrataciones"
            },
            {
              "title": "organismo_unidad_operativa_contrataciones_desc",
              "type": "string",
              "description": "Organismo que realiza la convocatoria. Organismo de máximo nivel jerárquico al que pertenece la unidad operativa de contrataciones."
            },
            {
              "title": "unidad_operativa_contrataciones_desc",
              "type": "string",
              "description": "Unidad operativa de contrataciones."
            },
            {
              "title": "tipo_procedimiento_contratacion",
              "type": "string",
              "description": "Tipo de procedimiento al que se adecua la contratación."
            },
            {
              "title": "ejercicio_procedimiento_anio",
              "type": "date",
              "description": "Año en el que se inició el proceso de la convocatoria."
            },
            {
              "title": "fecha_publicacion_convocatoria",
              "type": "date",
              "description": "Fecha de publicación de la convocatoria en formato AAAA-MM-DD, ISO 8601."
            },
            {
              "title": "modalidad_convocatoria",
              "type": "string",
              "description": "Modalidad bajo la cual se realiza la convocatoria."
            },
            {
              "title": "clase_convocatoria",
              "type": "string",
              "description": "Clase de la convocatoria."
            },
            {
              "title": "objeto_convocatoria",
              "type": "string",
              "description": "Objeto/objetivo de la convocatoria"
            }
          ]
        }
      ]
    }
  ]
}
```

## Anexo V - Taxonomía temática global de la APN para los datasets (JSON)

Esta es la [taxonomía temática global](https://raw.githubusercontent.com/datosgobar/paquete-apertura-datos/master/standards/metadata/superThemeTaxonomy.json):

```json
[
    {
        "id": "AGRI",
        "label": "Agroganadería, pesca y forestación",
        "description": "Por ejemplo: “Lechería: precio pagado al productor” o “Superficie forestada”."
    },
    {
        "id": "ECON",
        "label": "Economía y finanzas",
        "description": "Por ejemplo: “Deuda pública”."
    },
    {
        "id": "EDUC",
        "label": "Educación, cultura y deportes",
        "description": "Por ejemplo: “Registro de Establecimientos Educativos”."
    },
    {
        "id": "ENER",
        "label": "Energía",
        "description": "Por ejemplo: “Productos mineros exportados” o “Precios del GNC”."
    },
    {
        "id": "ENVI",
        "label": "Medio ambiente",
        "description": "Por ejemplo: “Operadores de residuos peligrosos”."
    },
    {
        "id": "GOVE",
        "label": "Gobierno y sector público",
        "description": "Por ejemplo: “Inmuebles del estado Nacional”."
    },
    {
        "id": "HEAL",
        "label": "Salud",
        "description": "Por ejemplo: “Estadísticas nacionales de VIH/SIDA”."
    },
    {
        "id": "INTR",
        "label": "Asuntos internacionales",
        "description": "Por ejemplo: “Representaciones argentinas en el exterior”."
    },
    {
        "id": "JUST",
        "label": "Justicia, seguridad y legales",
        "description": "Por ejemplo:”Censo penitenciario”."
    },
    {
        "id": "REGI",
        "label": "Regiones y ciudades",
        "description": "Por ejemplo: “Departamentos de la provincia de Río Negro”."
    },
    {
        "id": "SOCI",
        "label": "Población y sociedad",
        "description": "Por ejemplo: “Turistas residentes que viajan por Argentina”."
    },
    {
        "id": "TECH",
        "label": "Ciencia y tecnología",
        "description": "Por ejemplo: “Recursos humanos en ciencia y tecnología”."
    },
    {
        "id": "TRAN",
        "label": "Transporte",
        "description": "Por ejemplo: “Estadísticas viales”."
    }
]
```

## Anexo VI - Ejemplo de metadatos como texto

Este es un [ejemplo en markdown](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/data.md):

**Catálogo: Datos Argentina**

Portal de Datos Abiertos del Gobierno de la República Argentina

* Derechos sobre el catálogo: Derechos especificados en la licencia.

* Correo electrónico del autor: datos@modernizacion.gob.ar

* Autor: Ministerio de Modernización

* Licencia: Open Data Commons Open Database License 1.0

* Idioma(s): spa

* Fecha de creación o publicación: 2016-04-14T19:48:05.433640-03:00

* Taxonomía temática global: [http://datos.gob.ar/superThemeTaxonomy.json](http://datos.gob.ar/superThemeTaxonomy.json)

* Fecha de última actualización/modificación: 2016-04-19T19:48:05.433640-03:00

* Cobertura geográfica: ARG

* Página web del catálogo: [http://datos.gob.ar](http://datos.gob.ar/)

**Taxonomía temática específica**

* Convocatorias (convocatorias): Datasets sobre licitaciones en estado de convocatoria.

* Compras (compras): Datasets sobre compras realizadas.

* Contrataciones (contrataciones): Datasets sobre contrataciones.

* Adjudicaciones (adjudicaciones): Datasets sobre licitaciones adjudicadas.

* Normativa (normativa): Datasets sobre normativa para compras y contrataciones.

* Proveedores (proveedores): Datasets sobre proveedores del Estado.

**Datasets**

**Dataset: Sistema de contrataciones electrónicas**

Datos correspondientes al Sistema de Contrataciones Electrónicas (Argentina Compra)

* **Correo electrónico del autor**: onc@modernizacion.gob.ar

* **Autor**: Ministerio de Modernización. Secretaría de Modernización Administrativa. Oficina Nacional de Contrataciones

* **Página de referencias**: [http://datos.gob.ar/dataset/sistema-de-contrataciones-electronicas-argentina-compra](http://datos.gob.ar/dataset/sistema-de-contrataciones-electronicas-argentina-compra)

* **Temática(s) globales**: ECON

* **Fecha de publicación**: 2016-04-14T19:48:05.433640-03:00

* **Cobertura temporal**: 2015-01-01/2015-12-31

* **Fecha de última actualización/ modificación**: 2016-04-19T19:48:05.433640-03:00

* **Idioma(s)**: spa

* **Temática(s) específicas**: contrataciones, compras, convocatorias

* **Etiqueta(s)**: bienes, compras, contrataciones

* **Frecuencia de actualización**: R/P1Y

* **Cobertura geográfica**: ARG

* **Licencia**: Open Data Commons Open Database License 1.0

* **Correo electrónico del área/persona de contacto**: onc-compraselectronicas@modernizacion.gob.ar

* **Área/Persona de contacto**: Ministerio de Modernización. Secretaría de Modernización Administrativa. Oficina Nacional de Contrataciones. Dirección de Compras Electrónicas.

* **Identificador**: 99db6631-d1c9-470b-a73e-c62daa32c420

*Distribuciones*

**Distribución: Convocatorias abiertas durante el año 2015**

Listado de las convocatorias abiertas durante el año 2015 en el sistema de contrataciones electrónicas

* **URL de acceso**: [http://datos.gob.ar/dataset/sistema-de-contrataciones-electronicas-argentina-compra/archivo/fa3603b3-0af7-43cc-9da9-90a512217d8a](http://datos.gob.ar/dataset/sistema-de-contrataciones-electronicas-argentina-compra/archivo/fa3603b3-0af7-43cc-9da9-90a512217d8a)

* **Derechos sobre la distribución**: Derechos especificados en la licencia.

* **Licencia**: Open Data Commons Open Database License 1.0

* **Tamaño**: 5120

* **Formato del archivo**: CSV

* **Tipo de archivo**: text/csv

* **Fecha de última actualización/ modificación**: 2016-04-19T19:48:05.433640-03:00

* **URL de descarga**: [http://datos.gob.ar/dataset/069b5833-e57d-4d7a-859b-67a80cfdff20/resource/fa3603b3-0af7-43cc-9da9-90a512217d8a/download/convocatorias-2015.csv](http://datos.gob.ar/dataset/069b5833-e57d-4d7a-859b-67a80cfdff20/resource/fa3603b3-0af7-43cc-9da9-90a512217d8a/download/convocatorias-2015.csv)

* **Fecha de publicación**: 2016-04-14T19:48:05.433640-03:00

*Campos de la distribución*

* **procedimiento_id** (integer): Identificador único del procedimiento de contratación

* **organismo_unidad_operativa_contrataciones_id** (integer): Identificador único del organismo que realiza la convocatoria. Organismo de máximo nivel jerárquico al que pertenece la unidad operativa de contrataciones.

* **unidad_operativa_contrataciones_id** (integer): Identificador único de la unidad operativa de contrataciones

* **organismo_unidad_operativa_contrataciones_desc** (string): Organismo que realiza la convocatoria. Organismo de máximo nivel jerárquico al que pertenece la unidad operativa de contrataciones.

* **unidad_operativa_contrataciones_desc** (string): Unidad operativa de contrataciones.

* **tipo_procedimiento_contratacion** (string): Tipo de procedimiento al que se adecua la contratación.

* **ejercicio_procedimiento_anio** (date): Año en el que se inició el proceso de la convocatoria.

* **fecha_publicacion_convocatoria** (date): Fecha de publicación de la convocatoria en formato AAAA-MM-DD, ISO 8601.

* **modalidad_convocatoria** (string): Modalidad bajo la cual se realiza la convocatoria.

* **clase_convocatoria** (string): Clase de la convocatoria.

* **objeto_convocatoria** (string): Objeto/objetivo de la convocatoria

