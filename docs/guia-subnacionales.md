# Guía para la apertura de datos en gobiernos provinciales y locales

Si formás parte del equipo de trabajo de una provincia o municipio, esta guía te da los conceptos clave y las bases para que puedas diseñar e implementar políticas de datos abiertos. 

Desde la aprobación del [Plan de Apertura de Datos del decreto 117/2016](http://servicios.infoleg.gob.ar/infolegInternet/anexos/255000-259999/257755/norma.htm) y la [Ley de Acceso a la Información Pública 27275](http://servicios.infoleg.gob.ar/infolegInternet/anexos/265000-269999/265949/norma.htm), cada vez más organismos públicos y distintos niveles de la Administracion Pública empezaron a publicar sus datos, para mostrar transparencia en la gestión y que los  ciudadanos puedan tener acceso a información clara que puedan reutilizar.  

!!! note "Iniciativas de apertura de datos en Argentina"

    <!-- Listado con las diferentes iniciativas de apertura de datos de gobiernos sub-nacionales existentes en Argentina. -->

    Listado con los [catálogos de datos abiertos de organismos de la Administración Pública Nacional](http://datos.gob.ar/dataset/modernizacion-red-datos-abiertos-administracion-publica-nacional).

<!-- Esta guía toma como ejemplo casos locales donde las políticas de apertura se implementaron con éxito, como las Municipalidades de Córdoba y Mercedes, el Gobierno de la Ciudad de Buenos Aires y la Provincia de Mendoza.  -->

Cada unidad hace referencia a diferentes puntos a tener en cuenta al momento de implementarla: 

* Por qué publicar datos abiertos
* Cómo conformar un equipo
* Cómo identificar datos prioritarios y cómo abrirlos
* Cómo realizar una publicación de datos basada en buenas prácticas
* Cómo encontrar y conectar a la comunidad que usa datos abiertos

## ¿Por qué publicar datos abiertos?
 
Incorporar la publicación de datos abiertos como parte del flujo de trabajo genera diferentes resultados.
 
Por un lado, para quienes publicamos, hace que tomemos conciencia del estado de situación del activo de datos. A la vez, el esfuerzo por mejorar la calidad de los datos facilita el consumo y genera nuevos usos internos o menos costosos.
 
Por otro, para los diferentes sectores que articulan con el gobierno, les da la posibilidad de producir nuevo valor agregado sobre los datos generados y combinarlos con otras fuentes, ya sean propias o de terceros.
 
!!! note  "El Podcast de ILDA"
 
    La Iniciativa Latinoamericana por los Datos Abiertos (ILDA) cuenta con un podcast, donde conversan con actores que tuvieron roles clave en los procesos de apertura de datos de sus ciudades y gobiernos provinciales.
        
    * [Episodio II - De los bits a los átomos: Entrevista a Javier Arteaga (Nariño, Colombia) y Mariana Romiti (Santa Fé, Argentina)](https://idatosabiertos.org/episodio-2-de-los-bits-a-los-atomos/)
    * [Episodio III - Los datos cerca del vecino: Entrevista a Andrés Vázquez (Municipalidad de Córdoba)](https://idatosabiertos.org/episodio-3-los-datos-cerca-del-vecino/)
 
### ¿Qué son los datos abiertos?
 
Los datos abiertos son los que están **publicados en formatos reutilizables**, siguiendo **estándares y buenas prácticas** y que usan explícitamente una **licencia libre que permite su reutilización** por parte de terceros.
 
Los formatos reutilizables son los que permiten procesar la información que contienen. Por ejemplo, un archivo de texto separado por comas (CSV) que contiene una lista de los semáforos del municipio y sus coordenadas.
 
Por el contrario, existen otros formatos que dificultan procesar la información por la manera en que la presentan. Las imágenes escaneadas y los archivos PDF son el ejemplo más claro, ya que pueden contener texto o tablas pero no permiten trabajarlo como tal.
 
Al momento de publicar los datos, es preferible hacerlo en formatos abiertos como JSON o CSV en lugar de formatos propietarios como DTA o SAV, que requieren una licencia paga para su uso. Aunque también hay formatos propietarios con mucha difusión y aceptación como XLSX. En estos casos recomendamos publicar los datos **también en un formato abierto** por ejemplo, en XLSX y CSV.
 
Es importante la adhesión de forma explícita a una licencia que permita la reutilización de los datos con cualquier tipo de fin, incluyendo económicos. Recomendamos usar la licencia [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/deed.es).
 
### No todos los datos públicos son abiertos
 
Los datos públicos son aquellos que los organismos del Estado generan y/o administran para el cumplimiento de sus misiones y funciones. El acceso a la información pública es un derecho reconocido en el país por la Ley 27275/16, que contempla diferentes principios para fomentar la publicidad de toda la información poseída y generada por el sector público.
 
No todos los datos públicos pueden o deben publicarse (algunos están protegidos por legislación específica que lo prohíbe o regula) y un dato publicado no es abierto si no cumple con las condiciones de la sección anterior.
Existen normativas que protegen determinados datos públicos en casos particulares. Estas situaciones que en el marco de las políticas de acceso se toman como excepciones, al implementar una iniciativa de datos abiertos debemos contemplarlas, sobre todo cuando se tratan de datos que refieren a las personas.
 
Por esto recomendamos revisar, entre otras, las siguientes normativas nacionales y sus homólogas a nivel provincial:
 
* [Ley de protección de datos personales 23526/00](http://servicios.infoleg.gob.ar/infolegInternet/anexos/60000-64999/64790/norma.htm)
 
* [Ley del Sistema Estadístico 17622/68](http://servicios.infoleg.gob.ar/infolegInternet/anexos/20000-24999/24962/texact.htm)
 
* [Ley de Propiedad Intelectual 11723/33](http://servicios.infoleg.gob.ar/infolegInternet/anexos/40000-44999/42755/texact.htm)
 
## ¿Cómo publicar datos abiertos?
 
Si bien no hay una forma correcta de implementar una política de apertura de datos, dado que cada organización tiene sus propias dinámicas, estructuras y necesidades, te damos algunos puntos a tener en cuenta para llevarla adelante.
 
### Equipo
 
Conformar un equipo de trabajo es clave para avanzar esta línea de trabajo. Generalmente, estas iniciativas son llevadas a cabo por equipos reducidos y dinámicos, con la capacidad de ajustarse rápidamente a las necesidades del entorno. En esta unidad identificamos los roles y perfiles a tener en cuenta para formar los equipos a nivel municipal o provincial. Dependiendo de los objetivos, recursos y posibilidades de tu organismo, algunos de los roles puede que se concentren o dividan en una o varias personas.

#### Líder político
 
Es muy importante contar con el apoyo de una persona con liderazgo político que entienda e impulse la política de datos abiertos. Tener apoyo en los niveles más altos de la organización ayuda a legitimar y direccionar las acciones de una política de datos abiertos.
 
Quien tome este rol debe entender claramente el valor del proceso de apertura. Respaldarse en los índices internacionales, casos de estudio y [políticas nacionales](https://www.argentina.gob.ar/compromisoparalamodernizacion)  es un buen instrumento para validar ante los tomadores de decisiones las razones para participar de este tipo de iniciativas.
 
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
 
#### Equipos de Soporte
 
Otro punto a tener en cuenta es la importancia de relacionar al equipo con las áreas de soporte tanto en temas legales como en cuestiones técnicas informáticas. El área de legales nos ayuda a determinar la política de datos y asegurar su consistencia con las políticas de protección de datos personales. Las áreas de sistemas, por lo general, ayudan en los procesos de extracción y adecuación a estándares de los datos y a  instalar, configurar y mantener la plataforma de publicación seleccionada.


<!-- !!! note "Diferentes formatos en gobierno"
    
    Agregar en esta sección dos casos de equipos (uno de ciudad grande con la mayoría de los componentes y otro de un municipio que funcione con equipo base)

 -->
### Marco normativo

Es importante que las políticas públicas estén respaldadas por una normativa, que varía en su rango, acorde a los objetivos y alcances.

Los decretos, ya sean municipales o provinciales, tienen la limitante de que su alcance está supeditado al ámbito del poder ejecutivo. Una ley u ordenanza permitiría tener un alcance mayor, pero depende de procesos legislativos que muchas veces cuentan con proyecciones temporales mayores y resultados que no siempre están en línea con las expectativas de la gestión.

<!-- !!! note "Casos provinciales y municipales"
    Se pueden agregar ejemplos de algunas normativas que se hayan implementado. 

 -->

### Plataforma de publicación

Para facilitar el acceso y navegación a los activos de datos por parte de nuestros usuarios, es importante contar con una plataforma web que los concentre. Independientemente de la plataforma que utilicemos, tiene que garantizar y facilitar el proceso de documentación de los conjuntos de datos ya que los metadatos son una parte fundamental de las políticas de apertura.

#### ¿Qué plataforma adoptar?

Existen dos alternativas principales a la hora de tener en cuenta los recursos disponibles: instalar una plataforma de código abierto o contratar una plataforma como servicio pago.
 
Una plataforma de acceso libre y código abierto no implica costos de licenciamiento pero requiere capacidad de desarrollo y gestión tecnológica para implementar y dar soporte a un portal propio. Los costos deberán medirse en función de los recursos asignados a la implementación de la plataforma.

Una plataforma, bajo el modelo de licencia o “software as a service”, puede resultar más costosa en términos financieros, pero simplificará buena parte de los procesos de gestión tecnológica y de mantenimiento del portal.

#### Andino

Portal Andino es la plataforma de código abierto desarrollada por el equipo de Datos Abiertos de la Administración Pública Nacional de Argentina. Tiene el fin de facilitar el proceso de apertura de datos en los diferentes organismos públicos que quieran encarar el desafío, o estén obligados por alguna norma específica. Es la tecnología detrás del Portal de Datos del Poder Ejecutivo, así como el de varios de sus Ministerios, Secretarías y otros organismos públicos de orden provincial y otros poderes.

Andino es una versión de CKAN, una plataforma de código abierto de OKFN que cuenta con una nutrida comunidad de práctica y ya fue implementado en numerosos gobiernos en un gran número de países. 

<!-- !!! note "Portales ejemplares"
    Agregar links de portales subnacionales que puedan ser utilizados como ejemplos de buenas prácticas y con diferentes tecnologías. Indicar cúal utiliza cada uno. Que al menos 2 sean con Andino.  -->

### Buenas prácticas

Para lograr que un dato publicado sea realmente útil y fácil de usar por parte de terceros, existe un conjunto de buenas prácticas que conviene seguir.

!!! note  "Principios del Open Data Charter"

    La Carta Internacional por los Datos Abiertos presenta un conjunto de principios que deberían guiar los procesos de apertura de datos de los gobiernos que adhieren a la misma:

    * Abiertos por Defecto
    * Oportunos y Exhaustivos
    * Accesibles y Utilizables
    * Comparables e Interoperables
    * Para mejorar la Gobernanza y la Participación Ciudadana
    * Para el Desarrollo Incluyente y la Innovación


Te invitamos a leer las siguientes guías de buenas prácticas que publicamos con recomendaciones para una correcta política de apertura en la Administración Pública:

* [Guía para la publicación de datos en formatos abiertos](https://datosgobar.github.io/paquete-apertura-datos/guia-abiertos/).     Recomendaciones para publicar datos en formatos abiertos, estructurar bien una tabla, nombrar archivos y columnas, usar estándares básicos y trabajar con planillas de cálculo.
* [Guía para la identificación y uso de entidades interoperables](https://datosgobar.github.io/paquete-apertura-datos/guia-interoperables/). Recomendaciones y referencias para nombrar entidades en activos de datos, usando sus nombres y códigos oficiales.
* [Guía para el uso y la publicación de metadatos](https://datosgobar.github.io/paquete-apertura-datos/guia-metadatos/). Recomendaciones y estándares para documentar activos de datos.

## ¿Qué datasets publicar?

El marco normativo nacional y los índices internacionales (ver Anexo II), proponen una lista de datasets recomendados para publicar. Esto es sólo una guía para comenzar y despertar ideas: las necesidades específicas de cada municipio guiarán las prioridades teniendo en cuenta cuál será el uso que se dará a los datos publicados.

Estas instituciones no determinan el formato o campos específicos en que hay que publicar los datos de las distintas áreas. Para esto, existen diversos estándares que pueden ser utilizados para incrementar la usabilidad e interoperabilidad de los datos publicados, como las guías que recomendamos leer en la sección de buenas prácticas.


**Listado de datasets recomendados**
<table>
  <tr>
    <th>Área</th>
    <th>Conjunto de Datos</th>
    <th>Descripción</th>
    <!-- <th>Ley</th> -->
    <!-- <th>Decreto</th> -->
    <!-- <th>IDACA</th> -->
    <!-- <th>ODB</th> -->
  </tr>
  <tr>
    <td>Transparencia Fiscal</td>
    <td>Nómina de funcionarios públicos y sus salarios</td>
    <td>Listas de los funcionarios con referencia a la entidad a la que pertenecen, la categoría y el cargo, incluyendo pasantes y personal contratado en el marco de proyectos financiados por organismos multilaterales, detallando sus respectivas funciones y posición en el escalafón.
En el caso de autoridades superiores se recomienda publicar los salarios.</td>
    <!-- <td>X</td> -->
    <!-- <td>X</td> -->
    <!-- <td>X</td> -->
    <!-- <td></td> -->
  </tr>
  <tr>
    <td>Transparencia Fiscal</td>
    <td>Declaraciones juradas</td>
    <td>Declaración Jurada Patrimonial Integral de carácter público con su correspondiente relación a la Nómina de Funcionarios;</td>
    <!-- <td>X</td> -->
    <!-- <td>X</td> -->
    <!-- <td></td> -->
    <!-- <td></td> -->
  </tr>
  <tr>
    <td>Transparencia Fiscal</td>
    <td>Organigrama</td>
    <td>Organismos y entidades del estado con su estructura orgánica y funciones</td>
    <!-- <td>X</td> -->
    <!-- <td>X</td> -->
    <!-- <td></td> -->
    <!-- <td></td> -->
  </tr>
  <tr>
    <td>Transparencia Fiscal</td>
    <td>Presupuesto de Ingresos</td>
    <td>El presupuesto asignado a cada área, programa o función, las modificaciones durante cada ejercicio anual y el estado de ejecución actualizado en forma trimestral hasta el último nivel de desagregación en que se procese;</td>
    <!-- <td>X</td> -->
    <!-- <td></td> -->
    <!-- <td></td> -->
    <!-- <td>X</td> -->
  </tr>
  <tr>
    <td>Transparencia Fiscal</td>
    <td>Presupuesto de egresos</td>
    <td>Presupuesto del gobierno municipal a un nivel alto, el gasto gubernamental previsto para el próximo año:
Presupuesto por oficina de gobierno
Presupuesto por sub-secretaría
Descripciones de la secciones del presupuesto</td>
    <!-- <td>X</td> -->
    <!-- <td>X</td> -->
    <!-- <td>X</td> -->
    <!-- <td>X</td> -->
  </tr>
  <tr>
    <td>Transparencia Fiscal</td>
    <td>Registro de proveedores</td>
    <td>Nombre de proveedores adjudicados en contrataciones públicas, así como los socios y accionistas principales, de las sociedades o empresas proveedoras;</td>
    <!-- <td>X</td> -->
    <!-- <td></td> -->
    <!-- <td>X</td> -->
    <!-- <td>X</td> -->
  </tr>
  <tr>
    <td>Transparencia Fiscal</td>
    <td>Contrataciones públicas</td>
    <td>Listado de todos los procesos de contratación, los procesos de contratación de obras deberían tener un enlace a sus obras, con el fin de poder agrupar todos los contratos de una obra dada (diseño, construcción, fiscalización)</td>
    <!-- <td>X</td> -->
    <!-- <td>X</td> -->
    <!-- <td>X</td> -->
    <!-- <td>X</td> -->
  </tr>
  <tr>
    <td>Transparencia Fiscal</td>
    <td>Pagos de las contrataciones públicas</td>
    <td>Registros del gasto real (pasado) del gobierno municipal en un nivel transaccional detallado, incluyendo el objeto de gasto, monto y oficina gubernamental que realizó el gasto. Además sus beneficiarios;</td>
    <!-- <td>X</td> -->
    <!-- <td></td> -->
    <!-- <td>X</td> -->
    <!-- <td></td> -->
  </tr>
  <tr>
    <td>Transparencia gubernamental</td>
    <td>Servicios</td>
    <td>Los servicios que brinda el organismo directamente al público, incluyendo normas, cartas y protocolos de atención al cliente;</td>
    <!-- <td>X</td> -->
    <!-- <td></td> -->
    <!-- <td></td> -->
    <!-- <td></td> -->
  </tr>
  <tr>
    <td>Transparencia gubernamental</td>
    <td>Trámites</td>
    <td>Un índice de trámites y procedimientos que se realicen ante el organismo, así como los requisitos y criterios de asignación para acceder a las prestaciones</td>
    <!-- <td>X</td> -->
    <!-- <td></td> -->
    <!-- <td></td> -->
    <!-- <td></td> -->
  </tr>
  <tr>
    <td>Transparencia gubernamental</td>
    <td>Denuncias</td>
    <td>Mecanismos de presentación directa de solicitudes o denuncias a disposición del público en relación a acciones u omisiones del sujeto obligado</td>
    <!-- <td>X</td> -->
    <!-- <td></td> -->
    <!-- <td></td> -->
    <!-- <td></td> -->
  </tr>
  <tr>
    <td>Transparencia gubernamental</td>
    <td>Permisos</td>
    <td>Los permisos, concesiones y autorizaciones otorgados y sus titulares</td>
    <!-- <td>X</td> -->
    <!-- <td></td> -->
    <!-- <td></td> -->
    <!-- <td></td> -->
  </tr>
  <tr>
    <td>Datos geográficos</td>
    <td>Límites administrativos</td>
    <td>Datos sobre unidades administrativas o áreas definidas para el propósito de administración por el gobierno (local).
Nivel de frontera 1
Nivel de frontera 2
Cordenadas (latitud y longitud)
Nombre del polígono (barrio, ciudad)
Bordes de los polígonos</td>
    <!-- <td></td> -->
    <!-- <td></td> -->
    <!-- <td>X</td> -->
    <!-- <td></td> -->
  </tr>
  <tr>
    <td>Datos geográficos</td>
    <td>Transporte Público</td>
    <td>Horarios del transporte público y los recorridos de cada línea de transporte.</td>
    <!-- <td></td> -->
    <!-- <td></td> -->
    <!-- <td>X</td> -->
    <!-- <td>X</td> -->
  </tr>
  <tr>
    <td>Datos geográficos</td>
    <td>Mapa</td>
    <td>Mapa completo de la ciudad con información actualizada, listados sobre centros de salud, establecimientos educativos, centros de atención ciudadana y los espacios públicos de la ciudad</td>
    <!-- <td></td> -->
    <!-- <td></td> -->
    <!-- <td>X</td> -->
    <!-- <td>X</td> -->
  </tr>
  <tr>
    <td>Datos geográficos</td>
    <td>Catastro y dueños</td>
    <td>Catastro de las tierras e información sobre los dueños de las mismas</td>
    <!-- <td></td> -->
    <!-- <td></td> -->
    <!-- <td></td> -->
    <!-- <td>X</td> -->
  </tr>
  <tr>
    <td>Marco normativo (diferenciar por provincia y ciudad)</td>
    <td>Leyes, decretos, resoluciones, ordenanzas, acordadas</td>
    <td>Todas las leyes y los estatutos municipales sancionados por el Honorable Concejo Deliberante</td>
    <!-- <td>X</td> -->
    <!-- <td></td> -->
    <!-- <td>X</td> -->
    <!-- <td>X</td> -->
  </tr>
  <tr>
    <td>Elecciones</td>
    <td>Resultados de las elecciones</td>
  <td>Resultados de las últimas elecciones municipales desagregadas por mesas electorales.</td>
    <!-- <td></td> -->
    <!-- <td></td> -->
    <!-- <td>X</td> -->
    <!-- <td>X</td> -->
  </tr>
  <tr>
    <td>Medio ambiente</td>
    <td>Calidad de aire</td>
    <td>Concentración de contaminantes perjudiciales para la salud humana en agua y aire. Estaciones de monitoreo de aire y monitoreo de fuentes de agua.</td>
    <!-- <td></td> -->
    <!-- <td></td> -->
    <!-- <td>X</td> -->
    <!-- <td>X</td> -->
  </tr>
  <tr>
    <td>Medio ambiente</td>
    <td>Calidad de agua</td>
    <td>Concentración de contaminantes perjudiciales para la salud humana en agua y aire. Estaciones de monitoreo de aire y monitoreo de fuentes de agua.</td>
    <!-- <td></td> -->
    <!-- <td></td> -->
    <!-- <td>X</td> -->
    <!-- <td>X</td> -->
  </tr>
  <tr>
    <td>Estadísticas</td>
    <td>Crimen</td>
    <td>Estadísticas sobre niveles de crimen o listado de los mismos</td>
    <!-- <td></td> -->
    <!-- <td></td> -->
    <!-- <td></td> -->
    <!-- <td>X</td> -->
  </tr>
  <tr>
    <td>Estadísticas</td>
    <td>Educación</td>
    <td>Estadísticas de educación, cantidad de alumnos por aula (grado e institución), por sexo, por edad. Si se tiene estadísticas de notas de los alumnos</td>
    <!-- <td></td> -->
    <!-- <td></td> -->
    <!-- <td></td> -->
    <!-- <td>X</td> -->
  </tr>
  <tr>
    <td>Estadísticas</td>
    <td>Salud</td>
    <td>Disponibilidad de medicina, cantidad de pacientes atendidos por servicios de salud, etc</td>
    <!-- <td></td> -->
    <!-- <td></td> -->
    <!-- <td></td> -->
    <!-- <td>X</td> -->
  </tr>
</table>

## ¿Cómo evaluar la política de apertura?

El Open Data Barometer, el Open Data Index ([Ver Anexo II](https://datosgobar.github.io/guia-subnacionales/#anexo-ii-indices-internacionales-y-marco-normativo-que-fijan-prioridades-de-publicacion)) y su [edición local](http://ar-cities.survey.okfn.org/) son formas en las cuáles una política de apertura puede ser medida.

Dicho esto, existen otra serie de indicadores que pueden ser de ayuda, dependiendo del nivel de desarrollo de la política. Aquí algunos ejemplos que se pueden tener en cuenta una vez que se instalan estas políticas:

* Nuevos pedidos de datos. Indican que hay una demanda activa que está usando datos abiertos en el desarrollo de sus actividades y encuentra nuevas oportunidades de uso.

* Cantidad de participantes en eventos vinculados a uso de datos. Es una aproximación al tamaño de la comunidad que re-utiliza datos abiertos.

* Analíticas del sitio
    - Cantidad de descargas del portal
    - Usuarios que vuelven
    - Cantidad de consultas a una [API](https://datosgobar.github.io/paquete-apertura-datos/glosario/#api)

* Proyectos basados en datos abiertos. Este es un indicador cualitativo que muestra ejemplos de aplicaciones de los datos abiertos para fines específicos.

Si bien cada uno de estos indicadores señala algún aspecto relevante sobre la política de apertura, medir el impacto efectivo no es sencillo y no conviene evaluar la política siguiendo sólo una de estas métricas en particular.

## ¿Cómo difundir el uso de datos?
 
Uno de los aspectos cruciales que determinan el éxito y la sostenibilidad de una iniciativa de datos abiertos es el desarrollo de una comunidad de actores que reutilicen estos datos. Los datos abiertos son una materia prima con la cual se pueden producir diferentes productos, servicios, investigaciones, aplicaciones y visualizaciones. Para que suceda es necesario generar instancias en las que los actores que poseen estos conocimientos se acerquen a los datos públicos.
 
### Comunicar la iniciativa
 
El primer punto a resolver es cómo presentar la iniciativa en sociedad. Debemos desarrollar ciertas piezas comunicacionales contando nuestra propuesta a estos actores que serán los que vengan a aportar la última capa de valor a nuestra iniciativa.
 
Describir los objetivos de la iniciativa, mostrar con qué tecnologías se está trabajando y describir los activos de datos más destacados del portal de datos será nuestra carta de presentación.
 
!!! note ""
    [Presentación de portal institucional Ciudad de Mendoza](https://www.youtube.com/watch?v=rT4hfG0ewjI&feature=youtu.be)
 
Además de desarrollar productos comunicacionales específicos debemos cumplir con los procedimientos tradicionales de difusión, intentando cubrir la mayor cantidad de espacios donde se pueda dar publicidad al lanzamiento de la iniciativa.
 
Esto incluye, publicaciones en las redes sociales oficiales del gobierno, gacetillas de prensa para los medios locales y medios especializados que puedan tener interés en los datos publicados en el portal.
 
### Sectores reutilizadores
 
La sociedad en su conjunto puede encontrar inspiración en el portal de datos para agregarle valor a la comunidad en la que vive, pero existen conjuntos de actores que por su rol o sus habilidades serán el público objetivo de nuestras convocatorias, ya que son los que acercan el valor agregado de los datos públicos al resto. Tenemos que hacer foco en activar estos segmentos en el proceso de lanzamiento de la iniciativa. Identificamos cinco categorías que nos permiten reconocerlos y desarrollar estrategias de acercamiento con cada una de ellos.
 
#### Los funcionarios y empleados públicos
 
El conjunto de funcionarios y empleados de nuestro propio Gobierno son parte de la comunidad de usuarios y consumidores de los datos abiertos. Probablemente sea el segmento más importante dado que tener un portal que concentre diferentes activos de datos facilita su labor diaria y a la vez les permite seguir agregando valor en la gestión pública.
 
Un ejemplo de este tipo de interacción es el “Mapa de Oportunidades Comerciales” (MOC), una iniciativa del Gobierno de la Ciudad de Buenos Aires. El sitio cuenta con  información detallada por zona y rubro para ayudar a los usuarios a elegir la ubicación de un futuro emprendimiento comercial en la Ciudad.
 
![image alt text](assets/images/subnacionales_4.png)
 
El MOC brinda información detallada del panorama comercial a empresas y emprendedores para hacer más eficiente la toma de decisiones a la hora de abrir o potenciar los locales. Algunos de los datos con los que cuenta la plataforma son:
 
* Apertura y cierre de locales
* Nivel de riesgo
* Indicadores poblacionales
* Indicadores inmobiliarios
 
!!! note ""
    [Otros ejemplos de uso de datos abiertos por la Ciudad de Buenos Aires](https://medium.com/balab/qu%C3%A9-se-hizo-con-los-datos-de-la-ciudad-c435d74f9d0e)
 
#### Sociedad civil organizada
 
El conjunto de actores de la sociedad civil es un catalizador de las demandas sociales.
Los diferentes tipos de organizaciones sociales, como las ONGs, clubes, colegios profesionales y gremios, cada uno cuenta con sus agendas de incidencia que le permite a la iniciativa de datos publicar aquellos que sean pertinentes y sirvan para encarar las diferentes problemáticas reconocidas a nivel local.
 

#### Periodismo y desarrolladores de contenido
 
Los medios suelen ser un aliado clave en el éxito de las iniciativas de datos abiertos, ya que se convierten en reutilizadores de forma inmediata. Al estar compuestos por equipos multidisciplinarios, tienen naturalmente las herramientas y capacidades necesarias para realizar investigaciones, visualizaciones e innovar en formas de poner en valor los datos públicos.
 
El equipo de LA NACIÓN Data explora diariamente bases de datos gubernamentales y gran volumen de documentos públicos. Esta tarea permite detectar no solo nuevas fuentes de información, sino también datos que se convierten en importantes insumos de historias nunca antes contadas.
 
![image alt text](assets/images/subnacionales_2.png)
 
Con la disponibilidad de los datos producen herramientas como el simulador de créditos hipotecario o las verdades de la población carcelaria para derribar mitos que abonaban la xenofobia.
 
!!! note ""
    * [Calculadora de cuotas hipotecarias](https://www.lanacion.com.ar/2102095-creditos-hipotecarios-calcula-tus-cuotas-para-2018-y-los-proximos-dos-anos)
    * [Informe Cárceles argentinas](https://www.lanacion.com.ar/1861899-radiografia-de-las-carceles-argentinas)
 
 
#### Emprendedores tecnológicos
 
Las comunidades de programadores y emprendedores tecnológicos juegan un rol fundamental dado que cuentan con los conocimientos técnicos que les facilitan el trabajar con datos en niveles avanzados. Para llegar a estos conjuntos, podemos hacerlo a través de las cámaras TIC, comunidades de programación y ámbitos de promoción de emprendedores.
 
Puntualmente para los emprendedores, la disponibilidad de datos oficiales siempre es una oportunidad para desarrollar nuevas líneas de negocios, funcionalidades innovadoras y productos o servicios derivados. Tal es el caso de Dymaxion Labs, un emprendimiento tecnológico que desarrolló una plataforma de monitoreo de villas y asentamientos, un monitor de inundaciones, que permite observar y supervisar el avance de inundaciones en tiempo casi real y una aplicación para verificar modificaciones en el uso del suelo. Para esto, utiliza imágenes satelitales y datos abiertos generados por distintos actores. Entre ellos, los datos geoespaciales de la NASA y la Agencia Espacial Europea y datos de los portales del Ministerio de Energía, de las provincias de Buenos Aires, Córdoba y de la Ciudad de Buenos Aires, entre otros.
 
![image alt text](assets/images/subnacionales_0.png)
 
!!! note ""
    * [Unicef stories (en inglés)](http://unicefstories.org/2018/04/04/venturefunddymaxionlabs/)
    * [Nota Federico Baylé](https://www.youtube.com/watch?v=gIcPSnNyxVs)
 
 
#### Academia y comunidad educativa
 
Los datos son un recurso educativo importante en todos los niveles de formación. No sólo se pueden convertir en objeto de estudio y material fundamental para el desarrollo de investigaciones aplicadas, sino que además se pueden incorporar al planteamiento de problemas y trabajos prácticos. Insertar la temática y difundir la iniciativa en el sector académico es una prioridad ya que pone en valor datos reales para solucionar problemáticas existentes del municipio o la provincia.
 
!!! note  "Testeando la usabilidad"
 
    Es importante que se pueda integrar al usuario del portal en el proceso de diseño y optimización y actualización del mismo. Para esto existen diferentes técnicas y metodologías de diseño centrado en el usuario y testeos de usabilidad.
    
    En principio es recomendable que se puedan realizar este tipo de estudios, pero como punto de partida se deberían convocar a usuarios que representen los sectores reutilizadores y consultarles sobre su experiencia utilizando el portal, si les fue fácil encontrar los conjuntos de datos que buscan, comprender si el lenguaje utilizado es adecuado para el público general.
 
### Espacios de colaboración
 
Identificar e interactuar uno a uno con cada sector es indispensable pero no suficiente. Crear una comunidad entre todos los actores que agregan valor a los datos abiertos genera que surjan nuevas interacciones que pueden resultar en nuevos y/o mejores productos y servicios. La interacción de los diferentes conjuntos con Gobierno nos permite atravesar procesos de creación de políticas públicas mucho más enriquecedoras, porque da lugar a crear soluciones con los usuarios finales de las mismas.
 
Hay distintas maneras de generar estas interacciones, dependiendo de los objetivos que queramos cumplir. En el [Kit de Herramientas de Innovación](https://www.argentina.gob.ar/sites/default/files/4._kit_innovacion_2_-_herramientas_practicas_para_la_innovacion_publica.pdf) ([Ver Anexo I](https://datosgobar.github.io/paquete-apertura-datos/guia-subnacionales/#anexo-i-recursos-recomendados)) vas a encontrar distintos dispositivos que nos proponen diferentes maneras de acercarnos y generar una comunidad de práctica que agregue valor.

## Anexo I: recursos recomendados

Aquí un listado de guías y kits de apertura que pueden servir como complemento a los contenidos desarrollados:

* [Kit de Apertura de Datos](https://www.argentina.gob.ar/sites/default/files/2._kit_de_datos_abiertos.pdf) - Presidencia de la Nación Argentina
* [Kit de Gobierno Abierto](https://www.argentina.gob.ar/sites/default/files/kit_gobierno_abierto-alianza_para_el_gobierno_abierto.pdf) - Presidencia de la Nación Argentina
* [Kit de Innovación I](https://www.argentina.gob.ar/sites/default/files/4._kit_innovacion_-_herramientas_practicas_para_impulsar_la_innovacion_publica.pdf) - Presidencia de la Nación Argentina
* [Kit de Innovación II](https://www.argentina.gob.ar/sites/default/files/4._kit_innovacion_2_-_herramientas_practicas_para_la_innovacion_publica.pdf) - Presidencia de la Nación Argentina
* [Kit de Evaluación (Herramientas ágiles)](https://www.argentina.gob.ar/sites/default/files/1._digital_-_kit_de_evaluacion_-_herramientas_para_gestion_agil.pdf) - Presidencia de la Nación Argentina
* [Kit de Apertura Municipal](http://datos.gba.gob.ar/wp-content/uploads/2018/03/Kit-de-Apertura-Municipal-Gobierno-Abierto-PBA-2018.pdf) - Provincia de Buenos Aires
* [Manual de Municipio Abierto](http://datosgobierno.vicentelopez.gov.ar/docs/VicenteLopez-ManualDatosAbiertos.pdf) - Municipalidad de  Vicente López
* [Do It Yourself Open Data Toolkit](https://open.canada.ca/en/toolkit/diy) - Gobierno de Canadá (Inglés/Francés)
* [Recursos pedagógicos y metodológicos de apertura de datos](http://opendatalocale.net/ressources/) - Francia (Francés)
* [Paso a paso de una política de datos abiertos](https://opendatapolicyhub.sunlightfoundation.com/step-by-step/) - Sunlight Foundation (Inglés)

## Anexo II: índices internacionales y marco normativo que fijan prioridades de publicación

El marco normativo nacional fija algunos conjuntos de datos que es obligatorio publicar para organismos de la Administración Pública Nacional:

* **[La Ley 27275 de "Derecho de Acceso a la Información Pública"](http://servicios.infoleg.gob.ar/infolegInternet/anexos/265000-269999/265949/norma.htm) en su Artículo 32**
* **[El Decreto 117-2016 del "Plan de Apertura de Datos"](http://servicios.infoleg.gob.ar/infolegInternet/anexos/255000-259999/257755/norma.htm)**

Existen organizaciones internacionales que establecen los conjuntos de datos deseables a publicar como:

* **El _[Open Data Barometer (ODB)](https://opendatabarometer.org/)_**, desarrollado por la World Wide Web Foundation como un trabajo colaborativo de la red Open Data for Development (OD4D). Tiene como objetivo descubrir la verdadera prevalencia e impacto de las iniciativas de datos abiertos en torno a el mundo. Analiza las tendencias mundiales y proporciona datos comparativos sobre países y regiones utilizando una metodología en profundidad que combina datos contextuales, evaluaciones técnicas e indicadores secundarios.
* **El _[Global Open Data Index](https://index.okfn.org/) / Índice Global de Datos Abiertos (GODI)_**, administrado por Open Knowledge Network, mide la publicación de datos a nivel país. Sumada a estas mediciones nacionales, Argentina desarrolla desde hace dos años un índice a nivel local midiendo el nivel de publicación de datos abiertos de cada uno de los gobiernos de cada una de sus ciudades, en un [*Índice de datos abiertos de Ciudades de Argentina*](http://ar-cities.survey.okfn.org).

## Glosario

Ver [Glosario](glosario.md)
