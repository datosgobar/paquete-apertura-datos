# Guía para la identificación y uso de entidades interoperables

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

## Indice

- [Introducción](#introduccion)
- [Objetivo de esta guía](#objetivo-de-esta-guia)
- [Datos de entidades interoperables](#datos-de-entidades-interoperables)
  - [¿Qué son?](#que-son)
  - [¿Por qué es importante estandarizarlos?](#por-que-es-importante-estandarizarlos)
- [Tipos de entidades interoperables](#tipos-de-entidades-interoperables)
  - [Geográficas](#geograficas)
    - [Países o territorios internacionales](#paises-o-territorios-internacionales)
    - [Divisiones o unidades territoriales internas](#divisiones-o-unidades-territoriales-internas)
      - [A. Provincias -> Departamentos -> Fracciones Censales -> Radios Censales (PDFR)](#a-provincias-departamentos---fracciones-censales---radios-censales-pdfr)
      - [B. Provincias -> Municipios (PM)](#b-provincias-municipios-pm)
      - [C. Provincias -> Departamentos -> Localidades (PDL)](#c-provincias-departamentos---localidades-pdl)
      - [D. Aglomerados](#d-aglomerados)
      - [E. ¿Cómo nombrar los campos?](#e-como-nombrar-los-campos)
    - [Direcciones y lugares](#direcciones-y-lugares)
    - [**Códigos postales**](#codigos-postales)
  - [**Personas físicas**](#personas-fisicas)
  - [**Personas jurídicas**](#personas-juridicas)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Introducción

Esta guía busca ayudar a los organismos a instrumentar la Política de Datos Abiertos impulsada desde el Gobierno de la Nación Argentina, a través del Decreto N° 117/2016 del 12 de enero de 2016.

## Objetivo de esta guía

Esta es una **guía de buenas prácticas para el uso de entidades interoperables**. Se trata de datos básicos y fundamentales cuyo uso se repite frecuentemente entre datasets de temáticas y fuentes distintas.

Para hacer estas recomendaciones, nos basamos en estándares usados a nivel nacional e internacional y en la experiencia de trabajo del equipo de la Dirección Nacional de Datos e Información Pública del Ministerio de Modernización de la Nación.

Esta es **una guía colaborativa y en progreso**. Valoramos, y alentamos, a organizaciones y ciudadanos a plantear ideas, sugerencias, y comentarios que nos ayuden a crear un mejor documento.

Para una discusión sobre la estandarización de datos, recomendamos consultar la **Guía para la publicación de datos en formatos abiertos**. Este documento se complementa con esa guía y la **Guía para el uso y la publicación de metadatos**.

## Datos de entidades interoperables

### ¿Qué son?

Las entidades interoperables **son aquellas que se repiten y usan frecuentemente** **dentro de datasets de**:

* **Temáticas diversas entre sí**.

* **Una misma temática** (ej.: Salud), **pero no de otras** (como Educación, Economía, Transporte, etc).

La mayoría de los datasets incluyen campos que responden al dónde, quién, cuándo y qué. Estos campos permiten que los datasets sean interoperables entre sí.

Veamos un ejemplo. Una matriz origen-destino de pasajeros de transporte urbano que dice cuántos viajes se hacen desde la fracción censal A a la fracción censal B, puede interoperar con datos del Censo Nacional sobre las personas que viven en A o en B (desocupación, edad, condiciones de la vivienda, actividad laboral, etc.). Decimos entonces, que la fracción censal es una entidad interoperable.

Algunos ejemplos de entidades interoperables pueden ser:

* **Transversales** (afectan a la mayoría de las áreas temáticas)

    * **¿Dónde?**: geografía (países, provincias, departamentos, fracciones censales, localidades, direcciones, códigos postales).

    * **¿Quién?**: personas (físicas, jurídicas). Entidades (niveles gubernamentales, organismos internacionales, otros países, sociedad civil).

    * **¿Qué?**: categorías presupuesto. Clasificación de bienes transables.

* **Específicas** (afectan a alguna/s área/s temática/s específica/s)

    * **¿Qué?**: actividades económicas. Clasificación de enfermedades. Clasificación de términos clínicos. Clasificación de unidades educativas.

### ¿Por qué es importante estandarizarlos?

**Las entidades interoperables son las que permiten que los datasets hablen entre sí**, pero **esto no puede suceder cuando dos datasets nombran de forma distinta** a una misma entidad interoperable (como cuando se usan distintos sistemas de *ids* o se nombra una misma entidad con/sin mayúsculas, usando artículos y preposiciones (o no usándolos), usando abreviaturas, siglas, tildes, forma corta o completa de un nombre, etc.

Para que los datasets puedan ser interoperables, **deben identificarse todas las entidades interoperables presentes en un dataset y asegurarse de que los datos sobre ellas siguen el mismo estándar**.

A continuación, **proponemos una selección de estándares** producidos por organismos de la Administración Pública Nacional para identificación y uso de entidades interoperables presentes en un activo de datos, en algunas categorías transversales a varias áreas temáticas. **Recomendamos con énfasis usarlos** en todos aquellos casos en los que estén presentes esas entidades. Si por algún motivo esto fuera difícil de aplicar, sugerimos crear un diccionario que permita la traducción de estándares propios a los recomendados.

En los casos de **entidades interoperables específicas sobre alguna temática**, recomendamos **usar el estándar más difundido entre quienes trabajan con frecuencia sobre esa temática dentro de la Administración Pública Nacional**.

**Cuando no existan** estándares claros dentro de la APN para algún tipo de entidad interoperable en particular, sugerimos **adoptar el mejor estándar internacional en uso**, y seguirlo en forma consistente en todos los datasets que genere el organismo.

**La adopción de estándares** para el uso de datos de entidades interoperables está **sujeto a cambios y versionados. Por eso, siempre es importante comunicarlos** en forma clara y consistente.

Consideramos a los estándares que recomendamos en este documento como suficientemente estables, abarcativos, difundidos y mantenidos como para que su uso sea beneficioso para el aprovechamiento de los datos y su adopción transparente.

## Tipos de entidades interoperables

### Geográficas

#### Países o territorios internacionales

Los nombres y códigos de países o territorios internacionales deben seguir el estándar [ISO 3166-1](https://es.wikipedia.org/wiki/ISO_3166-1). Recomendamos que el dataset contenga un campo con el código alfabético de 3 dígitos del estándar (Código alfa-3) y otro con el nombre completo del país en español. Para esto, recomendamos usar los "Nombres de uso común" de la [lista de países y sus códigos alfa-3 que publica INDEC](http://www.indec.gov.ar/ftp/cuadros/territorio/codigo_paises.xls).

En esta guía, elegimos incluir los nombres de países oficiales y en castellano. Sin embargo, la denominación de los países varía de acuerdo al idioma que se utilice. Por eso, hacemos énfasis en la necesidad de incluir el código de país según el estándar ISO 3166, que es ampliamente usado por organismos internacionales.

A modo de ejemplo, en la Argentina nos referimos a uno de nuestros países vecinos coloquialmente como "Brasil", mientras que el nombre oficial en portugués es “República Federativa do Brasil” y la traducción oficial en español “República Federativa del Brasil”. El código de país según el estándar definido es “BRA” lo cual resuelve el problema de denominación.

Se recomienda también que el nombre del campo del código sea "pais_id" o, en el caso de que haya más de un campo “país” en el dataset, el nombre de cada campo finalice con “pais_id” (Ej.: “desde_pais_id”, “hasta_pais_id”), mientras que el campo con el nombre completo del país debería ser “pais_nombre”.

<span class="no-recomendado">**No recomendado**</span>

<table>
<tbody>
  <tr>
    <td>pais_origen</td>
    <td>pais_destino</td>
    <td>valor_usd</td>
  </tr>
  <tr>
    <td>Argentina</td>
    <td>China</td>
    <td>1405678</td>
  </tr>
  <tr>
    <td>República Popular China</td>
    <td>argentina</td>
    <td>2456786</td>
  </tr>
</tbody>
</table>

<span class="recomendado">**Recomendado**</span>

<table>
 <colgroup>
    <col style="width:18%">
    <col style="width:22%">
    <col style="width:18%">
    <col style="width:24%">
    <col style="width:18%">
  </colgroup>
<tbody>
  <tr>
    <td>origen_pais_id</td>
    <td>origen_pais_nombre</td>
    <td>destino_pais_id</td>
    <td>destino_pais_nombre</td>
    <td>valor_usd</td>
  </tr>
  <tr>
    <td>ARG</td>
    <td>Argentina</td>
    <td>CHN</td>
    <td>China</td>
    <td>1405678</td>
  </tr>
  <tr>
    <td>CHN</td>
    <td>China</td>
    <td>ARG</td>
    <td>Argentina</td>
    <td>2456786</td>
  </tr>
</tbody>
</table>


#### Divisiones o unidades territoriales internas

En el caso de las divisiones o unidades territoriales internas, recomendamos usar el sistema de identificadores de la cartografía censal del Censo Nacional 2010 del Instituto Nacional de Estadísticas y Censos ([listado de códigos](http://200.51.91.245/redarg/CENSOS/CPV2010rad/Docs/codigos_provincias.pdf) y [explicación metodológica](http://geoservicios.indec.gov.ar/codgeo/index.php?pagina=definiciones)), que incluye identificadores numéricos compuestos de una cantidad fija de dígitos (el tipo de datos debe ser textual, ya que tiene ceros a la izquierda que son significativos) para, entre otras, las siguientes entidades interoperables:

* Provincias
* Departamentos (Partidos o Comunas)
* Fracciones Censales
* Radios Censales
* Municipios
* Localidades
* Aglomerados

Este sistema de identificadores es consistente con el  usado por la Base de Asentamientos Humanos de la República Argentina ([BAHRA](http://www.bahra.gob.ar/)) para la identificación de localidades, que además lo extiende para incluir la posibilidad de referenciar sitios edificados (sumando 3 dígitos al identificador de una Localidad).

Sin embargo, en esta guía no abordamos los identificadores de entidades puntuales derivadas de las Localidades ( que implican avanzar a niveles de desagregación geográfica mayores).

Los nombres geográficos presentados en la BAHRA son oficiales, pero no se encuentran validados. El establecimiento de un procedimiento para la validación de los nombres geográficos es una tarea pendiente para la República Argentina.

¿Cómo se relacionan estas entidades entre sí? Veremos que estas unidades pueden ordenarse jerárquicamente de modo tal que algunas contienen a las otras, aunque no en todos los casos.  A continuación,  explicamos los conjuntos de entidades que conforman una jerarquía internamente consistente.

##### A. Provincias -> Departamentos -> Fracciones Censales -> Radios Censales (PDFR)

**La provincia es la jurisdicción de primer orden** que marca una división político-territorial de la República Argentina. El territorio nacional se divide en 23 de ellas (más la Ciudad de Buenos Aires), siendo que algunos territorios pueden ser marcados como "Indeterminado" (98) o "Sin declarar-Desconocido-Ignorado" (99).

Una **provincia se subdivide** a su vez en jurisdicciones de segundo orden que marcan una división político-administrativa y son llamadas **departamentos** en la mayoría de las provincias (con la excepción de la Provincia de Buenos Aires -Partidos- y la Ciudad de Buenos Aires -comunas-).

Un **departamento, a su vez, se puede subdividir en fracciones censales**, mientras que una **fracción censal se subdivide en radios censales**. Estas son unidades censales que forman parte de la estructura de relevamiento censal.

El tamaño de las fracciones y los radios en áreas urbanas se determina según la cantidad de viviendas. La fracción tiene un promedio de 5000 viviendas mientras que el radio tiene un promedio de 300.

Para bordes de localidades el radio urbano puede bajar a 200 viviendas, aproximadamente, y en localidades aisladas a 100 viviendas. En zonas rurales las fracciones y radios se determinan por la conjunción de distintos factores: características del terreno, accesibilidad y distancia entre las viviendas.

Los identificadores de cada una de estas divisiones se componen, sucesivamente, así:

<table id="identificadores-geograficos">
  <tr>
    <td><bold>Provincia</bold><br/>
    2 dígitos<br/>
    "06"<br/>
    Buenos Aires
    </td>
    <td><bold>Departamento</bold><br/>
    5 dígitos<br/>
    "06007"<br/>
    Adolfo Alsina
    </td>
    <td><bold>Fracción Censal</bold><br/>
    7 dígitos<br/>
    "0600702"
    </td>
    <td><bold>Radio Censal</bold><br/>
    9 dígitos<br/>
    "060070201"
    </td>
  </tr>
</table>


* **Provincia**: 2 dígitos. Ej.: "06" es la Provincia de “Buenos Aires”.

* **Departamento** (Partido -Provincia de Buenos Aires- o Comuna -Ciudad de Buenos Aires-): 5 dígitos. - Ej.: "06007" es el Departamento “Adolfo Alsina” de la provincia de “Buenos Aires”.

* **Fracciones censales**: 7 dígitos. - Ej.: "0600702" es una Fracción Censal del Departamento “Adolfo Alsina” de la provincia de “Buenos Aires”.

* **Radios censales**: 9 dígitos. - Ej.: "060070201" es un Radio Censal de la Fracción Censal “0600702” del Departamento “Adolfo Alsina” de la provincia de “Buenos Aires”.

##### B. Provincias -> Municipios (PM)

**Los municipios están contenidos por las provincias**, pero no las subdividen. Entre medio de ellos puede haber áreas rurales que no pertenezcan a ningún municipio. Los municipios son figuras políticas cuya normativa es potestad de cada provincia y puede haber diferencias significativas entre lo que se considera un municipio en cada una de ellas. Por ejemplo, en algunas provincias los municipios coinciden con los departamentos.

Sin embargo, un municipio siempre está completamente contenido por una sola provincia. Entre las divisiones territoriales internas consideradas en este documento, no hay otra que siempre contenga municipios completos. La superficie de un municipio puede atravesar los límites de departamentos, fracciones y radios censales (un municipio puede estar presente en uno o varios de ellos).

Los identificadores de los municipios se componen entonces con los de las provincias, así:


<table id="identificadores-geograficos" style="width: 50%" >
  <tr>
    <td><bold>Provincia</bold><br/>
    2 dígitos<br/>
    "14"<br/>
    Córdoba
    </td>
    <td><bold>Municipio</bold><br/>
    6 dígitos<br/>
    "140399"<br/>
    Camerillo
    </td>
  </tr>
</table>



* **Municipios**: 6 dígitos. - Ej.: "140399" es el Municipio “Camerillo” de la provincia de “Córdoba”.

##### C. Provincias -> Departamentos -> Localidades (PDL)

Las localidades censales están contenidas tanto por los departamentos como por los municipios. Para componer el identificador se deben usar los departamentos, de tal manera que los primeros 5 dígitos del identificador de una localidad corresponden al identificador del departamento que lo contiene, **los siguientes 3 dígitos son propios de la localidad**:


<table style="width: 70%" id="identificadores-geograficos">
  <tr>
    <td><bold>Provincia</bold><br/>
    2 dígitos<br/>
    "06"<br/>
    Buenos Aires
    </td>
    <td><bold>Departamento</bold><br/>
    5 dígitos<br/>
    "06007"<br/>
    Adolfo Alsina
    </td>
    <td><bold>Localidad</bold><br/>
    8 dígitos<br/>
    "06007010"<br/>
    Carhué
    </td>
      </tr>
</table>



* **Localidades**: 8 dígitos. - Ej.: "06007010" es la localidad “Carhué” del departamento “Adolfo Alsina” de la provincia de “Buenos Aires”.

La Ciudad de Buenos Aires constituye una excepción a esta regla ya que es una localidad compuesta por departamentos (comunas), de manera que no puede componerse identificador compuesto de tipo provincia-departamento-localidad. Para este caso, recomendamos usar el identificador de jurisdicción de primer nivel de la Ciudad de Buenos Aires ("02").

##### D. Aglomerados

Los aglomerados están definidos como conjuntos de localidades y tienen un* id *simple de 4 dígitos (no compuesto) ya que un aglomerado puede cruzar el límite entre 2 municipios, departamentos o provincias.


<table style="width: 30%" id="identificadores-geograficos">
  <tr>
    <td><bold>Aglomerado</bold><br/>
    4 dígitos<br/>
    "0001"<br/>
    Gran Buenos Aires
    </td>
    </tr>
</table>


##### E. ¿Cómo nombrar los campos?

Al igual que en el caso de los países o territorios internacionales, el dataset debe contener un campo con el código de la división o unidad territorial interna y otro con el nombre o descripción (en caso de que la tenga, anteriormente dijimos que las fracciones y radios censales no tienen nombre o descripción).

Los nombres de los campos identificadores deben ser, respectivamente:

* "provincia_id"
* "departamento_id"
* "fraccion_id"
* "radio_id"
* "municipio_id"
* "localidad_id"
* "aglomerado_id"

Análogamente, debe reemplazarse "_id" por “_nombre” para nombrar los campos que contiene el nombre de cada entidad, cuando esta lo tiene.

Resaltamos la importancia de que el tipo de datos del campo de un identificador es "textual" y no “numérico”. Esto es así porque un valor de tipo numérico no podría comenzar con ceros.

<span class="no-recomendado">**No recomendado**</span>

<table>
<tbody>
  <tr>
    <td>provincia</td>
    <td>flujo_comercial_tipo</td>
    <td>valor_usd</td>
  </tr>
  <tr>
    <td>Santiago del Estero</td>
    <td>Exportación</td>
    <td>1405678</td>
  </tr>
  <tr>
    <td>Stgo. del Estero</td>
    <td>Importación</td>
    <td>2456786</td>
  </tr>
  <tr>
    <td>Buenos Aires</td>
    <td>Exportación</td>
    <td>44949874</td>
  </tr>
  <tr>
    <td>BA</td>
    <td>Importación</td>
    <td>44040711</td>
  </tr>
</tbody>
</table>


<span class="recomendado">**Recomendado**</span>

<table>
<tbody>
  <tr>
    <td>provincia_id</td>
    <td>provincia_nombre</td>
    <td>flujo_comercial_tipo</td>
    <td>valor_usd</td>
  </tr>
  <tr>
    <td>86</td>
    <td>Santiago del Estero</td>
    <td>Exportación</td>
    <td>1405678</td>
  </tr>
  <tr>
    <td>86</td>
    <td>Santiago del Estero</td>
    <td>Importación</td>
    <td>2456786</td>
  </tr>
  <tr>
    <td>06</td>
    <td>Buenos Aires</td>
    <td>Exportación</td>
    <td>44949874</td>
  </tr>
  <tr>
    <td>06</td>
    <td>Buenos Aires</td>
    <td>Importación</td>
    <td>440407</td>
  </tr>
</tbody>
</table>


#### Direcciones y lugares

Siempre que sea posible, cuando un dataset contenga información que identifica a un punto en el espacio geográfico, recomendamos incluir las coordenadas de la manera establecida en la tercera tabla. Las coordenadas de un punto deben ser números decimales negativos o positivos contenidos en dos campos llamados "latitud" y “longitud”.

Si el dataset contiene información sobre direcciones (especialmente en los casos en los que no sea posible proveer coordenadas), recomendamos incluir:

* "calle_nombre"
* "calle_numero"
* "localidad_id"
* "localidad_nombre"
* "provincia_id"
* "provincia_nombre"

Si el dataset incluye direcciones fuera del territorio argentino, deben además incluirse:

* "pais_id"
* "pais_nombre"

<span class="no-recomendado">**No recomendado**</span>

<table>

<tbody>
  <tr>
    <td>lugar_nombre</td>
    <td>calle_nombre</td>
    <td>calle_numero</td>
    <td>ciudad</td>
  </tr>
  <tr>
    <td>Teatro Colón</td>
    <td>Cerrito</td>
    <td>604</td>
    <td>Ciudad Autónoma de Buenos Aires, CABA</td>
  </tr>
</tbody>
</table>


**Aceptable 1** - sólo dirección normalizada

<table>
 <colgroup>
    <col style="width:14%">
    <col style="width:14%">
    <col style="width:14%">
    <col style="width:14%">
     <col style="width:15%">
    <col style="width:13%">
    <col style="width:16%">
  </colgroup>
<tbody>
  <tr>
    <td style="font-size:11px;">lugar_nombre</td>
    <td style="font-size:11px;">calle_nombre</td>
    <td style="font-size:11px;">calle_numero</td>
    <td style="font-size:11px;">localidad_id</td>
    <td style="font-size:11px;">localidad_nombre</td>
    <td style="font-size:11px;">provincia_id</td>
    <td style="font-size:11px;">provincia_nombre</td>
  </tr>
  <tr>
    <td>Teatro Colón</td>
    <td>Cerrito</td>
    <td>604</td>
    <td>02001010</td>
    <td style="font-size:11px;">Ciudad de Buenos Aires</td>
    <td>02</td>
    <td style="font-size:11px;">Ciudad Autónoma de Buenos Aires</td>
  </tr>
</tbody>
</table>


**Aceptable 2** - sólo coordenadas

<table>
<tbody>
  <tr>
    <td>lugar_nombre</td>
    <td>latitud</td>
    <td>longitud</td>
  </tr>
  <tr>
    <td>Teatro Colón</td>
    <td>-34.601041</td>
    <td>-58.383079</td>
  </tr>
</tbody>
</table>


<span class="recomendado">**Recomendado**</span> - coordenadas y dirección normalizada

<table>
<tbody>
  <tr>
    <td  style="font-size:11px;">lugar_nombre</td>
    <td style="font-size:11px;">calle_nombre</td>
    <td style="font-size:11px;">calle_numero</td>
    <td style="font-size:11px;">localidad_id</td>
    <td style="font-size:11px;">localidad_nombre</td>
    <td style="font-size:11px;">provincia_id</td>
    <td style="font-size:11px;">provincia_nombre</td>
    <td style="font-size:11px;">latitud</td>
    <td style="font-size:11px;">longitud</td>
  </tr>
  <tr>
    <td style="font-size:10px;">Teatro Colón</td>
    <td style="font-size:9px;">Cerrito</td>
    <td style="font-size:10px;">604</td>
    <td style="font-size:10px;">02001010</td>
    <td style="font-size:10px;">Ciudad de Buenos Aires</td>
    <td style="font-size:10px;">02</td>
    <td style="font-size:10px;">Ciudad Autónoma de Buenos Aires</td>
    <td style="font-size:10px;">-34.601041</td>
    <td style="font-size:10px;">-58.383079</td>
  </tr>
</tbody>
</table>


#### **Códigos postales**

Los códigos postales deben estar contenidos en un campo llamado "codigo_postal" y seguir el formato definido por el Correo Argentino para el [Código Postal Argentino (CPA)](http://www.correoargentino.com.ar/formularios/cpa) a partir de la competencia asignada por la Secretaría de Comunicaciones mediante la Resolución N° 1368/98.

El CPA amplía la información del código postal, incorporando 4 letras que permiten identificar cada cara de manzana en las localidades de más de 500 habitantes. Las localidades de menos de 500 habitantes poseen un único CPA.

El CPA se compone de:

* 1 letra: Identifica a la Provincia.
* 4 números: El Código Postal tradicional.
* 3 letras: Identifican a la Cara de la Manzana.

Ej.: C1426BMD

<span class="no-recomendado">**No recomendado**</span>

<table  id="una-columna">
<tbody>
  <tr>
    <td>codigo_postal</td>
  </tr>
  <tr>
    <td>1426</td>
  </tr>
  <tr>
    <td>C 1426 BMD</td>
  </tr>
  <tr>
    <td>c1426bmd</td>
  </tr>
  <tr>
    <td>C1426</td>
  </tr>
</tbody>
</table>


<span class="recomendado">**Recomendado**</span>

<table id="una-columna">
<tbody>
  <tr>
    <td>codigo_postal</td>
  </tr>
  <tr>
    <td>C1426BMD</td>
  </tr>
  <tr>
    <td>C1426BMD</td>
  </tr>
  <tr>
    <td>C1426BMD</td>
  </tr>
  <tr>
    <td>C1426BMD</td>
  </tr>
</tbody>
</table>


### **Personas físicas**

Las personas físicas deben identificarse por su nombre completo separado en dos campos ("nombre" y “apellido”), cuando sea posible, donde deben consignarse todos los nombres y todos los apellidos que identifican a un individuo en su documento de identidad oficial, sea el que corresponda según el individuo se presente como residente nacional o extranjero.

Así mismo, recomendamos (de ser posible) agregar dos columnas "id" y “tipo_id” que respectivamente contengan el número o cadena de caracteres que constituye el identificador del documento oficial de la persona y el tipo de documento oficial al que este identificador corresponde (Ej.: DNI, LE, LC y Pasaporte).

Esto es sencillo en el caso de residentes nacionales, pero la variedad de tipos de documentos oficiales que puede presentar un residente extranjero es mucho más amplia y difícil de abarcar. En este último caso es suficiente con consignar si el documento es un "Pasaporte" u “Otro”. Adicionalmente, si el dataset puede contener datos de individuos de diferentes nacionalidades recomendamos agregar un campo “_pais” que contenga la nacionalidad del individuo de referencia.

Tal como explicamos en el caso de países o territorios internacionales, si hubiera más de un campo relativo a "personas" o la mera nomenclatura “nombre” pudiera prestarse a confusión, los campos correspondientes serán compuestos. Ejemplo:

* "sujeto_obligado_nombre"
* "sujeto_obligado_apellido"
* "sujeto_obligado_id"
* "sujeto_obligado_tipo_id"
* "sujeto_obligado_pais_id"
* "sujeto_obligado_pais_nombre"
* "representante_nombre"
* "representante_apellido"
* "representante_id"
* "representante_tipo_id"

<span class="no-recomendado">**No recomendado**</span>

<table>
<tbody>
  <tr>
    <td>sujeto_obligado</td>
    <td>representante</td>
  </tr>
  <tr>
    <td>José Pérez</td>
    <td>Carlos Gómez</td>
  </tr>
  <tr>
    <td>josé Pérez</td>
    <td>Carlos J. Gómez</td>
  </tr>
  <tr>
    <td>Pérez, José</td>
    <td>Gómez, Carlos</td>
  </tr>
  <tr>
    <td>Pérez, José</td>
    <td>Gómez, Carlos J.</td>
  </tr>
</tbody>
</table>


**Aceptable**

<table>
<tbody>
  <tr>
    <td  style="font-size:11px;">sujeto_obligado_nombre</td>
    <td style="font-size:11px;">sujeto_obligado_apellido</td>
    <td style="font-size:11px;">representante_nombre</td>
    <td style="font-size:11px;">representante_apellido</td>
  </tr>
  <tr>
    <td>José</td>
    <td>Pérez</td>
    <td>Carlos Jorge</td>
    <td>Gómez</td>
  </tr>
  <tr>
    <td>José</td>
    <td>Pérez</td>
    <td>Carlos Jorge</td>
    <td>Gómez</td>
  </tr>
  <tr>
    <td>José</td>
    <td>Pérez</td>
    <td>Carlos Jorge</td>
    <td>Gómez</td>
  </tr>
  <tr>
    <td>José</td>
    <td>Pérez</td>
    <td>Carlos Jorge</td>
    <td>Gómez</td>
  </tr>
</tbody>
</table>


<span class="recomendado">**Recomendado**</span>

<table>
<colgroup>
    <col style="width:20%">
    <col style="width:15%">
    <col style="width:15%">
    <col style="width:15%">
    <col style="width:15%">
    <col style="width:20%">
  </colgroup>
  <tbody>
  <tr>
    <td style="font-size:10px;">sujeto_obligado_nombre</td>
    <td style="font-size:10px;">sujeto_obligado_apellido</td>
    <td style="font-size:10px;">sujeto_obligado_id</td>
    <td style="font-size:10px;">sujeto_obligado_tipo_id</td>
    <td style="font-size:10px;">sujeto_obligado_pais_id</td>
    <td style="font-size:10px;">sujeto_obligado_pais_nombre</td>
  </tr>
  <tr>
    <td>José</td>
    <td>Pérez</td>
    <td style="font-size:10px;">11111111</td>
    <td>DNI</td>
    <td>ARG</td>
    <td>Argentina</td>
  </tr>
  <tr>
    <td>José</td>
    <td>Pérez</td>
    <td style="font-size:10px;">11111111</td>
    <td>DNI</td>
    <td>ARG</td>
    <td>Argentina</td>
  </tr>
  <tr>
    <td>José</td>
    <td>Pérez</td>
    <td style="font-size:10px;">11111111</td>
    <td>DNI</td>
    <td>ARG</td>
    <td>Argentina</td>
  </tr>
  <tr>
    <td>José</td>
    <td>Pérez</td>
    <td style="font-size:10px;">11111111</td>
    <td>DNI</td>
    <td>ARG</td>
    <td>Argentina</td>
  </tr>
</tbody>
</table>


### **Personas jurídicas**

Las entidades con personería jurídica local (Ej.: empresas argentinas, ONGs argentinas, etc.) deben registrarse con su CUIT y razón social. Por ejemplo:

* "exportador_cuit"
* "exportador_razon_social"

<span class="no-recomendado">**No recomendado**</span>

<table id="una-columna">
<tbody>
  <tr>
    <td>exportador</td>
  </tr>
  <tr>
    <td>Los Tomates Andinos</td>
  </tr>
  <tr>
    <td>Los Tomates</td>
  </tr>
  <tr>
    <td>Los Tomates Andinos SRL</td>
  </tr>
  <tr>
    <td>Tomates Andinos</td>
  </tr>
</tbody>
</table>


<span class="recomendado">**Recomendado**</span>

<table>
<tbody>
  <tr>
    <td>exportador_cuit</td>
    <td>exportador_razon_social</td>
  </tr>
  <tr>
    <td>33111111117</td>
    <td>Los Tomates Andinos SRL</td>
  </tr>
  <tr>
    <td >33111111117</td>
    <td>Los Tomates Andinos SRL</td>
  </tr>
  <tr>
    <td >33111111117</td>
    <td>Los Tomates Andinos SRL</td>
  </tr>
  <tr>
    <td >33111111117</td>
    <td>Los Tomates Andinos SRL</td>
  </tr>
</tbody>
</table>


Si el dataset sólo contiene personas jurídicas registradas en la jurisdicción argentina, el enfoque recomendado para nombrar los campos es el de agregar "_cuit" y “_razon_social” ya que es una nomenclatura específica mucho más descriptiva para el usuario que “_id” y “_desc”. Da cuenta del tipo de “_id” de que se trate y del tipo de descripción asociada.

La Administración Federal de Ingresos Públicos (AFIP) mantiene un [padrón actualizado](http://www.afip.gov.ar/genericos/cinscripcion/archivocompleto.asp) de todas las personas jurídicas que tienen un CUIT registrado en esa dependencia, que puede ser usado para normalizar o buscar la razón social.

En el caso de que el dataset pueda contener personas jurídicas fuera de la jurisdicción argentina, recomendamos un enfoque análogo al tratamiento de personas físicas:

* "inversor_id"
* "inversor_tipo_id" (Ej.: en el caso de una empresa argentina sería “CUIT”)
* "inversor_desc"
* "inversor_pais_id"
* "inversor_pais_nombre"

<span class="recomendado">**Recomendado**</span>

<table>
 <colgroup>
    <col style="width:20%">
    <col style="width:20%">
    <col style="width:17%">
    <col style="width:20%">
    <col style="width:23%">
  </colgroup>
<tbody>
  <tr>
    <td>inversor_id</td>
    <td>inversor_tipo_id</td>
    <td>inversor_desc</td>
    <td>inversor_pais_id</td>
    <td>inversor_pais_nombre</td>
  </tr>
  <tr>
    <td style="font-size:11px;">33111111117</td>
    <td>CUIT</td>
    <td>Los Tomates Andinos SRL</td>
    <td>ARG</td>
    <td>Argentina</td>
  </tr>
  <tr>
    <td style="font-size:11px;">33111111117</td>
    <td>CUIT</td>
    <td>Los Tomates Andinos SRL</td>
    <td>ARG</td>
    <td>Argentina</td>
  </tr>
  <tr>
    <td style="font-size:11px;">1234567890</td>
    <td>TIN</td>
    <td>Tomatoes Inc.</td>
    <td>USA</td>
    <td>Estados Unidos</td>
  </tr>
  <tr>
    <td style="font-size:11px;">987654321</td>
    <td>Steuer-Id</td>
    <td>Tomate</td>
    <td>DEU</td>
    <td>Alemania</td>
  </tr>
</tbody>
</table>


Dependiendo de la forma de recolección de los datos, la temática particular del dataset y las capacidades del organismo responsable del mantenimiento del activo de datos, puede ser difícil la recolección comprehensible de "_id" y “_tipo_id” de las personas jurídicas de jurisdicción extranjera. Por eso, estos campos pueden llegar a quedar frecuentemente en blanco (valor ausente). Sin embargo, recomendamos con especial énfasis registrar el nombre (“_desc”) de la entidad en cuestión y el país bajo cuya jurisdicción se encuentra.

