# Salud

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Establecimientos de Salud
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/salud)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/salud)**

<table>
    <tr>
        <th>organizacion_id</th>
        <th>organizacion_nombre</th>
        <th>organizacion_clasificacion</th>
        <th>organizacion_padre_id</th>
        <th>organizacion_area</th>
        <th>organizacion_fecha_creacion</th>
        <th>organizacion_imagen</th>
        <th>organizacion_contactos</th>
        <th>organizacion_direccion</th>
        <th>organizacion_enlaces</th>
        <th>organizacion_latitud</th>
        <th>organizacion_longitud</th>
    </tr>

    <tr>
        <td>2222</td>
        <td>Hospital Pirovano</td>
        <td>Hospital General</td>
        <td>0</td>
        <td>CABA, Republica Argentina</td>
        <td>1896-07-12</td>
        <td></td>
        <td>contacto@hospitalpirovano.org</td>
        <td>Av. Monroe 3555</td>
        <td>https://www.buenosaires.gob.ar/hospitalpirovano</td>
        <td></td>
        <td></td>
    </tr>
        
</table>
### Recurso: Estadísticas de Salud
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/salud)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/salud)**

<table>
    <tr>
        <th>indicador_anio</th>
        <th>indicador_organizacion_id</th>
        <th>indicador_nombre</th>
        <th>indicador_descripcion</th>
        <th>indicador_periodicidad</th>
        <th>indicador_ultima_medicion</th>
        <th>indicador_unidad_medida</th>
        <th>indicador_valor</th>
        <th>indicador_forma_calculo</th>
    </tr>

    <tr>
        <td>2018</td>
        <td>2222</td>
        <td>Cantidad de camas</td>
        <td>Cantidad de camas cada 1000 personas</td>
        <td>Anual</td>
        <td>2018-12-31</td>
        <td>Cantidad de camas</td>
        <td>5</td>
        <td>Se calcula la cantidad de camas disponibles de acuerdo a la cantidad de afiliados y se pondera el resultado para llevarlo a un valor equivalente sobre una poblacion de 1000 personas.</td>
    </tr>
        
</table>

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases



Descargar clases en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/salud)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/salud)**


<table>
    <tr>
        <th>nombre</th>
        <th>descripcion</th>
    </tr>

    <tr>
        <td>Organización</td>
        <td>Atributos de un establecimiento de salud.</td>
    </tr>
        
    <tr>
        <td>Indicador de Salud</td>
        <td>Atributos de un indicador de salud.</td>
    </tr>
        
</table>

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/salud)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/salud)**

### Recurso: Establecimientos de Salud

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
        <td>alfanumerico</td>
        <td>Debe ser un identificador único para la organización</td>
        <td>2222</td>
        <td>popolo:Organization</td>
        <td>Se puede utilizar una codificacion en base al presupuesto; ej: Código jurisdicccion:+código sub jurisdicción:+ ...</td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_nombre</td>
        <td>alfanumerico</td>
        <td>El nombre principal de la organización, por ejemplo su nombre legal</td>
        <td>Hospital Pirovano</td>
        <td>popolo:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_clasificacion</td>
        <td>alfanumerico</td>
        <td>La clasificación de la organización</td>
        <td>Hospital General</td>
        <td>popolo:Organization</td>
        <td>Indicar la especialidad del centro de salud</td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_padre_id</td>
        <td>alfanumerico</td>
        <td>Debe referenciar al id de la organización de la cual esta depende. Por ejemplo si es un sanatorio que depende de otra institución mayor</td>
        <td>0</td>
        <td>popolo:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_area</td>
        <td>alfanumerico</td>
        <td>Indica el área geografica donde se ubica la organizacion</td>
        <td>CABA, Republica Argentina</td>
        <td>popolo:Organization</td>
        <td>Se podría ampliar este campo a Provincia, Localidad o Codigo Postal</td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_fecha_creacion</td>
        <td>fecha</td>
        <td>Fecha en que fue creada la organización</td>
        <td>1896-07-12</td>
        <td>popolo:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_imagen</td>
        <td>uri</td>
        <td></td>
        <td></td>
        <td>popolo:Organization</td>
        <td>URL a logo o imagen que identifica a la organización</td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_contactos</td>
        <td>alfanumerico</td>
        <td>Mecanismos de contacto con las institución</td>
        <td>contacto@hospitalpirovano.org</td>
        <td>popolo:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_direccion</td>
        <td>uri</td>
        <td></td>
        <td>Av. Monroe 3555</td>
        <td>popolo:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_enlaces</td>
        <td>alfanumerico</td>
        <td>URL a la pagina web del centro educativo</td>
        <td>https://www.buenosaires.gob.ar/hospitalpirovano</td>
        <td>schema:PostalAddress</td>
        <td>Calle, Nro utilizar combinado con organizacion_area</td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_latitud</td>
        <td>numerico</td>
        <td>Telefono del centro educativo</td>
        <td></td>
        <td>schema:GeoCoordinates</td>
        <td>Opcional</td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_longitud</td>
        <td>numerico</td>
        <td>Correo electronico institucional del establecimiento</td>
        <td></td>
        <td>schema:GeoCoordinates</td>
        <td>Opcional</td>
    </tr>
        
</table>
### Recurso: Estadísticas de Salud

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
        <td>Indicador de Salud</td>
        <td>indicador_anio</td>
        <td>numerico</td>
        <td>Año en el cual se registra el indicador</td>
        <td>2018</td>
        <td>schema:Date</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Indicador de Salud</td>
        <td>indicador_organizacion_id</td>
        <td>alfanumérico</td>
        <td>Identificación del establecimiento de salud</td>
        <td>2222</td>
        <td>popolo:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Indicador de Salud</td>
        <td>indicador_nombre</td>
        <td>alfanumérico</td>
        <td>Identificación del indicador</td>
        <td>Cantidad de camas</td>
        <td>schema:QuantitativeValueDistribution</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Indicador de Salud</td>
        <td>indicador_descripcion</td>
        <td>texto</td>
        <td>Descripción de indicador, se puede complementar con información sobre como se relevan los datos.</td>
        <td>Cantidad de camas cada 1000 personas</td>
        <td>schema:QuantitativeValueDistribution</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Indicador de Salud</td>
        <td>indicador_periodicidad</td>
        <td>alfanumérico</td>
        <td>Cada cuanto tiempo se releva el indicador</td>
        <td>Anual</td>
        <td>schema:QuantitativeValueDistribution</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Indicador de Salud</td>
        <td>indicador_ultima_medicion</td>
        <td>fecha</td>
        <td>Ultima fecha en que se obtuvo el indicador</td>
        <td>2018-12-31</td>
        <td>schema:Date</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Indicador de Salud</td>
        <td>indicador_unidad_medida</td>
        <td>alfanumérico</td>
        <td>Unidad de medida</td>
        <td>Cantidad de camas</td>
        <td>schema:QuantitativeValueDistribution</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Indicador de Salud</td>
        <td>indicador_valor</td>
        <td>numerico</td>
        <td>Valor en numeros del indicador</td>
        <td>5</td>
        <td>schema:QuantitativeValueDistribution</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Indicador de Salud</td>
        <td>indicador_forma_calculo</td>
        <td>alfanumérico</td>
        <td>Especificar como se calcula el indicador, si se calcula en base a datos de otras fuentes.</td>
        <td>Se calcula la cantidad de camas disponibles de acuerdo a la cantidad de afiliados y se pondera el resultado para llevarlo a un valor equivalente sobre una poblacion de 1000 personas.</td>
        <td>schema:QuantitativeValueDistribution</td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
