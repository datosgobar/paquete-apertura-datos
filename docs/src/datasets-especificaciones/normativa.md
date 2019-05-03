# Normativa

Todas las leyes, decretos, resoluciones, ordenanzas, acordadas y estatutos estatutos municipales sancionados por el Honorable Concejo Deliberante.

* **Tema**: Justicia, seguridad y legales
* **Estándar referencia**: Akoma Ntoso
* **Formatos**: XML
* **Ejemplo:**: http://docs.oasis-open.org/legaldocml/akn-nc/v1.0/akn-nc-v1.0.html, http://docs.oasis-open.org/legaldocml/akn-core/v1.0/akn-core-v1.0-part2-specs.html

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Normas    
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/normativa/normas.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/normativa/normas.xlsx)**

<table>
    <tr>
        <th>norma_id</th>
        <th>norma_tipo</th>
        <th>norma_numero</th>
        <th>norma_nombre</th>
        <th>norma_organismo_origen</th>
        <th>norma_fecha_sancion</th>
        <th>norma_fecha_boletin</th>
        <th>norma_numero_boletin</th>
        <th>norma_pagina_boletin</th>
        <th>norma_texto_resumido</th>
        <th>norma_observaciones</th>
        <th>norma_url_original</th>
        <th>norma_url_texto_actual</th>
        <th>norma_modificada_por</th>
        <th>norma_modifica_a</th>
        <th>norma_region</th>
    </tr>

    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
        
</table>
### Recurso: Artículos 
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/normativa/articulos.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/normativa/articulos.xlsx)**

<table>
    <tr>
        <th>articulo_norma_id</th>
        <th>articulo_norma_fecha_sancion</th>
        <th>articulo_numero</th>
        <th>articulo_secuencia</th>
        <th>articulo_titulo</th>
        <th>articulo_texto</th>
        <th>articulo_notas</th>
    </tr>

    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases



Descargar clases en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/normativa/normativa-clases.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/normativa/normativa-clases.xlsx)**


<table>
    <tr>
        <th>nombre</th>
        <th>descripcion</th>
    </tr>

    <tr>
        <td>Norma</td>
        <td>Atributos de un elemento normativo (ley, decreto, disposición, etc).</td>
    </tr>
        
    <tr>
        <td>Artículo</td>
        <td>Atributos de un artículo perteneciente al cuerpo de un elemento normativo.</td>
    </tr>
        
</table>

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/normativa/normativa-campos.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/normativa/normativa-campos.xlsx)**

### Recurso: Normas    

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
        <td>Norma</td>
        <td>norma_id</td>
        <td>numérico</td>
        <td>Identificador único de la norma</td>
        <td></td>
        <td>akn:identification</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Norma</td>
        <td>norma_tipo</td>
        <td>alfanumérico</td>
        <td>Tipo de norma</td>
        <td></td>
        <td>akn:akomantosoType</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Norma</td>
        <td>norma_numero</td>
        <td>numérico</td>
        <td>Número asignado a la norma</td>
        <td></td>
        <td>akn:FRBRnumber</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Norma</td>
        <td>norma_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre o título resumido</td>
        <td></td>
        <td>akn:docTitle</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Norma</td>
        <td>norma_organismo_origen</td>
        <td>alfanumérico</td>
        <td>Nombre del organismo que la origina</td>
        <td></td>
        <td>akn:TLCorganization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Norma</td>
        <td>norma_fecha_sancion</td>
        <td>fecha</td>
        <td>Fecha en la que se sanciona la norma</td>
        <td></td>
        <td>akn:docDate</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Norma</td>
        <td>norma_fecha_boletin</td>
        <td>fecha</td>
        <td>Fecha de publicación en el boletón oficial</td>
        <td></td>
        <td>akn:docDate</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Norma</td>
        <td>norma_numero_boletin</td>
        <td>numérico</td>
        <td>Numero del boletín en el cual se publica la norma</td>
        <td></td>
        <td>akn:num</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Norma</td>
        <td>norma_pagina_boletin</td>
        <td>numérico</td>
        <td>Página del boletin en el cual se publica la norma</td>
        <td></td>
        <td>akn:num</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Norma</td>
        <td>norma_texto_resumido</td>
        <td>texto</td>
        <td>Resumen del texto de la norma para el boletín</td>
        <td></td>
        <td>akn:paragraph</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Norma</td>
        <td>norma_observaciones</td>
        <td>texto</td>
        <td>Texto con información adicional sobre la norma</td>
        <td></td>
        <td>akn:summary</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Norma</td>
        <td>norma_url_original</td>
        <td>url</td>
        <td>Enlace al texto original de la norma</td>
        <td></td>
        <td>akn:linkType</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Norma</td>
        <td>norma_url_texto_actual</td>
        <td>url</td>
        <td>Enlace al texto actual modificado de la norma</td>
        <td></td>
        <td>akn:linkType</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Norma</td>
        <td>norma_modificada_por</td>
        <td>numérico</td>
        <td>Identificador de la norma que modifica a esta</td>
        <td></td>
        <td>akn:overrules</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Norma</td>
        <td>norma_modifica_a</td>
        <td>numérico</td>
        <td>Identificador de la norma a la cual se modifica</td>
        <td></td>
        <td>akn:afectedDocument</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Norma</td>
        <td>norma_region</td>
        <td>alfanumérico</td>
        <td>Nombre de la provincia / ciudad donde se promulga la norma</td>
        <td></td>
        <td>akn:TLClocation</td>
        <td></td>
    </tr>
        
</table>
### Recurso: Artículos 

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
        <td>Articulo</td>
        <td>articulo_norma_id</td>
        <td>numérico</td>
        <td>Identificador único de la norma</td>
        <td></td>
        <td>akn:identification</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Articulo</td>
        <td>articulo_norma_fecha_sancion</td>
        <td>fecha</td>
        <td>Fecha en la que se sanciona la norma</td>
        <td></td>
        <td>akn:docDate</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Articulo</td>
        <td>articulo_numero</td>
        <td>numérico</td>
        <td>Numero del articulo</td>
        <td></td>
        <td>akn:FRBRnumber</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Articulo</td>
        <td>articulo_secuencia</td>
        <td>alfanumerico</td>
        <td>Secuencia del articulo</td>
        <td></td>
        <td>akn:num</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Articulo</td>
        <td>articulo_titulo</td>
        <td>alfanumerico</td>
        <td>Titulo del artículo</td>
        <td></td>
        <td>akn:docTitle</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Articulo</td>
        <td>articulo_texto</td>
        <td>texto</td>
        <td>Texto del artículo</td>
        <td></td>
        <td>akn:amendmentContent</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Articulo</td>
        <td>articulo_notas</td>
        <td>texto</td>
        <td>Notas del artículo</td>
        <td></td>
        <td>akn:summary</td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
