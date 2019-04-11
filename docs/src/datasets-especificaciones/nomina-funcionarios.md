# Nómina de funcionarios públicos y sus salarios

Listas de los funcionarios con referencia a la entidad a la que pertenecen, la categoría, el salario y el cargo, incluyendo pasantes y personal contratado en el marco de proyectos financiados por organismos multilaterales, detallando sus respectivas funciones y posición en el escalafón.

* **Tema**: Gobierno y sector público
* **Estándar referencia**: [Popolo](http://www.popoloproject.com/specs/)
* **Formatos**: JSON, XML, CSV
* **Ejemplo:**: http://www.popoloproject.com/examples/person.json

*Ver cómo incluir lo de Ley/Decreto...*

## Ejemplo

*Tabla con un ejemplo*

## Clases

Un funcionario es una `Persona` que tiene un determinado `Puesto` y es `Miembro` de una `Organización`. Al publicar la nómina de funcionarios tenemos que tener en cuenta los atributos necesarios de estas 4 clases.

Descargar clases en **[CSV](nomina-funcionarios-clases.csv)** | **[XLSX](nomina-funcionarios-clases.xlsx)**

<table>
    <tr>
        <th>Nombre</th>
        <th>Descripción</th>
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

## Campos

Descargar campos en **[CSV](nomina-funcionarios-campos.csv)** | **[XLSX](nomina-funcionarios-campos.xlsx)**

### Organización

<table>
    <tr>
        <th>clase</th>
        <th>titulo</th>
        <th>Tipo de dato</th>
        <th>descripcion</th>
        <th>ejemplo</th>
        <th>estandar_mapeo</th>
        <th>Notas</th>
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
        <td>nan</td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_clasificacion</td>
        <td>alfanumérico</td>
        <td>La clasificación de la organización, por ejemplo "Poder Ejecutivo"</td>
        <td>Poder Ejecutivo</td>
        <td>popolo:Organization</td>
        <td>nan</td>
    </tr>
        
</table>


### Puesto

<table>
    <tr>
        <th>clase</th>
        <th>titulo</th>
        <th>Tipo de dato</th>
        <th>descripcion</th>
        <th>ejemplo</th>
        <th>estandar_mapeo</th>
        <th>Notas</th>
    </tr>

    <tr>
        <td>Puesto</td>
        <td>puesto_id</td>
        <td>alfanumérico</td>
        <td>Un identificador único para el puesto</td>
        <td>1</td>
        <td>popolo:Membership</td>
        <td>nan</td>
    </tr>
        
    <tr>
        <td>Puesto</td>
        <td>puesto_nombre</td>
        <td>alfanumérico</td>
        <td>Una descripción o el nombre del puesto</td>
        <td>Intendente</td>
        <td>popolo:Post:label</td>
        <td>nan</td>
    </tr>
        
    <tr>
        <td>Puesto</td>
        <td>puesto_rol</td>
        <td>alfanumérico</td>
        <td>La función que cumple el titular del puesto</td>
        <td>Intendente</td>
        <td>popolo:Post</td>
        <td>nan</td>
    </tr>
        
    <tr>
        <td>Puesto</td>
        <td>puesto_salario_moneda</td>
        <td>alfanumérico</td>
        <td>Código de moneda para el salario</td>
        <td>https://en.wikipedia.org/wiki/ISO_4217
 https://www.currency-iso.org/en/home/tables/table-a1.html</td>
        <td>schema:EmployeeRole</td>
        <td>nan</td>
    </tr>
        
    <tr>
        <td>Puesto</td>
        <td>puesto_salario</td>
        <td>numerico</td>
        <td>Salario asociado al puesto</td>
        <td>190000</td>
        <td>schema:EmployeeRole</td>
        <td>nan</td>
    </tr>
        
</table>


### Miembro

<table>
    <tr>
        <th>clase</th>
        <th>titulo</th>
        <th>Tipo de dato</th>
        <th>descripcion</th>
        <th>ejemplo</th>
        <th>estandar_mapeo</th>
        <th>Notas</th>
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
        
</table>

### Persona

<table>
    <tr>
        <th>clase</th>
        <th>titulo</th>
        <th>Tipo de dato</th>
        <th>descripcion</th>
        <th>ejemplo</th>
        <th>estandar_mapeo</th>
        <th>Notas</th>
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
        <td>nan</td>
        <td>popolo:Person</td>
        <td>nan</td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_genero</td>
        <td>alfanumérico</td>
        <td>Genero de la persona.</td>
        <td>Ver codigos en: https://github.com/idatosabiertos/femicidios-latam/blob/master/docs/introduccion.md</td>
        <td>popolo:Person</td>
        <td>nan</td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_fecha_nacimiento</td>
        <td>fecha</td>
        <td>Fecha de nacimiento de la persona</td>
        <td>aaaa-mm-dd</td>
        <td>popolo:Person</td>
        <td>nan</td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_cv</td>
        <td>texto</td>
        <td>CV resumido</td>
        <td>nan</td>
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
        <td>nan</td>
        <td>popolo:Person</td>
        <td>Cuenta de correo institucional</td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_contacto</td>
        <td>texto</td>
        <td>Datos personales de contacto de la persona (opcional)</td>
        <td>nan</td>
        <td>popolo:Person</td>
        <td>Datos personales de contacto (no institucional) - Opcional</td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_otros_ingresos_descripcion</td>
        <td>texto</td>
        <td>Opcional: pero podría ser necesario declarar compensaciones, viaticos, etc.</td>
        <td>nan</td>
        <td>nan</td>
        <td>Opcional: pero podría ser necesario declarar compensaciones, viaticos, etc. del funcionario (persona)</td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_otros_ingresos_moneda</td>
        <td>alfanumérico</td>
        <td>Opcional: tipo moneda para el campo anterior</td>
        <td>https://en.wikipedia.org/wiki/ISO_4217
 https://www.currency-iso.org/en/home/tables/table-a1.html</td>
        <td>nan</td>
        <td>Opcional: tipo moneda para el campo anterior</td>
    </tr>
        
    <tr>
        <td>Persona</td>
        <td>persona_otros_ingresos</td>
        <td>numerico</td>
        <td>Opcional: importe para el campo anterior</td>
        <td>nan</td>
        <td>nan</td>
        <td>Opcional: importe para el campo anterior</td>
    </tr>
        
</table>





