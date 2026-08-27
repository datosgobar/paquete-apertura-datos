# Nómina de funcionarios públicos y sus salarios

Listas de los funcionarios con referencia a la entidad a la que pertenecen, la categoría, el salario y el cargo, incluyendo pasantes y personal contratado en el marco de proyectos financiados por organismos multilaterales, detallando sus respectivas funciones y posición en el escalafón.

* **Tema**: Gobierno y sector público
* **Estándar referencia**: [Popolo](http://www.popoloproject.com/specs/)
* **Formatos**: JSON, XML, CSV
* **Ejemplo:**: http://www.popoloproject.com/examples/person.json

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Nómina de funcionarios
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/nomina-funcionarios/nomina-funcionarios.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/nomina-funcionarios/nomina-funcionarios.xlsx)**

| organizacion_id | organizacion_nombre         | organizacion_clasificacion | puesto_id | puesto_nombre | puesto_rol | puesto_salario_moneda                                        | puesto_salario | miembro_fecha_ingreso | miembro_fecha_egreso | miembro_contacto                           | miembro_representando  | miembro_area_geografica | persona_id | persona_nombre | persona_genero                                               | persona_fecha_nacimiento | persona_cv | persona_enlaces | persona_email | persona_contacto | persona_otros_ingresos_descripcion | persona_otros_ingresos_moneda                                | persona_otros_ingresos |
| --------------- | --------------------------- | -------------------------- | --------- | ------------- | ---------- | ------------------------------------------------------------ | -------------- | --------------------- | -------------------- | ------------------------------------------ | ---------------------- | ----------------------- | ---------- | -------------- | ------------------------------------------------------------ | ------------------------ | ---------- | --------------- | ------------- | ---------------- | ---------------------------------- | ------------------------------------------------------------ | ---------------------- |
| 2               | Presidencia de la República | Poder Ejecutivo            | 1         | Intendente    | Intendente | https://en.wikipedia.org/wiki/ISO_4217 https://www.currency-iso.org/en/home/tables/table-a1.html | 190000         | aaaa-mm-dd            | aaaa-mm-dd           | Dirección, Telefonos, Correo institucional | Nombre de organización | Gualeguay               | DNI        |                | Ver codigos en: https://github.com/idatosabiertos/femicidios-latam/blob/master/docs/introduccion.md | aaaa-mm-dd               |            | Bio en LinkedIn |               |                  |                                    | https://en.wikipedia.org/wiki/ISO_4217 https://www.currency-iso.org/en/home/tables/table-a1.html | |

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases

Un funcionario es una `Persona` que tiene un determinado `Puesto` y es `Miembro` de una `Organización`. Al publicar la nómina de funcionarios tenemos que tener en cuenta los atributos necesarios de estas 4 clases.

Descargar clases en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/nomina-funcionarios-clases.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/nomina-funcionarios-clases.xlsx)**


| nombre       | descripcion |
| ------------ | ------------------------------------------------------------ |
| Organización | Atributos que describen a las instituciones públicas de las cuales se quieren publicar la nómina de funcionarios y salarios atributos que describen los cargos o puestos que existen en una organización dada atributos que describen la relación entre las personas y las organizaciones atributos para describir la nómina de funcionarios. |
| Puesto       | Atributos que describen a las instituciones públicas de las cuales se quieren publicar la nómina de funcionarios y salarios atributos que describen los cargos o puestos que existen en una organización dada atributos que describen la relación entre las personas y las organizaciones atributos para describir la nómina de funcionarios. |
| Miembro      | Atributos que describen a las instituciones públicas de las cuales se quieren publicar la nómina de funcionarios y salarios atributos que describen los cargos o puestos que existen en una organización dada atributos que describen la relación entre las personas y las organizaciones atributos para describir la nómina de funcionarios. |
| Persona      | Atributos que describen a las instituciones públicas de las cuales se quieren publicar la nómina de funcionarios y salarios atributos que describen los cargos o puestos que existen en una organización dada atributos que describen la relación entre las personas y las organizaciones atributos para describir la nómina de funcionarios. |

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/nomina-funcionarios-campos.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/nomina-funcionarios-campos.xlsx)**

### Recurso: Nómina de funcionarios

| clase        | titulo                             | tipo_dato    | descripcion                                                  | ejemplo                                                      | estandar_mapeo             | notas |
| ------------ | ---------------------------------- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------------- | ------------------------------------------------------------ |
| Organización | organizacion_id                    | alfanumérico | Debe ser un identificador único para la organización. Se puede utilizar una codificacion en base al presupuesto; ej: Código jurisdicccion:+código sub jurisdicción:+ ... | 2                                                            | popolo:Organization        | Se puede utilizar una codificacion en base al presupuesto; ej: Código jurisdicccion:+código sub jurisdicción:+ ... |
| Organización | organizacion_nombre                | alfanumérico | El nombre principal de la organización, por ejemplo su nombre legal | Presidencia de la República                                  | popolo:Organization        | |
| Organización | organizacion_clasificacion         | alfanumérico | La clasificación de la organización, por ejemplo "Poder Ejecutivo" | Poder Ejecutivo                                              | popolo:Organization        | |
| Puesto       | puesto_id                          | alfanumérico | Un identificador único para el puesto                        | 1                                                            | popolo:Membership          | |
| Puesto       | puesto_nombre                      | alfanumérico | Una descripción o el nombre del puesto                       | Intendente                                                   | popolo:Post:label          | |
| Puesto       | puesto_rol                         | alfanumérico | La función que cumple el titular del puesto                  | Intendente                                                   | popolo:Post                | |
| Puesto       | puesto_salario_moneda              | alfanumérico | Código de moneda para el salario                             | https://en.wikipedia.org/wiki/ISO_4217 https://www.currency-iso.org/en/home/tables/table-a1.html | schema:EmployeeRole        | |
| Puesto       | puesto_salario                     | numerico     | Salario asociado al puesto                                   | 190000                                                       | schema:EmployeeRole        | |
| Miembro      | miembro_fecha_ingreso              | fecha        | Fecha de ingreso a la organización                           | aaaa-mm-dd                                                   | popolo:Membership          | Fecha de ingreso a la organización |
| Miembro      | miembro_fecha_egreso               | fecha        | Fecha de egreso de la organización                           | aaaa-mm-dd                                                   | popolo:Membership          | Fecha de egreso de la organización |
| Miembro      | miembro_contacto                   | alfanumérico | Datos institucionales de contacto de la persona              | Dirección, Telefonos, Correo institucional                   | popolo:Membership          | Medios de contacto institucionales con el funcionario |
| Miembro      | miembro_representando              | alfanumérico | Si integra la organización en representación de otra organización | Nombre de organización                                       | popolo:Membership:onbehalf | Si integra la organización en representación de otra organización |
| Miembro      | miembro_area_geografica            | alfanumérico | Nombre del área geográfica de donde es la organización de la que es miembro | Gualeguay                                                    | popolo:Membership          | Lugar donde ejerce el cargo (provincia/localidad) |
| Persona      | persona_id                         | alfanumérico | Identificación de la persona                                 | DNI                                                          | popolo:Person              | Este campo puede ser el mismo que national_identity |
| Persona      | persona_nombre                     | alfanumérico | Nombre y Apellido de la persona                              |                                                              | popolo:Person              | |
| Persona      | persona_genero                     | alfanumérico | Genero de la persona.                                        | Ver codigos en: https://github.com/idatosabiertos/femicidios-latam/blob/master/docs/introduccion.md | popolo:Person              | |
| Persona      | persona_fecha_nacimiento           | fecha        | Fecha de nacimiento de la persona                            | aaaa-mm-dd                                                   | popolo:Person              | |
| Persona      | persona_cv                         | texto        | CV resumido                                                  |                                                              | popolo:Person:biography    | Se considera mas apropiado para un funcionario publico la publicación de su Curriculum Vitae. El termino biografía puede llevar a ambigüedades. |
| Persona      | persona_enlaces                    | URI          | Enlaces a contenido relacionado con la persona               | Bio en LinkedIn                                              | popolo:Person              | Enlaces a datos sobre la persona |
| Persona      | persona_email                      | URI:Mailto   | Cuenta de correo electrónico institucional                   |                                                              | popolo:Person              | Cuenta de correo institucional |
| Persona      | persona_contacto                   | texto        | Datos personales de contacto de la persona (opcional)        |                                                              | popolo:Person              | Datos personales de contacto (no institucional) - Opcional |
| Persona      | persona_otros_ingresos_descripcion | texto        | Opcional: pero podría ser necesario declarar compensaciones, viaticos, etc. |                                                              |                            | Opcional: pero podría ser necesario declarar compensaciones, viaticos, etc. del funcionario (persona) |
| Persona      | persona_otros_ingresos_moneda      | alfanumérico | Opcional: tipo moneda para el campo anterior                 | https://en.wikipedia.org/wiki/ISO_4217 https://www.currency-iso.org/en/home/tables/table-a1.html |                            | Opcional: tipo moneda para el campo anterior |
| Persona      | persona_otros_ingresos             | numerico     | Opcional: importe para el campo anterior                     |                                                              |                            | Opcional: importe para el campo anterior |

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
