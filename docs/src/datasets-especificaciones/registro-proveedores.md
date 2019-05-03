# Registro de Proveedores

Nombre de proveedores adjudicados en contrataciones públicas, así como los socios y accionistas principales, de las sociedades o empresas proveedoras.

* **Tema**: Gobierno y sector público
* **Estándar referencia**: [Beneficial Ownership](http://standard.openownership.org/en/master/)
* **Formatos**: JSON, XML, CSV

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Declaraciones de Proveedores
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/registro-proveedores/declaraciones-proveedores.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/registro-proveedores/declaraciones-proveedores.xlsx)**

<table>
    <tr>
        <th>declaracion_id</th>
        <th>declaracion_fecha</th>
        <th>declaracion_documentacion</th>
        <th>entidad_id</th>
        <th>entidad_fecha_preinscripcion</th>
        <th>entidad_tipo</th>
        <th>entidad_nombre</th>
        <th>entidad_jurisdiccion</th>
        <th>entidad_correo</th>
        <th>entidad_telefono</th>
        <th>entidad_domicilio_legal</th>
        <th>entidad_estado</th>
    </tr>

    <tr>
        <td>10529</td>
        <td>2020-12-31</td>
        <td>Declaración Jurada de Interes</td>
        <td>30628707093</td>
        <td>2018-01-01</td>
        <td>SRL</td>
        <td>HAL2000</td>
        <td>CABA</td>
        <td>info@hal2000.com</td>
        <td>+541152864897</td>
        <td>Av. Cordoba 1555</td>
        <td>Inscripto</td>
    </tr>
        
</table>
### Recurso: Apoderados o Referentes Legales de Proveedores
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/registro-proveedores/apoderados-o-referentes-legales-proveedores.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/registro-proveedores/apoderados-o-referentes-legales-proveedores.xlsx)**

<table>
    <tr>
        <th>declaracion_id</th>
        <th>persona_id</th>
        <th>persona_tipo</th>
        <th>persona_nombre</th>
        <th>persona_identificador_otro_id</th>
        <th>persona_limite_oferta</th>
    </tr>

    <tr>
        <td>10529</td>
        <td>579320998</td>
        <td>Socio</td>
        <td>Andrea Martinez</td>
        <td>30-62870709-3</td>
        <td></td>
    </tr>
        
</table>
### Recurso: Intereses Declarados por los Proveedores
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/registro-proveedores/intereses-declarados-por-proveedores.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/registro-proveedores/intereses-declarados-por-proveedores.xlsx)**

<table>
    <tr>
        <th>declaracion_id</th>
        <th>clase_id</th>
        <th>clase_descripcion</th>
        <th>clase_rubro_id</th>
        <th>clase_rubro_descripcion</th>
    </tr>

    <tr>
        <td>10529</td>
        <td>584798</td>
        <td>Serv. Detección Incendio</td>
        <td>58</td>
        <td>Serv. Profesional</td>
    </tr>
        
</table>

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases



Descargar clases en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/registro-proveedores/registro-proveedores-clases.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/registro-proveedores/registro-proveedores-clases.xlsx)**


<table>
    <tr>
        <th>nombre</th>
        <th>descripcion</th>
    </tr>

    <tr>
        <td>Declaración</td>
        <td>Atributos de la declaración de una organización al momento de consignarse como proveedora.</td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>Atributos de una empresa u organización que se constituye en un registro de proveedores.</td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>Atributos de las personas físicas responsables o representantes de la organización que se constituye en proveedora.</td>
    </tr>
        
    <tr>
        <td>Intereses</td>
        <td>Atributos de los intereses declarados por la organización respecto de los rubros o áreas en las cuales puede prestar servicios como proveedor.</td>
    </tr>
        
</table>

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/registro-proveedores/registro-proveedores-campos.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/registro-proveedores/registro-proveedores-campos.xlsx)**

### Recurso: Declaraciones de Proveedores

<table>
    <tr>
        <th>clase</th>
        <th>titulo</th>
        <th>tipo_dato</th>
        <th>descripcion</th>
        <th>ejemplo</th>
        <th>estandar_mapeo</th>
        <th>notas</th>
    </tr>

    <tr>
        <td>Declaración</td>
        <td>declaracion_id</td>
        <td>alfanumérico</td>
        <td>Identificador único de la declaración, número de inscripción.</td>
        <td>10529</td>
        <td>BO:EntityStatement</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Declaración</td>
        <td>declaracion_fecha</td>
        <td>fecha</td>
        <td>Fecha de vencimiento de la declaración</td>
        <td>2020-12-31</td>
        <td>BO:EntityStatement</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Declaración</td>
        <td>declaracion_documentacion</td>
        <td>alfanumérico</td>
        <td>Descripción del conjunto de documentos que tiene la parte interesada. Ver interes.</td>
        <td>Declaración Jurada de Interes</td>
        <td>BO:EntityStatement</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>entidad_id</td>
        <td>alfanumérico</td>
        <td>Identificadores oficiales para la entidad (CUIT/CUIL)</td>
        <td>30628707093</td>
        <td>BO:EntityStatement</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>entidad_fecha_preinscripcion</td>
        <td>alfanumérico</td>
        <td>Fecha de registro</td>
        <td>2018-01-01</td>
        <td>BO:EntityStatement</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>entidad_tipo</td>
        <td>alfanumérico</td>
        <td>Tipo de entidad (SA / SRL / etc)</td>
        <td>SRL</td>
        <td>BO:EntityStatement</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>entidad_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre de la entidad o Razón social</td>
        <td>HAL2000</td>
        <td>BO:EntityStatement</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>entidad_jurisdiccion</td>
        <td>alfanumérico</td>
        <td>Jurisdicción expresada utilizando la codificación ISO_3166-2</td>
        <td>CABA</td>
        <td>BO:EntityStatement</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>entidad_correo</td>
        <td>alfanumérico</td>
        <td>Correo electronico de la entidad</td>
        <td>info@hal2000.com</td>
        <td>Schema:ContactPoint</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>entidad_telefono</td>
        <td>alfanumérico</td>
        <td>Telefono de contacto de la entidad</td>
        <td>+541152864897</td>
        <td>Schema:ContactPoint</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>entidad_domicilio_legal</td>
        <td>alfanumérico</td>
        <td>Domicilio leglamente establecido por la entidad</td>
        <td>Av. Cordoba 1555</td>
        <td>BO:EntityStatement</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>entidad_estado</td>
        <td>alfanumérico</td>
        <td>Estado de la entidad</td>
        <td>Inscripto</td>
        <td>No estandarizado</td>
        <td></td>
    </tr>
        
</table>
### Recurso: Apoderados o Referentes Legales de Proveedores

<table>
    <tr>
        <th>clase</th>
        <th>titulo</th>
        <th>tipo_dato</th>
        <th>descripcion</th>
        <th>ejemplo</th>
        <th>estandar_mapeo</th>
        <th>notas</th>
    </tr>

    <tr>
        <td>Declaración</td>
        <td>declaracion_id</td>
        <td>alfanumérico</td>
        <td>Identificador único de la declaración, número de inscripción.</td>
        <td>10529</td>
        <td>BO:EntityStatement</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_id</td>
        <td>alfanumérico</td>
        <td>DNI</td>
        <td>579320998</td>
        <td>Bo:PersonStatement</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_tipo</td>
        <td>alfanumérico</td>
        <td>Se utiliza a la persona para registrar a representate legal, apoderado o cargo.</td>
        <td>Socio</td>
        <td>Bo:PersonStatement</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre completo habitual</td>
        <td>Andrea Martinez</td>
        <td>Bo:PersonStatement</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_identificador_otro_id</td>
        <td>alfanumérico</td>
        <td>CUIT / NIT</td>
        <td>30-62870709-3</td>
        <td>Bo:PersonStatement</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_limite_oferta</td>
        <td>alfanumérico</td>
        <td>Monto límite por oferta electronica, solo aplica a representates legales o apoderados</td>
        <td></td>
        <td>No estandarizado</td>
        <td></td>
    </tr>
        
</table>
### Recurso: Intereses Declarados por los Proveedores

<table>
    <tr>
        <th>clase</th>
        <th>titulo</th>
        <th>tipo_dato</th>
        <th>descripcion</th>
        <th>ejemplo</th>
        <th>estandar_mapeo</th>
        <th>notas</th>
    </tr>

    <tr>
        <td>Declaración</td>
        <td>declaracion_id</td>
        <td>alfanumérico</td>
        <td>Identificador único de la declaración, número de inscripción.</td>
        <td>10529</td>
        <td>BO:EntityStatement</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Intereses</td>
        <td>clase_id</td>
        <td>alfanumérico</td>
        <td>Identificador de la clase de interes</td>
        <td>584798</td>
        <td>Schema:Product</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Intereses</td>
        <td>clase_descripcion</td>
        <td>alfanumérico</td>
        <td>Descripción de la clase de interes o tipo de interes</td>
        <td>Serv. Detección Incendio</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Intereses</td>
        <td>clase_rubro_id</td>
        <td>alfanumérico</td>
        <td>Identificador del rubro asociado a la clase</td>
        <td>58</td>
        <td>Schema:Product</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Intereses</td>
        <td>clase_rubro_descripcion</td>
        <td>alfanumérico</td>
        <td>Descripción del rubro asociado a la clase</td>
        <td>Serv. Profesional</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
