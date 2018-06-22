# Guía para el uso y la publicación de metadatos

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

## Indice

- [Versión](#version)
- [Glosario](#glosario)
- [Introducción](#introduccion)
  - [Objetivo de esta guía](#objetivo-de-esta-guia)
  - [¿Qué son los metadatos?](#que-son-los-metadatos)
  - [¿Cómo se publican los metadatos?](#como-se-publican-los-metadatos)
  - [Público objetivo de esta guía](#publico-objetivo-de-esta-guia)
- [Perfil de Metadatos](#perfil-de-metadatos)
  - [Portal Andino](#portal-andino)
  - [Otros catálogos](#otros-catalogos)
  - [Estándar usado](#estandar-usado)
  - [Campos del perfil](#campos-del-perfil)
    - [Catálogo (`catalog`)](#catalogo-catalog)
    - [Dataset (`dataset`)](#dataset-dataset)
    - [Distribución (`distribution`)](#distribucion-distribution)
    - [Campo (`field`)](#campo-field)
    - [Tema (`theme`)](#tema-theme)
- [Extensiones especiales](#extensiones-especiales)
  - [Series de tiempo](#series-de-tiempo)
    - [Distribución de series de tiempo](#distribucion-de-series-de-tiempo)
    - [Tipo especial: indice de tiempo](#tipo-especial-indice-de-tiempo)
    - [Documentar un dataset de series de tiempo](#documentar-un-dataset-de-series-de-tiempo)
      - [Dataset (`dataset`) - series de tiempo](#dataset-dataset-series-de-tiempo)
      - [Distribución (`distribution`) - series de tiempo](#distribucion-distribution-series-de-tiempo)
      - [Campo (`field`) - series de tiempo](#campo-field-series-de-tiempo)
- [Anexo I - Taxonomía temática global de la APN para los datasets (tabla)](#anexo-i-taxonomia-tematica-global-de-la-apn-para-los-datasets-tabla)
- [Anexo II - Pautas para la selección de etiquetas](#anexo-ii-pautas-para-la-seleccion-de-etiquetas)
- [Anexo III - Especificación de frecuencias (según ISO-8601)](#anexo-iii-especificacion-de-frecuencias-segun-iso-8601)
- [Anexo IV - Ejemplo de data.json](#anexo-iv-ejemplo-de-datajson)
- [Anexo V - Taxonomía temática global de la APN para los datasets (JSON)](#anexo-v-taxonomia-tematica-global-de-la-apn-para-los-datasets-json)
- [Anexo VI - Ejemplo de metadatos como texto](#anexo-vi-ejemplo-de-metadatos-como-texto)
- [Anexo VII - Ejemplo de data.json con series de tiempo](#anexo-vii-ejemplo-de-datajson-con-series-de-tiempo)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Versión

Esta guía es compatible con la **versión 1.1 del Perfil de Metadatos** de la Política de Apertura de Datos de la Administración Pública Nacional.

## Glosario

**Activo de datos**

Es cualquier **colección de datos con valor informativo**, de propiedad de una entidad u organismo, que reflejan su actividad y son relevantes para el desarrollo de sus misiones y funciones, o para los actores de su ecosistema. Aunque puede designar piezas aisladas de información, suele emplearse para **identificar y tratar conjuntos de datos** que pueden ser comprendidos y tratados **como una única unidad a efectos de su gestión, uso, protección e intercambio**.

**Distribución o recurso**

**Es la unidad mínima de un catálogo de datos**. Se trata de los activos de datos que se publican allí y que pueden ser descargados y re-utilizados por un usuario como archivos. Los recursos **pueden tener diversos formatos** (.csv, .shp, etc.). Están acompañados de información contextual asociada ("metadata") que describe el tipo de información que se publica, el proceso por el cual se obtiene, la descripción de los campos del recurso y cualquier información extra que facilite su interpretación, procesamiento y lectura.

**Dataset**

**También llamado _conjunto de datos,_ es la pieza principal en todo catálogo**. Se trata de un activo de datos que agrupa recursos referidos a un mismo tema, que respetan una estructura de la información. Los recursos que lo componen pueden diferir en el formato en que se los presenta (por ejemplo: .csv, .json, .xls, etc.), la fecha a la que se refieren, el área geográfica cubierta, ser tablas de un mismo esquema de base de datos relacional o estar separados bajo algún otro criterio.

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

**La publicación de los metadatos puede ser muy diversa** en detalle, calidad y forma. **Una publicación muy elemental es un documento de texto** que ofrece una descripción del dataset y de cada uno de los recursos que lo componen. Es posible ver un [ejemplo textual](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/data.md) de los metadatos de un catálogo de datos en el **[Anexo VI - Ejemplo de metadatos como texto](#anexo-vi-ejemplo-de-metadatos-como-texto)**.

Sin embargo, **las computadoras no pueden leer fácilmente documentos de texto**. La organización sistemática de colecciones de datasets (es decir, la creación de un **catálogo** de datos) exige un nivel de complejidad mayor para facilitar su descubrimiento, indexación, y reutilización por parte de scripts y aplicaciones de todo tipo.

La potencial reutilización de los conjuntos de datos y la posibilidad de que los mismos sean correctamente federados desde el Portal Nacional de Datos Abiertos (datos.gob.ar) dependerá de la calidad de sus metadatos. Adoptar y/o desarrollar estándares y vocabularios controlados es importante para la lectura e interpretación de los conjuntos de datos por personas y por aplicaciones informáticas.

Para esto, **los catálogos de datos publican sus metadatos en un formato estructurado (JSON)** respetando un determinado perfil estandarizado. Recomendamos ver un [ejemplo en JSON](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/data.json) de los metadatos de un catálogo de datos en el **[Anexo IV - Ejemplo de data.json](#anexo-iv-ejemplo-de-datajson)**.

En el resto de este documento detallamos las características de los estándares y vocabularios controlados adoptados para catálogos de datos, datasets y distribuciones.

### Público objetivo de esta guía

Esta guía intenta ayudar a quienes:

* **Publican sus catálogos de datos mediante un adaptación del portal Andino**. Es decir,  del portal que el equipo de Datos de la Nación Argentina diseñó sobre la base de CKAN y que pueden adoptar las dependencias de la Administración Pública Nacional (así como también de otros niveles gubernamentales sub-nacionales o incluso entidades del público general) para gestionar la publicación centralizada de sus activos de datos.

    Si estás dentro de este grupo, **recomendamos leer la sección [Portal Andino](#portal-andino)**. Con ella, podrás comprender cómo completar cada campo en el formulario web del Portal Andino.

* **Publican sus catálogos de datos mediante otros medios**. Esto es, en forma directa en el dominio digital de la entidad responsable o de alguna forma alternativa en la red. Esas entidades deberán publicar su catálogo de datos en un archivo estructurado (JSON) llamado *data.json* alojado en un dominio de la forma *http://datos.[entidad].gob.ar/data.json* siguiendo las especificaciones del perfil de metadatos de esta guía.

    Si la apertura de tus datos se inscribe en esta modalidad, **te sugerimos leer la sección [Otros catálogos](#otros-catalogos)**. Te ayudará a comprender cómo generar y publicar un archivo *data.json* que cumpla con el perfil de metadatos de la política de apertura de datos de la Administración Pública Nacional.

## Perfil de Metadatos

### Portal Andino

**El [Portal Andino](https://github.com/datosgobar/portal-andino)** es una herramienta especialmente diseñada para facilitar la publicación y apertura de datos y **cumple con el perfil de metadatos de la Administración Pública Nacional** propuesto en esta guía.

Incluye formularios web para la carga de datos y metadatos. **La publicación de metadatos mediante este portal cumple con la versión 1.0 del perfil de metadatos recomendado en esta guía**. La versión 1.0 es anterior a la publicación de esta guía y se puede [consultar acá](http://paquete-apertura-datos.readthedocs.io/es/0.1.1/guia_metadatos.html#otros-catalogos).

El Portal debe publicarse en un dominio de la forma *http://datos.[entidad].gob.ar*. Esto asegura la publicación automática de los metadatos en formato data.json en *http://datos.[entidad].gob.ar/data.json*

El archivo *data.json* de un Portal Andino puede encontrarse en el directorio raíz del portal: *http://datos.[entidad].gob.ar/data.json*.

### Otros catálogos

Sin embargo, los organismos de la APN **pueden optar por desarrollar sus propias implementaciones del Perfil de Metadatos**.

Quienes opten por una solución alternativa al Portal Andino para publicar sus datos, deberán publicar los metadatos de su Catálogo en un archivo *data.json* en una URL como la siguiente: *http://datos.[entidad].gob.ar/data.json*.

En [entidad] recomendamos usar un nombre simple y breve que represente a la organización que publica el catálogo (por ejemplo: datos.jus.gob.ar, datos.tucuman.gob.ar, datos.pilar.gob.ar).

Este archivo deberá estar construido tal como se puede ver en el ejemplo del **[Anexo IV - Ejemplo de data.json](#anexo-iv-ejemplo-de-datajson)**, respetando el Perfil de Metadatos de la Administración Pública Nacional tal como se lo describe más adelante en la sección "*[Campos del perfil](#campos-del-perfil)*".

### Estándar usado

**El perfil de metadatos recomendado en esta guía es una adaptación del estándar [DCAT - AP](https://joinup.ec.europa.eu/solution/dcat-application-profile-data-portals-europe)**, usado por los países de la Unión Europea. DCAT es un vocabulario controlado definido por la W3C, ampliamente usado a nivel global para la descripción de catálogos de datos.

Según la W3C: "Mediante la utilización de DCAT para describir datasets en catálogos de datos, quienes publican aumentan la posibilidad de descubrimiento (*discoverability*) y permiten a aplicaciones informáticas consumir metadatos de manera simple desde múltiples catálogos. Además permite la publicación descentralizada de catálogos y favorece la búsqueda *federada* de datasets a través de varios sitios."

El perfil de metadatos propuesto para la Administración Pública Nacional se compone de 3 clases principales (*Catalog, Dataset y Distribution*) y 2 auxiliares (*Field* y *Theme*) que se relacionan según el siguiente esquema:

<div id="perfil-de-metadatos">

![Perfil de Metadatos](assets/der_perfil_metadatos.png)

</div>

A continuación, describimos los metadatos que el *data.json* debe contener, para cada una de estas clases.

### Campos del perfil

#### Catálogo (`catalog`)

El *data.json* de *quienes usen el portal Andino, se generará a través de los formularios completados, publicándose automáticamente en *http://datos.[entidad].gob.ar/data.json**.

Ejemplos de metadatos de un **catálogo**:

* [Catálogo en texto](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/data.md)
* [Catálogo en JSON](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/data.json)

Metadatos necesarios para describir el catálogo, que un *data.json* debe contener:

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
    <td>Identificador</td>
    <td>Recomendado</td>
    <td>En Argentina, es el identificador único del catálogo dentro de la Red de Nodos de Datos Abiertos de la Administración Pública Nacional. Este identificador es otorgado por la Dirección Nacional de Datos e Información Pública cuando un nuevo nodo pide ser incorporado a la red para su federación en el nodo concentrador de datos abiertos de la APN (http://www.datos.gob.ar).<br/> <br/> El identificador debe ser una o más palabras en minúsculas, separadas con guiones medios, sin usar caracteres especiales. Identifica en forma breve, sucinta y declarativa al nodo.</td>
    <td>"enacom"<br/>
    "energia"<br/>
    "desarrollo-social"<br/>
    "justicia"<br/>
    "arsat"</td>
    <td>identifier</td>
    <td>String</td>
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
    <td>Datasets</td>
    <td>Sí</td>
    <td>Contiene una lista de los datasets que forman parte del catálogo.</td>
    <td>[{...}, {...}]</td>
    <td>dataset</td>
    <td>Array</td>
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
    <td>Versión del perfil de metadatos</td>
    <td>Recomendado</td>
    <td>Es la versión del perfil de metadatos de la red de nodos de datos abiertos de la administración pública nacional de Argentina, utilizada en el catálogo.<br/><br/> Se utiliza para que distintas aplicaciones reconozcan y validen los metadatos del catálogo, y las funcionalidades disponibles para distintos fines.</td>
    <td>1.1</td>
    <td>version</td>
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

Es importante poner atención a los dos campos que contienen una lista de objetos: **`dataset`** y **`themeTaxonomy`**.

El **primero** contendrá una lista de objetos que describen (cada uno) los metadatos de los distintos datasets que componen el catálogo (en la próxima sección se describen los metadatos que debe contener cada uno de estos objetos).

El **segundo** también contiene una lista de objetos que, juntos, definen una taxonomía temática para el catálogo. Cada uno de estos objetos contiene los metadatos que describen a cada uno de los temas de esta taxonomía. Más adelante se describen estos metadatos en la sección Tema.

#### Dataset (`dataset`)

A continuación, describimos los metadatos que se deben completar para describir un dataset a la hora de su carga o actualización en el catálogo.

Ejemplos de metadatos de un **dataset**:

* [Dataset en texto](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/dataset.md)
* [Dataset en JSON](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/dataset.json)

Metadatos que el *data.json* debe contener, para describir a un dataset dentro de la lista contenida en el campo **`dataset`** del catálogo:

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
    <td>Identificador</td>
    <td>Si</td>
    <td>Identificador único del dataset, este identificador debe ser único para todo el catálogo.</td>
    <td>Un identificador único para el dataset. La URI u otro identificador único en el contexto del catálogo, ejemplo:<br/>"dataset-ejemplo-35782”</td>
    <td>identifier</td>
    <td>String</td>
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
    <td>Distribuciones</td>
    <td>Sí</td>
    <td>Lista de distribuciones que pertenecen al dataset y sus metadatos. Cada distribución se representa con un objeto ("{}") donde se describen los metadatos especificados para la clase "distribution" de este perfil de metadatos.</td>
    <td>[{...}, {...}]</td>
    <td>distribution</td>
    <td>Array</td>
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
    <td>Frecuencia de actualización</td>
    <td>Sí</td>
    <td>Frecuencia con la que se actualiza el dataset. Recomendamos especificar períodos normalizados con formato ISO-8601, agregando el campo “eventual” para datasets que se publican con una frecuencia eventual o no especificada. Anexo "Especificación de frecuencias según ISO-8601".</td>
    <td>“R/P1Y” para datasets que se actualizan anualmente</td>
    <td>accrualPeriodicity</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Fuente primaria</td>
    <td>No</td>
    <td>Fuente original o primaria de los datos publicados en el dataset. Se utiliza cuando la entidad responsable de la publicación del dataset, no es la entidad que produce los datos.<br/><br/> En el caso de organizaciones, detallar la estructura jerárquica separada por puntos, de manera jerárquicamente descendiente. Si la organización es parte de la Administración Pública Nacional y está listada en el dataset llamado "Estructura Organica del Poder Ejecutivo Nacional" (http://datos.gob.ar/dataset/estructura-organica-pen), deberá utilizarse la denominación allí documentada.</td>
    <td>Ministerio de Hacienda. Instituto Nacional de Estadísticas y Censos. Dirección Nacional de Cuentas Nacionales.</td>
    <td>source</td>
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
    <td>Etiqueta(s)</td>
    <td>Recomendado</td>
    <td>Palabras que describen el título o el contenido del recurso. Es necesario que las etiquetas se encuentren correctamente escritas, en plural y respetando la existencia de tags anteriores. Etiquetas que colaboran en la búsqueda de los usuarios. Cuanto más amplia y uniforme sea la lista de tags mayor será su eficiencia. A tales fines se recomienda ver el Anexo “Pautas para la selección de etiquetas”.</td>
    <td>["bienes", "compras","contrataciones"]</td>
    <td>keyword</td>
    <td>Array</td>
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
    <td>Licencia</td>
    <td>Recomendado</td>
    <td>Indica la licencia bajo la cual el dataset y todas sus distribuciones están disponibles mediante un enlace a la licencia o documento de la licencia seleccionada, o mediante el título textual de la licencia tal como aparece en la lista de <a href="http://opendefinition.org/licenses/">http://opendefinition.org/licenses/</a>. Recomendamos usar la licencia "Open Database License (ODbL) v1.0". Un dataset hereda por default la licencia general del catálogo salvo que se especifique una licencia diferente en este campo. Las distribuciones del dataset heredan esta licencia salvo que especifiquen una diferente.</td>
    <td>"http://opendatacommons.org/licenses/dbcl/1-0/" si se utiliza un enlace<br/>"Open Database License (ODbL) v1.0" si se consigna el nombre de la licencia a utilizar</td>
    <td>license</td>
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
</table>

Es importante prestar atención al campo **`distribution`** que contiene una lista de objetos que describen los metadatos de cada una de las distribuciones del daset. En la próxima sección abordaremos estos metadatos.

#### Distribución (`distribution`)

Estos son los metadatos que se deben completar al cargar o actualizar una distribución de un dataset en el catálogo para describirla.

Ejemplos de metadatos de una **distribución**:

* [Distribución en texto](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/distribution.md)
* [Distribución en JSON](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/distribution.json)

Metadatos que el *data.json* debe contener, para describir a una distribución dentro de la lista contenida en el campo **`distribution`** de un dataset:

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
    <td>Identificador</td>
    <td>Si</td>
    <td>Identificador único de la distribución, este identificador debe ser único para la distribución dentro del catálogo completo.<br/><br/>Debe estar compuesto por letras mayúsculas o minúsculas de la "a" a la "z" sin caracteres especiales (sin tildes y sin la "ñ"), números, guiones bajos "_", guiones medios "-" y puntos ".".</td>
    <td>1.2</td>
    <td>identifier</td>
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
    <td>Descripción</td>
    <td>Recomendado</td>
    <td>Breve descripción de la distribución. Recomendamos no escribir más de una línea. Toda información adicional puede ser incluida en la descripción del dataset.</td>
    <td>Listado de las convocatorias abiertas durante el año 2015 en el sistema de contrataciones electrónicas</td>
    <td>description</td>
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
    <td>Tipo de distribución</td>
    <td>Recomendado</td>
    <td>Indica el tipo de recurso.<br/><br/>"Archivo de datos" (file): archivo físico de algún formato de datos que se puede descargar.<br/>"API" (api): documentación en línea de un servicio web de datos.<br/>"Código" (code): repositorio o archivo con scripts utilizados para la generación, transformación, limpieza o validación de los datos de todo o parte del dataset.<br/>"Documentación" (documentation): documentación metodológica sobre los datos de todo o parte del dataset.</td>
    <td>file<br/>api<br/>code<br/>documentation</td>
    <td>type</td>
    <td>String</td>
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
    <td>Campos de la distribución</td>
    <td>Recomendado</td>
    <td>Lista de campos que contiene una distribución tabular (no aplica para aquellas distribuciones que no sean tablas) y sus metadatos. Cada campo se representa con un objeto ("{}") donde se describen los metadatos especificados para la clase "field" de este perfil de metadatos (como "nombre", "tipo" y "descripción").</td>
    <td>[{...}, {...}]</td>
    <td>field</td>
    <td>Array</td>
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
    <td>Formato del archivo</td>
    <td>Recomendado</td>
    <td>Indica el formato del archivo de la distribución. Si el tipo de la distribución está definido por IANA (http://www.iana.org/assignments/media-types/media-types.xml), debe usarse esa definición. En caso contrario deberán ponerse los caracteres después del punto final del archivo, que determinan el formato (cuando no está definido por IANA).</td>
    <td>"text/csv" definición de IANA "csv" caracteres finales después del punto</td>
    <td>format</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Nombre del archivo</td>
    <td>Recomendado</td>
    <td>Nombre de la distribución bajo el cual se descarga un archivo que contiene los datos, incluyendo la extensión del formato.<br/><br/>Debe estar compuesto por letras minúsculas de la "a" a la "z" sin caracteres especiales (sin tildes y sin la "ñ"), números y guiones medios "-".</td>
    <td>estructura-organica.csv</td>
    <td>fileName</td>
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
    <td>Tipo de archivo</td>
    <td>No</td>
    <td>Indica el tipo de archivo de la distribución, sólo si este está definido por IANA (http://www.iana.org/assignments/media-types/media-types.xml). En caso contrario este campo permanece vacío.</td>
    <td>"text/csv" definición de IANA "" cuando el formato no tiene definición en IANA</td>
    <td>mediaType</td>
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
    <td>Derechos sobre la distribución</td>
    <td>No</td>
    <td>Información sobre derechos aplicables a la distribución que no se hayan especificado en la licencia. Si se especifican, estos derechos sobreescriben a los del catálogo. En caso contrario, las distribuciones heredan los derechos especificados para el catálogo.</td>
    <td></td>
    <td>rights</td>
    <td>String</td>
  </tr>
</table>

Recomendamos poner atención al campo **`field`** que contiene una lista de objetos que describen los metadatos de cada uno de los campos de la distribución (en el **caso de distribuciones tabulares, únicamente**). En la próxima sección abordaremos estos metadatos.

#### Campo (`field`)

Recomendamos enfáticamente que las distribuciones tabulares **incluyan metadatos que ayuden a entender la información que contiene cada campo**. Documentarlos adecuadamente facilita enormemente la correcta utilización de los datos por parte de los usuarios.

En un portal Andino, estos metadatos se completan en el mismo formulario que se utiliza para cargar o actualizar una distribución.

Ejemplos de metadatos de un **campo**:

* [Metadatos de un campo de una distribución tabular en JSON](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/field.json)

Estos son los metadatos que el *data.json* debe contener para describir a un campo de una distribución tabular dentro de la lista contenida en el campo de metadatos **`field`** de una distribución:

<table  class="six-columns">
<colgroup>
    <col style="width:12%">
    <col style="width:12%">
    <col style="width:36%">
    <col style="width:20%">
    <col style="width:10%">
    <col style="width:10%">
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
    <td>El nombre del campo tal como se denomina en el encabezado de la distribución. Véase la "Guía para la publicación de datos en formatos abiertos" para una adecuada elección del nombre de un campo.<br/><br/>Se recomienda no exceder los 40 caracteres en la mayoría de los casos. En caso de que un título más largo se juzgue necesario o significativamente más claro, este no deberá exceder los 60 caracteres en ningún caso.<br/><br/>Debe estar compuesto por letras minúsculas de la "a" a la "z" sin caracteres especiales (sin tildes y sin la "ñ"), números y guiones bajos "_".</td>
    <td>Ejemplo para el cuarto campo de la distribución "Convocatorias abiertas durante el año 2015", valor para el nombre: "unidad_operativa_contrataciones_desc"</td>
    <td>title</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Tipo</td>
    <td>Recomendado</td>
    <td>El tipo de dato contenido en el campo según la lista utilizada por la librería recline.js (<a href="http://okfnlabs.org/recline/docs/models.html#types">http://okfnlabs.org/recline/docs/models.html#types</a>).
    <br/><br/>Los tipos incluidos en esta lista son:<br/><br/>
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
  <tr>
    <td>Identificador</td>
    <td>No</td>
    <td>El código identificador del campo. Debe ser único para todo el catálogo. Se utiliza cuando el campo requiere un identificador para ser utilizado en un sistema o aplicación, como en el caso de una base de series de tiempo (donde el identificador ejerce el rol de "nomenclador" del campo y debe ser único para todo el sistema - más allá incluso del presente catálogo).<br/><br/>Debe estar compuesto por letras mayúsculas o minúsculas de la "a" a la "z" sin caracteres especiales (sin tildes y sin la "ñ"), números, guiones bajos "_", guiones medios "-" y puntos ".".</td>
    <td>1.1_OGP_D_1993_A_17</td>
    <td>id</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Unidad de medida</td>
    <td>No</td>
    <td>La descripción de la unidad de medida en la que están expresados los valores del campo. Sólo se utiliza para campos de tipo numérico.</td>
    <td>Millones de pesos a precios de 1993</td>
    <td>units</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Tipo especial</td>
    <td>No</td>
    <td>El tipo de dato contenido en el campo, correspondiente a alguna extensión especial del perfil de metadatos.<br/><br/>El perfil de metadatos contempla el desarrollo de extensiones especiales destinadas a facilitar el desarrollo de aplicaciones automáticas que puedan leer e interpretar el contenido de una distribución o de un campo de un catálogo de datos abiertos, para su uso en sistemas específicos. Estas extensiones especiales buscan brindar mayor información sobre la estructura del dato para mejorar su interoperabilidad desatendida, de una forma sencilla.<br/><br/>Para más información leer la sección "Extensiones especiales". Ver "Series de tiempo" como ejemplo de una extensión especial al perfil de metadatos.</td>
    <td>time_index</td>
    <td>specialType</td>
    <td>String</td>
  </tr>
  <tr>
    <td>Detalle del tipo especial</td>
    <td>No</td>
    <td>Un parámetro que se puede especificar según el tipo especial de datos del campo en cuestión. Se utiliza para aportar información adicional sobre la estructura de datos del campo, según su definición en la extensión especial del perfil de metadatos a la que pertenece el "Tipo especial" con el que se define al campo. Sólo se puede usar si antes se definió un "Tipo especial".</td>
    <td>R/P1Y</td>
    <td>specialTypeDetail</td>
    <td>String</td>
  </tr>
</table>

Los primeros tres metadatos son útiles para **describir las características de cualquier campo de una distribución tabular**.

Los últimos cuatro metadatos son opcionales porque sólo cobran sentido al **describir las características de un campo, para casos específicos**. Mientras que no todos los campos de una distribución tabular tienen "**unidad de medida**", la asingación de un **"nomenclador" o "identificador"** suele ser útil para la identificación unívoca de variables en otros sistemas o aplicaciones, pero no en la generalidad de los casos.

Préstese especial atención a los últimos dos campos: estos constituyen la forma en que el Perfil de Metadatos **permite el desarrollo de extensiones para sistemas o aplicaciones**, desde su versión 1.1. Ver más en la sección [Extensiones especiales](#extensiones-especiales).

#### Tema (`theme`)

Cada catálogo de datos puede tener su propia taxonomía temática que permite clasificar a los datasets como pertenecientes a una o más categorías temáticas. Recomendamos que los temas tengan algunos metadatos que ayuden a un usuario a entenderlos mejor.

Estos son metadatos que el responsable de cargar o actualizar la taxonomía temática de un catálogo debe completar para describir los temas de la misma.

Ejemplos de metadatos de un **tema**:

* [Metadatos de un tema en JSON](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/theme.json)

Metadatos que el *data.json* debe contener, para describir a un tema de la taxonomía temática de un catálogo:

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

## Extensiones especiales

A partir de la versión 1.1, el perfil de metadatos propuesto para la Administración Pública Nacional plantea:

1. Un **esquema base de uso general** para la documentación de catálogos de datos abiertos
2. Un marco general para **desarrollar extensiones del perfil**, que permitan documentar casos especiales para el desarrollo de sistemas o aplicaciones.

El desarrollo de extensiones del perfil para uso de aplicaciones puede contemplar:

* La **obligatoriedad de campos de metadatos** que en el perfil base no son obligatorios (recomendados u optativos).
* La definición de uno o más **tipos especiales** (**`specialType`**) utilizados para que sistemas o aplicaciones interpreten de una forma específica los datos que encuentren en una distribución.

### Series de tiempo

Junto con la versión 1.1 del perfil de metadatos se propone una sencilla extensión para documentar **distribuciones que contienen series de tiempo**.

Esto sirve para su interpretación y extracción automática por parte de sistemas que compilan series de tiempo en bases de datos, servicios web, y de otras aplicaciones.

Debe tenerse en cuenta que la evolución de las posibilidades soportadas por la definición de esta extensión está directamente relacionada con la evolución de los sistemas desarrollados por la Dirección Nacional de Datos e Información Pública.

#### Distribución de series de tiempo

Es una tabla donde:

* Existe una columna que es el **índice de tiempo**
  - Es la **clave primaria única** de la tabla (identifica una fila única)
  - Tiene una **frecuencia temporal determinada** (es diaria, mensual, anual... pero no mezcla frecuencias).
* Cada una de las otras columnas son **series de tiempo**

<table  class="six-columns">
<colgroup>
    <col style="width:10%">
    <col style="width:18%">
    <col style="width:18%">
    <col style="width:18%">
    <col style="width:18%">
    <col style="width:18%">
  </colgroup>
  <tr>
    <td>indice_tiempo</td>
    <td>oferta_global_pib</td>
    <td>oferta_global_importacion</td>
    <td>demanda_global_exportacion</td>
    <td>demanda_global_ibif</td>
    <td>demanda_global_consumo_priv</td>
  </tr>
  <tr>
    <td>1993-01-01</td>
    <td>236520.0336</td>
    <td>22027.59999</td>
    <td>16340.95975</td>
    <td>45069.41348</td>
    <td>31952.717</td>
  </tr>
  <tr>
    <td>1994-01-01</td>
    <td>250307.886</td>
    <td>26682.25975</td>
    <td>18840.403</td>
    <td>51231.4255</td>
    <td>32094.804</td>
  </tr>
  <tr>
    <td>1995-01-01</td>
    <td>243186.1018</td>
    <td>24065.62925</td>
    <td>23084.79625</td>
    <td>44528.27725</td>
    <td>32338.89925</td>
  </tr>
  <tr>
    <td>1996-01-01</td>
    <td>256626.244</td>
    <td>28284.11475</td>
    <td>24850.043</td>
    <td>48483.8615</td>
    <td>33040.55475</td>
  </tr>
  <tr>
    <td>1997-01-01</td>
    <td>277441.3173</td>
    <td>35884.496</td>
    <td>27876.14225</td>
    <td>57047.5</td>
    <td>34104.32325</td>
  </tr>
  <tr>
    <td>1998-01-01</td>
    <td>288123.3068</td>
    <td>38903.79175</td>
    <td>30837.53425</td>
    <td>60780.6695</td>
    <td>35249.1645</td>
  </tr>
  <tr>
    <td>1999-01-01</td>
    <td>278369.0138</td>
    <td>34520.59125</td>
    <td>30448.89575</td>
    <td>53116.3155</td>
    <td>36173.34075</td>
  </tr>
</table>

La distribución debe ser un archivo CSV estándar (Ver **Guía para la publicación de datos en formatos abiertos**):

* Codificado en `utf-8`
* Separador de campos `,`
* Caracter decimal `.`

```
indice_tiempo,oferta_global_pib,oferta_global_importacion,demanda_global_exportacion,demanda_global_ibif,demanda_global_consumo_priv
1993-01-01,236520.033577,22027.5999938,16340.9597519,45069.4134803,31952.717001
1994-01-01,250307.886,26682.25975,18840.403,51231.4255,32094.804
1995-01-01,243186.10175,24065.62925,23084.79625,44528.27725,32338.89925
1996-01-01,256626.244,28284.11475,24850.043,48483.8615,33040.55475
1997-01-01,277441.31725,35884.496,27876.14225,57047.5,34104.32325
1998-01-01,288123.30675,38903.79175,30837.53425,60780.6695,35249.1645
1999-01-01,278369.01375,34520.59125,30448.89575,53116.3155,36173.34075
```

Ver ejemplo completo de una [distribución de series de tiempo](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/series_tiempo/distributions/oferta-demanda-global-precios-constantes-desestacionalizados-base-1993-valores-anuales.csv).

**Precisión de series con números enteros y decimales**

Las series deben contener valores con **números enteros** (`277441`) o con **números decimales** (`277441.31725`) pero no deben mezclarse dentro de la misma serie, si se desea preservar la precisión. Un número "entero" dentro de una serie decimal debe incluir `.0` al final (`277441.0`).

Los **números enteros** pueden tener cualquier cantidad de cifras, mientras que los **números decimales** sólo pueden tener **hasta 12 cifras en total**, incluyendo la parte entera y la parte decimal:

* `0.12345678901` está ok  (*serie decimal*)
* `12345678901.1` está ok  (*serie decimal*)
* `1234567.01234` está ok  (*serie decimal*)
* `0.1234567890123456789` NO está ok  (*serie decimal*)
* `123456789.01234567891` NO está ok  (*serie decimal*)
* `1234567890123456789.1` NO está ok  (*serie decimal*)
* `123456789123456789123` está ok (*serie entera*)

Casi todos los *software* que manejan números pueden usar decimales con hasta 12 cifras sin pérdida de precisión. Si bien existe software estadístico capaz de manejar decimales con más de 12 cifras, este límite debe ser analizado en cada caso y no está garantizado por la **API de Series de Tiempo de datos.gob.ar**.

#### Tipo especial: indice de tiempo

Una distribución de series de tiempo puede ser documentada fácilmente en un catálogo especificando uno de sus campos como "índice de tiempo" y aclarando la frecuencia que tiene (Ver el [Anexo III - Especificación de frecuencias (según ISO-8601)](#anexo-iii-especificacion-de-frecuencias-segun-iso-8601)).

Dentro de la variable `field` de la distribución:

```json
{
    "specialType": "time_index",
    "specialTypeDetail": "R/P1Y"
}
```

El indice de tiempo de una distribución con series de tiempo debe cumplir:

* **Fechas en ISO 8601** (`YYYY-MM-DD`)
* **Fechas en orden ascendente** (primera fila tiene el valor más antiguo, última fila el más reciente).
* Fechas pueden tener la parte de "tiempo" luego de la de "fecha", pero se desestima. (`YYYY-MM-DD` es exactamente igual que `YYYY-MM-DDThh:mm:ss`).
* Para una frecuencia dada (anual, semestral, trimestral, mensual o diaria) las **fechas admiten usar sólo la parte del estándar de fecha necesaria** o usar la **forma de fecha completa**.
    + Anual: YYYY está ok
    + Anual: YYYY-MM-DD está ok
    + Mensual: YYYY-MM está ok
    + Mensual: YYYY NO está ok
    + Trimestral: YYYY-MM está ok
    + Trimestral: YYYY NO está ok
* Las fechas están completas (el **índice de tiempo es _continuo_**).
    + Anual: 1980 / 1981 / 1982 está ok
    + Anual: 1980 / 1982 / 1983 NO está ok
    + Diaria
      - Frecuencia diaria _completa_ (lunes a domingo). No puede faltar ningún día de la semana.
      - Frecuencia diaria _hábil_ o `Business Daily` (lunes a viernes). No puede faltar ningún día hábil de la semana (un "martes" o "lunes" feriado, por ejemplo, debe figurar en el índice y dejar el valor de la observación nulo).
* Para una frecuencia dada (anual, semestral, trimestral, mensual o diaria) donde se use la forma completa, se debe **usar siempre _la fecha inicial_ del período**.
    + Mensual: 1980-01-01 / 1980-02-01 / 1980-03-01 está ok
    + Mensual: 1980-01-31 / 1980-02-28 / 1980-03-31 NO está ok
    + Trimestral: 1980-01-01 / 1980-04-01 / 1980-07-01 / 1980-10-01 está ok
    + Trimestral: 1980-02-01 / 1980-05-01 / 1980-08-01 / 1980-11-01 NO está ok
    + Semestral: 1980-01-01 / 1980-07-01 / 1981-01-01 está ok
    + Semestral: 1980-01-01 / 1980-08-01 / 1981-01-01 NO está ok
    + Semestral: 1980-01-31 / 1980-07-31 / 1981-01-31 NO está ok

#### Documentar un dataset de series de tiempo

A continuación se revisan los campos del perfil base que adquieren mayor relevancia para documentar series de tiempo, y se desglosa un ejemplo completo para cada parte del modelo de metadatos dentro de un *dataset* que contiene series de tiempo.

Ver ejemplo de catálogo completo en [Anexo VII - Ejemplo de data.json con series de tiempo](#anexo-vii-ejemplo-de-datajson-con-series-de-tiempo).

* **Dataset 1**: Oferta y Demanda Globales. Datos desestacionalizados. Base 1993
  - **Distribucion 1.1**: Oferta y Demanda Global. Precios constantes desestacionalizados. Base 1993. Valores anuales.
  - **Distribucion 1.2**: Oferta y Demanda Global. Precios constantes desestacionalizados. Base 1993. Valores trimestrales.

##### Dataset (`dataset`) - series de tiempo

```json
{
  "identifier": "1",
  "title": "Oferta y Demanda Globales: Datos desestacionalizados [Base 1993]",
  "description": "Componentes desestacionalizados de la oferta y demanda globales a precios de 1993.",
  "accrualPeriodicity": "R/P3M",
  "publisher": {
    "mbox": "ausolari@mecon.gob.ar",
    "name": "Ministerio de Hacienda. Secretaría de Política Económica. Subsecretaría de Programación Macroeconómica."
  },
  "source": "Ministerio de Hacienda. Instituto Nacional de Estadísticas y Censos. Dirección Nacional de Cuentas Nacionales.",
  "contactPoint": {
    "fn": "Ministerio de Hacienda. Secretaría de Política Económica. Subsecretaría de Programación Macroeconómica. Dirección de Información y Coyuntura"
  },
  "landingPage": "http://www.minhacienda.gob.ar/secretarias/politica-economica/programacion-macroeconomica/",
  "issued": "2017-08-22T17:51:26.553961-03:00",
  "keyword": [
    "oferta",
    "demanda",
    "pbi",
    "cuentas nacionales",
    "desestacionalizado"
  ],
  "superTheme": [
    "ECON"
  ],
  "temporal": "1993-01-01/2013-09-30",
  "theme": [
    "oferta_demanda"
  ],
  "distribution": [
    {
      "identifier": "1.1",
      "title": "Oferta y Demanda Globales a precios de 1993: Datos desestacionalizados en valores anuales [Base 1993]",
      "format": "CSV",
      "description": "Oferta y Demanda Globales por componente, a precios de comprador, en millones de pesos de 1993 y valores anuales desestacionalizados.",
      "issued": "2017-08-22T17:51:26.553961-03:00",
      "modified": "2017-08-22T17:51:26.553961-03:00",
      "accessURL": "https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/series_tiempo/distributions/oferta-demanda-global-precios-constantes-desestacionalizados-base-1993-valores-anuales.csv",
      "downloadURL": "https://raw.githubusercontent.com/datosgobar/paquete-apertura-datos/master/examples/series_tiempo/distributions/oferta-demanda-global-precios-constantes-desestacionalizados-base-1993-valores-anuales.csv",
      "field": [
        {
          "title": "indice_tiempo",
          "type": "date",
          "specialType": "time_index",
          "specialTypeDetail": "R/P1Y"
        },
        {
          "id": "1.1_OGP_D_1993_A_17",
          "title": "oferta_global_pbi",
          "description": "PIB desestacionalizado, en millones de pesos de 1993 y valores trimestrales",
          "type": "number",
          "units": "Millones de pesos a precios de 1993"
        },
        {
          "id": "1.1_OGI_D_1993_A_25",
          "title": "oferta_global_importacion",
          "description": "Importaciones desestacionalizadas, en millones de pesos de 1993 y valores trimestrales",
          "type": "number",
          "units": "Millones de pesos a precios de 1993"
        },
        {
          "id": "1.1_DGE_D_1993_A_26",
          "title": "demanda_global_exportacion",
          "description": "Exportaciones desestacionalizadas, en millones de pesos de 1993 y valores trimestrales",
          "type": "number",
          "units": "Millones de pesos a precios de 1993"
        },
        {
          "id": "1.1_DGI_D_1993_A_19",
          "title": "demanda_global_ibif",
          "description": "Inversion bruta interna fija desestacionalizada, en millones de pesos de 1993 y valores trimestrales",
          "type": "number",
          "units": "Millones de pesos a precios de 1993"
        },
        {
          "id": "1.1_DGCP_D_1993_A_27",
          "title": "demanda_global_consumo_priv",
          "description": "Consumo privado desestacionalizado, en millones de pesos de 1993 y valores trimestrales",
          "type": "number",
          "units": "Millones de pesos a precios de 1993"
        },
        {
          "id": "1.1_DGCP_D_1993_A_30",
          "title": "demanda_global_consumo_publico",
          "description": "Consumo publico desestacionalizado, en millones de pesos de 1993 y valores trimestrales",
          "type": "number",
          "units": "Millones de pesos a precios de 1993"
        }
      ]
    },
    {
      "identifier": "1.2",
      "title": "Oferta y Demanda Globales a precios de 1993: Datos desestacionalizados en valores trimestrales [Base 1993]",
      "format": "CSV",
      "description": "Oferta y Demanda Globales por componente, a precios de comprador, en millones de pesos de 1993 y valores anuales desestacionalizados.",
      "issued": "2017-08-22T17:51:26.553961-03:00",
      "modified": "2017-08-22T17:51:26.553961-03:00",
      "accessURL": "https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/series_tiempo/distributions/oferta-demanda-global-precios-constantes-desestacionalizados-base-1993-valores-trimestrales.csv",
      "downloadURL": "https://raw.githubusercontent.com/datosgobar/paquete-apertura-datos/master/examples/series_tiempo/distributions/oferta-demanda-global-precios-constantes-desestacionalizados-base-1993-valores-trimestrales.csv",
      "field": [
        {
          "title": "indice_tiempo",
          "type": "date",
          "specialType": "time_index",
          "specialTypeDetail": "R/P3M"
        },
        {
          "id": "1.2_OGP_D_1993_T_17",
          "title": "oferta_global_pbi",
          "description": "PBI a precios de comprador, en millones de pesos de 1993 y valores anuales.",
          "type": "number",
          "units": "Millones de pesos a precios de 1993"
        },
        {
          "id": "1.2_OGI_D_1993_T_25",
          "title": "oferta_global_importacion",
          "description": "Importación a precios de comprador, en millones de pesos de 1993 y valores anuales.",
          "type": "number",
          "units": "Millones de pesos a precios de 1993"
        },
        {
          "id": "1.2_DGE_D_1993_T_26",
          "title": "demanda_global_exportacion",
          "description": "Oferta global total a precios de comprador, en millones de pesos de 1993 y valores anuales.",
          "type": "number",
          "units": "Millones de pesos a precios de 1993"
        },
        {
          "id": "1.2_DGI_D_1993_T_19",
          "title": "demanda_global_ibif",
          "description": "Consumo privado, en millones de pesos  de 1993 y valores anuales.",
          "type": "number",
          "units": "Millones de pesos a precios de 1993"
        },
        {
          "id": "1.2_DGCP_D_1993_T_27",
          "title": "demanda_global_consumo_priv",
          "description": "Consumo publico, en millones de pesos de 1993 y valores anuales.",
          "type": "number",
          "units": "Millones de pesos a precios de 1993"
        },
        {
          "id": "1.2_DGCP_D_1993_T_30",
          "title": "demanda_global_consumo_publico",
          "description": "Inversion bruta interna fija, en millones de pesos de 1993  y valores anuales.",
          "type": "number",
          "units": "Millones de pesos a precios de 1993"
        }
      ]
    }
  ]
}
```

##### Distribución (`distribution`) - series de tiempo

```json
{
  "identifier": "1.1",
  "title": "Oferta y Demanda Globales a precios de 1993: Datos desestacionalizados en valores anuales [Base 1993]",
  "format": "CSV",
  "description": "Oferta y Demanda Globales por componente, a precios de comprador, en millones de pesos de 1993 y valores anuales desestacionalizados.",
  "issued": "2017-08-22T17:51:26.553961-03:00",
  "modified": "2017-08-22T17:51:26.553961-03:00",
  "accessURL": "https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/series_tiempo/distributions/oferta-demanda-global-precios-constantes-desestacionalizados-base-1993-valores-anuales.csv",
  "downloadURL": "https://raw.githubusercontent.com/datosgobar/paquete-apertura-datos/master/examples/series_tiempo/distributions/oferta-demanda-global-precios-constantes-desestacionalizados-base-1993-valores-anuales.csv",
  "field": [
    {
      "title": "indice_tiempo",
      "type": "date",
      "specialType": "time_index",
      "specialTypeDetail": "R/P1Y"
    },
    {
      "id": "1.1_OGP_D_1993_A_17",
      "title": "oferta_global_pbi",
      "description": "PIB desestacionalizado, en millones de pesos de 1993 y valores trimestrales",
      "type": "number",
      "units": "Millones de pesos a precios de 1993"
    },
    {
      "id": "1.1_OGI_D_1993_A_25",
      "title": "oferta_global_importacion",
      "description": "Importaciones desestacionalizadas, en millones de pesos de 1993 y valores trimestrales",
      "type": "number",
      "units": "Millones de pesos a precios de 1993"
    },
    {
      "id": "1.1_DGE_D_1993_A_26",
      "title": "demanda_global_exportacion",
      "description": "Exportaciones desestacionalizadas, en millones de pesos de 1993 y valores trimestrales",
      "type": "number",
      "units": "Millones de pesos a precios de 1993"
    },
    {
      "id": "1.1_DGI_D_1993_A_19",
      "title": "demanda_global_ibif",
      "description": "Inversion bruta interna fija desestacionalizada, en millones de pesos de 1993 y valores trimestrales",
      "type": "number",
      "units": "Millones de pesos a precios de 1993"
    },
    {
      "id": "1.1_DGCP_D_1993_A_27",
      "title": "demanda_global_consumo_priv",
      "description": "Consumo privado desestacionalizado, en millones de pesos de 1993 y valores trimestrales",
      "type": "number",
      "units": "Millones de pesos a precios de 1993"
    },
    {
      "id": "1.1_DGCP_D_1993_A_30",
      "title": "demanda_global_consumo_publico",
      "description": "Consumo publico desestacionalizado, en millones de pesos de 1993 y valores trimestrales",
      "type": "number",
      "units": "Millones de pesos a precios de 1993"
    }
  ]
}
```

##### Campo (`field`) - series de tiempo

**Serie de tiempo**

```json
{
  "id": "1.1_DGCP_D_1993_A_27",
  "title": "demanda_global_consumo_priv",
  "description": "Consumo privado desestacionalizado, en millones de pesos de 1993 y valores trimestrales",
  "type": "number",
  "units": "Millones de pesos a precios de 1993"
}
```

**Indice de tiempo**

```json
{
  "title": "indice_tiempo",
  "type": "date",
  "specialType": "time_index",
  "specialTypeDetail": "R/P1Y"
}
```

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
      <td>Datos referidos a agroganadería, pesca y forestación. Por ejemplo: 'Lechería: precio pagado al productor' o 'Superficie forestada'.</td>
    </tr>
    <tr>
      <td>ECON</td>
      <td>Economía y finanzas</td>
      <td>Datos referidos a economía y finanzas. Por ejemplo: 'Deuda pública'.</td>
    </tr>
    <tr>
      <td>EDUC</td>
      <td>Educación, cultura y deportes</td>
      <td>Datos referidos a educación, cultura y deportes. Por ejemplo: 'Registro de Establecimientos Educativos'.</td>
    </tr>
    <tr>
      <td>ENER</td>
      <td>Energía</td>
      <td>Datos referidos a energía. Por ejemplo: 'Productos mineros exportados' o 'Precios del GNC'.</td>
    </tr>
    <tr>
      <td>ENVI</td>
      <td>Medio ambiente</td>
      <td>Datos referidos a medio ambiente. Por ejemplo: 'Operadores de residuos peligrosos'.</td>
    </tr>
    <tr>
      <td>GOVE</td>
      <td>Gobierno y sector público</td>
      <td>Datos referidos a gobierno y sector público. Por ejemplo: 'Inmuebles del estado Nacional'.</td>
    </tr>
    <tr>
      <td>HEAL</td>
      <td>Salud</td>
      <td>Datos referidos a salud. Por ejemplo: 'Estadísticas nacionales de VIH/SIDA'.</td>
    </tr>
    <tr>
      <td>INTR</td>
      <td>Asuntos internacionales</td>
      <td>Datos referidos a asuntos internacionales. Por ejemplo: 'Representaciones argentinas en el exterior'.</td>
    </tr>
    <tr>
      <td>JUST</td>
      <td>Justicia, seguridad y legales</td>
      <td>Datos referidos a justicia, seguridad y legales. Por ejemplo: 'Censo penitenciario'.</td>
    </tr>
    <tr>
      <td>REGI</td>
      <td>Regiones y ciudades</td>
      <td>Datos referidos a regiones y ciudades. Por ejemplo: 'Departamentos de la provincia de Río Negro'.</td>
    </tr>
    <tr>
      <td>SOCI</td>
      <td>Población y sociedad</td>
      <td>Datos referidos a población y sociedad. Por ejemplo: 'Turistas residentes que viajan por Argentina'.</td>
    </tr>
    <tr>
      <td>TECH</td>
      <td>Ciencia y tecnología</td>
      <td>Datos referidos a ciencia y tecnología. Por ejemplo: 'Recursos humanos en ciencia y tecnología'.</td>
    </tr>
    <tr>
      <td>TRAN</td>
      <td>Transporte</td>
      <td>Datos referidos a transporte. Por ejemplo: 'Estadísticas viales'.</td>
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
        "id":"AGRI",
        "label":"Agroganadería, pesca y forestación",
        "description":"Datos referidos a agroganadería, pesca y forestación. Por ejemplo: 'Lechería: precio pagado al productor' o 'Superficie forestada'."
    },
    {
        "id":"ECON",
        "label":"Economía y finanzas",
        "description":"Datos referidos a economía y finanzas. Por ejemplo: 'Deuda pública'."
    },
    {
        "id":"EDUC",
        "label":"Educación, cultura y deportes",
        "description":"Datos referidos a educación, cultura y deportes. Por ejemplo: 'Registro de Establecimientos Educativos'."
    },
    {
        "id":"ENER",
        "label":"Energía",
        "description":"Datos referidos a energía. Por ejemplo: 'Productos mineros exportados' o 'Precios del GNC'."
    },
    {
        "id":"ENVI",
        "label":"Medio ambiente",
        "description":"Datos referidos a medio ambiente. Por ejemplo: 'Operadores de residuos peligrosos'."
    },
    {
        "id":"GOVE",
        "label":"Gobierno y sector público",
        "description":"Datos referidos a gobierno y sector público. Por ejemplo: 'Inmuebles del estado Nacional'."
    },
    {
        "id":"HEAL",
        "label":"Salud",
        "description":"Datos referidos a salud. Por ejemplo: 'Estadísticas nacionales de VIH/SIDA'."
    },
    {
        "id":"INTR",
        "label":"Asuntos internacionales",
        "description":"Datos referidos a asuntos internacionales. Por ejemplo: 'Representaciones argentinas en el exterior'."
    },
    {
        "id":"JUST",
        "label":"Justicia, seguridad y legales",
        "description":"Datos referidos a justicia, seguridad y legales. Por ejemplo: 'Censo penitenciario'."
    },
    {
        "id":"REGI",
        "label":"Regiones y ciudades",
        "description":"Datos referidos a regiones y ciudades. Por ejemplo: 'Departamentos de la provincia de Río Negro'."
    },
    {
        "id":"SOCI",
        "label":"Población y sociedad",
        "description":"Datos referidos a población y sociedad. Por ejemplo: 'Turistas residentes que viajan por Argentina'."
    },
    {
        "id":"TECH",
        "label":"Ciencia y tecnología",
        "description":"Datos referidos a ciencia y tecnología. Por ejemplo: 'Recursos humanos en ciencia y tecnología'."
    },
    {
        "id":"TRAN",
        "label":"Transporte",
        "description":"Datos referidos a transporte. Por ejemplo: 'Estadísticas viales'."
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

## Anexo VII - Ejemplo de data.json con series de tiempo

Este es un [ejemplo de data.json](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/series_tiempo/data.json):

```json
{
  "identifier": "sspm",
  "title": "Datos Programación Macroeconómica",
  "description": "Catálogo de datos abiertos de la Subsecretaría de Programación Macroeconómica.",
  "publisher": {
    "name": "Ministerio de Hacienda. Secretaría de Política Económica. Subsecretaría de Programación Macroeconómica.",
    "mbox": "ausolari@mecon.gob.ar"
  },
  "issued": "2017-09-28T00:00:00",
  "modified": "2017-09-28T00:00:00",
  "license": "Open Database License (ODbL) v1.0",
  "superThemeTaxonomy": "http://datos.gob.ar/superThemeTaxonomy.json",
  "themeTaxonomy": [
    {
      "id": "nivel_actividad",
      "description": "Datos sobre nivel actividad",
      "label": "Nivel actividad"
    },
    {
      "id": "intercambio_comercial",
      "description": "Datos sobre intercambio comercial",
      "label": "Intercambio Comercial"
    }
  ],
  "language": [
    "SPA"
  ],
  "spatial": "ARG",
  "dataset": [
    {
      "identifier": "1",
      "title": "Oferta y Demanda Globales: Datos desestacionalizados [Base 1993]",
      "description": "Componentes desestacionalizados de la oferta y demanda globales a precios de 1993.",
      "accrualPeriodicity": "R/P3M",
      "publisher": {
        "mbox": "ausolari@mecon.gob.ar",
        "name": "Ministerio de Hacienda. Secretaría de Política Económica. Subsecretaría de Programación Macroeconómica."
      },
      "source": "Ministerio de Hacienda. Instituto Nacional de Estadísticas y Censos. Dirección Nacional de Cuentas Nacionales.",
      "contactPoint": {
        "fn": "Ministerio de Hacienda. Secretaría de Política Económica. Subsecretaría de Programación Macroeconómica. Dirección de Información y Coyuntura"
      },
      "landingPage": "http://www.minhacienda.gob.ar/secretarias/politica-economica/programacion-macroeconomica/",
      "issued": "2017-08-22T17:51:26.553961-03:00",
      "keyword": [
        "oferta",
        "demanda",
        "pbi",
        "cuentas nacionales",
        "desestacionalizado"
      ],
      "superTheme": [
        "ECON"
      ],
      "temporal": "1993-01-01/2013-09-30",
      "theme": [
        "nivel_actividad"
      ],
      "distribution": [
        {
          "identifier": "1.1",
          "title": "Oferta y Demanda Globales a precios de 1993: Datos desestacionalizados en valores anuales [Base 1993]",
          "format": "CSV",
          "description": "Oferta y Demanda Globales por componente, a precios de comprador, en millones de pesos de 1993 y valores anuales desestacionalizados.",
          "issued": "2017-08-22T17:51:26.553961-03:00",
          "modified": "2017-08-22T17:51:26.553961-03:00",
          "accessURL": "https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/series_tiempo/distributions/oferta-demanda-global-precios-constantes-desestacionalizados-base-1993-valores-anuales.csv",
          "downloadURL": "https://raw.githubusercontent.com/datosgobar/paquete-apertura-datos/master/examples/series_tiempo/distributions/oferta-demanda-global-precios-constantes-desestacionalizados-base-1993-valores-anuales.csv",
          "field": [
            {
              "title": "indice_tiempo",
              "type": "date",
              "specialType": "time_index",
              "specialTypeDetail": "R/P1Y"
            },
            {
              "id": "1.1_OGP_D_1993_A_17",
              "title": "oferta_global_pbi",
              "description": "PIB desestacionalizado, en millones de pesos de 1993 y valores trimestrales",
              "type": "number",
              "units": "Millones de pesos a precios de 1993"
            },
            {
              "id": "1.1_OGI_D_1993_A_25",
              "title": "oferta_global_importacion",
              "description": "Importaciones desestacionalizadas, en millones de pesos de 1993 y valores trimestrales",
              "type": "number",
              "units": "Millones de pesos a precios de 1993"
            },
            {
              "id": "1.1_DGE_D_1993_A_26",
              "title": "demanda_global_exportacion",
              "description": "Exportaciones desestacionalizadas, en millones de pesos de 1993 y valores trimestrales",
              "type": "number",
              "units": "Millones de pesos a precios de 1993"
            },
            {
              "id": "1.1_DGI_D_1993_A_19",
              "title": "demanda_global_ibif",
              "description": "Inversion bruta interna fija desestacionalizada, en millones de pesos de 1993 y valores trimestrales",
              "type": "number",
              "units": "Millones de pesos a precios de 1993"
            },
            {
              "id": "1.1_DGCP_D_1993_A_27",
              "title": "demanda_global_consumo_priv",
              "description": "Consumo privado desestacionalizado, en millones de pesos de 1993 y valores trimestrales",
              "type": "number",
              "units": "Millones de pesos a precios de 1993"
            },
            {
              "id": "1.1_DGCP_D_1993_A_30",
              "title": "demanda_global_consumo_publico",
              "description": "Consumo publico desestacionalizado, en millones de pesos de 1993 y valores trimestrales",
              "type": "number",
              "units": "Millones de pesos a precios de 1993"
            }
          ]
        },
        {
          "identifier": "1.2",
          "title": "Oferta y Demanda Globales a precios de 1993: Datos desestacionalizados en valores trimestrales [Base 1993]",
          "format": "CSV",
          "description": "Oferta y Demanda Globales por componente, a precios de comprador, en millones de pesos de 1993 y valores anuales desestacionalizados.",
          "issued": "2017-08-22T17:51:26.553961-03:00",
          "modified": "2017-08-22T17:51:26.553961-03:00",
          "accessURL": "https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/series_tiempo/distributions/oferta-demanda-global-precios-constantes-desestacionalizados-base-1993-valores-trimestrales.csv",
          "downloadURL": "https://raw.githubusercontent.com/datosgobar/paquete-apertura-datos/master/examples/series_tiempo/distributions/oferta-demanda-global-precios-constantes-desestacionalizados-base-1993-valores-trimestrales.csv",
          "field": [
            {
              "title": "indice_tiempo",
              "type": "date",
              "specialType": "time_index",
              "specialTypeDetail": "R/P3M"
            },
            {
              "id": "1.2_OGP_D_1993_T_17",
              "title": "oferta_global_pbi",
              "description": "PBI a precios de comprador, en millones de pesos de 1993 y valores anuales.",
              "type": "number",
              "units": "Millones de pesos a precios de 1993"
            },
            {
              "id": "1.2_OGI_D_1993_T_25",
              "title": "oferta_global_importacion",
              "description": "Importación a precios de comprador, en millones de pesos de 1993 y valores anuales.",
              "type": "number",
              "units": "Millones de pesos a precios de 1993"
            },
            {
              "id": "1.2_DGE_D_1993_T_26",
              "title": "demanda_global_exportacion",
              "description": "Oferta global total a precios de comprador, en millones de pesos de 1993 y valores anuales.",
              "type": "number",
              "units": "Millones de pesos a precios de 1993"
            },
            {
              "id": "1.2_DGI_D_1993_T_19",
              "title": "demanda_global_ibif",
              "description": "Consumo privado, en millones de pesos  de 1993 y valores anuales.",
              "type": "number",
              "units": "Millones de pesos a precios de 1993"
            },
            {
              "id": "1.2_DGCP_D_1993_T_27",
              "title": "demanda_global_consumo_priv",
              "description": "Consumo publico, en millones de pesos de 1993 y valores anuales.",
              "type": "number",
              "units": "Millones de pesos a precios de 1993"
            },
            {
              "id": "1.2_DGCP_D_1993_T_30",
              "title": "demanda_global_consumo_publico",
              "description": "Inversion bruta interna fija, en millones de pesos de 1993  y valores anuales.",
              "type": "number",
              "units": "Millones de pesos a precios de 1993"
            }
          ]
        }
      ]
    }
  ]
}
```
