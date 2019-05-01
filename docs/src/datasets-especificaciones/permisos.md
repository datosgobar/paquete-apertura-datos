# Permisos

Los permisos, concesiones y autorizaciones otorgados y sus titulares.

* **Tema**: Gobierno y sector público
* **Estándar referencia**: https://schema.org/
* **Formatos**: CSV

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos
    
### Recurso: Permisos  
**[CSV](permisos/permisos.csv)** | **[XLSX](permisos/permisos.xlsx)**

<table>
    <tr>
        <th>entidad_id</th>
        <th>entidad_nombre</th>
        <th>permiso_id</th>
        <th>permiso_tipo</th>
        <th>permiso_subtipo</th>
        <th>permiso_inicio</th>
        <th>permiso_fin</th>
        <th>permiso_detalles</th>
        <th>permiso_area</th>
        <th>permiso_geo</th>
        <th>permiso_provincia</th>
        <th>permiso_localidad</th>
        <th>permiso_resolucion_enlace</th>
        <th>permiso_es_prorroga</th>
        <th>permiso_id_padre</th>
        <th>participacion_exacta</th>
    </tr>

    <tr>
        <td>CUIT</td>
        <td></td>
        <td></td>
        <td>Permiso/Concesión/Autorización</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>SI / NO</td>
        <td></td>
        <td>numero en porcentaje</td>
    </tr>
        
</table>

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](permisos-campos.csv)** | **[XLSX](permisos-campos.xlsx)**

### Recurso: Permisos  

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
        <td>Entidad (Organización, Empresa, etc)</td>
        <td>entidad_id</td>
        <td>alfanumerico</td>
        <td>Identificacion de la organización/empresa que obtiene el permiso</td>
        <td>CUIT</td>
        <td>popolo:Organization
 schema:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Entidad (Organización, Empresa, etc)</td>
        <td>entidad_nombre</td>
        <td>alfanumerico</td>
        <td>Nombre de la organización/empresa que tiene el permiso</td>
        <td></td>
        <td>popolo:Organization
 schema:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Permisos / Concesiones</td>
        <td>permiso_id</td>
        <td>alfanumerico</td>
        <td>Identificación del permiso</td>
        <td></td>
        <td>schema:GovernmentPermit</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Permisos / Concesiones</td>
        <td>permiso_tipo</td>
        <td>alfanumerico</td>
        <td>Tipo de permiso</td>
        <td>Permiso/Concesión/Autorización</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Permisos / Concesiones</td>
        <td>permiso_subtipo</td>
        <td>alfanumerico</td>
        <td>Otras clasificaciones</td>
        <td></td>
        <td>schema:Thing</td>
        <td>Categorizar dependiendo del tipo de permiso</td>
    </tr>
        
    <tr>
        <td>Permisos / Concesiones</td>
        <td>permiso_inicio</td>
        <td>fecha</td>
        <td>Fecha de inicio del permiso/concesión</td>
        <td></td>
        <td>schema:GovernmentPermit</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Permisos / Concesiones</td>
        <td>permiso_fin</td>
        <td>fecha</td>
        <td>Fecha de fin del permiso/concesión</td>
        <td></td>
        <td>schema:GovernmentPermit</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Permisos / Concesiones</td>
        <td>permiso_detalles</td>
        <td>texto</td>
        <td>Descripción al detalle del permiso/concesión</td>
        <td></td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Permisos / Concesiones</td>
        <td>permiso_area</td>
        <td>alfanumerico</td>
        <td>Area dónde se realiza la actividad</td>
        <td></td>
        <td>schema:Place</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Permisos / Concesiones</td>
        <td>permiso_geo</td>
        <td>geografico</td>
        <td>geoJson u otro formato de georeferenciación del área geográfica donde se realiza la actividad</td>
        <td></td>
        <td>schema:Place</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Permisos / Concesiones</td>
        <td>permiso_provincia</td>
        <td>alfanumerico</td>
        <td>Provincia dónde se realiza la actividad</td>
        <td></td>
        <td>schema:PostalAddress</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Permisos / Concesiones</td>
        <td>permiso_localidad</td>
        <td>alfanumerico</td>
        <td>Localidad dónde se realiza la actividad</td>
        <td></td>
        <td>schema:PostalAddress</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Permisos / Concesiones</td>
        <td>permiso_resolucion_enlace</td>
        <td>url</td>
        <td>Enlace a la resolución que otorga el permiso/concesión/autorización</td>
        <td></td>
        <td>schema:Permit</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Permisos / Concesiones</td>
        <td>permiso_es_prorroga</td>
        <td>booleano</td>
        <td>Indica si los datos corresponden a una prórroga o al permiso/concesión original</td>
        <td>SI / NO</td>
        <td></td>
        <td></td>
    </tr>
        
    <tr>
        <td>Permisos / Concesiones</td>
        <td>permiso_id_padre</td>
        <td>alfanumerico</td>
        <td>En caso de ser una prorroga, el Id de la concesión original</td>
        <td></td>
        <td>schema:GovernmentPermit</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Participacion</td>
        <td>participacion_exacta</td>
        <td>numerico</td>
        <td>Porcentaje exacto de la participación.</td>
        <td>numero en porcentaje</td>
        <td>BO:Share</td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
