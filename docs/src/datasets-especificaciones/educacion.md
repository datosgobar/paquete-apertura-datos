# Estadísticas de Educación

Estadísticas de educación, cantidad de alumnos por aula (grado e institución), por sexo, por edad. Si se tiene estadísticas de notas de los alumnos.

* **Tema**: Educación, cultura y deportes
* **Formatos**: JSON, CSV

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Establecimientos Educativos
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/educacion)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/educacion)**

<table>
    <tr>
        <th>establecimiento_id</th>
        <th>establecimiento_nombre</th>
        <th>establecimiento_numero</th>
        <th>establecimiento_direccion</th>
        <th>establecimiento_localidad_id</th>
        <th>establecimiento_localidad_nombre</th>
        <th>establecimiento_departamento_id</th>
        <th>establecimiento_departamento_nombre</th>
        <th>establecimiento_provincia_id</th>
        <th>establecimiento_provincia_nombre</th>
        <th>establecimiento_latitud</th>
        <th>establecimiento_longitud</th>
        <th>establecimiento_codigo_postal</th>
        <th>establecimiento_url</th>
        <th>establecimiento_telefono</th>
        <th>establecimiento_email</th>
    </tr>

    <tr>
        <td>322255</td>
        <td>Bandera Argentina</td>
        <td>25</td>
        <td>Letonia esq. Combate de Costa Brava</td>
        <td>82007020000</td>
        <td>Boquet</td>
        <td>82007</td>
        <td>Belgrano</td>
        <td>82</td>
        <td>Santa Fe</td>
        <td>-34.9059072</td>
        <td>-58.3830589</td>
        <td>C1416</td>
        <td>http://esc25de1.blogspot.com/</td>
        <td>+541143127793</td>
        <td>mi-escuela@educacion.gob.ar</td>
    </tr>
        
</table>
### Recurso: Rendimiento de los Estudiantes
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/educacion)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/educacion)**

<table>
    <tr>
        <th>estudiante_id</th>
        <th>estudiante_sexo</th>
        <th>estudiante_fecha_nacimiento</th>
        <th>rendimiento_anio</th>
        <th>establecimiento_id</th>
        <th>curso_id</th>
        <th>curso_nombre</th>
        <th>clase_id</th>
        <th>rendimiento_asistencias</th>
        <th>rendimiento_faltas</th>
        <th>rendimiento_calificacion</th>
    </tr>

    <tr>
        <td>256326</td>
        <td>Mujer</td>
        <td>2012-03</td>
        <td>2018</td>
        <td>322255</td>
        <td>3A</td>
        <td>3er año primaria</td>
        <td></td>
        <td>230</td>
        <td>20</td>
        <td>8</td>
    </tr>
        
</table>

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases

Un `Estudiante` concurre a un `Establecimiento` para desarrollar actividades formativas que realiza con un determinado `Rendimiento` como resultado.

Descargar clases en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/educacion)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/educacion)**


<table>
    <tr>
        <th>nombre</th>
        <th>descripcion</th>
    </tr>

    <tr>
        <td>Establecimiento</td>
        <td>Atributos de un establecimiento educativo donde concurren estudiantes como parte de su formación académica principal.</td>
    </tr>
        
    <tr>
        <td>Estudiante</td>
        <td>Atributos de una persona física que concurre a un establecimiento educativo a los fines de desarrollar actividades académicas o de aprendizaje.</td>
    </tr>
        
    <tr>
        <td>Rendimiento</td>
        <td>Atributos del resultado o rendimiento de un estudiante dentro de una unidad académica, curso o segmento educativo determinado.</td>
    </tr>
        
</table>

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/educacion)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/educacion)**

### Recurso: Establecimientos Educativos

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
        <td>Establecimiento</td>
        <td>establecimiento_id</td>
        <td>alfanumérico</td>
        <td>Identificación del establecimiento educativo.</td>
        <td>322255</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Establecimiento</td>
        <td>establecimiento_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre principal u oficial del establecimiento educativo en caso de que lo tenga.</td>
        <td>Bandera Argentina</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Establecimiento</td>
        <td>establecimiento_numero</td>
        <td>numérico</td>
        <td>Numero del establecimiento educativo en caso de que tenga.</td>
        <td>25</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Establecimiento</td>
        <td>establecimiento_direccion</td>
        <td>alfanumérico</td>
        <td>Dirección del establecimiento.</td>
        <td>Letonia esq. Combate de Costa Brava</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Establecimiento</td>
        <td>establecimiento_localidad_id</td>
        <td>alfanumérico</td>
        <td>Identificador oficial de la localidad del establecimiento.</td>
        <td>82007020000</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Establecimiento</td>
        <td>establecimiento_localidad_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre oficial de la localidad del establecimiento.</td>
        <td>Boquet</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Establecimiento</td>
        <td>establecimiento_departamento_id</td>
        <td>alfanumérico</td>
        <td>Identificador oficial del departamento del establecimiento.</td>
        <td>82007</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Establecimiento</td>
        <td>establecimiento_departamento_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre oficial del departamento del establecimiento.</td>
        <td>Belgrano</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Establecimiento</td>
        <td>establecimiento_provincia_id</td>
        <td>alfanumérico</td>
        <td>Identificador oficial de la provincia del establecimiento.</td>
        <td>82</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Establecimiento</td>
        <td>establecimiento_provincia_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre oficial de la provincia del establecimiento.</td>
        <td>Santa Fe</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Establecimiento</td>
        <td>establecimiento_latitud</td>
        <td>numérico</td>
        <td>Latitud del establecimiento como número decimal (EPSG: 4326).</td>
        <td>-34.9059072</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Establecimiento</td>
        <td>establecimiento_longitud</td>
        <td>numérico</td>
        <td>Longitud del establecimiento como número decimal (EPSG: 4326).</td>
        <td>-58.3830589</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Establecimiento</td>
        <td>establecimiento_codigo_postal</td>
        <td>alfanumérico</td>
        <td>Código postal del establecimiento.</td>
        <td>C1416</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Establecimiento</td>
        <td>establecimiento_url</td>
        <td>alfanumérico</td>
        <td>URL a la pagina web del centro educativo</td>
        <td>http://esc25de1.blogspot.com/</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Establecimiento</td>
        <td>establecimiento_telefono</td>
        <td>alfanumérico</td>
        <td>Telefono del centro educativo</td>
        <td>+541143127793</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Establecimiento</td>
        <td>establecimiento_email</td>
        <td>alfanumérico</td>
        <td>Correo electronico institucional del establecimiento</td>
        <td>mi-escuela@educacion.gob.ar</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
</table>
### Recurso: Rendimiento de los Estudiantes

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
        <td>Estudiante</td>
        <td>estudiante_id</td>
        <td>alfanumérico</td>
        <td>Identificación única del estudiante. Esta es una identificación interna del sistema de registro, anónima, no pudiendo ser su DNI o similar, protegida para impedir la asociación no autorizada a datos personales identificatorios del estudiante.</td>
        <td>256326</td>
        <td>CEDS:K12Student</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estudiante</td>
        <td>estudiante_sexo</td>
        <td>alfanumérico</td>
        <td>Sexo biológico del estudiante ("Hombre", "Mujer" o "No especificado").</td>
        <td>Mujer</td>
        <td>CEDS:K12Student</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estudiante</td>
        <td>estudiante_fecha_nacimiento</td>
        <td>alfanumérico</td>
        <td>Fecha de nacimiento (ISO 8601). Con el objeto de proteger la anonimización de los datos se recomienda tomar solamente mes y año.</td>
        <td>2012-03</td>
        <td>CEDS:K12Student</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Rendimiento</td>
        <td>rendimiento_anio</td>
        <td>alfanumérico</td>
        <td>Año en el cual se registra el rendimiento del alumno.</td>
        <td>2018</td>
        <td>CEDS:Course</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Rendimiento</td>
        <td>establecimiento_id</td>
        <td>alfanumérico</td>
        <td>Identificación del establecimiento.</td>
        <td>322255</td>
        <td>CEDS:K12Course</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Rendimiento</td>
        <td>curso_id</td>
        <td>alfanumérico</td>
        <td>Identificación del curso. Este dato es opcional: en el caso de que posibilite la identificación de alumnos se debe evitar.</td>
        <td>3A</td>
        <td>CEDS:K12Course</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Rendimiento</td>
        <td>curso_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre del curso. Este dato es opcional: en el caso de que posibilite la identificación de alumnos se debe evitar.</td>
        <td>3er año primaria</td>
        <td>CEDS:K12Course</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Rendimiento</td>
        <td>clase_id</td>
        <td>alfanumérico</td>
        <td>Identificación de la clase, aplica a niveles secundarios y superiores. Este dato es opcional: en el caso de que posibilite la identificación de alumnos se debe evitar.</td>
        <td></td>
        <td>CEDS:K12Course</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Rendimiento</td>
        <td>rendimiento_asistencias</td>
        <td>alfanumérico</td>
        <td>Cantidad de asistencias en el año del estudiante.</td>
        <td>230</td>
        <td>CEDS:K12Attendance</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Rendimiento</td>
        <td>rendimiento_faltas</td>
        <td>alfanumérico</td>
        <td>Cantidad de faltas en el año del estudiante.</td>
        <td>20</td>
        <td>CEDS:K12Attendance</td>
        <td>El estandar establece el campo créditos</td>
    </tr>
        
    <tr>
        <td>Rendimiento</td>
        <td>rendimiento_calificacion</td>
        <td>alfanumérico</td>
        <td>Calificación obtenida por el estudiante al finalizar el año.</td>
        <td>8</td>
        <td>CEDS:K12Attendance</td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
