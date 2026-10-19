---
title: "Perfil de Aplicación Nacional de Metadatos para Datos Abiertos"
---

<p class="solo-impresion">ANEXO I</p>


<p class="solo-impresion">La última versión de este documento se encuentra en https://datosgobar.github.io/paquete-apertura-datos/perfil-metadatos/.</p>


## Introducción

### Objetivo

El Perfil de Aplicación Nacional de Metadatos para Datos Abiertos **es una especificación para documentar activos de datos digitales**, desarrollado para organismos de la Administración Pública Nacional, con el fin de catalogar de manera homogénea todos sus activos de datos abiertos a la ciudadanía y el público en general.

El perfil tiene por objetivo facilitar la búsqueda y acceso por parte de los usuarios a los activos de datos digitales abiertos mediante la implementación de un catálogo central normalizado, que permita la integración efectiva en sistemas, aplicaciones y flujos de trabajo con datos.

### Antecedentes

El Perfil de Aplicación Nacional de Metadatos para Datos Abiertos **es una extensión de [DCAT - AP](https://joinup.ec.europa.eu/solution/dcat-application-profile-data-portals-europe)**, usado por los países de la Unión Europea. DCAT es un vocabulario controlado definido por la W3C, ampliamente usado a nivel global para la descripción de catálogos de datos.

Según la W3C: "Mediante la utilización de DCAT para describir datasets en catálogos de datos, quienes publican aumentan la posibilidad de descubrimiento (*discoverability*) y permiten a aplicaciones informáticas consumir metadatos de manera simple desde múltiples catálogos. Además permite la publicación descentralizada de catálogos y favorece la búsqueda *federada* de datasets a través de varios sitios."

Así mismo, este perfil toma elementos del [Perfil Regional de Metadatos](https://perfil-regional-metadatos.readthedocs.io) definido como un repositorio de soluciones comunes sobre documentación de activos de datos abiertos, por un conjunto de países del continente americano entre los que se cuenta la Argentina.

## Terminología

* **Perfil de Aplicación**: es una especificación que re-utiliza términos de uno o más estándares base, sumando mayor especificidad al identificar elementos obligatorios, recomendados y opcionales, y recomendaciones de vocabularios controlados orientadas al caso de aplicación.
* **Catálogo**: es una lista o colección de activos de datos documentados siguiendo la estructura y definiciones de un determinado perfil de metadatos.
* **Dataset**: es un conjunto de datos que agrupa recursos referidos a un mismo tema, que respetan una estructura de la información que los relaciona entre sí.
* **Distribución**: es un recurso o activo de datos que se puede descargar (un archivo) y sus metadatos asociados. Puede tener diversos formatos (csv, shp, xlsx, etc) o estar disponible en línea (html, php).
* **Activo de datos**: es la forma más genérica de referirse a cualquier recurso o conjunto de recursos de datos que pueda ser tratado como una unidad a efectos de su gestión, uso, protección, intercambio o referencia.
* **Campo obligatorio**: es una propiedad de uso obligatorio para el cumplimiento del perfil. Permite que todos los activos de datos cuenten con una documentación básica homogénea.
* **Campo recomendado**: es una propiedad que, si bien no es obligatoria, su uso es recomendado para una mayor calidad de documentación de activos de datos.
* **Campo opcional**: es una propiedad disponible para su uso en caso de que sea de utilidad para el organismo, pero que no necesariamente aplica para todos los casos.

## Referencia

### Esquema

El Perfil de Aplicación Nacional de Metadatos para Datos Abiertos de la Administración Pública Nacional se compone de **3 clases obligatorias** (*Catalog, Dataset y Distribution*), **2 clases recomendadas** (*Field* y *Theme*).

En el diagrama, la primera columna de cada clase indica el nivel de exigencia
del campo: **Obligatorio**, **Recomendado** u **Opcional**. Los campos anidados
se escriben en notacion de punto (`publisher.name` es el `name` dentro de
`publisher`).

<pre class="mermaid">
erDiagram
    direction LR

    Catalog ||--|{ Dataset : dataset
    Catalog ||--o{ Theme : themeTaxonomy
    Dataset ||--|{ Distribution : distribution
    Distribution ||--o{ Field : field

    Catalog {
        Recomendado identifier
        Obligatorio title
        Obligatorio description
        Obligatorio publisher.name
        Obligatorio publisher.mbox
        Obligatorio dataset
        Recomendado issued
        Recomendado modified
        Recomendado version
        Recomendado language
        Recomendado license
        Recomendado homepage
        Obligatorio superThemeTaxonomy
        Recomendado themeTaxonomy
        Opcional rights
        Opcional spatial
    }

    Dataset {
        Obligatorio identifier
        Obligatorio title
        Obligatorio description
        Obligatorio publisher.name
        Recomendado publisher.mbox
        Recomendado contactPoint.fn
        Recomendado contactPoint.hasEmail
        Obligatorio distribution
        Obligatorio superTheme
        Recomendado theme
        Obligatorio issued
        Recomendado modified
        Obligatorio accrualPeriodicity
        Recomendado source
        Recomendado landingPage
        Recomendado keyword
        Recomendado temporal
        Recomendado license
        Opcional language
        Opcional spatial
    }

    Distribution {
        Obligatorio identifier
        Obligatorio title
        Recomendado description
        Obligatorio downloadURL
        Obligatorio accessURL
        Recomendado field
        Obligatorio issued
        Recomendado modified
        Recomendado format
        Recomendado fileName
        Recomendado license
        Opcional mediaType
        Opcional byteSize
        Opcional rights
    }

    Field {
        Recomendado title
        Recomendado type
        Recomendado description
        Opcional id
        Opcional units
        Opcional specialType
        Opcional specialTypeDetail
    }

    Theme {
        Recomendado id
        Recomendado label
        Recomendado description
    }
</pre>

### Clases del perfil

#### Obligatorias

| Nombre       | Descripción |
| ------------ | ------------------------------------------------------------ |
| Catalog      | Catálogo o repositorio que contiene los Datasets en él descriptos. Contiene una lista de Datasets en el atributo `dataset`. |
| Dataset      | Entidad conceptual que representa un conjunto de datos estrechamente relacionados entre sí. Contiene una lista de Distributions en el atributo `distribution`. |
| Distribution | Archivo físico que contiene datos y sus metadatos descriptivos adicionales. Puede contener una lista de Fields en el atributo `field`. |

#### Recomendadas

| Nombre | Descripción |
| ------ | ------------------------------------------------------- |
| Field  | Columna o campo de un archivo de datos tabular. |
| Theme  | Temática bajo la cual un Dataset puede ser clasificado. |

### Campos del perfil

#### Catálogo (`catalog`)

| Nombre                                      | Requerido   | Descripción                                                  | Ejemplo                                                      | Variable (data.json) | Tipo (data.json) |
| ------------------------------------------- | ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------- | ---------------- |
| Identificador                               | Recomendado | En Argentina, es el identificador único del catálogo dentro de la Red de Nodos de Datos Abiertos de la Administración Pública Nacional. Este identificador es otorgado por la Dirección de Datos Públicos cuando un nuevo nodo pide ser incorporado a la red para su federación en el nodo concentrador de datos abiertos de la APN (https://www.datos.gob.ar).<br/> <br/> El identificador debe ser una o más palabras en minúsculas, separadas con guiones medios, sin usar caracteres especiales. Identifica en forma breve, sucinta y declarativa al nodo. | "enacom"<br/> "energia"<br/> "desarrollo-social"<br/> "justicia"<br/> "arsat" | identifier           | String |
| Nombre                                      | Sí          | Nombre dado al catálogo. Debe ser claro, breve y lo suficientemente abstracto como para abarcar la multiplicidad de datasets que contiene. | Datos Argentina                                              | title                | String |
| Descripción                                 | Sí          | Descripción del contenido del catálogo.                      | Portal de Datos Abiertos del Gobierno de la República Argentina | description          | String |
| Autor                                       | Sí          | Responsable de la publicación del catálogo.                  | Jefatura de Gabinete de Ministros                            | publisher -> name    | String |
| Correo electrónico del autor                | Sí          | Correo electrónico de contacto del responsable de la publicación del catálogo. | datos@jgm.gob.ar                                             | publisher -> mbox    | String |
| Datasets                                    | Sí          | Contiene una lista de los datasets que forman parte del catálogo. | [{...}, {...}]                                               | dataset              | Array |
| Fecha de creación o publicación             | Recomendado | Fecha de creación o publicación del catálogo. Se escribe según el formato ISO-8601, tipeado como fecha simple o fecha con hora, con el mayor detalle posible que sea relevante para el dataset. | "2016-04-14T19:48:05.433640" para especificar fecha y hora<br/>"2016-04-14" para especificar fecha únicamente | issued               | String |
| Fecha de última actualización/ modificación | Recomendado | Fecha de última actualización/modificación del catálogo. Se escribe según el formato ISO-8601, tipeado como fecha simple o fecha con hora, con el mayor detalle posible que sea relevante para el dataset. | "2016-04-19T19:48:05.433640" para especificar fecha y hora<br/>"2016-04-19" para especificar fecha únicamente | modified             | String |
| Versión del perfil de metadatos             | Recomendado | Es la versión del perfil de metadatos de la red de nodos de datos abiertos de la administración pública nacional de Argentina, utilizada en el catálogo.<br/><br/> Se utiliza para que distintas aplicaciones reconozcan y validen los metadatos del catálogo, y las funcionalidades disponibles para distintos fines. | 1.1                                                          | version              | String |
| Idioma(s)                                   | Recomendado | Lenguaje para la descripción de los metadatos de los datasets contenidos en el catálogo. Hay 2 estándares ISO que pueden ser utilizados para este campo:<br/> (a) ISO 639-1 (2 letras)<br/> (b) ISO 639-2/T (3 letras) es el más recomendado.<br/> Puede definirse 1 o más lenguajes en una lista. (<a href="https://www.loc.gov/standards/iso639-2/php/code_list.php">Link a los estándares ISO</a>) | ["es"] para un lenguaje ISO 639-1<br/> ["spa", "eng"] para dos lenguajes ISO 639-2 | language             | Array |
| Licencia                                    | Recomendado | Indica la licencia bajo la cual todos los datasets y distribuciones del catálogo están disponibles mediante un enlace a la licencia o documento de la licencia seleccionada, o mediante el título textual de la licencia tal como aparece en la lista de <a href="https://opendefinition.org/licenses/">https://opendefinition.org/licenses/</a> . recomendamos usar la licencia "Creative Commons Attribution 4.0". Un dataset o distribución que especifique una licencia diferente, sobreescribe a la licencia general del catálogo. | "https://creativecommons.org/licenses/by/4.0/legalcode.es" si se utiliza un enlace<br/>"Creative Commons Attribution 4.0" si se consigna el nombre de la licencia a utilizar | license              | String |
| Página web del catálogo                     | Recomendado | Dirección web de acceso a la página principal del catálogo. Enlace a la página principal del catálogo. | https://datos.gob.ar                                         | homepage             | String |
| Taxonomía temática global                   | Sí          | Es el sistema de clasificación temática global de la Administración Pública Nacional. Compone una lista de temas globales y está publicada en <a href="https://datos.gob.ar/superThemeTaxonomy.json">https://datos.gob.ar/superThemeTaxonomy.json</a>. | https://datos.gob.ar/superThemeTaxonomy.json                 | superThemeTaxonomy   | String |
| Taxonomía temática específica               | Recomendado | Es el sistema de clasificación temática específica, creado por la organización responsable del catálogo. Compone una lista de temas específicos a los datasets del catálogo. Si se clasifica algún dataset del catálogo como perteneciente a uno o más temas, este campo es obligatorio ya que se debe explicitar una taxonomía temática para poder usar sus temas. | [{...}, {...}]                                               | themeTaxonomy        | Array |
| Derechos sobre el catálogo                  | No          | Información sobre derechos aplicables al catálogo en el caso que no se hayan especificado en la licencia. Los datasets y sus distribuciones heredan la información sobre derechos aplicables al catálogo, a menos que especifiquen unos derechos distintos. |                                                              | rights               | String |
| Cobertura geográfica                        | No          | El área geográfica cubierta por el catálogo. Una región o un lugar determinado. Puede tomar valores:<br/> a) De países y, provincias y municipios argentinos, según las recomendaciones de la Guía para la identificación y uso de entidades interoperables.<br/> b) Un área de coordenadas representada por latitud/ longitud en el orden: minima longitud, mínima latitud, máxima longitud, máxima latitud.<br/> c) Un punto geográfico representado por latitud/longitud.<br/> d) Si la referencia geográfico no está identificada en la Guía para la identificación y uso de entidades interoperables indicar la URIs según geonames.org; ej : https://sws.geonames.org/6255146 | "ARG" es el código para la República Argentina.<br/> "06007" es el código de un departamento<br/> [-58.111111, -35.111111, -57.111111, -33.111111] es un bounding box<br/> [-58.111111, -35.111111] es un punto geográfico<br/>"https://sws.geonames.org/6255146" | spatial              | String or Array |

#### Dataset (`dataset`)

| Nombre                                          | Requerido   | Descripción                                                  | Ejemplo                                                      | Variable (data.json)     | Tipo (data.json) |
| ----------------------------------------------- | ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------ | ---------------- |
| Identificador                                   | Si          | Identificador único del dataset, este identificador debe ser único para todo el catálogo. | Un identificador único para el dataset. La URI u otro identificador único en el contexto del catálogo, ejemplo:<br/>"dataset-ejemplo-35782” | identifier               | String |
| Título                                          | Sí          | Nombre asignado al dataset tal como será publicado. Debe ser claro y lo suficientemente abstracto como para abarcar la multiplicidad de distribuciones que contiene. Se recomienda no exceder los 100 caracteres en la mayoría de los casos. En caso de que un título más largo se juzgue necesario o relevante, este no deberá exceder los 200 caracteres. | Sistema de Contrataciones Electrónicas (Argentina Compra)    | title                    | String |
| Descripción                                     | Sí          | Descripción del contenido del dataset de un modo claro y conciso. Se recomienda no exceder los 500 caracteres en la mayoría de los casos. En caso de que una descripción más larga se juzgue necesaria o relevante, ésta no deberá exceder los 1500 caracteres. | Datos correspondiente al Sistema de Contrataciones Electrónicas (Argentina Compra) | description              | String |
| Autor                                           | Sí          | Responsable de la publicación del dataset. En el caso de organizaciones, detallar la estructura jerárquica separada por puntos, de manera jerárquicamente descendiente. Si la organización es parte de la Administración Pública Nacional y está listada en el dataset llamado "Estructura Organica del Poder Ejecutivo Nacional" (<a href="https://datos.gob.ar/dataset/jgm-estructura-organica-autoridades-poder-ejecutivo-nacional">https://datos.gob.ar/dataset/estructura-organica-pen</a>), deberá utilizarse la denominación allí documentada. | Jefatura de Gabinete de Ministros. Secretaría de Innovación Administrativa. Oficina Nacional de Contrataciones. | publisher -> name        | String |
| Correo electrónico del autor                    | Recomendado | Correo electrónico de contacto del responsable de la publicación del dataset. | onc@jgm.gob.ar                                               | publisher -> mbox        | String |
| Área/Persona de contacto                        | Recomendado | Área/persona de contacto que puede brindar información relevante sobre el dataset. | Jefatura de Gabinete de Ministros. Secretaría de Innovación Administrativa. Oficina Nacional de Contrataciones. Dirección de Compras Electrónicas. | contactPoint -> fn       | String |
| Correo electrónico del área/persona de contacto | Recomendado | Correo electrónico del área/persona de contacto que puede brindar información relevante sobre el dataset. | onc-compraselectronicas@jgm.gob.ar                           | contactPoint -> hasEmail | String |
| Distribuciones                                  | Sí          | Lista de distribuciones que pertenecen al dataset y sus metadatos. Cada distribución se representa con un objeto ("{}") donde se describen los metadatos especificados para la clase "distribution" de este perfil de metadatos. | [{...}, {...}]                                               | distribution             | Array |
| Temática(s) globales                            | Sí          | Temática/s o categoría/s globales a la/s que se refiere el dataset al ser publicado. Un dataset puede pertenecer a más de una categoría global, de manera que el tipo de valor de este campo es una lista de categorías. La/s categoría/s o temática/s globales deben adoptarse según el campo "Código (authority code)" del Anexo "Taxonomía temática para los datasets", que contiene una lista predefinida de temática/s globales. | ["ECON"]                                                     | superTheme               | Array |
| Temática(s) específicas                         | Recomendado | Temática/s o categoría/s específica/s a la/s que se refiere el dataset al ser publicado. Un dataset puede pertenecer a más de una categoría específica, de manera que el tipo de valor de este campo es una lista de categorías. La taxonomía a utilizar debe ser creada por la autoridad responsable del Catálogo. Se deben usar los ids (ver campo "id" de la clase Theme) de los temas definidos en la taxonomía para componer la lista (no se deben usar las etiquetas ni las descripciones). | ["Contrataciones", "Compras", "Macroeconomía"]               | theme                    | Array |
| Fecha de publicación                            | Sí          | Fecha de publicación del dataset. Según el formato ISO-8601, tipeado como fecha simple o fecha con hora, con el mayor detalle posible que sea relevante para el dataset. | "2016-04-14T19:48:05.433640" para especificar fecha y hora<br/>"2016-04-14" para especificar fecha únicamente | issued                   | String |
| Fecha de última actualización/ modificación     | Recomendado | Fecha de última actualización/modificación del dataset (ya sea de sus datos o de sus metadatos). Según el formato ISO-8601, tipeado como fecha simple o fecha con hora, con el mayor detalle posible que sea relevante para el dataset. | "2016-04-19T19:48:05.433640" para especificar fecha y hora<br/>"2016-04-19" para especificar fecha únicamente | modified                 | String |
| Frecuencia de actualización                     | Sí          | Frecuencia con la que se actualiza el dataset. Recomendamos especificar períodos normalizados con formato ISO-8601, agregando el campo “eventual” para datasets que se publican con una frecuencia eventual o no especificada. Anexo "Especificación de frecuencias según ISO-8601". | “R/P1Y” para datasets que se actualizan anualmente           | accrualPeriodicity       | String |
| Fuente primaria                                 | No          | Fuente original o primaria de los datos publicados en el dataset. Se utiliza cuando la entidad responsable de la publicación del dataset, no es la entidad que produce los datos.<br/><br/> En el caso de organizaciones, detallar la estructura jerárquica separada por puntos, de manera jerárquicamente descendiente. Si la organización es parte de la Administración Pública Nacional y está listada en el dataset llamado "Estructura Organica del Poder Ejecutivo Nacional" (https://datos.gob.ar/dataset/estructura-organica-pen), deberá utilizarse la denominación allí documentada. | Ministerio de Hacienda. Instituto Nacional de Estadísticas y Censos. Dirección Nacional de Cuentas Nacionales. | source                   | String |
| Página de referencias                           | No          | URL de una página web a través de la cual se puede acceder al dataset, sus recursos o información adicional sobre el mismo. | https://datos.gob.ar/dataset/modernizacion-sistema-contrataciones-electronicas-argentina-compra | landingPage              | String |
| Etiqueta(s)                                     | Recomendado | Palabras que describen el título o el contenido del recurso. Es necesario que las etiquetas se encuentren correctamente escritas, en plural y respetando la existencia de tags anteriores. Etiquetas que colaboran en la búsqueda de los usuarios. Cuanto más amplia y uniforme sea la lista de tags mayor será su eficiencia. A tales fines se recomienda ver el Anexo “Pautas para la selección de etiquetas”. | ["bienes", "compras","contrataciones"]                       | keyword                  | Array |
| Cobertura temporal                              | Recomendado | Período de tiempo cubierto por el dataset. El intervalo de tiempo está formado por una fecha de inicio y una de fin separadas por “/”, en formato ISO 8601, con el nivel de especificidad requerido por el dataset. | 2015-01-01/2015-12-31<br/>2015-01-01T00:45:00Z/2016-01-15T00:06:00Z | temporal                 | String |
| Licencia                                        | Recomendado | Indica la licencia bajo la cual el dataset y todas sus distribuciones están disponibles mediante un enlace a la licencia o documento de la licencia seleccionada, o mediante el título textual de la licencia tal como aparece en la lista de <a href="https://opendefinition.org/licenses/">https://opendefinition.org/licenses/</a>. Recomendamos usar la licencia "Creative Commons Attribution 4.0". Un dataset hereda por default la licencia general del catálogo salvo que se especifique una licencia diferente en este campo. Las distribuciones del dataset heredan esta licencia salvo que especifiquen una diferente. | "https://creativecommons.org/licenses/by/4.0/legalcode.es" si se utiliza un enlace<br/>"Creative Commons Attribution 4.0" si se consigna el nombre de la licencia a utilizar | license                  | String |
| Idioma(s)                                       | No          | Lenguaje para la descripción de los metadatos del dataset. Hay 2 estándares ISO que pueden ser utilizados para este campo:<br/> (a) ISO 639-1 (2 letras)<br/> (b) ISO 639-2/T (3 letras) es el más recomendado.<br/> Puede definirse 1 o más lenguajes en una lista. Los lenguajes especificados para un dataset, sobreesriben a los del catálogo. Si este campo está vacío el dataset hereda los lenguajes del catálogo. (<a href="https://www.loc.gov/standards/iso639-2/php/code_list.php">Link a los estándares ISO</a>) | ["es"] para un lenguaje ISO 639-1<br/> ["spa", ”eng"] para dos lenguajes ISO 639-2 | language                 | Array |
| Cobertura geográfica                            | No          | Una región o lugar determinado al que el dataset haga referencia.Una región o un lugar determinado. Puede tomar valores:<br/> a) De países y, provincias y municipios argentinos, según las recomendaciones de la Guía para la identificación y uso de entidades interoperables.<br/> b) Un área de coordenadas representada por latitud/ longitud en el orden: minima longitud, minima latitud, maxima longitud, maxima latitud.<br/> c) Un punto geográfico representado por latitud/longitud.<br/> d) Si la referencia geográfico no está identificada en la Guía para la identificación y uso de entidades interoperables indicar la URIs según geonames.org; ej : https://sws.geonames.org/6255146" | "ARG" es el código para la República Argentina.<br/> "06007" es el código de un departamento<br/> [-58.111111, -35.111111, -57.111111, -33.111111] es un bounding box<br/>[-58.111111, -35.111111] es un punto geográfico<br/> "https://sws.geonames.org/6255146" | spatial                  | Array or String |

#### Distribución (`distribution`)

| Nombre                                      | Requerido   | Descripción                                                  | Ejemplo                                                      | Variable (data.json) | Tipo (data.json) |
| ------------------------------------------- | ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------- | ---------------- |
| Identificador                               | Si          | Identificador único de la distribución, este identificador debe ser único para la distribución dentro del catálogo completo.<br/><br/>Debe estar compuesto por letras mayúsculas o minúsculas de la "a" a la "z" sin caracteres especiales (sin tildes y sin la "ñ"), números, guiones bajos "_", guiones medios "-" y puntos ".". | 2.1                                                          | identifier           | String |
| Título                                      | Sí          | Nombre asignado a la distribución.                           | Convocatorias 2017                                           | title                | String |
| Descripción                                 | Recomendado | Breve descripción de la distribución. Recomendamos no escribir más de una línea. Toda información adicional puede ser incluida en la descripción del dataset. | Listado de convocatorias abiertas durante el 2017 en el nuevo sistema "COMPR.AR". | description          | String |
| URL de descarga                             | Sí          | URL que permite la descarga directa de la distribución del dataset, vincula directamente a un archivo descargable en un formato dado. | https://infra.datos.gob.ar/catalog/modernizacion/dataset/2/distribution/2.1/download/convocatorias-2017.csv | downloadURL          | String |
| Tipo de distribución                        | Recomendado | Indica el tipo de recurso.<br/><br/>"Archivo de datos" (file): archivo físico de algún formato de datos que se puede descargar.<br/>"API" (api): documentación en línea de un servicio web de datos.<br/>"Código" (code): repositorio o archivo con scripts utilizados para la generación, transformación, limpieza o validación de los datos de todo o parte del dataset.<br/>"Documentación" (documentation): documentación metodológica sobre los datos de todo o parte del dataset. | file<br/>api<br/>code<br/>documentation                      | type                 | String |
| URL de acceso                               | Sí          | URL que permite el acceso a la distribución del dataset. Puede ser una página, feed u otro tipo de recurso que dé acceso indirecto a las distribuciones. Si las distribuciones son solo accesibles a través de la página de referencia del dataset, debe completarse el valor de la URL de acceso a la distribución con el mismo valor de la página de referencia del dataset. | https://datos.gob.ar/dataset/modernizacion-sistema-contrataciones-electronicas-argentina-compra/archivo/modernizacion_2.1 | accessURL            | String |
| Campos de la distribución                   | Recomendado | Lista de campos que contiene una distribución tabular (no aplica para aquellas distribuciones que no sean tablas) y sus metadatos. Cada campo se representa con un objeto ("{}") donde se describen los metadatos especificados para la clase "field" de este perfil de metadatos (como "nombre", "tipo" y "descripción"). | [{...}, {...}]                                               | field                | Array |
| Fecha de publicación                        | Sí          | Fecha de publicación de la distribución. Según el formato ISO-8601, tipeado como fecha simple o fecha con hora, con el mayor detalle posible que sea relevante para el dataset. | "2016-04-14T19:48:05.433640" para especificar fecha y hora<br/>"2016-04-14" para especificar fecha únicamente | issued               | String |
| Fecha de última actualización/ modificación | Recomendado | Fecha de última actualización/modificación de la distribución. Según el formato ISO-8601, tipeado como fecha simple o fecha con hora, con el mayor detalle posible que sea relevante para el dataset. | "2018-02-01T19:48:05.433640" para especificar fecha y hora<br/>"2018-02-01" para especificar fecha únicamente | modified             | String |
| Formato del archivo                         | Recomendado | Indica el formato del archivo de la distribución. Si el tipo de la distribución está definido por IANA (https://www.iana.org/assignments/media-types/media-types.xml), debe usarse esa definición. En caso contrario deberán ponerse los caracteres después del punto final del archivo, que determinan el formato (cuando no está definido por IANA). | CSV                                                          | format               | String |
| Nombre del archivo                          | Recomendado | Nombre de la distribución bajo el cual se descarga un archivo que contiene los datos, incluyendo la extensión del formato.<br/><br/>Debe estar compuesto por letras minúsculas de la "a" a la "z" sin caracteres especiales (sin tildes y sin la "ñ"), números y guiones medios "-". | convocatorias-2017.csv                                       | fileName             | String |
| Hash del archivo                            | Recomendado | Hash SHA512 del archivo para verificar su autenticidad.      | 64fe31b306852eef92c788b3be852221b6be8aea9b291a2cd9af36d67de43632eb21926f88d80232e80b0ce90027c761a60dac8710b2cb69250bb9f51c1356f4 | hash                 | String |
| Licencia                                    | Recomendado | Indica la licencia bajo la cual la distribución está disponible mediante un enlace a la licencia o documento de la licencia seleccionada, o mediante el título textual de la licencia tal como aparece en la lista de <a href="https://opendefinition.org/licenses/">https://opendefinition.org/licenses/</a>. Recomendamos usar la licencia "Creative Commons Attribution 4.0". Una distribución hereda por default la licencia del dataset al que pertenece, salvo que se especifique una licencia diferente en este campo. | "https://creativecommons.org/licenses/by/4.0/legalcode.es" si se utiliza un enlace<br/> "Creative Commons Attribution 4.0" si se consigna el nombre de la licencia a utilizar | license              | String |
| Tipo de archivo                             | No          | Indica el tipo de archivo de la distribución, sólo si este está definido por IANA (https://www.iana.org/assignments/media-types/media-types.xml). En caso contrario este campo permanece vacío. | "text/csv" definición de IANA "" cuando el formato no tiene definición en IANA | mediaType            | String |
| Tamaño                                      | No          | Tamaño de la distribución en bytes. El tamaño puede ser aproximado cuando no se conozca el tamaño exacto. | Ejemplo para un archivo de 5Kb aproximadamente: "5120”       | byteSize             | Integer |
| Derechos sobre la distribución              | No          | Información sobre derechos aplicables a la distribución que no se hayan especificado en la licencia. Si se especifican, estos derechos sobreescriben a los del catálogo. En caso contrario, las distribuciones heredan los derechos especificados para el catálogo. |                                                              | rights               | String |

#### Campo (`field`)

Recomendamos enfáticamente que las distribuciones tabulares **incluyan metadatos que ayuden a entender la información que contiene cada campo**. Documentarlos adecuadamente facilita enormemente la correcta utilización de los datos por parte de los usuarios.

| Nombre                    | Requerido   | Descripción                                                  | Ejemplo                                                      | Variable (data.json) | Tipo (data.json) |
| ------------------------- | ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------- | ---------------- |
| Nombre                    | Recomendado | El nombre del campo tal como se denomina en el encabezado de la distribución. Véase la "Guía para la publicación de datos en formatos abiertos" para una adecuada elección del nombre de un campo.<br/><br/>Se recomienda no exceder los 40 caracteres en la mayoría de los casos. En caso de que un título más largo se juzgue necesario o significativamente más claro, este no deberá exceder los 60 caracteres en ningún caso.<br/><br/>Debe estar compuesto por letras minúsculas de la "a" a la "z" sin caracteres especiales (sin tildes y sin la "ñ"), números y guiones bajos "_". | unidad_operativa_contrataciones_desc                         | title                | String |
| Tipo                      | Recomendado | El tipo de dato contenido en el campo según la lista utilizada por la librería recline.js (<a href="https://okfnlabs.org/recline/docs/models.html#types">https://okfnlabs.org/recline/docs/models.html#types</a>). <br/><br/>Los tipos incluidos en esta lista son:<br/><br/> string (text): Valores de texto.<br/> number (double, float, numeric): Números que puedan no ser enteros (incluyen decimales).<br/> integer (int): Números que siempre son enteros.<br/> date: Fecha simple expresada según el estándar ISO 8601 incluyendo únicamente año, mes y día (YYYY-MM-DD) como en "2016-02-01".<br/> time: Tiempo expresado según el estándar ISO 8601 incluyendo únicamente horas, minutos y segundos (hh:mm:ss) como en "10:05:00".<br/> date-time (datetime, timestamp): Fecha completa expresada según el estándar ISO 8601 incluyendo año, mes, día, horas, minutos y segundos (YYYY-MM-DDThh:mm:ssZ) como en "2016-02-01T10:05:00+03:00"<br/> boolean (bool): Valores verdadero/falso.<br/> binary: Representación de datos binarios base64.<br/> geo_point: Ver estructura en <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/geo-point.html">https://www.elastic.co/guide/en/elasticsearch/reference/current/geo-point.html.</a><br/> geojson: ver en <a href="https://geojson.org/">https://geojson.org/</a><br/> array: Lista de valores.<br/> object (json): Objeto de JSON.<br/> any: Campo que puede contener valores de cualquier tipo. | Convocatorias 2017                                           | type                 | String |
| Descripción               | Recomendado | La descripción de la información que contiene el campo.      | Organismo que realiza la convocatoría. Organismo de máximo nivel jerárquico al que pertenece la unidad operativa de contrataciones. | description          | String |
| Identificador             | No          | El código identificador del campo. Debe ser único para todo el catálogo. Se utiliza cuando el campo requiere un identificador para ser utilizado en un sistema o aplicación, como en el caso de una base de series de tiempo (donde el identificador ejerce el rol de "nomenclador" del campo y debe ser único para todo el sistema - más allá incluso del presente catálogo).<br/><br/>Debe estar compuesto por letras mayúsculas o minúsculas de la "a" a la "z" sin caracteres especiales (sin tildes y sin la "ñ"), números, guiones bajos "_", guiones medios "-" y puntos ".". | 1.1_OGP_D_1993_A_17                                          | id                   | String |
| Unidad de medida          | No          | La descripción de la unidad de medida en la que están expresados los valores del campo. Sólo se utiliza para campos de tipo numérico. | Millones de pesos a precios de 1993                          | units                | String |
| Tipo especial             | No          | El tipo de dato contenido en el campo, correspondiente a alguna extensión especial del perfil de metadatos.<br/><br/>El perfil de metadatos contempla el desarrollo de extensiones especiales destinadas a facilitar el desarrollo de aplicaciones automáticas que puedan leer e interpretar el contenido de una distribución o de un campo de un catálogo de datos abiertos, para su uso en sistemas específicos. Estas extensiones especiales buscan brindar mayor información sobre la estructura del dato para mejorar su interoperabilidad desatendida, de una forma sencilla.<br/><br/>Para más información leer la sección "Extensiones especiales". Ver "Series de tiempo" como ejemplo de una extensión especial al perfil de metadatos. | time_index                                                   | specialType          | String |
| Detalle del tipo especial | No          | Un parámetro que se puede especificar según el tipo especial de datos del campo en cuestión. Se utiliza para aportar información adicional sobre la estructura de datos del campo, según su definición en la extensión especial del perfil de metadatos a la que pertenece el "Tipo especial" con el que se define al campo. Sólo se puede usar si antes se definió un "Tipo especial". | R/P1Y                                                        | specialTypeDetail    | String |

Los primeros tres metadatos **describen las características de cualquier campo de una distribución tabular**.

Los últimos cuatro metadatos son opcionales: **describen las características de un campo para casos específicos**. 

No todos los campos de una distribución tabular tienen "**unidad de medida**", y la asingación de un **"nomenclador" o "identificador"** suele ser útil para la identificación unívoca de variables en algunos sistemas o aplicaciones, pero no en la generalidad de los casos.

Los últimos dos campos **se utilizan para el desarrollo de extensiones para sistemas o aplicaciones**, desde la versión 1.1 del perfil de metadatos. Ver más en la sección [Extensiones especiales](#extensiones-especiales).

#### Tema (`theme`)

Cada catálogo de datos puede tener su propia taxonomía temática que permite clasificar a los datasets como pertenecientes a una o más categorías temáticas. La definición de un tema dentro de la taxonomía es obligatoria en caso de que se desee clasificar un dataset bajo ese tema.

| Nombre        | Requerido   | Descripción                               | Ejemplo                                                      | Variable (data.json) | Tipo (data.json) |
| ------------- | ----------- | ----------------------------------------- | ------------------------------------------------------------ | -------------------- | ---------------- |
| Identificador | Recomendado | El identificador del tema.                | AGRI                                                         | id                   | String |
| Etiqueta      | Recomendado | La etiqueta o título de un tema.          | Agricultura, pesca, silvicultura y alimentación              | label                | String |
| Descripción   | Recomendado | Una breve y concisa descripción del tema. | Bajo este concepto se incluyen datasets que cubren dominios tales como agricultura, pesca, forestación o alimentos. | description          | String |

### Extensiones especiales

A partir de la versión 1.1, el perfil de metadatos plantea:

1. Un **esquema base** de uso general para la documentación de catálogos de datos abiertos
2. Un **marco para desarrollar extensiones del perfil**, que permitan documentar casos especiales para el desarrollo de sistemas o aplicaciones.

El desarrollo de extensiones del perfil para uso de aplicaciones puede contemplar:

* La **obligatoriedad de campos de metadatos** que en el perfil base no son obligatorios (recomendados u optativos).
* La **definición de uno o más tipos especiales** (**`specialType`**) utilizados para que sistemas o aplicaciones interpreten de una forma específica los datos que encuentren en una distribución.

#### Series de tiempo

Especificación para documentar **distribuciones que contienen series de tiempo**. Permite la extracción de datos automática y segura por parte de sistemas que compilan series de tiempo.

La [API de Series de Tiempo de la República Argentina](https://apis.datos.gob.ar/series) puede leer cualquier distribución publicada por un organismo de la Administración Pública Nacional bajo esta especificación.

La evolución de las posibilidades soportadas por esta extensión está directamente relacionada con la evolución de los sistemas desarrollados por la Dirección de Datos Públicos.

##### Distribución de series de tiempo

Es un archivo CSV con las siguientes propiedades:

* Codificación: `utf-8`
* Separador de campos: `,`
* Caracter decimal: `.`
* Primera columna: es el **índice de tiempo**.
    - Es la **clave primaria única** de la tabla (identifica una fila única)
    - Tiene una **frecuencia temporal determinada** (es diaria, mensual, trimestral, semestral o anual).
* Resto de las columnas: cada una es una **serie de tiempo** diferente.

| indice_tiempo | oferta_global_pib | oferta_global_importacion | demanda_global_exportacion | demanda_global_ibif | demanda_global_consumo_priv |
| ------------- | ----------------- | ------------------------- | -------------------------- | ------------------- | --------------------------- |
| 1993-01-01    | 236520.0336       | 22027.59999               | 16340.95975                | 45069.41348         | 31952.717 |
| 1994-01-01    | 250307.886        | 26682.25975               | 18840.403                  | 51231.4255          | 32094.804 |
| 1995-01-01    | 243186.1018       | 24065.62925               | 23084.79625                | 44528.27725         | 32338.89925 |
| 1996-01-01    | 256626.244        | 28284.11475               | 24850.043                  | 48483.8615          | 33040.55475 |
| 1997-01-01    | 277441.3173       | 35884.496                 | 27876.14225                | 57047.5             | 34104.32325 |
| 1998-01-01    | 288123.3068       | 38903.79175               | 30837.53425                | 60780.6695          | 35249.1645 |
| 1999-01-01    | 278369.0138       | 34520.59125               | 30448.89575                | 53116.3155          | 36173.34075 |

La misma tabla abierta como un archivo de texto se vería así:

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

Ver ejemplo completo de una [distribución de series de tiempo](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/series_tiempo/distributions/oferta-demanda-global-precios-constantes-desestacionalizados-base-1993-valores-anuales.csv) en el repositorio digital de este documento.

##### Tipo especial: indice de tiempo

Una distribución de series de tiempo puede ser documentada fácilmente en un catálogo especificando el primero de sus campos como "índice de tiempo" y aclarando la frecuencia que tiene (Ver el [Anexo III - Especificación de frecuencias (según ISO-8601)](#anexo-i-especificacion-de-frecuencias)).

Dentro de la variable `field` de la distribución:

```json
    {
        "specialType": "time_index",
        "specialTypeDetail": "R/P1Y"
    }
```

Propiedades que debe cumplir:

| Nombre                                            | Descripción                                                  | Ejemplo |
| ------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ISO 8601                                          | Los valores deben seguir la parte de la "fecha" del estándar ISO 8601 (`YYYY-MM-DD`). Pueden tener la parte de "tiempo" luego de la de "fecha" pero esta se desestima si la frecuencia es menor a "diaria". (`YYYY-MM-DD` es igual que `YYYY-MM-DDThh:mm:ss`) | 2016-01-01 |
| Orden ascendente                                  | La primer fila tiene la fecha más antigua y la última fila tiene la fecha más reciente. | 2016-01-01<br>2017-01-01<br>2018-01-01<br>2019-01-01 |
| Requerimientos mínimos para la frecuencia elegida | Para una frecuencia dada (anual, semestral, trimestral, mensual o diaria) las fechas admiten usar sólo la parte del estándar de fecha necesaria o usar la forma de fecha completa. <br> <br>Anual: YYYY está bien <br>Anual: YYYY-MM-DD está bien <br>Mensual: YYYY-MM está bien <br>Mensual: YYYY NO está bien <br>Trimestral: YYYY-MM está bien <br>Trimestral: YYYY NO está bien | Anual: <br> 2019 <br> 2019-01-01 <br> <br> Mensual: <br> 2019-01 <br> 2019-01-01 <br> <br> Trimestral: <br> 2019-01 <br> 2019-04 <br> 2019-07 <br> 2019-10 <br> 2019-01-01 <br> 2019-04-01 <br> |
| Línea del tiempo completa                         | El índice de tiempo es continuo (no le faltan valores). <br> <br> Anual: 1980 / 1981 / 1982 está bien <br> Anual: 1980 / 1982 / 1983 NO está bien <br> <br> Se aceptan tanto la frecuencia diaria "lunes a domingo" (no puede faltar ningún día de la semana) como la frecuencia diaria "de lunes a viernes" (no puede faltar ningún día hábil de la semana). Si hubiera un "lunes" feriado, este debe estar en la distribución y dejar el valor vacío (en caso de que no lo hubiere). | Anual: <br> 1890 <br> 1891 <br> 1892 <br> |
| Fecha inicial del período cubierto                | Para una frecuencia dada (anual, semestral, trimestral, mensual o diaria) donde se use la forma completa, se debe usar siempre la fecha inicial del período. <br> <br> Mensual: 1980-01-01 / 1980-02-01 / 1980-03-01 está bien <br> Mensual: 1980-01-31 / 1980-02-28 / 1980-03-31 NO está bien <br> <br> Trimestral: 1980-01-01 / 1980-04-01 / 1980-07-01 / 1980-10-01 está bien <br> Trimestral: 1980-02-01 / 1980-05-01 / 1980-08-01 / 1980-11-01 NO está bien <br> <br> Semestral: 1980-01-01 / 1980-07-01 / 1981-01-01 está bien <br> Semestral: 1980-01-01 / 1980-08-01 / 1981-01-01 NO está bien <br> Semestral: 1980-01-31 / 1980-07-31 / 1981-01-31 NO está bien | Mensual: <br> 1980-01-01 <br> 1980-02-01 <br> 1980-03-01 <br> <br> Trimestral: <br> 1980-01-01 <br> 1980-04-01 <br> 1980-07-01 <br> 1980-10-01 <br> <br> Semestral: <br> 1980-01-01 <br> 1980-07-01 <br> 1981-01-01 <br> |

## Condiciones de cumplimiento del perfil

### Proveedores de metadatos

Los organismos de la Administración Pública Nacional deben generar y administrar en forma permanente su propio catálogo incluyendo todos los activos de datos digitales publicados en línea bajo su autoridad, tutela o responsabilidad (ver sub-sección ["Alcance"](#alcance) de esta sección).

El catálogo debe estar publicado según las pautas de este documento, en formato [JSON](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/data.json) o [XLSX](https://raw.githubusercontent.com/datosgobar/paquete-apertura-datos/master/examples/catalog.xlsx) de estructura compatible.

El catálogo debe publicarse en una URL que cumpla alguna de estas 3 condiciones:

* Sea propiedad digital del organismo.
* Esté contenida en el dominio argentina.gob.ar o alguno de sus subdominios, bajo el cual el organismo gestione la publicación de sus contenidos.
* Esté contenida en el dominio datos.gob.ar o alguno de sus subdominios, bajo el cual el organismo gestione la publicación de datos o metadatos bajo su tutela.

Así mismo, tanto la URL donde se publica el catálogo como las URLs de descarga de los archivos en él documentados, **deben contar con certificado SSL** instalado en el servidor.

Se recomienda que el nombre del archivo que contiene el catálogo sea `data.json` o `catalog.xlsx` según el formato original en que se publique, pero esto no es una condición excluyente.

**La URL de descarga del catálogo del organismo deberá figurar en forma visible en la sección de transparencia activa** de su propiedad digital o de su sitio web en el dominio argentina.gob.ar.

### Alcance

**Los organismos de la Administración Pública Nacional deben documentar en su catálogo todos los activos de datos digitales publicados en línea.**

Se entiende por tales a:

* Todos los archivos descargables de formatos CSV, TXT (tabular), XLS, XLSX, ODS, DTA, SAV, DBF, JSON, XML, GEOJSON, KML, SHP o RDF.
* Todos los archivos de otros formatos que sean versiones más recientes de los incluidos en el punto anterior.
* Todos los archivos de otros formatos no incluidos en los puntos anteriores, siempre que sean diseñados para almacenar datos tabulares.
* Todos los archivos de formatos comprimidos ZIP, RAR o cualquier otro que contengan dentro algún archivo de los formatos anteriormente mencionados.
* Todos los archivos PDF, DOC, DOCX, HTML, TXT y otros formatos de documentos que contengan documentación metodológica referida a archivos de los formatos anteriores. Estos se consideran complementarios y deben documentarse siempre en conjunto con los archivos que efectivamente contienen los datos.
* Todas las URLs que contengan documentación de uso de APIs o servicios web de datos total o parcialmente abiertos al público general.

### Consumidores de metadatos

Una aplicación diseñada para leer metadatos de un catálogo publicado según este perfil deberá:

* Procesar correctamente todos los campos obligatorios de las clases obligatorias del perfil.
* Procesar correctamente (según su definición) todos aquellos campos no obligatorios que declare utilizar hacia sus usuarios.
* Implementar las validaciones necesarias para procesar correctamente los casos válidos definidos en las extensiones especiales.

## Anexos

### Anexo I - Especificación de frecuencias

Especificación de frecuencias según ISO-8601.

| Frecuencia                | Valor según ISO-8601 |
| ------------------------- | -------------------- |
| Cada diez años            | R/P10Y |
| Cada cuatro años          | R/P4Y |
| Cada tres años            | R/P3Y |
| Cada dos años             | R/P2Y |
| Anual                     | R/P1Y |
| Cada medio año            | R/P6M |
| Cuatrimestral             | R/P4M |
| Trimestral                | R/P3M |
| Bimestral                 | R/P2M |
| Mensual                   | R/P1M |
| Cada 15 días              | R/P0.5M |
| Tres veces por mes        | R/P0.33M |
| Semanal                   | R/P1W |
| Dos veces a la semana     | R/P0.5W |
| Tres veces a la semana    | R/P0.33W |
| Diaria                    | R/P1D |
| Cada hora                 | R/PT1H |
| Continuamente actualizado | R/PT1S |
| Eventual                  | eventual |

### Anexo II - Taxonomía temática

El Portal Nacional de Datos usa la [taxonomía temática definida por la Unión Europea](https://publications.europa.eu/mdr/authority/data-theme/index.html).

**Cada catálogo de datos puede desarrollar su propia taxonomía**, cuyo uso se expresa en  los siguientes campos de metadatos (y sus equivalentes para el Portal Andino):

* **themeTaxonomy**: es un campo de metadatos del catálogo que define una lista de temas que se pueden usar para clasificar los datasets. Refiere al esquema completo de la taxonomía en sí, no a alguna de sus etiquetas en particular.
* **theme**: es un campo de metadatos de un Dataset. Refiere a la/s etiqueta/s en particular bajos la/s cuales un dataset es clasificado temáticamente. Sólo pueden usarse etiquetas que estén definidas en la taxonomía temática de *themeTaxonomy*.

Además del uso de una taxonomía propia de cada catálogo de datos, **recomendamos la clasificación de los datasets según la taxonomía del Portal Nacional de Datos.** Esta es una *súper taxonomía* a la que cada catálogo hace referencia mediante los siguientes campos de metadatos (y sus equivalentes para el Portal Andino):

* **superThemeTaxonomy**: es un campo de metadatos del catálogo que apunta a la URL donde el Portal Nacional de Datos documenta la taxonomía temática de la Administración Pública Nacional.
* **superTheme**: es un campo de metadatos de un dataset. Refiere a la/s etiqueta/s en particular bajos la/s cuales un dataset es clasificado temáticamente, según la *súper taxonomía* que es la de la Administración Pública Nacional. Sólo pueden usarse etiquetas que estén definidas en la taxonomía temática de *superThemeTaxonomy*.

**La ventaja de usar una súper taxonomía** temática es que** facilita la clasificación de datasets** por parte de un usuario según un conjunto de categorías temáticas más generales, que son interoperables con las usadas por otros países del mundo. Esto, a su vez, **facilita la clasificación de datasets cosechados por el Portal Nacional de Datos**.

| Identificador (id) | Etiqueta (label)                   | Descripción (description) |
| ------------------ | ---------------------------------- | ------------------------------------------------------------ |
| AGRI               | Agroganadería, pesca y forestación | Datos referidos a agroganadería, pesca y forestación. Por ejemplo: 'Lechería: precio pagado al productor' o 'Superficie forestada'. |
| ECON               | Economía y finanzas                | Datos referidos a economía y finanzas. Por ejemplo: 'Deuda pública'. |
| EDUC               | Educación, cultura y deportes      | Datos referidos a educación, cultura y deportes. Por ejemplo: 'Registro de Establecimientos Educativos'. |
| ENER               | Energía                            | Datos referidos a energía. Por ejemplo: 'Productos mineros exportados' o 'Precios del GNC'. |
| ENVI               | Medio ambiente                     | Datos referidos a medio ambiente. Por ejemplo: 'Operadores de residuos peligrosos'. |
| GOVE               | Gobierno y sector público          | Datos referidos a gobierno y sector público. Por ejemplo: 'Inmuebles del estado Nacional'. |
| HEAL               | Salud                              | Datos referidos a salud. Por ejemplo: 'Estadísticas nacionales de VIH/SIDA'. |
| INTR               | Asuntos internacionales            | Datos referidos a asuntos internacionales. Por ejemplo: 'Representaciones argentinas en el exterior'. |
| JUST               | Justicia, seguridad y legales      | Datos referidos a justicia, seguridad y legales. Por ejemplo: 'Censo penitenciario'. |
| REGI               | Regiones y ciudades                | Datos referidos a regiones y ciudades. Por ejemplo: 'Departamentos de la provincia de Río Negro'. |
| SOCI               | Población y sociedad               | Datos referidos a población y sociedad. Por ejemplo: 'Turistas residentes que viajan por Argentina'. |
| TECH               | Ciencia y tecnología               | Datos referidos a ciencia y tecnología. Por ejemplo: 'Recursos humanos en ciencia y tecnología'. |
| TRAN               | Transporte                         | Datos referidos a transporte. Por ejemplo: 'Estadísticas viales'. |

Esta es la [taxonomía temática global](https://raw.githubusercontent.com/datosgobar/paquete-apertura-datos/master/standards/metadata/superThemeTaxonomy.json) en JSON:

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

### Anexo III - Ejemplo de catálogo

Este es un [ejemplo de catálogo en data.json](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/data.json):

```json
{
  "title": "Datos Argentina",
  "description": "Portal de Datos Abiertos del Gobierno de la República Argentina",
  "publisher": {
    "name": "Jefatura de Gabinete de Ministros",
    "mbox": "datos@jgm.gob.ar"
  },
  "issued": "2016-04-14T19:48:05.433640-03:00",
  "modified": "2016-04-19T19:48:05.433640-03:00",
  "language": [
    "spa"
  ],
  "superThemeTaxonomy": "https://datos.gob.ar/superThemeTaxonomy.json",
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
  "license": "Creative Commons Attribution 4.0",
  "homepage": "https://datos.gob.ar",
  "rights": "Derechos especificados en la licencia.",
  "spatial": "ARG",
  "dataset": [
    {
      "title": "Sistema de Contrataciones Electrónicas (Argentina Compra)",
      "description": "Datos correspondientes al Sistema de Contrataciones Electrónicas (Argentina Compra)",
      "publisher": {
        "name": "Jefatura de Gabinete de Ministros. Secretaría de Innovación Administrativa. Oficina Nacional de Contrataciones",
        "mbox": "onc@jgm.gob.ar"
      },
      "contactPoint": {
        "fn": "Jefatura de Gabinete de Ministros. Secretaría de Innovación Administrativa. Oficina Nacional de Contrataciones. Dirección de Compras Electrónicas.",
        "hasEmail": "onc-compraselectronicas@jgm.gob.ar"
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
      "landingPage": "https://datos.gob.ar/dataset/modernizacion-sistema-contrataciones-electronicas-argentina-compra",
      "license": "Creative Commons Attribution 4.0",
      "distribution": [
        {
          "accessURL": "https://datos.gob.ar/dataset/modernizacion-sistema-contrataciones-electronicas-argentina-compra/archivo/modernizacion_2.1",
          "description": "Listado de las convocatorias abiertas durante el año 2015 en el sistema de contrataciones electrónicas",
          "format": "CSV",
          "mediaType": "text/csv",
          "downloadURL": "https://infra.datos.gob.ar/catalog/modernizacion/dataset/2/distribution/2.1/download/convocatorias-2017.csv",
          "title": "Convocatorias 2017",
          "license": "Creative Commons Attribution 4.0",
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

Este es el mismo [ejemplo de catálogo en texto](https://github.com/datosgobar/paquete-apertura-datos/blob/master/examples/data.md):

**Catálogo: Datos Argentina**

Portal de Datos Abiertos del Gobierno de la República Argentina

* Derechos sobre el catálogo: Derechos especificados en la licencia.
* Correo electrónico del autor: datos@jgm.gob.ar
* Autor: Jefatura de Gabinete de Ministros
* Licencia: Creative Commons Attribution 4.0
* Idioma(s): spa
* Fecha de creación o publicación: 2016-04-14T19:48:05.433640-03:00
* Taxonomía temática global: [https://datos.gob.ar/superThemeTaxonomy.json](https://datos.gob.ar/superThemeTaxonomy.json)
* Fecha de última actualización/modificación: 2016-04-19T19:48:05.433640-03:00
* Cobertura geográfica: ARG
* Página web del catálogo: [https://datos.gob.ar](https://datos.gob.ar/)

**Taxonomía temática específica**

* Convocatorias (convocatorias): Datasets sobre licitaciones en estado de convocatoria.
* Compras (compras): Datasets sobre compras realizadas.
* Contrataciones (contrataciones): Datasets sobre contrataciones.
* Adjudicaciones (adjudicaciones): Datasets sobre licitaciones adjudicadas.
* Normativa (normativa): Datasets sobre normativa para compras y contrataciones.
* Proveedores (proveedores): Datasets sobre proveedores del Estado.

**Datasets**

**Dataset: Sistema de Contrataciones Electrónicas (Argentina Compra)**

Datos correspondientes al Sistema de Contrataciones Electrónicas (Argentina Compra)

* **Correo electrónico del autor**: onc@jgm.gob.ar
* **Autor**: Jefatura de Gabinete de Ministros. Secretaría de Innovación Administrativa. Oficina Nacional de Contrataciones
* **Página de referencias**: [https://datos.gob.ar/dataset/modernizacion-sistema-contrataciones-electronicas-argentina-comprampra)
* **Temática(s) globales**: ECON
* **Fecha de publicación**: 2016-04-14T19:48:05.433640-03:00
* **Cobertura temporal**: 2015-01-01/2015-12-31
* **Fecha de última actualización/ modificación**: 2016-04-19T19:48:05.433640-03:00
* **Idioma(s)**: spa
* **Temática(s) específicas**: contrataciones, compras, convocatorias
* **Etiqueta(s)**: bienes, compras, contrataciones
* **Frecuencia de actualización**: R/P1Y
* **Cobertura geográfica**: ARG
* **Licencia**: Creative Commons Attribution 4.0
* **Correo electrónico del área/persona de contacto**: onc-compraselectronicas@jgm.gob.ar
* **Área/Persona de contacto**: Jefatura de Gabinete de Ministros. Secretaría de Innovación Administrativa. Oficina Nacional de Contrataciones. Dirección de Compras Electrónicas.
* **Identificador**: 99db6631-d1c9-470b-a73e-c62daa32c420

*Distribuciones*

**Distribución: Convocatorias 2017**

Listado de las convocatorias abiertas durante el año 2015 en el sistema de contrataciones electrónicas

* **URL de acceso**: [https://datos.gob.ar/dataset/modernizacion-sistema-contrataciones-electronicas-argentina-compra/archivo/modernizacion_2.1](https://datos.gob.ar/dataset/modernizacion-sistema-contrataciones-electronicas-argentina-compra/archivo/modernizacion_2.1)
* **Derechos sobre la distribución**: Derechos especificados en la licencia.
* **Licencia**: Creative Commons Attribution 4.0
* **Tamaño**: 5120
* **Formato del archivo**: CSV
* **Tipo de archivo**: text/csv
* **Fecha de última actualización/ modificación**: 2016-04-19T19:48:05.433640-03:00
* **URL de descarga**: [https://infra.datos.gob.ar/catalog/modernizacion/dataset/2/distribution/2.1/download/convocatorias-2017.csv](https://infra.datos.gob.ar/catalog/modernizacion/dataset/2/distribution/2.1/download/convocatorias-2017.csv)
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

### Anexo IV - Series de tiempo

Ejemplo de dataset con series de tiempo en JSON:

* **Dataset 1**: Oferta y Demanda Globales. Datos desestacionalizados. Base 1993
  - **Distribucion 1.1**: Oferta y Demanda Global. Precios constantes desestacionalizados. Base 1993. Valores anuales.
  - **Distribucion 1.2**: Oferta y Demanda Global. Precios constantes desestacionalizados. Base 1993. Valores trimestrales.

#### Dataset (`dataset`) - series de tiempo

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
  "landingPage": "https://www.minhacienda.gob.ar/secretarias/politica-economica/programacion-macroeconomica/",
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

#### Distribución (`distribution`) - series de tiempo

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

#### Campo (`field`) - series de tiempo

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

#### Catálogo (catalog) - series de tiempo

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
  "license": "Creative Commons Attribution 4.0",
  "superThemeTaxonomy": "https://datos.gob.ar/superThemeTaxonomy.json",
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
      "landingPage": "https://www.minhacienda.gob.ar/secretarias/politica-economica/programacion-macroeconomica/",
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

### Anexo V - Pautas para la selección de etiquetas

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
