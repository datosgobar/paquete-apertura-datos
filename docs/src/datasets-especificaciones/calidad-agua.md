# Calidad del Agua

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos
    
### Recurso: Estacion  
**[CSV](calidad-agua/estacion.csv)** | **[XLSX](calidad-agua/estacion.xlsx)**

<table>
    <tr>
        <th>estacion_id</th>
        <th>estacion_nombre</th>
        <th>estacion_region</th>
        <th>estacion_latitud</th>
        <th>estacion_longitud</th>
        <th>estacion_zonahoraria</th>
        <th>estacion_tipo</th>
        <th>estacion_cuenca</th>
        <th>estacion_subcuenca</th>
        <th>estacion_fecha_desde</th>
        <th>estacion_fecha_hasta</th>
        <th>estacion_muestreos</th>
    </tr>

    <tr>
        <td>1001</td>
        <td>Chapelco</td>
        <td>San Martin de Los Andes</td>
        <td>-40.180854</td>
        <td>-71.318434</td>
        <td>UTC-3</td>
        <td>Agua Superficial - Fondo</td>
        <td>Lago Lacar</td>
        <td></td>
        <td>2010-01-06</td>
        <td>2019-03-29</td>
        <td>834</td>
    </tr>
        
</table>
### Recurso: Contaminante
**[CSV](calidad-agua/contaminante.csv)** | **[XLSX](calidad-agua/contaminante.xlsx)**

<table>
    <tr>
        <th>contaminante_estacion_id</th>
        <th>contaminante_cuenca</th>
        <th>contaminante_subcuenca</th>
        <th>contaminante_nombre</th>
        <th>contaminante_unidad</th>
        <th>contaminante_actualizado</th>
        <th>contaminante_valor</th>
        <th>contaminante_validez</th>
    </tr>

    <tr>
        <td>1001</td>
        <td>Lago Lacar</td>
        <td></td>
        <td>Potencial de hidrogeno</td>
        <td></td>
        <td>2019-03-29</td>
        <td>7.1</td>
        <td>5 días</td>
    </tr>
        
</table>

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](calidad-agua-campos.csv)** | **[XLSX](calidad-agua-campos.xlsx)**

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
        <td>fecha</td>
        <td>Coordenadas geograficas</td>
        <td>-40.180854</td>
        <td>schema:GeoCoordinates</td>
        <td>Fecha de registro de la parcela</td>
    </tr>
        
    <tr>
        <td>Estacion</td>
        <td>estacion_longitud</td>
        <td>numerico</td>
        <td>Coordenadas geograficas</td>
        <td>-71.318434</td>
        <td>schema:GeoCoordinates</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estacion</td>
        <td>estacion_zonahoraria</td>
        <td>texto</td>
        <td>Campo opcional para indicar la zona horaria</td>
        <td>UTC-3</td>
        <td>schema:BroadcastService</td>
        <td>Descripción de las estructuras edificadas</td>
    </tr>
        
    <tr>
        <td>Estacion</td>
        <td>estacion_tipo</td>
        <td>texto</td>
        <td>Describe si la estación es superficial o de profundidad</td>
        <td>Agua Superficial - Fondo</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estacion</td>
        <td>estacion_cuenca</td>
        <td>alfanumerico</td>
        <td>Nombre de la cuenca</td>
        <td>Lago Lacar</td>
        <td>schema:Place</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estacion</td>
        <td>estacion_subcuenca</td>
        <td>alfanumerico</td>
        <td>Nombre de la subcuenca</td>
        <td></td>
        <td>schema:Place</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estacion</td>
        <td>estacion_fecha_desde</td>
        <td>fecha</td>
        <td>Fecha de inicio de la medición</td>
        <td>2010-01-06</td>
        <td>schema:Date</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estacion</td>
        <td>estacion_fecha_hasta</td>
        <td>fecha</td>
        <td>Ultima fecha de medición</td>
        <td>2019-03-29</td>
        <td>schema:Date</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estacion</td>
        <td>estacion_muestreos</td>
        <td>numerico</td>
        <td>Cantidad de muestreos realizados en el período</td>
        <td>834</td>
        <td>schema:Thing</td>
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
        <td>contaminante_cuenca</td>
        <td>alfanumerico</td>
        <td>Nombre de la cuenca</td>
        <td>Lago Lacar</td>
        <td>schema:Place</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contaminante</td>
        <td>contaminante_subcuenca</td>
        <td>alfanumerico</td>
        <td>Nombre de la subcuenca</td>
        <td></td>
        <td>schema:Place</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contaminante</td>
        <td>contaminante_nombre</td>
        <td>alfanumerico</td>
        <td>Nombre del contaminante que se esta midiendo</td>
        <td>Potencial de hidrogeno</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contaminante</td>
        <td>contaminante_unidad</td>
        <td>alfanumerico</td>
        <td>Unidad de medida en que se establece el valor</td>
        <td></td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contaminante</td>
        <td>contaminante_actualizado</td>
        <td>fecha</td>
        <td>Fecha y hora de actualizado el valor</td>
        <td>2019-03-29</td>
        <td>schema:Date</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contaminante</td>
        <td>contaminante_valor</td>
        <td>numerico</td>
        <td>Valor obtenido en la medición</td>
        <td>7.1</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contaminante</td>
        <td>contaminante_validez</td>
        <td>alfanumerico</td>
        <td>Indica la duración de validez del dato</td>
        <td>5 días</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
