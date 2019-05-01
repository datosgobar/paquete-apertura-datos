# Denuncias

Mecanismos de presentación directa de solicitudes o denuncias a disposición del público en relación a acciones u omisiones del sujeto obligado.

* **Tema**: Gobierno y sector público
* **Estándar referencia**: https://schema.org/
* **Formatos**: JSON, XML, CSV
* **Ejemplo:**: http://www.popoloproject.com/examples/person.json

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos
    
### Recurso: Denuncia  
**[CSV](denuncias/denuncia.csv)** | **[XLSX](denuncias/denuncia.xlsx)**

<table>
    <tr>
        <th>organizacion_id</th>
        <th>organizacion_nombre</th>
        <th>denunciante_id</th>
        <th>denunciante_nombre</th>
        <th>denunciante_genero</th>
        <th>denunciante_edad</th>
        <th>denunciante_ascendencia</th>
        <th>denuncia_id</th>
        <th>denuncia_fecha</th>
        <th>denuncia_hora</th>
        <th>denuncia_medio</th>
        <th>denuncia_lugar_radicacion</th>
        <th>denuncia_enlace_seguimiento</th>
        <th>denuncia_estado_actual</th>
        <th>denuncia_direccion</th>
        <th>denuncia_latitud</th>
        <th>denuncia_longitud</th>
        <th>denuncia_detalle</th>
        <th>denuncia_categoria</th>
        <th>denuncia_tipo</th>
        <th>denuncia_subtipo</th>
        <th>denuncia_otra_clasificacion</th>
        <th>denuncia_fecha_ultimo_cambio</th>
        <th>denuncia_comentario_ultimo_cambio</th>
    </tr>

    <tr>
        <td>325</td>
        <td>Municipio de Bahia Blanca</td>
        <td>23668249</td>
        <td>Lucía Sánchez</td>
        <td>Femenino</td>
        <td>26</td>
        <td></td>
        <td>3384556</td>
        <td>2019-03-12</td>
        <td>14:45</td>
        <td>Página web</td>
        <td></td>
        <td>https://www.bahia.gob.ar/vecinos/</td>
        <td>Activo</td>
        <td>Alsina 1600</td>
        <td>-38.705048</td>
        <td>-62.250596</td>
        <td>Cable se encuentra colgando desde la columna de alumbrado.</td>
        <td>Alumbrado</td>
        <td>Cable Suelto</td>
        <td></td>
        <td></td>
        <td>2019-03-15</td>
        <td>Se envió equipo a reparar el cable</td>
    </tr>
        
</table>

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](denuncias-campos.csv)** | **[XLSX](denuncias-campos.xlsx)**

### Recurso: Denuncia  

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
        <td>alfanumerio</td>
        <td>El nombre principal de la organización, por ejemplo su nombre legal</td>
        <td>Municipio de Bahia Blanca</td>
        <td>popolo:Organization
 schema:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>denunciante_id</td>
        <td>alfanumerico</td>
        <td></td>
        <td>23668249</td>
        <td>popolo:Person
 schema:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>denunciante_nombre</td>
        <td>alfanumerico</td>
        <td></td>
        <td>Lucía Sánchez</td>
        <td>popolo:Person
 schema:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>denunciante_genero</td>
        <td>alfanumerico</td>
        <td></td>
        <td>Femenino</td>
        <td>popolo:Person
 schema:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>denunciante_edad</td>
        <td>numerico</td>
        <td></td>
        <td>26</td>
        <td>popolo:Person
 schema:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>denunciante_ascendencia</td>
        <td>alfanumerico</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_id</td>
        <td>alfanumerico</td>
        <td></td>
        <td>3384556</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_fecha</td>
        <td>fecha</td>
        <td></td>
        <td>2019-03-12</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_hora</td>
        <td>fecha</td>
        <td></td>
        <td>14:45</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_medio</td>
        <td>alfanumerico</td>
        <td>Indica de que forma fue realizada la denuncia</td>
        <td>Página web</td>
        <td></td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_lugar_radicacion</td>
        <td>alfanumerico</td>
        <td>Oficina o dependencia que recepciono la denuncia ya sea presencial, electrónica, telefónica u otro medio.</td>
        <td></td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_enlace_seguimiento</td>
        <td>url</td>
        <td>De existir un enlace para hacer seguimiento a la denuncia, opcional</td>
        <td>https://www.bahia.gob.ar/vecinos/</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_estado_actual</td>
        <td>alfanumerico</td>
        <td>Ultimo estado de la denuncia</td>
        <td>Activo</td>
        <td></td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_direccion</td>
        <td>alfanumerico</td>
        <td></td>
        <td>Alsina 1600</td>
        <td>schema:PostalAddress</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_latitud</td>
        <td>numerico</td>
        <td></td>
        <td>-38.705048</td>
        <td>schema:GeoCoordinates</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_longitud</td>
        <td>numerico</td>
        <td></td>
        <td>-62.250596</td>
        <td>schema:GeoCoordinates</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_detalle</td>
        <td>texto</td>
        <td>Detalle brindado por el denunciante al realizar la denuncia</td>
        <td>Cable se encuentra colgando desde la columna de alumbrado.</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_categoria</td>
        <td>alfanumerico</td>
        <td></td>
        <td>Alumbrado</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_tipo</td>
        <td>alfanumerico</td>
        <td></td>
        <td>Cable Suelto</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_subtipo</td>
        <td>alfanumerico</td>
        <td></td>
        <td></td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_otra_clasificacion</td>
        <td>alfanumerico</td>
        <td></td>
        <td></td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_fecha_ultimo_cambio</td>
        <td>fecha</td>
        <td></td>
        <td>2019-03-15</td>
        <td>schema:Date</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_comentario_ultimo_cambio</td>
        <td>texto</td>
        <td></td>
        <td>Se envió equipo a reparar el cable</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
