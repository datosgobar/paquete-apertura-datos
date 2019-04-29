# Calidad del Aire

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos
    
### Recurso: Estacion  
**[CSV](calidad-aire/estacion.csv)** | **[XLSX](calidad-aire/estacion.xlsx)**

<table>
    <tr>
        <th>estacion_id</th>
        <th>estacion_nombre</th>
        <th>estacion_region</th>
        <th>estacion_latitud</th>
        <th>estacion_longitud</th>
        <th>estacion_zonahoraria</th>
    </tr>

    <tr>
        <td>1001</td>
        <td>Chapelco</td>
        <td>San Martin de Los Andes</td>
        <td>-40.1808541022993</td>
        <td>-71.31843</td>
        <td>UTC-3</td>
    </tr>
        
</table>
### Recurso: Contaminante
**[CSV](calidad-aire/contaminante.csv)** | **[XLSX](calidad-aire/contaminante.xlsx)**

<table>
    <tr>
        <th>contaminante_estacion_id</th>
        <th>contaminante_nombre</th>
        <th>contaminante_unidad</th>
        <th>contaminante_actualizado</th>
        <th>contaminante_valor</th>
        <th>contaminante_validez</th>
    </tr>

    <tr>
        <td>1001</td>
        <td>Dióxido de azufre</td>
        <td>µg/m3</td>
        <td>2019-02-26 0:00:00</td>
        <td>0.27</td>
        <td>1 hora</td>
    </tr>
        
</table>

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](calidad-aire-campos.csv)** | **[XLSX](calidad-aire-campos.xlsx)**

### Recurso: Estacion  

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
        <td>Estacion</td>
        <td>estacion_id</td>
        <td>alfanumerico</td>
        <td>Identificación de la estación</td>
        <td>1001</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estacion</td>
        <td>estacion_nombre</td>
        <td>alfanumerico</td>
        <td>Nombre de la estación</td>
        <td>Chapelco</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estacion</td>
        <td>estacion_region</td>
        <td>alfanumerico</td>
        <td>Nombre del país/provincia o localidad</td>
        <td>San Martin de Los Andes</td>
        <td>schema:Place</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estacion</td>
        <td>estacion_latitud</td>
        <td>numerico</td>
        <td>Coordenadas geograficas</td>
        <td>-40.1808541022993</td>
        <td>schema:GeoCoordinates</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estacion</td>
        <td>estacion_longitud</td>
        <td>numerico</td>
        <td>Coordenadas geograficas</td>
        <td>-71.31843</td>
        <td>schema:GeoCoordinates</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estacion</td>
        <td>estacion_zonahoraria</td>
        <td>alfanumerico</td>
        <td>Campo opcional para indicar la zona horaria</td>
        <td>UTC-3</td>
        <td>schema:BroadcastService</td>
        <td></td>
    </tr>
        
</table>
### Recurso: Contaminante

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
        <td>Contaminante</td>
        <td>contaminante_estacion_id</td>
        <td>alfanumerico</td>
        <td>Identificación de la estación</td>
        <td>1001</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contaminante</td>
        <td>contaminante_nombre</td>
        <td>alfanumerico</td>
        <td>Nombre del contaminante que se esta midiendo</td>
        <td>Dióxido de azufre</td>
        <td>schema:GeoCoordinates</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contaminante</td>
        <td>contaminante_unidad</td>
        <td>alfanumerico</td>
        <td>Unidad de medida en que se establece el valor</td>
        <td>µg/m3</td>
        <td>schema:GeoCoordinates</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contaminante</td>
        <td>contaminante_actualizado</td>
        <td>fecha</td>
        <td>Fecha y hora de actualizado el valor</td>
        <td>2019-02-26 0:00:00</td>
        <td>schema:Date</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contaminante</td>
        <td>contaminante_valor</td>
        <td>numerico</td>
        <td>Valor obtenido en la medición</td>
        <td>0.27</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contaminante</td>
        <td>contaminante_validez</td>
        <td>alfanumerico</td>
        <td>Indica la duración de validez del dato</td>
        <td>1 hora</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
