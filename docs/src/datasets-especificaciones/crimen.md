# Estadísticas del Crimen

Estadísticas sobre niveles de crimen o listado de los mismos.

* **Tema**: Justicia, seguridad y legales
* **Estándar referencia**: [Open Crime Data Standard](https://github.com/spotcrimebrit/SpotCrime-Open-Crime-Data-Standard)
* **Formatos**: JSON, CSV

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Crimen    
**[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/crimen/crimen.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/crimen/crimen.xlsx)**

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
        <th>crimen_latitude</th>
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
        <td>-387.169.673</td>
        <td>-622.486.776</td>
        <td>Homicidio</td>
        <td></td>
        <td>865542</td>
        <td>2336</td>
    </tr>
        
</table>
### Recurso: Estadísticas Crimen
**[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/crimen/estadisticas-crimen.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/crimen/estadisticas-crimen.xlsx)**

<table>
    <tr>
        <th>estadistica_anio</th>
        <th>estadistica_mes</th>
        <th>estadistica_provincia</th>
        <th>estadistica_departamento</th>
        <th>estadistica_localidad</th>
        <th>estadistica_barrio</th>
        <th>estadistica_tipo_delito</th>
        <th>estadistica_genero_victima</th>
        <th>estadistica_genero_victimario</th>
        <th>estadistica_edad_victima</th>
        <th>estadistica_edad_victimario</th>
        <th>estadistica_vinculo_victima_victimario</th>
        <th>estadistica_situacion_victimario</th>
        <th>estadistica_cantidad</th>
    </tr>

    <tr>
        <td>2018</td>
        <td>6</td>
        <td>Buenos Aires</td>
        <td>Bahia Blanca</td>
        <td>Bahia Blanca</td>
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

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/crimen-campos.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/crimen-campos.xlsx)**

### Recurso: Crimen    

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
        <td>crimen_latitude</td>
        <td>numérico</td>
        <td>Coordenadas geograficas expresadas en latitud</td>
        <td>-387.169.673</td>
        <td>Schema:GeoCoordinates</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Crimen</td>
        <td>crimen_longitud</td>
        <td>numérico</td>
        <td>Coordenadas geogrñaficas expresadas en longitud</td>
        <td>-622.486.776</td>
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
### Recurso: Estadísticas Crimen

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
        <td>Estadísticas Crimen</td>
        <td>estadistica_anio</td>
        <td>alfanumérico</td>
        <td>Año en que se recoge la información estadística a publicar</td>
        <td>2018</td>
        <td>Schema:Date</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estadísticas Crimen</td>
        <td>estadistica_mes</td>
        <td>alfanumérico</td>
        <td>Mes en que se recoge la información estadistica a publicar</td>
        <td>6</td>
        <td>Schema:Date</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estadísticas Crimen</td>
        <td>estadistica_provincia</td>
        <td>alfanumérico</td>
        <td>Nombre de la provincia donde se produce el hecho</td>
        <td>Buenos Aires</td>
        <td>Schema:PostalAddress</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estadísticas Crimen</td>
        <td>estadistica_departamento</td>
        <td>alfanumérico</td>
        <td>Nombre del departamento donde se produce el hecho</td>
        <td>Bahia Blanca</td>
        <td>Schema:PostalAddress</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estadísticas Crimen</td>
        <td>estadistica_localidad</td>
        <td>alfanumérico</td>
        <td>Nombre de la localidad donde se produce el hecho</td>
        <td>Bahia Blanca</td>
        <td>Schema:PostalAddress</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estadísticas Crimen</td>
        <td>estadistica_barrio</td>
        <td>alfanumérico</td>
        <td>Nombre del barrio donde se produce el hecho</td>
        <td>Bella Vista</td>
        <td>Schema:PostalAddress</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estadísticas Crimen</td>
        <td>estadistica_tipo_delito</td>
        <td>alfanumérico</td>
        <td>Tipificación del delito</td>
        <td>Homicidio</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estadísticas Crimen</td>
        <td>estadistica_genero_victima</td>
        <td>alfanumérico</td>
        <td>Genero de la victima</td>
        <td>Mujer</td>
        <td>Schema:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estadísticas Crimen</td>
        <td>estadistica_genero_victimario</td>
        <td>alfanumérico</td>
        <td>Genero del victimario</td>
        <td>Varón</td>
        <td>Schema:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estadísticas Crimen</td>
        <td>estadistica_edad_victima</td>
        <td>alfanumérico</td>
        <td>Las edades pueden ser exactas 20, 25 o por rangos, entre 0 y 10; entre 10 y 25, etc</td>
        <td>45</td>
        <td>Schema:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estadísticas Crimen</td>
        <td>estadistica_edad_victimario</td>
        <td>alfanumérico</td>
        <td>Las edades pueden ser exactas 20, 25 o por rangos, entre 0 y 10; entre 10 y 25, etc</td>
        <td>48</td>
        <td>Schema:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estadísticas Crimen</td>
        <td>estadistica_vinculo_victima_victimario</td>
        <td>alfanumérico</td>
        <td>Vinculo si existia entre la victima y el victimario, generalmente aplica a casos de violencia familiar o de genero</td>
        <td>Pareja</td>
        <td>vCard:related:type_value</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estadísticas Crimen</td>
        <td>estadistica_situacion_victimario</td>
        <td>alfanumérico</td>
        <td>Situación actual del victimario</td>
        <td>Suicidio</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estadísticas Crimen</td>
        <td>estadistica_cantidad</td>
        <td>alfanumérico</td>
        <td>Cantidad en numeros de casos</td>
        <td>2</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
