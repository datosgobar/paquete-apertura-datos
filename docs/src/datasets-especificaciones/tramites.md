# Trámites

Un índice de trámites y procedimientos que se realicen ante el organismo, así como los requisitos y criterios de asignación para acceder a las prestaciones.

* **Tema**: Gobierno y sector público
* **Estándar referencia**: https://schema.org/
* **Formatos**: JSON, XML, CSV

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Trámites  
**[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/tramites/tramites.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/tramites/tramites.xlsx)**

<table>
    <tr>
        <th>organizacion_id</th>
        <th>organizacion_nombre</th>
        <th>tramite_id</th>
        <th>tramite_nombre</th>
        <th>tramite_descripcion</th>
        <th>tramite_area_depende</th>
        <th>tramite_dias_semana</th>
        <th>tramite_hora inicio</th>
        <th>tramite_hora_fin</th>
        <th>tramite_prerequisitos</th>
        <th>tramite_costo</th>
        <th>tramite_area_direccion</th>
        <th>tramite_web</th>
    </tr>

    <tr>
        <td>325</td>
        <td>Municipio de Bahia Blanca</td>
        <td>76</td>
        <td>Licencia Original</td>
        <td>Si tramitás por primera vez una licencia, o se te venció hace más de 90 días, tenés que hacer el siguiente trámite.</td>
        <td>Dirección de Tránsito y Transporte,</td>
        <td>Lunes a Viernes</td>
        <td>7:45</td>
        <td>16:00</td>
        <td>Sacar turno para el Curso de Seguridad Vial ingresando a “Capacitación”. Solo principiantes o quienes tengan licencias vencidas hace más de 5 años. (Ingresar a Turnos de Licencia). Sacar turno para iniciar el trámite ingresando a “Solicitar Turno”. (Ingresar a Turnos de Licencia) Documento de Identidad: original y copia, con domicilio en el partido de Bahía Blanca. En caso de no tener el DNI, presentar constancia de DNI en trámite, con todos los datos, incluso el domicilio. Menores de 18 años: Deben tener autorización de padre y madre, o tutor, certificada por un Juez de Paz o un Escribano Público. Si alguno de los padres hubiera fallecido, hay que adjuntar el Certificado o partida de defunción, y la Partida de nacimiento o Libreta de Familia. El siguiente formulario debe completarse por duplicado. (Descargar formulario) Las fotos se toman en la Dirección General de Tránsito y Transporte al momento de presentación para sacar la licencia. Presentar la constancia de grupo sanguíneo, la cual podrá ser emitida por hospital público, o por un laboratorio privado. Abonar los sellados correspondientes. Licencias de clase C,D y E: El solicitante debe tener entre 21 y 65 años y un año de antigüedad con licencia clase B. en este caso se debe presentar un audiometría actualizada y certificado de antecedentes penales.</td>
        <td>1364</td>
        <td>Undiano 1165</td>
        <td>https://www.bahia.gob.ar/tramites/conducir/original/</td>
    </tr>
        
</table>

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases



Descargar clases en **[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/tramites-clases.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/tramites-clases.xlsx)**


<table>
    <tr>
        <th>nombre</th>
        <th>descripcion</th>
    </tr>

    <tr>
        <td>Organización</td>
        <td>Atributos de la organización que presta el servicio.</td>
    </tr>
        
    <tr>
        <td>Trámite</td>
        <td>Atributos del trámite disponible en la organización.</td>
    </tr>
        
</table>

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/tramites-campos.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/tramites-campos.xlsx)**

### Recurso: Trámites  

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
        <td>Trámite</td>
        <td>tramite_id</td>
        <td>alfanumerico</td>
        <td>Un identificador único para el trámite</td>
        <td>76</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Trámite</td>
        <td>tramite_nombre</td>
        <td>alfanumerico</td>
        <td>Nombre del trámite</td>
        <td>Licencia Original</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Trámite</td>
        <td>tramite_descripcion</td>
        <td>texto</td>
        <td>Descripción del trámite</td>
        <td>Si tramitás por primera vez una licencia, o se te venció hace más de 90 días, tenés que hacer el siguiente trámite.</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Trámite</td>
        <td>tramite_area_depende</td>
        <td>alfanumerico</td>
        <td>Nombre del área de quien depende el trámite</td>
        <td>Dirección de Tránsito y Transporte,</td>
        <td>popolo:Organization
 schema:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Trámite</td>
        <td>tramite_dias_semana</td>
        <td>alfanumerico</td>
        <td>Dias de la semana en que se puede realizar el tramite</td>
        <td>Lunes a Viernes</td>
        <td>schema:OpeningHours</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Trámite</td>
        <td>tramite_hora inicio</td>
        <td>hora</td>
        <td>Hora de inicio de atencion</td>
        <td>7:45</td>
        <td>schema:OpeningHours</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Trámite</td>
        <td>tramite_hora_fin</td>
        <td>hora</td>
        <td>Hora de cierre de atención</td>
        <td>16:00</td>
        <td>schema:OpeningHours</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Trámite</td>
        <td>tramite_prerequisitos</td>
        <td>texto</td>
        <td>Detalle de prerequisitos para realizar el trámite</td>
        <td>Sacar turno para el Curso de Seguridad Vial ingresando a “Capacitación”. Solo principiantes o quienes tengan licencias vencidas hace más de 5 años. (Ingresar a Turnos de Licencia). Sacar turno para iniciar el trámite ingresando a “Solicitar Turno”. (Ingresar a Turnos de Licencia) Documento de Identidad: original y copia, con domicilio en el partido de Bahía Blanca. En caso de no tener el DNI, presentar constancia de DNI en trámite, con todos los datos, incluso el domicilio. Menores de 18 años: Deben tener autorización de padre y madre, o tutor, certificada por un Juez de Paz o un Escribano Público. Si alguno de los padres hubiera fallecido, hay que adjuntar el Certificado o partida de defunción, y la Partida de nacimiento o Libreta de Familia. El siguiente formulario debe completarse por duplicado. (Descargar formulario) Las fotos se toman en la Dirección General de Tránsito y Transporte al momento de presentación para sacar la licencia. Presentar la constancia de grupo sanguíneo, la cual podrá ser emitida por hospital público, o por un laboratorio privado. Abonar los sellados correspondientes. Licencias de clase C,D y E: El solicitante debe tener entre 21 y 65 años y un año de antigüedad con licencia clase B. en este caso se debe presentar un audiometría actualizada y certificado de antecedentes penales.</td>
        <td>schema:Thing:description</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Trámite</td>
        <td>tramite_costo</td>
        <td>texto</td>
        <td>Detalles sobre el costo del tramite</td>
        <td>1364</td>
        <td>schema:QuantitativeValue</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Trámite</td>
        <td>tramite_area_direccion</td>
        <td>alfanumerico</td>
        <td>Dirección dónde se puede iniciar o consultar el trámite en persona</td>
        <td>Undiano 1165</td>
        <td>popolo:Organization
 schema:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Trámite</td>
        <td>tramite_web</td>
        <td>URI</td>
        <td>URL al sitio web dónde se puede iniciar y/o dar seguimiento al tramite</td>
        <td>https://www.bahia.gob.ar/tramites/conducir/original/</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
