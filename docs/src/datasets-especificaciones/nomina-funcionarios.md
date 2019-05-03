# Nómina de funcionarios públicos y sus salarios

Listas de los funcionarios con referencia a la entidad a la que pertenecen, la categoría, el salario y el cargo, incluyendo pasantes y personal contratado en el marco de proyectos financiados por organismos multilaterales, detallando sus respectivas funciones y posición en el escalafón.

* **Tema**: Gobierno y sector público
* **Estándar referencia**: [Popolo](http://www.popoloproject.com/specs/)
* **Formatos**: JSON, XML, CSV
* **Ejemplo:**: http://www.popoloproject.com/examples/person.json

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Nómina de funcionarios
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/nomina-funcionarios)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/nomina-funcionarios)**

<table>
    <tr>
        <th>organizacion_id</th>
        <th>organizacion_nombre</th>
        <th>organizacion_clasificacion</th>
        <th>puesto_id</th>
        <th>puesto_nombre</th>
        <th>puesto_rol</th>
        <th>puesto_salario_moneda</th>
        <th>puesto_salario</th>
        <th>miembro_fecha_ingreso</th>
        <th>miembro_fecha_egreso</th>
        <th>miembro_contacto</th>
        <th>miembro_representando</th>
        <th>miembro_area_geografica</th>
        <th>persona_id</th>
        <th>persona_nombre</th>
        <th>persona_genero</th>
        <th>persona_fecha_nacimiento</th>
        <th>persona_cv</th>
        <th>persona_enlaces</th>
        <th>persona_email</th>
        <th>persona_contacto</th>
        <th>persona_otros_ingresos_descripcion</th>
        <th>persona_otros_ingresos_moneda</th>
        <th>persona_otros_ingresos</th>
    </tr>

    <tr>
        <td>2</td>
        <td>Presidencia de la República</td>
        <td>Poder Ejecutivo</td>
        <td>1</td>
        <td>Intendente</td>
        <td>Intendente</td>
        <td>https://en.wikipedia.org/wiki/ISO_4217
 https://www.currency-iso.org/en/home/tables/table-a1.html</td>
        <td>190000</td>
        <td>aaaa-mm-dd</td>
        <td>aaaa-mm-dd</td>
        <td>Dirección, Telefonos, Correo institucional</td>
        <td>Nombre de organización</td>
        <td>Gualeguay</td>
        <td>DNI</td>
        <td></td>
        <td>Ver codigos en: https://github.com/idatosabiertos/femicidios-latam/blob/master/docs/introduccion.md</td>
        <td>aaaa-mm-dd</td>
        <td></td>
        <td>Bio en LinkedIn</td>
        <td></td>
        <td></td>
        <td></td>
        <td>https://en.wikipedia.org/wiki/ISO_4217
 https://www.currency-iso.org/en/home/tables/table-a1.html</td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases

Un funcionario es una `Persona` que tiene un determinado `Puesto` y es `Miembro` de una `Organización`. Al publicar la nómina de funcionarios tenemos que tener en cuenta los atributos necesarios de estas 4 clases.

Descargar clases en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/nomina-funcionarios)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/nomina-funcionarios)**


<table>
    <tr>
        <th>nombre</th>
        <th>descripcion</th>
    </tr>

    <tr>
        <td>Organización</td>
        <td>Atributos que describen a las instituciones públicas de las cuales se quieren publicar la nómina de funcionarios y salarios atributos que describen los cargos o puestos que existen en una organización dada atributos que describen la relación entre las personas y las organizaciones atributos para describir la nómina de funcionarios.</td>
    </tr>
        
    <tr>
        <td>Puesto</td>
        <td>Atributos que describen a las instituciones públicas de las cuales se quieren publicar la nómina de funcionarios y salarios atributos que describen los cargos o puestos que existen en una organización dada atributos que describen la relación entre las personas y las organizaciones atributos para describir la nómina de funcionarios.</td>
    </tr>
        
    <tr>
        <td>Miembro</td>
        <td>Atributos que describen a las instituciones públicas de las cuales se quieren publicar la nómina de funcionarios y salarios atributos que describen los cargos o puestos que existen en una organización dada atributos que describen la relación entre las personas y las organizaciones atributos para describir la nómina de funcionarios.</td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>Atributos que describen a las instituciones públicas de las cuales se quieren publicar la nómina de funcionarios y salarios atributos que describen los cargos o puestos que existen en una organización dada atributos que describen la relación entre las personas y las organizaciones atributos para describir la nómina de funcionarios.</td>
    </tr>
        
</table>

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/nomina-funcionarios)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/nomina-funcionarios)**

### Recurso: Nómina de funcionarios

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
        <td>alfanumérico</td>
        <td>Debe ser un identificador único para la organización. Se puede utilizar una codificacion en base al presupuesto; ej: Código jurisdicccion:+código sub jurisdicción:+ ...</td>
        <td>2</td>
        <td>popolo:Organization</td>
        <td>Se puede utilizar una codificacion en base al presupuesto; ej: Código jurisdicccion:+código sub jurisdicción:+ ...</td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_nombre</td>
        <td>alfanumérico</td>
        <td>El nombre principal de la organización, por ejemplo su nombre legal</td>
        <td>Presidencia de la República</td>
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
        
    <tr>
        <td>Puesto</td>
        <td>puesto_id</td>
        <td>alfanumérico</td>
        <td>Un identificador único para el puesto</td>
        <td>1</td>
        <td>popolo:Membership</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Puesto</td>
        <td>puesto_nombre</td>
        <td>alfanumérico</td>
        <td>Una descripción o el nombre del puesto</td>
        <td>Intendente</td>
        <td>popolo:Post:label</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Puesto</td>
        <td>puesto_rol</td>
        <td>alfanumérico</td>
        <td>La función que cumple el titular del puesto</td>
        <td>Intendente</td>
        <td>popolo:Post</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Puesto</td>
        <td>puesto_salario_moneda</td>
        <td>alfanumérico</td>
        <td>Código de moneda para el salario</td>
        <td>https://en.wikipedia.org/wiki/ISO_4217
 https://www.currency-iso.org/en/home/tables/table-a1.html</td>
        <td>schema:EmployeeRole</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Puesto</td>
        <td>puesto_salario</td>
        <td>numerico</td>
        <td>Salario asociado al puesto</td>
        <td>190000</td>
        <td>schema:EmployeeRole</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Miembro</td>
        <td>miembro_fecha_ingreso</td>
        <td>fecha</td>
        <td>Fecha de ingreso a la organización</td>
        <td>aaaa-mm-dd</td>
        <td>popolo:Membership</td>
        <td>Fecha de ingreso a la organización</td>
    </tr>
        
    <tr>
        <td>Miembro</td>
        <td>miembro_fecha_egreso</td>
        <td>fecha</td>
        <td>Fecha de egreso de la organización</td>
        <td>aaaa-mm-dd</td>
        <td>popolo:Membership</td>
        <td>Fecha de egreso de la organización</td>
    </tr>
        
    <tr>
        <td>Miembro</td>
        <td>miembro_contacto</td>
        <td>alfanumérico</td>
        <td>Datos institucionales de contacto de la persona</td>
        <td>Dirección, Telefonos, Correo institucional</td>
        <td>popolo:Membership</td>
        <td>Medios de contacto institucionales con el funcionario</td>
    </tr>
        
    <tr>
        <td>Miembro</td>
        <td>miembro_representando</td>
        <td>alfanumérico</td>
        <td>Si integra la organización en representación de otra organización</td>
        <td>Nombre de organización</td>
        <td>popolo:Membership:onbehalf</td>
        <td>Si integra la organización en representación de otra organización</td>
    </tr>
        
    <tr>
        <td>Miembro</td>
        <td>miembro_area_geografica</td>
        <td>alfanumérico</td>
        <td>Nombre del área geográfica de donde es la organización de la que es miembro</td>
        <td>Gualeguay</td>
        <td>popolo:Membership</td>
        <td>Lugar donde ejerce el cargo (provincia/localidad)</td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_id</td>
        <td>alfanumérico</td>
        <td>Identificación de la persona</td>
        <td>DNI</td>
        <td>popolo:Person</td>
        <td>Este campo puede ser el mismo que national_identity</td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre y Apellido de la persona</td>
        <td></td>
        <td>popolo:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_genero</td>
        <td>alfanumérico</td>
        <td>Genero de la persona.</td>
        <td>Ver codigos en: https://github.com/idatosabiertos/femicidios-latam/blob/master/docs/introduccion.md</td>
        <td>popolo:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_fecha_nacimiento</td>
        <td>fecha</td>
        <td>Fecha de nacimiento de la persona</td>
        <td>aaaa-mm-dd</td>
        <td>popolo:Person</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_cv</td>
        <td>texto</td>
        <td>CV resumido</td>
        <td></td>
        <td>popolo:Person:biography</td>
        <td>Se considera mas apropiado para un funcionario publico la publicación de su Curriculum Vitae. El termino biografía puede llevar a ambigüedades.</td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_enlaces</td>
        <td>URI</td>
        <td>Enlaces a contenido relacionado con la persona</td>
        <td>Bio en LinkedIn</td>
        <td>popolo:Person</td>
        <td>Enlaces a datos sobre la persona</td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_email</td>
        <td>URI:Mailto</td>
        <td>Cuenta de correo electrónico institucional</td>
        <td></td>
        <td>popolo:Person</td>
        <td>Cuenta de correo institucional</td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_contacto</td>
        <td>texto</td>
        <td>Datos personales de contacto de la persona (opcional)</td>
        <td></td>
        <td>popolo:Person</td>
        <td>Datos personales de contacto (no institucional) - Opcional</td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_otros_ingresos_descripcion</td>
        <td>texto</td>
        <td>Opcional: pero podría ser necesario declarar compensaciones, viaticos, etc.</td>
        <td></td>
        <td></td>
        <td>Opcional: pero podría ser necesario declarar compensaciones, viaticos, etc. del funcionario (persona)</td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_otros_ingresos_moneda</td>
        <td>alfanumérico</td>
        <td>Opcional: tipo moneda para el campo anterior</td>
        <td>https://en.wikipedia.org/wiki/ISO_4217
 https://www.currency-iso.org/en/home/tables/table-a1.html</td>
        <td></td>
        <td>Opcional: tipo moneda para el campo anterior</td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_otros_ingresos</td>
        <td>numerico</td>
        <td>Opcional: importe para el campo anterior</td>
        <td></td>
        <td></td>
        <td>Opcional: importe para el campo anterior</td>
    </tr>
        
</table>

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
