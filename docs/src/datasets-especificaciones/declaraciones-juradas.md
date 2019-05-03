# Declaraciones Juradas

Declaración Jurada Patrimonial Integral de carácter público con su correspondiente relación a la Nómina de Funcionarios.

* **Tema**: Gobierno y sector público
* **Estándar referencia**: Organizaciones, Personas, Membership de Popolo extendiendo la última para agregar su declaración jurada http://www.popoloproject.com/specs y vCard
* **Formatos**: JSON, XML, CSV

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Declaración Personal
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/declaraciones-juradas/declaracion-personal.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/declaraciones-juradas/declaracion-personal.xlsx)**

<table>
    <tr>
        <th>declaracion_id</th>
        <th>declaracion_presentacion_fecha</th>
        <th>declaracion_descripcion</th>
        <th>persona_id</th>
        <th>persona_id_tipo</th>
        <th>persona_otro_id</th>
        <th>persona_otro_id_tipo</th>
        <th>persona_nombre</th>
        <th>persona_genero</th>
        <th>persona_fecha_nacimiento</th>
        <th>persona_nacionalidad</th>
        <th>persona_estado_civil</th>
        <th>persona_estudios</th>
        <th>persona_retiro_voluntario</th>
        <th>persona_sin_actividad</th>
        <th>persona_sin_actividad_desde</th>
        <th>persona_horas_por_semana</th>
        <th>persona_es_proveedor</th>
        <th>miembro_organizacion_id</th>
        <th>miembro_fecha_ingreso</th>
        <th>puesto_nombre</th>
        <th>puesto_rol</th>
        <th>organizacion_nombre</th>
        <th>organizacion_clasificacion</th>
    </tr>

    <tr>
        <td>2011889182</td>
        <td>08-02-2017</td>
        <td>Anual 2016 Rectificativa 1</td>
        <td>578379323</td>
        <td>DNI</td>
        <td>27173460711</td>
        <td>CUIL</td>
        <td>Juan Pérez</td>
        <td>Masculino</td>
        <td>1966-02-18</td>
        <td>Argentino</td>
        <td>Casado</td>
        <td>Universitario</td>
        <td>No</td>
        <td>No</td>
        <td></td>
        <td>40</td>
        <td>No</td>
        <td>2</td>
        <td>2002-31-08</td>
        <td>Jefe</td>
        <td>Jefe de Sección</td>
        <td>Ministerio de Modernización</td>
        <td>Poder Ejecutivo</td>
    </tr>
        
</table>
### Recurso: Declaración de Grupo Familiar
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/declaraciones-juradas/declaracion-grupo-familiar.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/declaraciones-juradas/declaracion-grupo-familiar.xlsx)**

<table>
    <tr>
        <th>declaracion_id</th>
        <th>persona_id</th>
        <th>persona_id_tipo</th>
        <th>persona_otro_id</th>
        <th>persona_otro_id_tipo</th>
        <th>persona_nombre</th>
        <th>persona_genero</th>
        <th>persona_fecha_nacimiento</th>
        <th>persona_nacionalidad</th>
        <th>persona_relacionado_con_id</th>
        <th>persona_relacionado_con_nombre</th>
        <th>persona_tipo_relacion</th>
    </tr>

    <tr>
        <td>2011889182</td>
        <td>579129534</td>
        <td>DNI</td>
        <td>27461236079</td>
        <td>CUIL</td>
        <td>Ana Pérez</td>
        <td>Femenino</td>
        <td>1966-02-18</td>
        <td>Argentina</td>
        <td>578379323</td>
        <td>Juan Pérez</td>
        <td>Hija</td>
    </tr>
        
</table>
### Recurso: Declaración de Bienes y deudas
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/declaraciones-juradas/declaracion-bienes-deudas.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/declaraciones-juradas/declaracion-bienes-deudas.xlsx)**

<table>
    <tr>
        <th>declaracion_id</th>
    </tr>

    <tr>
        <td>2011889182</td>
    </tr>
        
</table>
### Recurso: Declaración de Bienes y Deudas
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/declaraciones-juradas/declaracion-bienes-deudas.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/declaraciones-juradas/declaracion-bienes-deudas.xlsx)**

<table>
    <tr>
        <th>bienes_momento</th>
        <th>bienes_tipo</th>
        <th>bienes_descripcion</th>
        <th>bienes_origen_fondos</th>
        <th>bienes_porcentaje_titularidad</th>
        <th>bienes_moneda</th>
        <th>bienes_importe</th>
        <th>deudas_momento</th>
        <th>deudas_tipo</th>
        <th>deudas_descripcion</th>
        <th>deudas_clasificacion</th>
        <th>deudas_radicacion</th>
        <th>deudas_moneda</th>
        <th>deudas_importe</th>
    </tr>

    <tr>
        <td>Inicio del período</td>
        <td>Inmueble</td>
        <td>Apartamento de 300mts2</td>
        <td>Herencia</td>
        <td>100</td>
        <td>USD</td>
        <td>450000</td>
        <td>Inicio del período</td>
        <td>Común</td>
        <td>Kooj S.A. CUIT 31579842356</td>
        <td>Otras deudas</td>
        <td>Argentina</td>
        <td>USD</td>
        <td>25000</td>
    </tr>
        
</table>
### Recurso: Declaración de Postulaciones a Cargos Electivos
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/declaraciones-juradas/declaracion-postulaciones-cargos-electivos.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/declaraciones-juradas/declaracion-postulaciones-cargos-electivos.xlsx)**

<table>
    <tr>
        <th>declaracion_id</th>
        <th>postulacion_descripcion</th>
    </tr>

    <tr>
        <td>2011889182</td>
        <td>Diputado periodo 2013 - 2017</td>
    </tr>
        
</table>
### Recurso: Declaración de Patrimonio, Ingresos y Gastos
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/declaraciones-juradas/declaracion-patrimonio-ingresos-gastos.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/declaraciones-juradas/declaracion-patrimonio-ingresos-gastos.xlsx)**

<table>
    <tr>
        <th>declaracion_id</th>
        <th>patrimonio_ingreso_gasto_tipo</th>
        <th>patrimonio_ingreso_gasto_descripcion</th>
        <th>patrimonio_ingreso_gasto_moneda</th>
        <th>patrimonio_ingreso_gasto_importe</th>
    </tr>

    <tr>
        <td>2011889182</td>
        <td>Ingreso</td>
        <td>Total de Ingresos 4ta categoría</td>
        <td>ARS</td>
        <td>2354169</td>
    </tr>
        
</table>

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases



Descargar clases en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/declaraciones-juradas/declaraciones-juradas-clases.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/declaraciones-juradas/declaraciones-juradas-clases.xlsx)**


<table>
    <tr>
        <th>nombre</th>
        <th>descripcion</th>
    </tr>

    <tr>
        <td>Declaración</td>
        <td>Atributos de la declaración jurada que realiza una persona.</td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>Atributos de la persona que realiza la declaración jurada o de las personas descriptas en ella.</td>
    </tr>
        
    <tr>
        <td>Miembro</td>
        <td>Atributos de una persona en su caracter de miembro de una organización.</td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>Atributos de una organización a la que puede pertenecer la persona que realiza la declaración jurada.</td>
    </tr>
        
    <tr>
        <td>Bienes</td>
        <td>Atributos de los bienes declarados por la persona que realiza la declaración jurada.</td>
    </tr>
        
    <tr>
        <td>Deudas</td>
        <td>Atributos de las deudas declaradas por la persona que realiza la declaración jurada.</td>
    </tr>
        
</table>

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/declaraciones-juradas/declaraciones-juradas-campos.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/declaraciones-juradas/declaraciones-juradas-campos.xlsx)**

### Recurso: Declaración Personal

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
        <td>Declaración</td>
        <td>declaracion_id</td>
        <td>alfanumérico</td>
        <td>Identificador de la declaración jurada.</td>
        <td>2011889182</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Declaración</td>
        <td>declaracion_presentacion_fecha</td>
        <td>fecha</td>
        <td>Fecha en que se presenta la declaración jurada.</td>
        <td>08-02-2017</td>
        <td></td>
        <td></td>
    </tr>
        
    <tr>
        <td>Declaración</td>
        <td>declaracion_descripcion</td>
        <td>texto</td>
        <td>Título o descripción de la declaración jurada.</td>
        <td>Anual 2016 Rectificativa 1</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_id</td>
        <td>alfanumérico</td>
        <td>Número de identificación de la persona según el sistema de identificación oficial principal en uso en el país donde reside.</td>
        <td>578379323</td>
        <td>popolo:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_id_tipo</td>
        <td>alfanumérico</td>
        <td>Tipo de identificación personal utilizado.</td>
        <td>DNI</td>
        <td></td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_otro_id</td>
        <td>alfanumérico</td>
        <td>Número de identificación de la persona según algún sistema de identificación oficial alternativo en uso en el país donde reside.</td>
        <td>27173460711</td>
        <td>popolo:Person</td>
        <td>CUIT/CUIL</td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_otro_id_tipo</td>
        <td>alfanumérico</td>
        <td>Tipo de identificación personal alternativo utilizado.</td>
        <td>CUIL</td>
        <td></td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre completo de la persona.</td>
        <td>Juan Pérez</td>
        <td>popolo:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_genero</td>
        <td>alfanumérico</td>
        <td>Género según el cual se identifica la persona declarado según la normativa vigente para la presentación de declaraciones juradas en el país.</td>
        <td>Masculino</td>
        <td>popolo:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_fecha_nacimiento</td>
        <td>fecha</td>
        <td>Fecha de nacimiento de la persona.</td>
        <td>1966-02-18</td>
        <td>popolo:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_nacionalidad</td>
        <td>numerico</td>
        <td>Nacionalidad de la persona.</td>
        <td>Argentino</td>
        <td>popolo:Person:nationalIdentity</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_estado_civil</td>
        <td>alfanumérico</td>
        <td>Estado civil de la persona.</td>
        <td>Casado</td>
        <td>popolo:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_estudios</td>
        <td>alfanumérico</td>
        <td>Máximo nivel de estudio alcanzado (primario/secundario/tecnico/universitario/posgrados/etc)</td>
        <td>Universitario</td>
        <td></td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_retiro_voluntario</td>
        <td>alfanumérico</td>
        <td>Respuesta a pregunta si se ha acogido a retiro voluntario.</td>
        <td>No</td>
        <td></td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_sin_actividad</td>
        <td>alfanumérico</td>
        <td>Respuesta a pregunta si ha suspendido actividad o goza de licencia.</td>
        <td>No</td>
        <td></td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_sin_actividad_desde</td>
        <td>fecha</td>
        <td>Fecha desde cuando ha suspendido actividad o goza de licencia.</td>
        <td></td>
        <td>Schema:Date</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_horas_por_semana</td>
        <td>numerico</td>
        <td>Carga horaria de trabajo semanal.</td>
        <td>40</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_es_proveedor</td>
        <td>alfanumérico</td>
        <td>Indica si la persona es o fue proveedor, contratista, etc en los últimos 3 años.</td>
        <td>No</td>
        <td></td>
        <td></td>
    </tr>
        
    <tr>
        <td>Miembro</td>
        <td>miembro_organizacion_id</td>
        <td>alfanumérico</td>
        <td>Identificador de la organización de la cual es miembro.</td>
        <td>2</td>
        <td>popolo:Membership</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Miembro</td>
        <td>miembro_fecha_ingreso</td>
        <td>fecha</td>
        <td>Fecha de ingreso a la organización de la cual es miembro.</td>
        <td>2002-31-08</td>
        <td>popolo:Membership</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Miembro</td>
        <td>puesto_nombre</td>
        <td>alfanumérico</td>
        <td></td>
        <td>Jefe</td>
        <td>popolo:Post:label</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Miembro</td>
        <td>puesto_rol</td>
        <td>alfanumérico</td>
        <td>La función que cumple el titular del puesto</td>
        <td>Jefe de Sección</td>
        <td>popolo:Post</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_nombre</td>
        <td>alfanumérico</td>
        <td>El nombre principal de la organización, por ejemplo su nombre legal</td>
        <td>Ministerio de Modernización</td>
        <td>popolo:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_clasificacion</td>
        <td>alfanumérico</td>
        <td>La clasificación de la organización, por ejemplo "Poder Ejecutivo"</td>
        <td>Poder Ejecutivo</td>
        <td>popolo:Organization</td>
        <td></td>
    </tr>
        
</table>
### Recurso: Declaración de Grupo Familiar

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
        <td>Declaración</td>
        <td>declaracion_id</td>
        <td>alfanumérico</td>
        <td>Identificador de la declaración jurada</td>
        <td>2011889182</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_id</td>
        <td>alfanumérico</td>
        <td>Número de identificación de la persona según el sistema de identificación oficial principal en uso en el país donde reside.</td>
        <td>579129534</td>
        <td>popolo:Person</td>
        <td>DNI</td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_id_tipo</td>
        <td>alfanumérico</td>
        <td>Tipo de identificación personal utilizado.</td>
        <td>DNI</td>
        <td></td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_otro_id</td>
        <td>alfanumérico</td>
        <td>Número de identificación de la persona según algún sistema de identificación oficial alternativo en uso en el país donde reside.</td>
        <td>27461236079</td>
        <td>popolo:Person</td>
        <td>CUIT/CUIL</td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_otro_id_tipo</td>
        <td>alfanumérico</td>
        <td>Tipo de identificación personal alternativo utilizado.</td>
        <td>CUIL</td>
        <td></td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre completo de la persona.</td>
        <td>Ana Pérez</td>
        <td>popolo:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_genero</td>
        <td>alfanumérico</td>
        <td>Género según el cual se identifica la persona declarado según la normativa vigente para la presentación de declaraciones juradas en el país.</td>
        <td>Femenino</td>
        <td>popolo:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_fecha_nacimiento</td>
        <td>fecha</td>
        <td>Fecha de nacimiento de la persona.</td>
        <td>1966-02-18</td>
        <td>popolo:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_nacionalidad</td>
        <td>numerico</td>
        <td>Nacionalidad de la persona.</td>
        <td>Argentina</td>
        <td>popolo:Person:national_identity</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_relacionado_con_id</td>
        <td>alfanumérico</td>
        <td>Identificador de la persona con la cual mantiene el vínculo.</td>
        <td>578379323</td>
        <td>vCard:related</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_relacionado_con_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre de la persona con la cual mantiene el vínculo.</td>
        <td>Juan Pérez</td>
        <td>foaf:knows</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_tipo_relacion</td>
        <td>alfanumérico</td>
        <td>Describe tipo de relación (Esposa/Esposo, Hija/Hijo, Madre/Padre, etc)</td>
        <td>Hija</td>
        <td>vCard:related:type_value</td>
        <td>Tipo de vínculo (https://tools.ietf.org/html/rfc6350#section-6.6.6)</td>
    </tr>
        
</table>
### Recurso: Declaración de Bienes y deudas

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
        <td>Declaración</td>
        <td>declaracion_id</td>
        <td>alfanumérico</td>
        <td>Identificador de la declaración jurada.</td>
        <td>2011889182</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
</table>
### Recurso: Declaración de Bienes y Deudas

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
        <td>Bienes</td>
        <td>bienes_momento</td>
        <td>numerico</td>
        <td>Describe el momento en el cual se declara el bien.</td>
        <td>Inicio del período</td>
        <td>Schema:Thing</td>
        <td>Momento en el que se declaran los bienes Inicio del período | Fin del período</td>
    </tr>
        
    <tr>
        <td>Bienes</td>
        <td>bienes_tipo</td>
        <td>alfanumérico</td>
        <td>Tipo de bien.</td>
        <td>Inmueble</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Bienes</td>
        <td>bienes_descripcion</td>
        <td>texto</td>
        <td>Descripción del concepto declarado.</td>
        <td>Apartamento de 300mts2</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Bienes</td>
        <td>bienes_origen_fondos</td>
        <td>alfanumérico</td>
        <td>Origen de los fondos Ingresos propios | Donación, etc.</td>
        <td>Herencia</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Bienes</td>
        <td>bienes_porcentaje_titularidad</td>
        <td>numerico</td>
        <td>Valor numérico que indica en que porcentaje se es titular del bien. 25, 50, 100, etc</td>
        <td>100</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Bienes</td>
        <td>bienes_moneda</td>
        <td>alfanumérico</td>
        <td>Tipo de moneda.</td>
        <td>USD</td>
        <td>Schema:Thing</td>
        <td>Moneda en la cual se declara el importe. Campo opcional si solo se acepta en moneda nacional.
 https://www.currency-iso.org/en/home/tables/table-a1.html</td>
    </tr>
        
    <tr>
        <td>Bienes</td>
        <td>bienes_importe</td>
        <td>numerico</td>
        <td>Valor del bien en moneda.</td>
        <td>450000</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Deudas</td>
        <td>deudas_momento</td>
        <td>alfanumérico</td>
        <td>Describe el momento en el cual se declara la deuda.</td>
        <td>Inicio del período</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Deudas</td>
        <td>deudas_tipo</td>
        <td>alfanumérico</td>
        <td>Tipo de deuda.</td>
        <td>Común</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Deudas</td>
        <td>deudas_descripcion</td>
        <td>texto</td>
        <td>Descripción de las dedudas declaradas.</td>
        <td>Kooj S.A. CUIT 31579842356</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Deudas</td>
        <td>deudas_clasificacion</td>
        <td>alfanumérico</td>
        <td>Clasificación de las deudas declaradas.</td>
        <td>Otras deudas</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Deudas</td>
        <td>deudas_radicacion</td>
        <td>alfanumérico</td>
        <td>Territorio donde se radica la deuda</td>
        <td>Argentina</td>
        <td>Schema:Thing</td>
        <td>País dónde se radica la deuda.</td>
    </tr>
        
    <tr>
        <td>Deudas</td>
        <td>deudas_moneda</td>
        <td>alfanumérico</td>
        <td>Tipo de moneda.</td>
        <td>USD</td>
        <td>Schema:Currency</td>
        <td>Moneda en la cual se declara el importe. Campo opcional si solo se acepta en moneda nacional.
 https://www.currency-iso.org/en/home/tables/table-a1.html</td>
    </tr>
        
    <tr>
        <td>Deudas</td>
        <td>deudas_importe</td>
        <td>numerico</td>
        <td>Importe de las dedudas declaradas.</td>
        <td>25000</td>
        <td>Schema:MonetaryAmount</td>
        <td></td>
    </tr>
        
</table>
### Recurso: Declaración de Postulaciones a Cargos Electivos

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
        <td>Declaración</td>
        <td>declaracion_id</td>
        <td>alfanumérico</td>
        <td>Identificador de la declaración jurada.</td>
        <td>2011889182</td>
        <td>Schema:Thing</td>
        <td>Identificador de la declaración jurada</td>
    </tr>
        
    <tr>
        <td>Postulación</td>
        <td>postulacion_descripcion</td>
        <td>alfanumérico</td>
        <td>Describe el cargo al cual se postuló.</td>
        <td>Diputado periodo 2013 - 2017</td>
        <td>Schema:Thing</td>
        <td></td>
    </tr>
        
</table>
### Recurso: Declaración de Patrimonio, Ingresos y Gastos

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
        <td>Declaración</td>
        <td>declaracion_id</td>
        <td>alfanumérico</td>
        <td>Identificador de la declaración jurada.</td>
        <td>2011889182</td>
        <td>Schema:Thing</td>
        <td>Identificador de la declaración jurada</td>
    </tr>
        
    <tr>
        <td>Declaración</td>
        <td>patrimonio_ingreso_gasto_tipo</td>
        <td>alfanumérico</td>
        <td>Tipo del elemento partrimonial, ingreso o gasto declarado.</td>
        <td>Ingreso</td>
        <td>Schema:Thing</td>
        <td>Lista de valores: Patrimonio | Ingreso | Gasto</td>
    </tr>
        
    <tr>
        <td>Declaración</td>
        <td>patrimonio_ingreso_gasto_descripcion</td>
        <td>texto</td>
        <td>Descripción del elemento partrimonial, ingreso o gasto declarado.</td>
        <td>Total de Ingresos 4ta categoría</td>
        <td>Schema:Thing</td>
        <td>Descripción del concepto declarado</td>
    </tr>
        
    <tr>
        <td>Declaración</td>
        <td>patrimonio_ingreso_gasto_moneda</td>
        <td>alfanumérico</td>
        <td>Moneda  del elemento partrimonial, ingreso o gasto declarado.</td>
        <td>ARS</td>
        <td>Schema:Currency</td>
        <td>Tipo de moneda en que se declara. En caso de que sea siempre en moneda nacional, este campo es opcional.
 https://www.currency-iso.org/en/home/tables/table-a1.html</td>
    </tr>
        
    <tr>
        <td>Declaración</td>
        <td>patrimonio_ingreso_gasto_importe</td>
        <td>numerico</td>
        <td>Importe o valor del elemento partrimonial, ingreso o gasto declarado.</td>
        <td>2354169</td>
        <td>Schema:MonetaryAmount</td>
        <td>Importe en moneda nacional</td>
    </tr>
        
</table>

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
