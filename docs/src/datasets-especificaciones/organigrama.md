# Organigrama

Organismos y entidades del estado con su estructura orgánica y funciones.

* **Tema**: Gobierno y sector público
* **Estándar referencia**: [Organizaciones de Popolo](http://www.popoloproject.com/specs/organization.html)
* **Formatos**: JSON, XML, CSV
* **Ejemplo:**: http://www.popoloproject.com/examples/organization.json

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Organigrama
**[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/organigrama/organigrama.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/organigrama/organigrama.xlsx)**

<table>
    <tr>
        <th>organizacion_id</th>
        <th>organizacion_nombre</th>
        <th>organizacion_clasificacion</th>
        <th>organizacion_padre_id</th>
        <th>organizacion_area</th>
        <th>organizacion_fecha_creacion</th>
        <th>organizacion_fecha_final</th>
        <th>organizacion_imagen</th>
        <th>organizacion_contactos</th>
        <th>organizacion_direccion</th>
        <th>organizacion_latitud</th>
        <th>organizacion_longitud</th>
        <th>organizacion_enlaces</th>
    </tr>

    <tr>
        <td>2</td>
        <td>Ministerio de Modernización</td>
        <td>Poder Ejecutivo</td>
        <td>1</td>
        <td>ARG</td>
        <td>2015-06-01</td>
        <td></td>
        <td>https://www.argentina.gob.ar/profiles/argentinagobar/themes/argentinagobar/argentinagobar_theme/logo.svg</td>
        <td>(54-011) 5985-8700 / 4343-9001</td>
        <td>Av. Roque Sáenz Peña 511 (Entrepiso) - CABA</td>
        <td>-34.607617</td>
        <td>-58.373771</td>
        <td>https://www.argentina.gob.ar/modernizacion</td>
    </tr>
        
</table>

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases



Descargar clases en **[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/organigrama-clases.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/organigrama-clases.xlsx)**


<table>
    <tr>
        <th>nombre</th>
        <th>descripcion</th>
    </tr>

    <tr>
        <td>Organización</td>
        <td>Atributos que describen a las instituciones públicas que componen el organigrama.</td>
    </tr>
        
</table>

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/organigrama-campos.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/organigrama-campos.xlsx)**

### Recurso: Organigrama

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
        <td>Organización</td>
        <td>organizacion_id</td>
        <td>alfanumérico</td>
        <td>Identificador único para la organización.</td>
        <td>2</td>
        <td>popolo:Organization</td>
        <td>Se puede utilizar una codificacion en base al presupuesto; ej: Código jurisdicccion:+código sub jurisdicción:+ ...</td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_nombre</td>
        <td>alfanumérico</td>
        <td>El nombre principal de la organización, por ejemplo su nombre legal.</td>
        <td>Ministerio de Modernización</td>
        <td>popolo:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_clasificacion</td>
        <td>alfanumérico</td>
        <td>La clasificación de la organización, por ejemplo "Poder Ejecutivo"</td>
        <td>Poder Ejecutivo</td>
        <td>popolo:Organization</td>
        <td>Ej: Poder Ejecutivo / Poder Judicial / Empresa Publica / etc.</td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_padre_id</td>
        <td>alfanumérico</td>
        <td>Debe referenciar al id de la organización de la cual esta depende. Por ejemplo la Presidencia de la Nación depende del Poder Ejecutivo.</td>
        <td>1</td>
        <td>popolo:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_area</td>
        <td>alfanumérico</td>
        <td>Indica el área geografica donde se ubica la organizacion, utilizando el código ISO alpha 3 para país ("ARG") o los códigos oficiales de INDEC para provincias ("06") o municipios ("822931").</td>
        <td>ARG</td>
        <td>popolo:Organization</td>
        <td>Se podría ampliar este campo a Provincia, Localidad o Codigo Postal</td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_fecha_creacion</td>
        <td>fecha</td>
        <td>Fecha en que fue creada la organización.</td>
        <td>2015-06-01</td>
        <td>popolo:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_fecha_final</td>
        <td>fecha</td>
        <td>Fecha en que dejo de existir la organización.</td>
        <td></td>
        <td>popolo:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_imagen</td>
        <td>uri</td>
        <td>Logo de la organización, url a la imagen de la organización.</td>
        <td>https://www.argentina.gob.ar/profiles/argentinagobar/themes/argentinagobar/argentinagobar_theme/logo.svg</td>
        <td>popolo:Organization</td>
        <td>URL a logo o imagen que identifica a la organización</td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_contactos</td>
        <td>alfanumérico</td>
        <td>Datos de contacto de la organización.</td>
        <td>(54-011) 5985-8700 / 4343-9001</td>
        <td>popolo:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_direccion</td>
        <td>alfanumérico</td>
        <td>Dirección de la organización.</td>
        <td>Av. Roque Sáenz Peña 511 (Entrepiso) - CABA</td>
        <td>schema:PostalAddress</td>
        <td>Calle, Nro utilizar combinado con organizacion_area</td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_latitud</td>
        <td>numerico</td>
        <td>Coordenadas geográficas de la ubicación de la organización (latitud).</td>
        <td>-34.607617</td>
        <td>schema:GeoCoordinates</td>
        <td>Opcional</td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_longitud</td>
        <td>numerico</td>
        <td>Coordenadas geográficas de la ubicación de la organización (longitud).</td>
        <td>-58.373771</td>
        <td>schema:GeoCoordinates</td>
        <td>Opcional</td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_enlaces</td>
        <td>uri</td>
        <td>Elaces externos que contengan información sobre la organización. Se puede tener mas de un enlace, por lo que se podria diferenciar cada campo con una secuencia de numeros; ej: organización_enlaces_1, … , organización_enlaces_n</td>
        <td>https://www.argentina.gob.ar/modernizacion</td>
        <td>popolo:Organization</td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
