# Guía para la apertura de datos en gobiernos provinciales y locales

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## Indice

- [Agradecimientos](#agradecimientos)
- [Sobre esta guía](#sobre-esta-guia)
- [1. ¿Qué son los datos abiertos?](#1-que-son-los-datos-abiertos)
    - [Formatos reutilizables](#formatos-reutilizables)
    - [Estándares y buenas prácticas](#estandares-y-buenas-pr%C3%A1cticas)
    - [Licencia libre](#licencia-libre)
- [2. ¿Qué se necesita para hacer apertura de datos?](#2-que-se-necesita-para-hacer-apertura-de-datos)
    - [Equipo](#equipo)
    - [Cómo asociar los roles a los procesos de trabajo](#como-asociar-los-roles-a-los-procesos-de-trabajo)
    - [El equipo según la escala de gobierno](#el-equipo-segun-la-escala-de-gobierno)
    - [Marco normativo](#marco-normativo)
    - [Plataforma de publicación](#plataforma-de-publicacion)
    - [Buenas prácticas](#buenas-practicas)
- [3. ¿Qué datos publicar?](#3-que-datos-publicar)
    - [Listado de datasets recomendados](#listado-de-datasets-recomendados)
- [4. Acercate a tu comunidad](#4-acercate-a-tu-comunidad)
    - [Actores claves](#actores-claves)
    - [Espacios de colaboración](#espacios-de-colaboracion)
- [5. Instrumentos para evaluar la política de apertura](#5-instrumentos-para-evaluar-la-politica-de-apertura)
    - [Índices](#indices)
    - [Indicadores](#indicadores)
- [Reflexiones finales](#reflexiones-finales)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Agradecimientos

Este documento fue realizado por el equipo de la Dirección Nacional de Datos e Información Pública  junto con la Iniciativa Latinoamericana por los Datos Abiertos (ILDA).

La preparación de esta guía de implementación ha sido posible gracias al financiamiento del fondo de transparencia del BID, que se beneficia de las generosas contribuciones de los gobiernos de Canadá, Noruega y Suecia, así como de Mastercard Corporation.

## Sobre esta guía

Desde la aprobación del Plan de Apertura de Datos del decreto 117/2016 y la Ley de Acceso a la Información Pública 27275, cada vez más organismos públicos y distintos niveles de la Administración Pública empezaron a publicar sus datos,  para promover la transparencia de la gestión y que los ciudadanos puedan acceder a datos claros que puedan reutilizar. Si formás parte del equipo de trabajo de una provincia o gobierno local, en esta guía te ofrecemos las bases y los conceptos clave para que puedas diseñar e implementar políticas de datos abiertos.

En la primera sección de esta guía te contamos qué son y qué no son los datos abiertos. En la segunda, vas a encontrar los criterios básicos para llevar adelante una política de apertura y algunas referencias de buenas prácticas nacionales e internacionales que te recomendamos tener en cuenta antes de la implementación. En la tercera, te compartimos un listado de datasets que pueden servir como guía cuando tengas que priorizar y decidir qué publicar.  En la cuarta, te facilitamos algunas herramientas que te permiten conectar con comunidades claves. Por último, conocé algunos indicadores específicos para evaluar el desempeño de tu política.

Incorporar la publicación de datos abiertos como parte del flujo de trabajo genera diferentes resultados. Por un lado, hace que quienes publicamos tomemos conciencia del estado de situación de los activos de datos públicos y hagamos un esfuerzo por mejorar su calidad. Por otro, les da la posibilidad, a los diferentes sectores que articulan con el gobierno, de producir nuevo valor agregado sobre los datos generados y combinarlos con otras fuentes, ya sean propias o de terceros.

Los conceptos y herramientas que te presentamos en esta publicación son la sistematización de buenas prácticas a la que llegamos como resultado de la exploración y testeo de procesos de apertura de datos en la Subsecretaría de Innovación Pública y Gobierno Abierto de la Secretaría de Gobierno de Modernización de la Nación. Algunos de los recursos que compartimos en esta guía son relativamente nuevos y no están todavía extendidos entre las organizaciones del sector público. En otros casos, se trata de herramientas ya conocidas a las que les sumamos algunos aportes para que puedan ser implementados de manera ágil.

## 1. ¿Qué son los datos abiertos?

Los datos son materia prima necesaria para generar información.  Llamamos públicos a aquellos datos que son generados o están bajo la guarda gubernamental. Pero eso no significa que estén abiertos, disponibilizados para que el sector público y el privado, las organizaciones de la sociedad civil, las universidades y la ciudadanía en general, puedan reutilizarlos, agregarles valor y crear nuevos o mejores servicios.

Los datos abiertos son aquellos que se caracterizan por estar publicados en formatos reutilizables, siguiendo estándares y buenas prácticas y que usan explícitamente una licencia libre que permite su reutilización por parte de terceros. En esta primera sección te contamos qué implica cada uno de estos aspectos. 

### Formatos reutilizables

Son los que permiten procesar la información que contienen. Por ejemplo, un archivo de texto separado por comas (CSV) que contiene una lista de los semáforos del municipio y sus coordenadas.

Por el contrario, existen otros formatos que dificultan procesar la información por la manera en que la presentan. Las imágenes escaneadas y los archivos PDF son el ejemplo más claro, ya que pueden contener texto o tablas pero no permiten trabajarlo como tal.

Al momento de publicar los datos, es preferible hacerlo en formatos abiertos como JSON o CSV en lugar de formatos propietarios como DTA o SAV, que requieren una licencia paga para su uso. Hay formatos propietarios con mucha difusión y aceptación,  como XLSX. Si ya publicás los datos en estos formatos, te recomendamos hacerlo también en un formato abierto. Por ejemplo, si publicás en XLSX, hacerlo además en CSV.
 
### Estándares y buenas prácticas

Diferentes áreas temáticas cuentan con marcos de guía y referencia -locales, nacionales e incluso internacionales- que colaboran con la mejor publicación de sus datos y, además, fuerzan a las organizaciones a pensar qué tipo de datos precisan, cómo los recolectan, de qué manera se almacenan y cómo son los procesos de uso de los mismos.

En ese sentido, se pueden encontrar numerosos ejemplos de estándares de datos como el de Contrataciones Abiertas, el  General Feeds Transport Specification  (GFTS) o incluso el de femicidios que se encuentra desarrollando Iniciativa Latinoamericana por los Datos Abiertos (ILDA).

Entre los procedimientos recomendables es importante considerar los metadatos, es decir grupos de datos que describen el contenido informativo de un recurso o datasets. La fecha de creación, qué organismo es responsable de la base, la versión de la base datos, son ejemplos de metadatos. Los metadatos son útiles para poder contextualizar y entender el orígen de los datos que informa el análisis y uso por parte de terceros.

A mayor cantidad de metadatos más sencillo resulta el uso de datos. En particular, los metadatos sobre la fecha y las condiciones de reutilización aplicables deben conservarse -no alterarse ni suprimirse- ya que son de suma importancia para entender en forma más acabada los datos publicados. En Argentina, se sugiere seguir el Perfil de Aplicación Nacional para Metadatos de Datos Abiertos.

### Licencia libre

Por último, es importante la adhesión de forma explícita a una licencia que permita la reutilización de los datos con cualquier tipo de fin, incluyendo económicos. Recomendamos usar la licencia Creative Commons Attribution 4.0, que permite compartir y redistribuir el material en cualquier medio o formato, así como adaptar, remezclar y construir a partir del material, en tanto se cumpla con la atribución correspondiente, citando las fuentes e indicando si se han realizado cambios. 

!!! note "No todos los datos públicos son o pueden ser abiertos"

    Los datos públicos son aquellos que los organismos del Estado generan y/o administran para el cumplimiento de sus misiones y funciones. El acceso a la información pública es un derecho reconocido en el país por la Ley 27275/16, que contempla diferentes principios para fomentar la publicidad de toda la información poseída y generada por el sector público.
    
    No todos los datos públicos pueden o deben publicarse (algunos están protegidos por legislación específica que lo prohíbe o regula) y un dato publicado no es abierto si no cumple con las condiciones de la sección anterior.
    
    Existen normativas que protegen determinados datos públicos en casos particulares. Estas situaciones que en el marco de las políticas de acceso se toman como excepciones, al implementar una iniciativa de datos abiertos debemos contemplarlas.
    
    Por esto, recomendamos tener en cuenta las siguientes normativas nacionales, sus normas complementarias y modificatorias, así como la normativa específica de tu provincia o gobierno local:

    * Ley de protección de datos personales 23.526/00
    * Ley del Sistema Estadístico 17.622/68
    * Ley de Procedimiento Fiscal 11.683
    * Ley de Propiedad Intelectual 11.723/33

## 2. ¿Qué se necesita para hacer apertura de datos?

Si decidís llevar adelante una política de apertura de datos, te recomendamos crear un plan de implementación con una justificación clara de cómo se realizará. Algunos gobiernos prefieren procesos de abajo hacia arriba, involucrando a distintos niveles jerárquicos de forma descentralizada, mientras otros prefieren procesos de arriba hacia abajo, con más control jerárquico.

Si bien no hay una forma correcta de hacerlo -cada organización tiene sus propias dinámicas, estructuras y necesidades- en esta sección te compartimos algunas consideraciones sobre cuatro puntos a tener en cuenta para llevarla adelante: el equipo de trabajo, el marco normativo,  la plataforma de implementación y buenas prácticas para la publicación.

### Equipo

Conformar un equipo de trabajo es clave para avanzar la línea de trabajo. Generalmente, estas iniciativas son llevadas a cabo por equipos reducidos y dinámicos, con la capacidad de ajustarse rápidamente a las necesidades del entorno. A continuación, identificamos los roles y perfiles a tener en cuenta para formar los equipos a nivel municipal o provincial. Dependiendo de los objetivos, recursos y posibilidades de tu organismo, algunos de los roles pueden concentrarse o dividirse en una o varias personas.

Cabe destacar que según el tamaño del gobierno local o provincial, es posible que la gestión política sea interna, pero se pueden tercerizar el resto de los roles. De hecho los denominados “equipos de soporte” son tercerizaciones internas que aún en los casos más grandes suelen ser recursos que no son parte del equipo de datos abiertos, sino que son puestos o roles que ya existen en otras áreas a los cuáles se les solicitan servicios cuándo es necesario.

#### Líder político

Es muy importante contar con el apoyo de una persona con liderazgo político que entienda e impulse la política de datos abiertos. Tener apoyo en los niveles más altos de la organización ayuda a legitimar y direccionar las acciones de una política de datos abiertos.

Quien tome este rol debe entender claramente el valor del proceso de apertura. Respaldarse en los índices internacionales, casos de estudio y políticas nacionales es un buen instrumento para validar ante los tomadores de decisiones las razones para participar de este tipo de iniciativas.

#### Coordinador

Es quien lidera a nivel operativo la política de datos abiertos. Entre sus funciones principales se encuentran:

* Alinear las prioridades de gestión de la administración con la política de datos abiertos.
* Identificar qué datos es prioritario abrir y establecer los procesos para su apertura, en conjunto con los responsables de los datos.
* Asegurar el cumplimiento de estándares.
* Oficiar de enlace con otras dependencias de gobierno, los usuarios de datos y la sociedad en general.
* Priorizar productos específicos de la entidad que promuevan el uso de datos abiertos.
* Rendir cuentas por el desarrollo de la política a nivel gubernamental.

Si bien este rol puede ser ejercido por distintos tipos de perfiles, es importante que quien lo ocupe entienda cómo funciona la apertura de datos, los estándares disponibles y los posibles casos de uso. No es sólo un rol gerencial, sino que requiere ciertas capacidades técnicas mínimas.

#### Perfil técnico

El responsable de este rol tiene a su cargo las definiciones que van a dar forma a la política de datos abiertos como:

* Trabajar con los responsables de las bases de datos originales para ordenar su apertura estableciendo protocolos técnicos para ese fin.
* Realizar o liderar procesos de limpieza de datos.
* Administrar el portal de datos abiertos de la dependencia, asegurándose que esté al día con las actualizaciones disponibles.
* Promover e implementar estándares en materia de datos.
* Desarrollar o supervisar el desarrollo de servicios para consulta de datos (tales como APIS)
* Oficiar de enlace con la comunidad técnica a nivel nacional así como con contrapartes a nivel local del sector privado, academia o sociedad civil.

Quien tome este rol requiere un fuerte componente técnico, debe contar con entendimiento de sistemas, estándares de datos, conocimientos de programación y gestión de la tecnología en el sector público.

#### Perfil analista

La función de este rol es hacer uso y explotación de los datos para facilitar y apoyar el uso de los datos abiertos por parte de la ciudadanía y dentro de su propia estructura. En particular:

* Promover el entendimiento y aprovechamiento de los datos tanto hacia adentro como hacia afuera de la organización.
* Liderar los procesos de análisis y visualización de datos, con un fuerte foco en la comunicación.
* Asistir en los procesos de limpieza de datos.
* Manejar con solvencia paquetes de análisis de datos.

Para poder cumplir con los objetivos, quien tome este rol necesita tener un correcto manejo de herramientas de visualización de datos y una visión comunicacional sobre los productos a desarrollar.

#### Equipos de soporte

Otro punto a tener en cuenta es la importancia de relacionar al equipo con las áreas de soporte tanto en temas legales como en cuestiones técnicas informáticas y de comunicación. El área de legales nos ayuda a determinar la política de datos y asegurar su consistencia con las políticas de protección de datos personales.

Las áreas de sistemas, por lo general, ayudan en los procesos de extracción y adecuación a estándares de los datos y a instalar, configurar y mantener la plataforma de publicación seleccionada. Las áreas de comunicación colaboran con la difusión de la iniciativa en las comunidades existentes.

### Cómo asociar los roles a los procesos de trabajo

La Iniciativa Latinoamericana por los Datos Abiertos (ILDA) desarrolló un lienzo modelo que puede ser útil en las primeras :

<table>
    <tr>
        <th>Etapa</th>
        <th>Acciones</th>
        <th>Objetivo</th>
        <th>Responsables</th>
    </tr>
    <tr>
        <td>0</td>
        <td>Concientización</td>
        <td>Comenzar el proceso</td>
        <td>Líder político</td>
    </tr>
    <tr>
        <td>1</td>
        <td>Sensibilización</td>
        <td>Sumar al liderazgo técnico y funcionariado al proyecto</td>
        <td>Líder político/ Coordinador</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Reclutamiento</td>
        <td>Conformar el equipo, con recursos propios o de terceros</td>
        <td>Líder político/ Coordinador</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Capacitación</td>
        <td>Compartir conceptos, visión y necesidades para llevar adelante la política</td>
        <td>Equipo de datos</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Relevamiento de activos</td>
        <td>Identificar los datos existentes, su estado y potencial de reutilización</td>
        <td>Coordinador, Analista y Áreas de gobierno</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Priorización de apertura</td>
        <td>Una vez identificados los datos, proyectar etapas de apertura según criterios técnicos y de reutilización</td>
        <td>Coordinador, Analista y Áreas de gobierno</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Desarrollo del portal</td>
        <td>Construir un espacio donde publicar los datos abiertos</td>
        <td>Técnico/ Equipos de Soporte</td>
    </tr>
    <tr>
        <td>7</td>
        <td>Preparación de los datos</td>
        <td>En paralelo con el desarrollo del portal, se deben preparar y documentar los conjuntos de datos a publicar</td>
        <td>Técnico/ Analista y Áreas de gobierno</td>
    </tr>
    <tr>
        <td>8</td>
        <td>Publicación del portal</td>
        <td>Lanzamiento comunicacional de la iniciativa</td>
        <td>Equipo de datos, Líder político y Áreas de Soporte</td>
    </tr>
    <tr>
        <td>9</td>
        <td>Fomento de la reutilización</td>
        <td>Convocatoria a actores intermediarios para trabajar con los datos publicados</td>
        <td>Técnico y Analista</td>
    </tr>
</table>

### El equipo según la escala de gobierno

Te compartimos tres ejemplos de iniciativas gubernamentales de datos abiertos con equipos de escala creciente.

<table>
    <tr>
        <th>Rol</th>
        <th>Ejemplo 1</th>
        <th>Ejemplo 2</th>
        <th>Ejemplo 3</th>
    </tr>
    <tr>
        <td style="vertical-align:middle">Político</td>
        <td rowspan="2" style="vertical-align:middle">Una sola persona cumple con la coordinación política y operativa de la iniciativa sin tener un equipo específico dedicado a la gestión.</td>
        <td>El liderazgo político se ejerce por fuera del equipo</td>
        <td>El rango del área encargada permite que el líder político esté dentro del equipo</td>
    </tr>
    <tr>
        <td style="vertical-align:middle">Coordinador</td>
        <td rowspan="3" style="vertical-align:middle">El coordinador cumple con el rol de gestionar las cuestiones operativas y poner en valor los datos publicados.</td>
        <td>El coordinador cumple con las gestiones operativas</td>
    </tr>
    <tr>
        <td style="vertical-align:middle">Analista</td>
        <td rowspan="4" style="vertical-align:middle">El resto de los roles se tercerizan y se les solicita a las áreas pre-existentes que aporten recursos para el cumplimiento de las tareas.</td>
        <td>Existe al menos un analista que trabaja en la depuración de los datos</td>
    </tr>
    <tr>
        <td style="vertical-align:middle">Técnico</td>
        <td>Al menos un técnico trabaja en la publicación y explotación de los datos</td>
    </tr>
    <tr>
        <td style="vertical-align:middle">Legal</td>
        <td rowspan="2" style="vertical-align:middle">El soporte técnico y legal se le solicita a las áreas pre-existentes.</td>
        <td>Se incorpora un recurso especialista en temas legales respecto de datos y acceso a la información</td>
    </tr>
    <tr>
        <td style="vertical-align:middle">Informática</td>
        <td>Al menos un técnico se dedica al mantenimiento del portal y a la creación de aplicaciones con los datos publicados</td>
    </tr>
</table>

### Marco normativo

Es importante que las políticas públicas estén respaldadas por una normativa, que varía en su rango, acorde a los objetivos y alcances.

El marco normativo nacional fija algunos conjuntos de datos que es obligatorio publicar para organismos de la Administración Pública Nacional:

* La Ley 27275 de "Derecho de Acceso a la Información Pública" en su Artículo 32
* El Decreto 117/2016 del "Plan de Apertura de Datos"

Además, insta a los organismos del Poder Ejecutivo Nacional a establecer y comunicar sus propios compromisos de apertura.

En la mayoría de los casos provinciales y locales en Argentina se pueden encontrar decretos y/u ordenanzas que regulan la apertura y/o adhesión al Plan Nacional. Te damos algunos ejemplos: La Provincia de Mendoza, declaró la adhesión al Plan de Apertura Nacional (Decreto 378/2017); mientras tanto, la Municipalidad de Córdoba -entre otras- estableció las provisiones para preparar el plan de apertura de sus dependencias (Decreto 1155/2017), tal como la Ciudad de Buenos Aires, que fue uno de los distritos pioneros en regular la apertura de datos(Decreto 156/2012), en 2012; la Ciudad de Bahía Blanca incluye la apertura de sus datos en un decreto sobre Modernización y Gobierno Abierto en 2015.

Es importante que conozcas las normativas de tu provincia y localidad -y su relación con las regulaciones nacionales- a la hora de elaborar el plan de implementación de tu política de apertura de datos. 

### Plataforma de publicación

Para facilitar el acceso y navegación a los activos de datos por parte de nuestros usuarios, es importante contar con una plataforma web que los agrupe y facilite su búsqueda y descarga. Independientemente de la plataforma que utilices, es importante garantizar y facilitar el proceso de documentación de los conjuntos de datos publicados, ya que los metadatos son una parte fundamental para contextualizar los datos abiertos.

Tené en cuenta que es fundamental integrar al usuario del portal en el proceso de diseño,  optimización y actualización del mismo. En recomendable que representen a los sectores reutilizadores y consultarles sobre su experiencia utilizando el portal, si les es fácil encontrar los conjuntos de datos que buscan, comprender si el lenguaje utilizado es adecuado para el público general.

#### ¿Qué plataforma adoptar?

Existen dos alternativas principales a la hora de tener en cuenta los recursos disponibles: instalar una plataforma de código abierto o contratar una plataforma como servicio pago.

Una plataforma de acceso libre y código abierto no implica costos de licenciamiento, pero requiere capacidad de desarrollo y gestión tecnológica para implementar y dar soporte a un portal propio. Los costos deberán medirse en función de los recursos asignados a la implementación de la plataforma.

Una plataforma, bajo el modelo de licencia o “software as a service”, puede resultar más costosa en términos financieros, pero simplificará buena parte de los procesos de gestión tecnológica y de mantenimiento del portal.

#### Andino

Portal Andino es la plataforma de código abierto desarrollada por el equipo de Datos Abiertos de la Administración Pública Nacional de Argentina. Tiene el fin de facilitar el proceso de apertura de datos en los diferentes organismos públicos que quieran encarar el desafío, o estén obligados por alguna norma específica. Es la tecnología detrás del Portal de Datos del Poder Ejecutivo, así como el de varios de sus Ministerios, Secretarías y otros organismos públicos de orden provincial y otros poderes.

Andino es una versión de CKAN, una plataforma de código abierto de OKFN que cuenta con una nutrida comunidad de práctica y ya fue implementado en numerosos gobiernos de distintos países del mundo.

### Buenas prácticas
 
Para lograr que un dato publicado sea realmente útil y fácil de usar por parte de terceros, existe un conjunto de buenas prácticas que te recomendamos seguir. No son una receta infalible, pero ayudan a considerar una implementación más ordenada de la política.

Proponete incluir datos que cumplan con los estándares locales y en lo posible nacionales e internacionales que ya existen para datos abiertos y no olvides la relevancia de los metadatos a la hora de documentar tus publicaciones de datos.

Considerá, para empezar, expresar con claridad los principios de la Carta Internacional de Datos Abiertos (Open Data Charter, 2015) en tu política. Los siguientes seis principios fueron elaborados para guiar los procesos de apertura de datos de los gobiernos adherentes.

* **Abiertos por Defecto**. En lugar de exigir una solicitud de acceso a la información para acceder a los datos públicos, la transparencia de los gobiernos debería ser activa, es decir, que los datos deberían abrirse y disponibilizarse siempre -mientras no afecten el derecho a la privacidad- y en el caso de no ser publicados deberían presentar las razones.  

* **Oportunos y Exhaustivos**. Los datos abiertos son valiosos sólo si son relevantes para los usuarios -ciudadanos, otros gobiernos y organizaciones de la sociedad civil y del sector privado-, a quienes se los debería consultar a la hora de priorizar los datasets a publicar. Es importante que los datos que se abren sean precisos y de alta calidad. En la medida de lo posible, en su forma original. 

* **Accesibles y Utilizables**. Los datos abiertos deberían estar puestos a disposición de manera visible y gratuita, en un portal central con licencia abierta y en múltiples formatos estandarizados, sin barreras burocráticas o administrativas que puedan disuadir a las personas de acceder a ellos. 


* **Comparables e Interoperables**. Para que los datos sean más eficaces y útiles deberían poder ser fáciles de comparar, interoperar y reutilizar con sus localizaciones geográficas y de tiempo.  Para eso, deberán usarse estándares relacionados con formatos, estructura e identificadores comunes, al momento de recolectar y publicar los datos, que sean legibles tanto para humanos como para máquinas. Para esto, podrán usarse las normas internacionales existentes y se deberá apoyar la creación de normas globales comunes donde aún no existan. 

* **Para mejorar la Gobernanza y la Participación Ciudadana**. La publicación de datos abiertos fortalece la confianza en las instituciones públicas y refuerza la obligación de los gobiernos de respetar el Estado de Derecho. Por eso, deberían implementarse capacitaciones para el uso eficaz de los datos en el diseño y desarrollo de políticas; incorporar procesos de control y rendición de cuentas para informar periódicamente a la ciudadanía sobre los avances y el impacto de las iniciativas; y brindar protección para respetar el derecho a la libertad de expresión a los utilizadores de datos. 


* **Para el Desarrollo Incluyente y la Innovación**. La apertura de datos puede ayudar a identificar desafíos y buscar nuevas soluciones posibles a retos sociales y económicos, locales y globales, tales como la pobreza, el hambre, el cambio climático y la desigualdad. Por eso, debe ser función de los gobiernos no sólo abrir los datos, sino también -mediante programas de capacitación, alianzas y otras iniciativas- apoyar activamente la reutilización innovadora de los datos, acercándoles a las comunidades claves las herramientas, los conocimientos y los recursos para entenderlos y usarlos de forma eficaz. 

!!! note "Nuestras guías de buenas prácticas"

    Te invitamos a leer las siguientes guías que publicamos con recomendaciones para una correcta política de apertura en la Administración Pública:

    * [Guía para la publicación de datos en formatos abiertos](https://datosgobar.github.io/paquete-apertura-datos/guia-abiertos/). Recomendaciones para publicar datos en formatos abiertos, estructurar bien una tabla, nombrar archivos y columnas, usar estándares básicos y trabajar con planillas de cálculo.
    * [Guía para la identificación y uso de entidades interoperables](https://datosgobar.github.io/paquete-apertura-datos/guia-interoperables/). Recomendaciones y referencias para nombrar entidades en activos de datos, usando sus nombres y códigos oficiales.
    * [Guía para el uso y la publicación de metadatos](https://datosgobar.github.io/paquete-apertura-datos/guia-metadatos/). Recomendaciones y estándares para documentar activos de datos.

## 3. ¿Qué datos publicar?

El marco normativo nacional y los índices internacionales recomiendan la publicación de ciertos datasets. En esta sección te compartimos un listado que puede funcionar como guía para comenzar y despertar ideas, pero las necesidades específicas de cada gobierno, provincial o local, guiarán las prioridades teniendo en cuenta cuál será el uso que se dará a los datos publicados.

A la hora de elaborar el inventario de tu provincia o localidad, te recomendamos identificar cuáles son o podrían ser más demandados. No te olvides de las fuentes de los datos, los organismos que generan y gestionan los datos son quienes mejor los conocen. Invítalos a ser parte de la comunidad y desarrollá planes de publicación junto con ellos.

### Listado de datasets recomendados

<table>
    <tr>
        <th>Área</th>
        <th>Conjunto de Datos</th>
        <th>Descripción</th>
    </tr>
    <tr>
        <td>Gobierno y Sector Público</td>
        <td><a href="https://datosgobar.github.io/paquete-apertura-datos/datasets-especificaciones/nomina-funcionarios/">Nómina de funcionarios públicos y sus salarios</a></td>
        <td>Listas de los funcionarios con referencia a la entidad a la que pertenecen, la categoría y el cargo, incluyendo pasantes y personal contratado en el marco de proyectos financiados por organismos multilaterales, detallando sus respectivas funciones y posición en el escalafón. En el caso de autoridades superiores se recomienda publicar los salarios.</td>
    </tr>
    <tr>
        <td>Gobierno y Sector Público</td>
        <td>Declaraciones juradas</td>
        <td>Declaración Jurada Patrimonial Integral de carácter público con su correspondiente relación a la Nómina de Funcionarios.</td>
    </tr>
    <tr>
        <td>Gobierno y Sector Público</td>
        <td><a href="https://datosgobar.github.io/paquete-apertura-datos/datasets-especificaciones/organigrama/">Organigrama</a></td>
        <td>Organismos y entidades del estado con su estructura orgánica y funciones.</td>
    </tr>
    <tr>
        <td>Economía y Finanzas</td>
        <td><a href="https://datosgobar.github.io/paquete-apertura-datos/datasets-especificaciones/presupuesto/">Presupuesto</a></td>
        <td>El presupuesto asignado a cada área, programa o función, las modificaciones durante cada ejercicio anual y el estado de ejecución actualizado en forma trimestral hasta el último nivel de desagregación en que se procese.</td>
    </tr>
<!--     <tr>
        <td>Economía y Finanzas</td>
        <td>Presupuesto de egresos</td>
        <td>Presupuesto del gobierno municipal a un nivel alto, el gasto gubernamental previsto para el próximo año: Presupuesto por oficina de gobierno Presupuesto por sub-secretaría Descripciones de la secciones del presupuesto.</td>
    </tr>
 -->    <tr>
        <td>Gobierno y Sector Público</td>
        <td><a href="https://datosgobar.github.io/paquete-apertura-datos/datasets-especificaciones/registro-proveedores/">Registro de proveedores</a></td>
        <td>Nombre de proveedores adjudicados en contrataciones públicas, así como los socios y accionistas principales, de las sociedades o empresas proveedoras.</td>
    </tr>
    <tr>
        <td>Gobierno y Sector Público</td>
        <td><a href="https://datosgobar.github.io/paquete-apertura-datos/datasets-especificaciones/contrataciones-publicas/">Contrataciones públicas</a></td>
        <td>Listado de todos los procesos de contratación, los procesos de contratación de obras deberían tener un enlace a sus obras, con el fin de poder agrupar todos los contratos de una obra dada (diseño, construcción, fiscalización).</td>
    </tr>
    <tr>
        <td>Gobierno y Sector Público</td>
        <td>Pagos de las contrataciones públicas</td>
        <td>Registros del gasto real (pasado) del gobierno municipal en un nivel transaccional detallado, incluyendo el objeto de gasto, monto y oficina gubernamental que realizó el gasto. Además sus beneficiarios.</td>
    </tr>
    <tr>
        <td>Gobierno y Sector Público</td>
        <td><a href="https://datosgobar.github.io/paquete-apertura-datos/datasets-especificaciones/servicios/">Servicios</a></td>
        <td>Los servicios que brinda el organismo directamente al público, incluyendo normas, cartas y protocolos de atención al cliente.</td>
    </tr>
    <tr>
        <td>Gobierno y Sector Público</td>
        <td><a href="https://datosgobar.github.io/paquete-apertura-datos/datasets-especificaciones/tramites/">Trámites</a></td>
        <td>Un índice de trámites y procedimientos que se realicen ante el organismo, así como los requisitos y criterios de asignación para acceder a las prestaciones.</td>
    </tr>
    <tr>
        <td>Gobierno y Sector Público</td>
        <td><a href="https://datosgobar.github.io/paquete-apertura-datos/datasets-especificaciones/denuncias/">Denuncias</a></td>
        <td>Mecanismos de presentación directa de solicitudes o denuncias a disposición del público en relación a acciones u omisiones del sujeto obligado.</td>
    </tr>
    <tr>
        <td>Gobierno y Sector Público</td>
        <td><a href="https://datosgobar.github.io/paquete-apertura-datos/datasets-especificaciones/permisos/">Permisos</a></td>
        <td>Los permisos, concesiones y autorizaciones otorgados y sus titulares.</td>
    </tr>
    <tr>
        <td>Regiones y Ciudades</td>
        <td>Límites administrativos</td>
        <td>Datos sobre unidades administrativas o áreas definidas para el propósito de administración por el gobierno (local). Nivel de frontera 1 Nivel de frontera 2 Cordenadas (latitud y longitud) Nombre del polígono (barrio, ciudad) Bordes de los polígonos.</td>
    </tr>
    <tr>
        <td>Transporte</td>
        <td>Transporte Público</td>
        <td>Horarios del transporte público y los recorridos de cada línea de transporte.</td>
    </tr>
    <tr>
        <td>Regiones y Ciudades</td>
        <td>Mapa</td>
        <td>Mapa completo de la ciudad con información actualizada, listados sobre centros de salud, establecimientos educativos, centros de atención ciudadana y los espacios públicos de la ciudad.</td>
    </tr>
    <tr>
        <td>Regiones y Ciudades</td>
        <td>Catastro y dueños</td>
        <td>Catastro de las tierras e información sobre los dueños de las mismas.</td>
    </tr>
    <tr>
        <td>Justicia, Seguridad y Legales</td>
        <td><a href="https://datosgobar.github.io/paquete-apertura-datos/datasets-especificaciones/normativa/">Leyes, decretos, resoluciones, ordenanzas, acordadas</a></td>
        <td>Todas las leyes y los estatutos municipales sancionados por el Honorable Concejo Deliberante.</td>
    </tr>
    <tr>
        <td>Gobierno y Sector Público</td>
        <td><a href="https://datosgobar.github.io/paquete-apertura-datos/datasets-especificaciones/elecciones/">Resultados de las elecciones</a></td>
        <td>Resultados de las últimas elecciones locales desagregadas por mesas electorales.</td>
    </tr>
    <tr>
        <td>Medio ambiente</td>
        <td><a href="https://datosgobar.github.io/paquete-apertura-datos/datasets-especificaciones/calidad-aire/">Calidad de aire</a></td>
        <td>Concentración de contaminantes perjudiciales para la salud humana en agua y aire. Estaciones de monitoreo de aire y monitoreo de fuentes de agua.</td>
    </tr>
    <tr>
        <td>Medio ambiente</td>
        <td><a href="https://datosgobar.github.io/paquete-apertura-datos/datasets-especificaciones/calidad-agua/">Calidad de agua</a></td>
        <td>Concentración de contaminantes perjudiciales para la salud humana en agua y aire. Estaciones de monitoreo de aire y monitoreo de fuentes de agua.</td>
    </tr>
    <tr>
        <td>Justicia, Seguridad y Legales</td>
        <td><a href="https://datosgobar.github.io/paquete-apertura-datos/datasets-especificaciones/crimen/">Crimen</a></td>
        <td>Estadísticas sobre niveles de crimen o listado de los mismos.</td>
    </tr>
    <tr>
        <td>Educación</td>
        <td>Educación</td>
        <td>Estadísticas de educación, cantidad de alumnos por aula (grado e institución), por sexo, por edad. Si se tiene estadísticas de calidad educativa, incluir.</td>
    </tr>
    <tr>
        <td>Salud</td>
        <td><a href="https://datosgobar.github.io/paquete-apertura-datos/datasets-especificaciones/salud/">Salud</a></td>
        <td>Disponibilidad de medicina, cantidad de pacientes atendidos por servicios de salud, etc.</td>
    </tr>
</table>

## 4. Acercate a tu comunidad

Los datos abiertos son una materia prima con la cual se pueden producir diferentes productos, servicios, investigaciones, aplicaciones y visualizaciones. Por eso, uno de los aspectos cruciales que determinan el éxito y la sostenibilidad de una política de datos abiertos es el desarrollo de una comunidad de actores que los reutilicen. Para que esto suceda es necesario encontrar las formas de comunicar la iniciativa, promover espacios de colaboración y generar distintas instancias en las que las personas que poseen estos conocimientos se acerquen a los datos.

En esta sección, te contamos cuáles pueden ser las comunidades claves a las que deberías comunicarles la política de apertura  y de qué maneras pueden reutilizar los datos que abrís. Al final, te compartimos un enfoque participativo que además de difundir la iniciativa, abre espacios colaborativos de trabajo.

### Actores claves

La sociedad en su conjunto puede encontrar inspiración en el portal de datos para agregarle valor a la comunidad en la que vive, pero existen conjuntos de actores que por su rol o sus habilidades serán el público objetivo de nuestras convocatorias, ya que son los que acercan el valor agregado de los datos públicos al resto.

Incluir y hacer participar a estos segmentos en el proceso de lanzamiento de la iniciativa es fundamental. Identificamos cinco categorías que nos permiten reconocerlos y desarrollar estrategias de acercamiento con cada una de ellos.

#### Los funcionarios y empleados públicos

El conjunto de funcionarios y empleados de nuestro propio Gobierno son parte de la comunidad de usuarios y consumidores de los datos abiertos. Probablemente sea el segmento más importante dado que tener un portal que concentre diferentes activos de datos facilita su labor diaria y a la vez les permite seguir agregando valor en la gestión pública.

Un ejemplo de este tipo de interacción es el “Mapa de Oportunidades Comerciales” (MOC), una iniciativa del Gobierno de la Ciudad de Buenos Aires. El sitio cuenta con información detallada por zona y rubro para ayudar a los usuarios a elegir la ubicación de un futuro emprendimiento comercial en la Ciudad.

El MOC brinda información detallada del panorama comercial a empresas y emprendedores para hacer más eficiente la toma de decisiones a la hora de abrir o potenciar los locales. Algunos de los datos con los que cuenta la plataforma son:

* Apertura y cierre de locales
* Nivel de riesgo
* Indicadores poblacionales
* Indicadores inmobiliarios

#### Sociedad civil organizada

El conjunto de actores de la sociedad civil es un catalizador de las demandas sociales. Los diferentes tipos de organizaciones sociales, como las organizaciones sin fines de lucro, clubes, colegios profesionales y gremios, cada uno cuenta con sus agendas de incidencia que le permiten a la iniciativa de datos publicar aquellos que sean pertinentes y sirvan para encarar las diferentes problemáticas reconocidas a nivel local.

Uno de los ejemplos que pueden mencionarse es ¿A qué precio? Esta plataforma, desarrollada por  Chequeado recopila información sobre compras de medicamentos de VIH, oncológicos, vacunas antigripales y anticonceptivos realizadas por el Gobierno Nacional y el Gobierno de la Ciudad de Buenos Aires durante 2016 y 2017. Este sitio se compone por datos de los sitios de compras pública oficiales de la página del Ministerio de Salud de la Nación y del Boletín Oficial. Además, se presentaron pedidos de acceso a la información pública que permitieron obtener otros datos que luego fueron organizados en una base para facilitar su comparación.

#### Periodismo y desarrolladores de contenido

Los medios suelen ser un aliado clave en el éxito de las iniciativas de datos abiertos, ya que se convierten en reutilizadores de forma inmediata. Al estar compuestos por equipos multidisciplinarios, tienen naturalmente las herramientas y capacidades necesarias para realizar investigaciones, visualizaciones e innovar en formas de poner en valor los datos públicos.

El equipo de LA NACIÓN Data explora diariamente bases de datos gubernamentales y gran volumen de documentos públicos. Esta tarea permite detectar no sólo nuevas fuentes de información, sino también datos que se convierten en importantes insumos de historias nunca antes contadas.

Con la disponibilidad de los datos producen iniciativas como el simulador de créditos hipotecario  o publicaciones como  “Las verdades de la población carcelaria” para derribar mitos que abonaban la xenofobia.

#### Emprendedores tecnológicos

Las comunidades de programadores y emprendedores tecnológicos juegan un rol fundamental dado que cuentan con los conocimientos técnicos que les facilitan el trabajo con datos en niveles avanzados. Para llegar a estos conjuntos, podemos hacerlo a través de las cámaras TIC, comunidades de programación y ámbitos de promoción de emprendedores.

Puntualmente para los emprendedores, la disponibilidad de datos oficiales siempre es una oportunidad para desarrollar nuevas líneas de negocios, funcionalidades innovadoras y productos o servicios derivados. Tal es el caso de la plataforma Credirati, que toma los datos que sobre las líneas de crédito que publica todos los días el Banco Central de la República Argentina (BCRA). En el portal Credirati, los ciudadanos y ciudadanas pueden comparar y elegir el crédito hipotecario más adecuado a sus necesidades solamente indicando el monto del inmueble y la ubicación de lo que se busca.

#### Academia y comunidad educativa

Los datos son un recurso educativo importante en todos los niveles de formación. No sólo se pueden convertir en objeto de estudio y material fundamental para el desarrollo de investigaciones aplicadas, sino que además se pueden incorporar al planteamiento de problemas y trabajos prácticos. Insertar la temática y difundir la iniciativa en el sector académico es una prioridad ya que pone en valor datos reales para solucionar problemáticas existentes del municipio o la provincia.

Ejemplo del uso de los datos para desarrollar investigaciones académicas es la tesis de maestría Yo, reutilizador de datos de Federico Baylé. Para su tesis, Baylé desarrolló un mapa de detección automática que permitía conocer la evolución de los asentamientos en La Matanza. Esta investigación inicial luego dio paso a la creación de DymaxionLab, un emprendimiento tecnológico que desarrolló una plataforma de monitoreo de barrios de emergencia y asentamientos con un monitor de inundaciones, que permite observar y supervisar el avance de inundaciones en tiempo casi real y una aplicación para verificar modificaciones en el uso del suelo. Para esto, utiliza imágenes satelitales y datos abiertos generados por distintos actores. Entre ellos, los datos geoespaciales de la NASA y la Agencia Espacial Europea y datos de los portales del Ministerio de Energía, de las provincias de Buenos Aires, Córdoba y de la Ciudad de Buenos Aires, entre otros.

### Espacios de colaboración

Identificar e interactuar uno a uno con cada sector es indispensable pero no suficiente. Crear una comunidad entre todos los actores que agregan valor a los datos abiertos permite que surjan nuevos y/o mejores productos y servicios. El contacto de los diferentes conjuntos con Gobierno nos permite atravesar procesos de creación de políticas públicas mucho más enriquecedoras, porque da lugar a crear soluciones con los usuarios finales de las mismas.

Hay distintas maneras de generar estas interacciones, dependiendo de los objetivos que queramos cumplir. En el kit de Herramientas para la participación ciudadana vas a encontrar criterios para organizar seis dispositivos de innovación abierta: las charlas inspiracionales, los talleres creativos, las mesas de trabajo, las desconferencias, los hackatones y los concursos de innovación abierta. Todos permiten mapear o construir comunidades, inspirar la gestión con nuevas perspectivas y acercarse a la ciudadanía fomentando una participación que agregue valor al ciclo de vida de la política. Parte del sentido de abrir la iniciativa es conectar perfiles, generaciones y experiencias que no se cruzan con frecuencia.

* **Charla inspiracional**. Una sesión en la que un orador especializado expone una idea en un breve período de tiempo buscando despertar la curiosidad de los asistentes, con herramientas o casos diferentes de los que se suelen tratar a diario.

* **Taller creativo**. Un encuentro presencial en el que diversos perfiles trabajan en conjunto con el objetivo de crear propuestas innovadoras que respondan a desafíos públicos previamente planteados.

* **Mesa de trabajo**. Un canal presencial de diálogo entre la sociedad civil y el gobierno. Apuntan a intercambiar y contrastar experiencias para establecer declaraciones co-creadas sobre un tema en particular.

* **Desconferencia**. Una jornada para la circulación de información y generación de redes intensivo donde, a diferencia de la conferencia tradicional, la agenda se organiza al principio del encuentro a partir de las propuestas que hacen los mismos asistentes.

* **Hackatones**. Un evento -de entre 24 y 72 hs- que convoca a personas que quieran trabajar en equipos con el objetivo de buscar soluciones a una problemática en particular. El espíritu de la palabra “hack” consiste en desarmar, investigar y romper con lo tradicional, para diseñar nuevos productos, servicios o experiencias que mejoren la calidad de vida de la ciudadanía.

* **Concurso de innovación abierta**. Es una convocatoria que invita a la ciudadanía a sumar ideas para resolver desafíos públicos. Este dispositivo es el más completo y extenso en términos de tiempo. Está compuesto por diferentes fases entre las que se contemplan mentorías, presentaciones y asesoramiento de expertos, con el fin de que los participantes puedan definir una estrategia que les permita iterar y mejorar sus propuestas.

Estos espacios de colaboración representan una oportunidad para abrir canales de diálogo, construir formas genuinas de sinergia  y viabilizar la acción colectiva. Es una forma de pensar una democracia más abierta, que no sólo genera soluciones para las personas, sino también con las personas.

## 5. Instrumentos para evaluar la política de apertura


Existen distintas formas de que la planificación, el monitoreo y la evaluación de una política formen parte de la gestión diaria de la organización, a fin de que los equipos puedan entender en qué medida se están alcanzando los objetivos previstos, retroalimentar el proceso de diseño e implementación y maximizar los resultados que se buscan alcanzar.

En esta sección, te compartimos las referencias de algunos índices e indicadores que te recomendamos tener en cuenta desde el inicio de la política. La evidencia que que recolectes puede ser útil para detectar nuevos problemas, tomar decisiones sobre bases más sólidas, mejorar el impacto de la iniciativa y elaborar una comunicación efectiva de la política.

### Índices

Existen distintas formas de medir una política de apertura, tales como el Barómetro de Datos Abiertos, el  Índice de Datos Abiertos Global, su edición local, el Índice de Datos Abiertos de Ciudades de Argentina o el Índice OURdata de la Organización para la Cooperación y el Desarrollo Económicos​ (OCDE).

#### El Barómetro de Datos Abiertos

Desarrollado por la World Wide Web Foundation como un trabajo colaborativo de la red Open Data for Development (OD4D),  tiene como objetivo mostrar el impacto de las iniciativas de datos abiertos en todo el mundo, a través del análisis de datos contextuales, evaluaciones técnicas e indicadores secundarios para analizar las tendencias mundiales y comparar países.

#### El Índice de Datos Abiertos Global

Administrado por Open Knowledge Network, tiene como fin medir el estado de los datos abiertos en el mundo por medio de una encuesta que evalúa la apertura de los conjuntos de datos específicos. Su versión local es el Índice de Datos Abiertos de Ciudades de Argentina. 


#### El Índice de Datos Abiertos de Ciudades de Argentina

A cargo de la Fundación Conocimiento Abierto, evalúa las iniciativas de apertura de datos de acuerdo a once categorías de datos: presupuestos, gasto público, compras y contrataciones, obras públicas, funcionarios, límites administrativos, lugares públicos, transporte, medio ambiente, ordenanzas y resultados electorales.  Dentro de cada una de estas categorías se considera, al igual que en la edición global, si son recopilados por el gobierno; la facilidad para acceder a ellos, que estén online y de manera gratuita; el uso de licencias abiertas que permitan su reutilización libre; si están en formatos abiertos; y si es fácil su utilización o requieren esfuerzo extra. De acuerdo a los resultados, se les adjudica un puntaje para determinar el grado de apertura de sus datos; a mayor puntaje, mejor. 

 
#### El Índice OURdata de la OCDE

Evalúa los esfuerzos gubernamentales de los países miembros para implementar datos abiertos en términos de apertura, utilidad y reutilización de los datos del gobierno. 

!!! note ""
    Estas evaluaciones globales permiten establecer comparaciones entre diferentes jurisdicciones y proporcionan a los promotores de la apertura, dentro y fuera de los gobiernos, información para apoyar su trabajo o para abogar por mejoras y / o cambios. 

### Indicadores

Existen otra serie de indicadores que pueden ser de ayuda. Si bien cada uno de ellos señala algún aspecto relevante sobre la política de apertura, tené en cuenta que medir el impacto efectivo no es sencillo y no conviene evaluar la política siguiendo sólo una de estas métricas en particular.

**Nuevos pedidos de datos**. Indican que hay una demanda activa que está usando datos abiertos en el desarrollo de sus actividades y encuentra nuevas oportunidades de uso.

**Cantidad de participantes en eventos vinculados a uso de datos**. Es una aproximación al tamaño de la comunidad que re-utiliza datos abiertos.

**Analíticas del sitio**. En general los portales de datos son propiedades digitales de bajo tránsito, pero siempre es bueno conocer la evolución de los usuarios, la cantidad que vuelven, las descargas que realizan.

**Cantidad de consultas a una API**.  Del mismo modo que con el portal es importante conocer el uso de nuestros servicios de datos, para conocer su crecimiento en el tiempo.

**Actualización del portal y sus datos**. La reutilización de los datos dependerá de la calidad de los mismos por lo que es importante asegurarnos que se mantienen actualizados.

**Conjuntos de datos incorporados al portal mensualmente**. La publicación de nuevos conjuntos de datos sobre nuevas temáticas nos permite ampliar los usuarios de los mismos.

**Proyectos basados en datos abiertos**. Este es un indicador cualitativo que muestra ejemplos de aplicaciones de los datos abiertos para fines específicos.

## Reflexiones finales

**¡Qué bueno verte por acá!**

Sí. Nos alegramos. Porque si llegaste hasta el final, es probable que las herramientas para abrir datos públicos te hayan resultado de interés. La serie de conceptos y herramientas que te presentamos no son otra cosa que un conjunto de prácticas que creemos que deben ser compartidas entre las personas que trabajan día a día en organismos provinciales y locales. Así que si logramos transmitirte esta devoción por acercar el gobierno a la ciudadanía y mejorar la gestión de forma continua, ¡ayudanos a que estas iniciativas se multipliquen acercándole esta guía a alguien más!

Como te contamos al principio, este ejemplar forma parte de una amplia serie de publicaciones, entre las que sistematizamos metodologías y enfoques que consideramos valiosos. Si te interesa profundizar tus conocimientos sobre esta temática, te recomendamos leer otras publicaciones en las que compartimos y explicamos herramientas útiles para llevar estas ideas a la realidad:

* **Introducción a la apertura de datos**. Conocé un marco introductorio en el que desarrollamos conceptos y herramientas vinculadas a los datos abiertos, sus características y beneficios. Te compartimos el camino ideal para empezar a abrir los datos en un organismo.

* **Herramientas para la transparencia y rendición de cuentas**. Claves para un Gobierno abierto. Conocé qué es Gobierno Abierto y aprendé los aspectos fundamentales de sus pilares. Te contamos algunos conceptos fundamentales vinculados a la la capacidad de solicitar y acceder a información por parte de la ciudadanía. Además, aprendé en qué consiste y cómo puede tu organismo llevar adelante una rendición de cuentas que le permita dar a conocer los resultados y manejos de fondos, acciones y decisiones.

* **Herramientas para una gestión ágil. Teoría de cambio y pensamiento evaluativo**. Aprendé técnicas para monitorear y evaluar políticas, generar evidencia, reflexionar sobre lo que se hizo, se hace y se va a hacer para poder aprender de los errores y potenciar los aciertos.

* **Guía para la apertura de datos en la Administración Pública Nacional**. Te compartimos los recursos necesarios para publicar datos en los organismos de la APN. Aprendé cómo mejorar la calidad, identificar activos de datos y publicarlos como un servicio.

Esperamos que esta guía te haya inspirado nuevas ideas y conectado con formas alternativas de gestionar. Esperamos -porque anhelamos ser cada vez más los que buscamos mejorar la forma en que hacemos las cosas- que esta lectura se convierta en un primer paso al que le sucedan las manos a la obra.

## Anexo: material para talleristas

* [Marco de trabajo para talleristas](./guia-subnacionales/taller.md)
* [Descargá la presentación base para el taller de sensibilización](https://docs.google.com/presentation/d/1cmuh7750Ruhl0DFhA3EJKI-A-7LTG2wOm-3ZsVMtyA8/export/pptx?id=1cmuh7750Ruhl0DFhA3EJKI-A-7LTG2wOm-3ZsVMtyA8&pageid=g569e770ac0_0_161)
* [Presentación base para taller de co-creación](https://docs.google.com/presentation/d/1jFnqXhGl-B-BTWPIgdOHoNKbhL9221NdILDJP58ijaA/export/pptx?id=1jFnqXhGl-B-BTWPIgdOHoNKbhL9221NdILDJP58ijaA&pageid=g513ab9e99d_1_0)
