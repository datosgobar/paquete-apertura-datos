# Denuncias

Mecanismos de presentación directa de solicitudes o denuncias a disposición del público en relación a acciones u omisiones del sujeto obligado.

* **Tema**: Gobierno y sector público
* **Estándar referencia**: https://schema.org/
* **Formatos**: JSON, XML, CSV
* **Ejemplo:**: http://www.popoloproject.com/examples/person.json

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Denuncias 
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/denuncias/denuncias.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/denuncias/denuncias.xlsx)**

<table>
    <tr>
        <th>organizacion_id</th>
        <th>organizacion_nombre</th>
        <th>denunciante_id</th>
        <th>denunciante_id_tipo</th>
        <th>denunciante_nombre</th>
        <th>denunciante_genero</th>
        <th>denunciante_edad</th>
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
        <td>DNI</td>
        <td>Lucía Sánchez</td>
        <td>Femenino</td>
        <td>26</td>
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

## Clases



Descargar clases en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/denuncias/denuncias-clases.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/denuncias/denuncias-clases.xlsx)**


<table>
    <tr>
        <th>nombre</th>
        <th>descripcion</th>
    </tr>

    <tr>
        <td>Persona</td>
        <td>Atributos de la persona física que realiza la denuncia.</td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>Atributos de una organización a la cual o donde se realiza la denuncia.</td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>Atributos de la denuncia realizada por la persona en la organización.</td>
    </tr>
        
</table>

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/denuncias/denuncias-campos.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/denuncias/denuncias-campos.xlsx)**

### Recurso: Denuncias 

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
        <td>El nombre principal de la organización, por ejemplo su nombre legal.</td>
        <td>Municipio de Bahia Blanca</td>
        <td>popolo:Organization
 schema:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>denunciante_id</td>
        <td>alfanumerico</td>
        <td>Identificador de la persona que denuncia.</td>
        <td>23668249</td>
        <td>popolo:Person
 schema:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>denunciante_id_tipo</td>
        <td>alfanumerico</td>
        <td>Tipo de identificación de la persona que denuncia.</td>
        <td>DNI</td>
        <td></td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>denunciante_nombre</td>
        <td>alfanumerico</td>
        <td>Nombre completo del denunciante.</td>
        <td>Lucía Sánchez</td>
        <td>popolo:Person
 schema:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>denunciante_genero</td>
        <td>alfanumerico</td>
        <td>Género según el cual se identifica la persona declarado según la normativa vigente para la presentación de declaraciones juradas en el país.</td>
        <td>Femenino</td>
        <td>popolo:Person
 schema:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>denunciante_edad</td>
        <td>numerico</td>
        <td>Edad al momento de la denuncia.</td>
        <td>26</td>
        <td>popolo:Person
 schema:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_id</td>
        <td>alfanumerico</td>
        <td>Identificador de la denuncia realizada.</td>
        <td>3384556</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_fecha</td>
        <td>fecha</td>
        <td>Fecha de la denuncia.</td>
        <td>2019-03-12</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_hora</td>
        <td>fecha</td>
        <td>Hora de la denuncia.</td>
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
        <td>Dirección donde sucedió el hecho denunciado.</td>
        <td>Alsina 1600</td>
        <td>schema:PostalAddress</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_latitud</td>
        <td>numerico</td>
        <td>Latitud donde sucedió el hecho denunciado.</td>
        <td>-38.705048</td>
        <td>schema:GeoCoordinates</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_longitud</td>
        <td>numerico</td>
        <td>Longitud donde sucedió el hecho denunciado.</td>
        <td>-62.250596</td>
        <td>schema:GeoCoordinates</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_detalle</td>
        <td>texto</td>
        <td>Detalle brindado por el denunciante al realizar la denuncia.</td>
        <td>Cable se encuentra colgando desde la columna de alumbrado.</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_categoria</td>
        <td>alfanumerico</td>
        <td>Categoría o clasificación del hecho denunciado.</td>
        <td>Alumbrado</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_tipo</td>
        <td>alfanumerico</td>
        <td>Tipo de denuncia (esto es una clasificación más específica que "categoría").</td>
        <td>Cable Suelto</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_subtipo</td>
        <td>alfanumerico</td>
        <td>Subtipo de denuncia (esto es una clasificación más específica que "tipo", si aplica).</td>
        <td></td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_otra_clasificacion</td>
        <td>alfanumerico</td>
        <td>Categoría o clasificación alternativa del hecho denunciado.</td>
        <td></td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_fecha_ultimo_cambio</td>
        <td>fecha</td>
        <td>Fecha de la última modificación que sufrió la denuncia.</td>
        <td>2019-03-15</td>
        <td>schema:Date</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Denuncia</td>
        <td>denuncia_comentario_ultimo_cambio</td>
        <td>texto</td>
        <td>Comentario agregado a la denuncia en el último cambio.</td>
        <td>Se envió equipo a reparar el cable</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
