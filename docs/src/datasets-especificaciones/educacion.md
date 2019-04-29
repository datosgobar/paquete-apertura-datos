# Educación

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos
    
### Recurso: Establecimiento
**[CSV](educacion/establecimiento.csv)** | **[XLSX](educacion/establecimiento.xlsx)**

<table>
    <tr>
        <th>establecimiento_id</th>
        <th>establecimiento_nombre</th>
        <th>establecimiento_numero</th>
        <th>establecimiento_direccion</th>
        <th>establecimiento_ciudad</th>
        <th>establecimiento_zona</th>
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
        <td>Buenos Aires</td>
        <td>Retiro</td>
        <td>-34.9059072</td>
        <td>-58.3830589</td>
        <td>C1416</td>
        <td>http://esc25de1.blogspot.com/</td>
        <td>(54) 11 4312-7793</td>
        <td></td>
    </tr>
        
</table>
### Recurso: EstudianteRendimiento
**[CSV](educacion/estudianterendimiento.csv)** | **[XLSX](educacion/estudianterendimiento.xlsx)**

<table>
    <tr>
        <th>estudiante_id</th>
        <th>estudiante_genero</th>
        <th>estudiante_fecha_nacimiento</th>
        <th>estudiante_etnia_raza</th>
        <th>rendimiento_anio</th>
        <th>rendimiento_establecimiento_id</th>
        <th>rendimiento_curso_id</th>
        <th>rendimiento_curso_nombre</th>
        <th>rendimiento_clase_id</th>
        <th>rendimiento_asistencias</th>
        <th>rendimiento_faltas</th>
        <th>rendimiento_calificacion</th>
    </tr>

    <tr>
        <td>256326</td>
        <td>Mujer</td>
        <td>2012-03</td>
        <td>Caucasico</td>
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

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](educacion-campos.csv)** | **[XLSX](educacion-campos.xlsx)**

### Recurso: Establecimiento

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
        <td>Identificación del establecimiento educativo</td>
        <td>322255</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Establecimiento</td>
        <td>establecimiento_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre del establecimiento educativo en caso de que tenga</td>
        <td>Bandera Argentina</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Establecimiento</td>
        <td>establecimiento_numero</td>
        <td>numérico</td>
        <td>Numero del establecimiento educativo en caso de que tenga</td>
        <td>25</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Establecimiento</td>
        <td>establecimiento_direccion</td>
        <td>alfanumérico</td>
        <td>Dirección, numero de puerta</td>
        <td>Letonia esq. Combate de Costa Brava</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Establecimiento</td>
        <td>establecimiento_ciudad</td>
        <td>alfanumérico</td>
        <td>Ciudad del establecimiento</td>
        <td>Buenos Aires</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Establecimiento</td>
        <td>establecimiento_zona</td>
        <td>alfanumérico</td>
        <td>Provincia, Departamento</td>
        <td>Retiro</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Establecimiento</td>
        <td>establecimiento_latitud</td>
        <td>numérico</td>
        <td></td>
        <td>-34.9059072</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Establecimiento</td>
        <td>establecimiento_longitud</td>
        <td>numérico</td>
        <td></td>
        <td>-58.3830589</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Establecimiento</td>
        <td>establecimiento_codigo_postal</td>
        <td>alfanumérico</td>
        <td></td>
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
        <td>(54) 11 4312-7793</td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Establecimiento</td>
        <td>establecimiento_email</td>
        <td>alfanumérico</td>
        <td>Correo electronico institucional del establecimiento</td>
        <td></td>
        <td>CEDS:K12School</td>
        <td></td>
    </tr>
        
</table>
### Recurso: EstudianteRendimiento

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
        <td>Idenitficacion unica del estudiante, identificación interna del sistema de registro no pudiendo ser su DNI o similar</td>
        <td>256326</td>
        <td>CEDS:K12Student</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estudiante</td>
        <td>estudiante_genero</td>
        <td>alfanumérico</td>
        <td>Identificación de genero del estudiante o sexo</td>
        <td>Mujer</td>
        <td>CEDS:K12Student</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estudiante</td>
        <td>estudiante_fecha_nacimiento</td>
        <td>alfanumérico</td>
        <td>Fecha de nacimiento, con el objeto de anonimizar los datos se podría tomar solamente mes y año</td>
        <td>2012-03</td>
        <td>CEDS:K12Student</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estudiante</td>
        <td>estudiante_etnia_raza</td>
        <td>alfanumérico</td>
        <td>Ascendencia racial o etnica</td>
        <td>Caucasico</td>
        <td>CEDS:K12Student</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Rendimiento</td>
        <td>rendimiento_anio</td>
        <td>alfanumérico</td>
        <td>Año en el cual se registra el rendimiento del alumno</td>
        <td>2018</td>
        <td>CEDS:Course</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Rendimiento</td>
        <td>rendimiento_establecimiento_id</td>
        <td>alfanumérico</td>
        <td>Identificación del establecimiento</td>
        <td>322255</td>
        <td>CEDS:K12Course</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Rendimiento</td>
        <td>rendimiento_curso_id</td>
        <td>alfanumérico</td>
        <td>Idenitficación del curso, este dato es opcional en el caso de que posibilite la identificación de alumnos se debe evitar</td>
        <td>3A</td>
        <td>CEDS:K12Course</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Rendimiento</td>
        <td>rendimiento_curso_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre del curso</td>
        <td>3er año primaria</td>
        <td>CEDS:K12Course</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Rendimiento</td>
        <td>rendimiento_clase_id</td>
        <td>alfanumérico</td>
        <td>Identificación de la clase, aplica a niveles secundarios y superiores, este dato es opcional en el caso de que posibilite la identificación de alumnos se debe evitar</td>
        <td></td>
        <td>CEDS:K12Course</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Rendimiento</td>
        <td>rendimiento_asistencias</td>
        <td>alfanumérico</td>
        <td>Cantidad de asistencias en el año del estudiante</td>
        <td>230</td>
        <td>CEDS:K12Attendance</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Rendimiento</td>
        <td>rendimiento_faltas</td>
        <td>alfanumérico</td>
        <td>Cantidad de faltas en el año del estudiante</td>
        <td>20</td>
        <td>CEDS:K12Attendance</td>
        <td>El estandar establece el campo créditos</td>
    </tr>
        
    <tr>
        <td>Rendimiento</td>
        <td>rendimiento_calificacion</td>
        <td>alfanumérico</td>
        <td>Calificación obtenida por el estudiante al finalizar el año</td>
        <td>8</td>
        <td>CEDS:K12Attendance</td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
