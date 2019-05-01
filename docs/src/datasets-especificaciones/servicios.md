# Servicios

Los servicios que brinda el organismo directamente al público, incluyendo normas, cartas y protocolos de atención al cliente.

* **Tema**: Gobierno y sector público
* **Estándar referencia**: https://schema.org/
* **Formatos**: JSON, XML, CSV

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Servicio  
**[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/servicios/servicio.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/servicios/servicio.xlsx)**

<table>
    <tr>
        <th>organizacion_id</th>
        <th>organizacion_nombre</th>
        <th>servicio_id</th>
        <th>servicio_nombre</th>
        <th>servicio_proveedor</th>
        <th>servicio_contacto</th>
        <th>servicio_descripcion</th>
        <th>servicio_fecha_inicio</th>
        <th>servicio_fecha_fin</th>
        <th>servicio_dias_semana</th>
        <th>servicio_hora inicio</th>
        <th>servicio_hora_fin</th>
        <th>servicio_costo</th>
        <th>servicio_enlace</th>
        <th>servicio_enlace_descripcion</th>
        <th>servicio_tramite_inicio_id</th>
        <th>servicio_tramite_nombre</th>
    </tr>

    <tr>
        <td>325</td>
        <td>Municipio de Bahia Blanca</td>
        <td></td>
        <td>Poda</td>
        <td>Arbolado urbano</td>
        <td>Parque de Mayo s/n - 2914880350</td>
        <td>Los vecinos deben solicitar al municipio autorización para podar o extraer un árbol. Para ello, ingresando al Centro de Atención al Vecino en la web del Municipio de Bahía Blanca, el vecino puede solicitar un turno para la realización del trabajo, justificando los motivos de la solicitud (interferencia peatonal, interferencia vehicular, interferencia con luminarias o carteles, riesgo de caída de ramas, etc.), indicando, además, la dirección de referencia para intervención, las observaciones que quiera formular e, incluso, puede adjuntar una foto del árbol a intervenir.</td>
        <td>2019-03-01</td>
        <td>2019-09-30</td>
        <td>Lunes a Viernes</td>
        <td>8:00</td>
        <td>17:00</td>
        <td>Sin costo</td>
        <td>https://www.bahia.gob.ar/arbolado/poda/</td>
        <td>https://www.bahia.gob.ar/arbolado/poda/</td>
        <td>333</td>
        <td>Poda de árbol, extracción de árbol o corte de raíz.</td>
    </tr>
        
</table>

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/servicios-campos.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/servicios-campos.xlsx)**

### Recurso: Servicio  

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
        <td>Debe ser un identificador único para la organización. Se puede utilizar una codificacion en base al presupuesto; ej: Código jurisdicccion:+código sub jurisdicción:+ ...</td>
        <td>325</td>
        <td>popolo:Organization
 schema:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_nombre</td>
        <td>alfanumerico</td>
        <td>El nombre principal de la organización, por ejemplo su nombre legal</td>
        <td>Municipio de Bahia Blanca</td>
        <td>popolo:Organization
 schema:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Servicio</td>
        <td>servicio_id</td>
        <td>alfanumerico</td>
        <td>Identificador del servicio</td>
        <td></td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Servicio</td>
        <td>servicio_nombre</td>
        <td>alfanumerico</td>
        <td>Nombre del servicio</td>
        <td>Poda</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Servicio</td>
        <td>servicio_proveedor</td>
        <td>alfanumerico</td>
        <td>Area que brinda el servicio dentro de la organización</td>
        <td>Arbolado urbano</td>
        <td>schema:Service</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Servicio</td>
        <td>servicio_contacto</td>
        <td>alfanumerico</td>
        <td>Punto de contacto del area que brinda el servicio dentro de la organización</td>
        <td>Parque de Mayo s/n - 2914880350</td>
        <td>schema:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Servicio</td>
        <td>servicio_descripcion</td>
        <td>texto</td>
        <td>Descripción del servicio</td>
        <td>Los vecinos deben solicitar al municipio autorización para podar o extraer un árbol. Para ello, ingresando al Centro de Atención al Vecino en la web del Municipio de Bahía Blanca, el vecino puede solicitar un turno para la realización del trabajo, justificando los motivos de la solicitud (interferencia peatonal, interferencia vehicular, interferencia con luminarias o carteles, riesgo de caída de ramas, etc.), indicando, además, la dirección de referencia para intervención, las observaciones que quiera formular e, incluso, puede adjuntar una foto del árbol a intervenir.</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Servicio</td>
        <td>servicio_fecha_inicio</td>
        <td>fecha</td>
        <td>Fecha de inicio servicio</td>
        <td>2019-03-01</td>
        <td>schema:Demand:availabilityStarts</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Servicio</td>
        <td>servicio_fecha_fin</td>
        <td>fecha</td>
        <td>Fecha de fin del servicio</td>
        <td>2019-09-30</td>
        <td>schema:Demand:availabilityEnds</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Servicio</td>
        <td>servicio_dias_semana</td>
        <td>alfanumerico</td>
        <td>Dias de la semana en que se brinda el servicio</td>
        <td>Lunes a Viernes</td>
        <td>schema:OpeningHours</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Servicio</td>
        <td>servicio_hora inicio</td>
        <td>hora</td>
        <td></td>
        <td>8:00</td>
        <td>schema:OpeningHours</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Servicio</td>
        <td>servicio_hora_fin</td>
        <td>hora</td>
        <td></td>
        <td>17:00</td>
        <td>schema:OpeningHours</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Servicio</td>
        <td>servicio_costo</td>
        <td>alfanumerico</td>
        <td>Costo asociado al servicio</td>
        <td>Sin costo</td>
        <td>schema:QuantitativeValue</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Servicio</td>
        <td>servicio_enlace</td>
        <td>URI</td>
        <td>URL a sitio web con información adicional o dónde se puede solicitar el servicio</td>
        <td>https://www.bahia.gob.ar/arbolado/poda/</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Servicio</td>
        <td>servicio_enlace_descripcion</td>
        <td>texto</td>
        <td>Descripción del contenido a obtener del enlace</td>
        <td>https://www.bahia.gob.ar/arbolado/poda/</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Servicio</td>
        <td>servicio_tramite_inicio_id</td>
        <td>alfanumerico</td>
        <td>Identificación del trámite que asociado al servicio</td>
        <td>333</td>
        <td>schema:Thing</td>
        <td>En caso de que el servicio requiera el inicio de un tramite se identifica el tramite relacionado</td>
    </tr>
        
    <tr>
        <td>Servicio</td>
        <td>servicio_tramite_nombre</td>
        <td>alfanumerico</td>
        <td></td>
        <td>Poda de árbol, extracción de árbol o corte de raíz.</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
