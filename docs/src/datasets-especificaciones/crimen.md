# Estadísticas del Crimen

Estadísticas sobre niveles de crimen o listado de los mismos.

* **Tema**: Justicia, seguridad y legales
* **Estándar referencia**: [Open Crime Data Standard](https://github.com/spotcrimebrit/SpotCrime-Open-Crime-Data-Standard)
* **Formatos**: JSON, CSV

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Crímenes  
**[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/crimen/crimenes.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/crimen/crimenes.xlsx)**

<table>
    <tr>
        <th>crimen_fecha</th>
        <th>crimen_hora</th>
        <th>crimen_region</th>
        <th>crimen_ciudad</th>
        <th>crimen_barrio</th>
        <th>crimen_codigo_postal</th>
        <th>crimen_seccional</th>
        <th>crimen_lugar</th>
        <th>crimen_latitud</th>
        <th>crimen_longitud</th>
        <th>crimen_tipo</th>
        <th>crimen_descripcion</th>
        <th>crimen_id_caso</th>
        <th>crimen_id_incidente</th>
    </tr>

    <tr>
        <td>2018-02-02</td>
        <td>22:35</td>
        <td>Buenos Aires</td>
        <td>Bahia Blanca</td>
        <td>Bella Vista</td>
        <td>B8000</td>
        <td>5</td>
        <td>San Lorenzo esq. Garay</td>
        <td>-38.7169673</td>
        <td>-62.2486776</td>
        <td>Homicidio</td>
        <td></td>
        <td>865542</td>
        <td>2336</td>
    </tr>
        
</table>
### Recurso: Estadísticas Criminales
**[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/crimen/estadisticas-criminales.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/crimen/estadisticas-criminales.xlsx)**

<table>
    <tr>
        <th>mes</th>
        <th>provincia_id</th>
        <th>provincia_nombre</th>
        <th>departamento_id</th>
        <th>departamento_nombre</th>
        <th>localidad_id</th>
        <th>localidad_nombre</th>
        <th>barrio_nombre</th>
        <th>delito_tipo</th>
        <th>victima_sexo</th>
        <th>victimario_sexo</th>
        <th>victima_edad</th>
        <th>victimario_edad</th>
        <th>vinculo_victima_victimario</th>
        <th>situacion_victimario</th>
        <th>casos_cantidad</th>
    </tr>

    <tr>
        <td>2018-02</td>
        <td>Buenos Aires</td>
        <td></td>
        <td>Bahia Blanca</td>
        <td></td>
        <td>Bahia Blanca</td>
        <td></td>
        <td>Bella Vista</td>
        <td>Homicidio</td>
        <td>Mujer</td>
        <td>Varón</td>
        <td>45</td>
        <td>48</td>
        <td>Pareja</td>
        <td>Suicidio</td>
        <td>2</td>
    </tr>
        
</table>

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases



Descargar clases en **[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/crimen-clases.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/crimen-clases.xlsx)**


<table>
    <tr>
        <th>nombre</th>
        <th>descripcion</th>
    </tr>

    <tr>
        <td>Crimen</td>
        <td>Atributos de un hecho criminal determinado.</td>
    </tr>
        
    <tr>
        <td>Indicador Criminal</td>
        <td>Atributos de un indicador criminal que recoge una cantidad de casos de ocurrencia, con diversas dimensiones de apertura (que son sus atributos).</td>
    </tr>
        
</table>

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/crimen-campos.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/crimen-campos.xlsx)**

### Recurso: Crímenes  

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
        <td>Crimen</td>
        <td>crimen_fecha</td>
        <td>fecha</td>
        <td>Fecha del crimen</td>
        <td>2018-02-02</td>
        <td>Schema:DateTime</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Crimen</td>
        <td>crimen_hora</td>
        <td>hora</td>
        <td>Hora del crimen</td>
        <td>22:35</td>
        <td>Schema:DateTime</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Crimen</td>
        <td>crimen_region</td>
        <td>alfanumérico</td>
        <td>Zona, región, provincia, departamento</td>
        <td>Buenos Aires</td>
        <td>Schema:PostalAddress</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Crimen</td>
        <td>crimen_ciudad</td>
        <td>alfanumérico</td>
        <td>Ciudad donde se perpetro el crimen</td>
        <td>Bahia Blanca</td>
        <td>Schema:PostalAddress</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Crimen</td>
        <td>crimen_barrio</td>
        <td>alfanumérico</td>
        <td>Nombre del barrio donde se produce el hecho</td>
        <td>Bella Vista</td>
        <td>Schema:PostalAddress</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Crimen</td>
        <td>crimen_codigo_postal</td>
        <td>alfanumérico</td>
        <td>Codigo postal del lugar donde se produce el hecho</td>
        <td>B8000</td>
        <td>Schema:PostalAddress</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Crimen</td>
        <td>crimen_seccional</td>
        <td>alfanumérico</td>
        <td>Identificación de la sección policial donde ocurrió el hecho.</td>
        <td>5</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Crimen</td>
        <td>crimen_lugar</td>
        <td>alfanumérico</td>
        <td>Dirección; calle, numero , esquinas</td>
        <td>San Lorenzo esq. Garay</td>
        <td>Schema:PostalAddress</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Crimen</td>
        <td>crimen_latitud</td>
        <td>numérico</td>
        <td>Coordenadas geograficas expresadas en latitud</td>
        <td>-38.7169673</td>
        <td>Schema:GeoCoordinates</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Crimen</td>
        <td>crimen_longitud</td>
        <td>numérico</td>
        <td>Coordenadas geogrñaficas expresadas en longitud</td>
        <td>-62.2486776</td>
        <td>Schema:GeoCoordinates</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Crimen</td>
        <td>crimen_tipo</td>
        <td>alfanumérico</td>
        <td>Tipo de crimen</td>
        <td>Homicidio</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Crimen</td>
        <td>crimen_descripcion</td>
        <td>texto</td>
        <td>Detalles del crimen</td>
        <td></td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Crimen</td>
        <td>crimen_id_caso</td>
        <td>alfanumérico</td>
        <td>Identificación del caso. Puede haber un caso con muchos incidentes.</td>
        <td>865542</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Crimen</td>
        <td>crimen_id_incidente</td>
        <td>alfanumérico</td>
        <td>Identificación del incidente</td>
        <td>2336</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
</table>
### Recurso: Estadísticas Criminales

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
        <td>Indicador Criminal</td>
        <td>mes</td>
        <td>alfanumérico</td>
        <td>Año y mes en que se recoge la información según ISO 8601 (YYYY-MM).</td>
        <td>2018-02</td>
        <td>Schema:Date</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Indicador Criminal</td>
        <td>provincia_id</td>
        <td>alfanumérico</td>
        <td>Identificador oficial de la provincia donde de produce el hecho.</td>
        <td>Buenos Aires</td>
        <td>Schema:PostalAddress</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Indicador Criminal</td>
        <td>provincia_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre de la provincia donde se produce el hecho.</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
        
    <tr>
        <td>Indicador Criminal</td>
        <td>departamento_id</td>
        <td>alfanumérico</td>
        <td>Identificador oficial del departamento donde de produce el hecho.</td>
        <td>Bahia Blanca</td>
        <td>Schema:PostalAddress</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Indicador Criminal</td>
        <td>departamento_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre del departamento donde se produce el hecho.</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
        
    <tr>
        <td>Indicador Criminal</td>
        <td>localidad_id</td>
        <td>alfanumérico</td>
        <td>Identificador oficial de la localidad donde de produce el hecho.</td>
        <td>Bahia Blanca</td>
        <td>Schema:PostalAddress</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Indicador Criminal</td>
        <td>localidad_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre de la localidad donde se produce el hecho.</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
        
    <tr>
        <td>Indicador Criminal</td>
        <td>barrio_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre del barrio donde se produce el hecho.</td>
        <td>Bella Vista</td>
        <td>Schema:PostalAddress</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Indicador Criminal</td>
        <td>delito_tipo</td>
        <td>alfanumérico</td>
        <td>Tipificación del delito.</td>
        <td>Homicidio</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Indicador Criminal</td>
        <td>victima_sexo</td>
        <td>alfanumérico</td>
        <td>Genero de la victima.</td>
        <td>Mujer</td>
        <td>Schema:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Indicador Criminal</td>
        <td>victimario_sexo</td>
        <td>alfanumérico</td>
        <td>Genero del victimario.</td>
        <td>Varón</td>
        <td>Schema:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Indicador Criminal</td>
        <td>victima_edad</td>
        <td>alfanumérico</td>
        <td>Las edades pueden ser exactas 20, 25 o por rangos, entre 0 y 10; entre 10 y 25, etc.</td>
        <td>45</td>
        <td>Schema:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Indicador Criminal</td>
        <td>victimario_edad</td>
        <td>alfanumérico</td>
        <td>Las edades pueden ser exactas 20, 25 o por rangos, entre 0 y 10; entre 10 y 25, etc.</td>
        <td>48</td>
        <td>Schema:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Indicador Criminal</td>
        <td>vinculo_victima_victimario</td>
        <td>alfanumérico</td>
        <td>Vinculo si existia entre la victima y el victimario, generalmente aplica a casos de violencia familiar o de genero.</td>
        <td>Pareja</td>
        <td>vCard:related:type_value</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Indicador Criminal</td>
        <td>situacion_victimario</td>
        <td>alfanumérico</td>
        <td>Situación actual del victimario.</td>
        <td>Suicidio</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Indicador Criminal</td>
        <td>casos_cantidad</td>
        <td>alfanumérico</td>
        <td>Cantidad en numeros de casos.</td>
        <td>2</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
