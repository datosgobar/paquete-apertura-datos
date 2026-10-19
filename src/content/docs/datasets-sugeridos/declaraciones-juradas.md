---
title: "Declaraciones Juradas"
---

Declaración Jurada Patrimonial Integral de carácter público con su correspondiente relación a la Nómina de Funcionarios.

* **Tema**: Gobierno y sector público
* **Estándar referencia**: Organizaciones, Personas, Membership de Popolo extendiendo la última para agregar su declaración jurada http://www.popoloproject.com/specs y vCard
* **Formatos**: JSON, XML, CSV

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Declaración Personal
**[CSV](/paquete-apertura-datos/datasets-sugeridos/declaraciones-juradas/declaracion-personal.csv)** | **[XLSX](/paquete-apertura-datos/datasets-sugeridos/declaraciones-juradas/declaracion-personal.xlsx)**

| declaracion_id | declaracion_presentacion_fecha | declaracion_descripcion    | persona_id | persona_id_tipo | persona_otro_id | persona_otro_id_tipo | persona_nombre | persona_genero | persona_fecha_nacimiento | persona_nacionalidad | persona_estado_civil | persona_estudios | persona_retiro_voluntario | persona_sin_actividad | persona_sin_actividad_desde | persona_horas_por_semana | persona_es_proveedor | miembro_organizacion_id | miembro_fecha_ingreso | puesto_nombre | puesto_rol      | organizacion_nombre         | organizacion_clasificacion |
| -------------- | ------------------------------ | -------------------------- | ---------- | --------------- | --------------- | -------------------- | -------------- | -------------- | ------------------------ | -------------------- | -------------------- | ---------------- | ------------------------- | --------------------- | --------------------------- | ------------------------ | -------------------- | ----------------------- | --------------------- | ------------- | --------------- | --------------------------- | -------------------------- |
| 2011889182     | 08-02-2017                     | Anual 2016 Rectificativa 1 | 578379323  | DNI             | 27173460711     | CUIL                 | Juan Pérez     | Masculino      | 1966-02-18               | Argentino            | Casado               | Universitario    | No                        | No                    |                             | 40                       | No                   | 2                       | 2002-31-08            | Jefe          | Jefe de Sección | Ministerio de Modernización | Poder Ejecutivo |

### Recurso: Declaración de Grupo Familiar
**[CSV](/paquete-apertura-datos/datasets-sugeridos/declaraciones-juradas/declaracion-grupo-familiar.csv)** | **[XLSX](/paquete-apertura-datos/datasets-sugeridos/declaraciones-juradas/declaracion-grupo-familiar.xlsx)**

| declaracion_id | persona_id | persona_id_tipo | persona_otro_id | persona_otro_id_tipo | persona_nombre | persona_genero | persona_fecha_nacimiento | persona_nacionalidad | persona_relacionado_con_id | persona_relacionado_con_nombre | persona_tipo_relacion |
| -------------- | ---------- | --------------- | --------------- | -------------------- | -------------- | -------------- | ------------------------ | -------------------- | -------------------------- | ------------------------------ | --------------------- |
| 2011889182     | 579129534  | DNI             | 27461236079     | CUIL                 | Ana Pérez      | Femenino       | 1966-02-18               | Argentina            | 578379323                  | Juan Pérez                     | Hija |

### Recurso: Declaración de Bienes y deudas
**[CSV](/paquete-apertura-datos/datasets-sugeridos/declaraciones-juradas/declaracion-bienes-deudas.csv)** | **[XLSX](/paquete-apertura-datos/datasets-sugeridos/declaraciones-juradas/declaracion-bienes-deudas.xlsx)**

| declaracion_id |
| -------------- |
| 2011889182 |

### Recurso: Declaración de Bienes y Deudas
**[CSV](/paquete-apertura-datos/datasets-sugeridos/declaraciones-juradas/declaracion-bienes-deudas.csv)** | **[XLSX](/paquete-apertura-datos/datasets-sugeridos/declaraciones-juradas/declaracion-bienes-deudas.xlsx)**

| bienes_momento     | bienes_tipo | bienes_descripcion     | bienes_origen_fondos | bienes_porcentaje_titularidad | bienes_moneda | bienes_importe | deudas_momento     | deudas_tipo | deudas_descripcion         | deudas_clasificacion | deudas_radicacion | deudas_moneda | deudas_importe |
| ------------------ | ----------- | ---------------------- | -------------------- | ----------------------------- | ------------- | -------------- | ------------------ | ----------- | -------------------------- | -------------------- | ----------------- | ------------- | -------------- |
| Inicio del período | Inmueble    | Apartamento de 300mts2 | Herencia             | 100                           | USD           | 450000         | Inicio del período | Común       | Kooj S.A. CUIT 31579842356 | Otras deudas         | Argentina         | USD           | 25000 |

### Recurso: Declaración de Postulaciones a Cargos Electivos
**[CSV](/paquete-apertura-datos/datasets-sugeridos/declaraciones-juradas/declaracion-postulaciones-cargos-electivos.csv)** | **[XLSX](/paquete-apertura-datos/datasets-sugeridos/declaraciones-juradas/declaracion-postulaciones-cargos-electivos.xlsx)**

| declaracion_id | postulacion_descripcion |
| -------------- | ---------------------------- |
| 2011889182     | Diputado periodo 2013 - 2017 |

### Recurso: Declaración de Patrimonio, Ingresos y Gastos
**[CSV](/paquete-apertura-datos/datasets-sugeridos/declaraciones-juradas/declaracion-patrimonio-ingresos-gastos.csv)** | **[XLSX](/paquete-apertura-datos/datasets-sugeridos/declaraciones-juradas/declaracion-patrimonio-ingresos-gastos.xlsx)**

| declaracion_id | patrimonio_ingreso_gasto_tipo | patrimonio_ingreso_gasto_descripcion | patrimonio_ingreso_gasto_moneda | patrimonio_ingreso_gasto_importe |
| -------------- | ----------------------------- | ------------------------------------ | ------------------------------- | -------------------------------- |
| 2011889182     | Ingreso                       | Total de Ingresos 4ta categoría      | ARS                             | 2354169 |

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases



Descargar clases en **[CSV](/paquete-apertura-datos/datasets-sugeridos/declaraciones-juradas-clases.csv)** | **[XLSX](/paquete-apertura-datos/datasets-sugeridos/declaraciones-juradas-clases.xlsx)**


| nombre       | descripcion |
| ------------ | ------------------------------------------------------------ |
| Declaración  | Atributos de la declaración jurada que realiza una persona. |
| Persona      | Atributos de la persona que realiza la declaración jurada o de las personas descriptas en ella. |
| Miembro      | Atributos de una persona en su caracter de miembro de una organización. |
| Organización | Atributos de una organización a la que puede pertenecer la persona que realiza la declaración jurada. |
| Bienes       | Atributos de los bienes declarados por la persona que realiza la declaración jurada. |
| Deudas       | Atributos de las deudas declaradas por la persona que realiza la declaración jurada. |

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](/paquete-apertura-datos/datasets-sugeridos/declaraciones-juradas-campos.csv)** | **[XLSX](/paquete-apertura-datos/datasets-sugeridos/declaraciones-juradas-campos.xlsx)**

### Recurso: Declaración Personal

| clase        | titulo                         | tipo_dato    | descripcion                                                  | ejemplo                     | estandar_mapeo                 | notas |
| ------------ | ------------------------------ | ------------ | ------------------------------------------------------------ | --------------------------- | ------------------------------ | --------- |
| Declaración  | declaracion_id                 | alfanumérico | Identificador de la declaración jurada.                      | 2011889182                  | schema:Thing                   | |
| Declaración  | declaracion_presentacion_fecha | fecha        | Fecha en que se presenta la declaración jurada.              | 08-02-2017                  |                                | |
| Declaración  | declaracion_descripcion        | texto        | Título o descripción de la declaración jurada.               | Anual 2016 Rectificativa 1  | schema:Thing                   | |
| Persona      | persona_id                     | alfanumérico | Número de identificación de la persona según el sistema de identificación oficial principal en uso en el país donde reside. | 578379323                   | popolo:Person                  | |
| Persona      | persona_id_tipo                | alfanumérico | Tipo de identificación personal utilizado.                   | DNI                         |                                | |
| Persona      | persona_otro_id                | alfanumérico | Número de identificación de la persona según algún sistema de identificación oficial alternativo en uso en el país donde reside. | 27173460711                 | popolo:Person                  | CUIT/CUIL |
| Persona      | persona_otro_id_tipo           | alfanumérico | Tipo de identificación personal alternativo utilizado.       | CUIL                        |                                | |
| Persona      | persona_nombre                 | alfanumérico | Nombre completo de la persona.                               | Juan Pérez                  | popolo:Person                  | |
| Persona      | persona_genero                 | alfanumérico | Género según el cual se identifica la persona declarado según la normativa vigente para la presentación de declaraciones juradas en el país. | Masculino                   | popolo:Person                  | |
| Persona      | persona_fecha_nacimiento       | fecha        | Fecha de nacimiento de la persona.                           | 1966-02-18                  | popolo:Person                  | |
| Persona      | persona_nacionalidad           | numerico     | Nacionalidad de la persona.                                  | Argentino                   | popolo:Person:nationalIdentity | |
| Persona      | persona_estado_civil           | alfanumérico | Estado civil de la persona.                                  | Casado                      | popolo:Person                  | |
| Persona      | persona_estudios               | alfanumérico | Máximo nivel de estudio alcanzado (primario/secundario/tecnico/universitario/posgrados/etc) | Universitario               |                                | |
| Persona      | persona_retiro_voluntario      | alfanumérico | Respuesta a pregunta si se ha acogido a retiro voluntario.   | No                          |                                | |
| Persona      | persona_sin_actividad          | alfanumérico | Respuesta a pregunta si ha suspendido actividad o goza de licencia. | No                          |                                | |
| Persona      | persona_sin_actividad_desde    | fecha        | Fecha desde cuando ha suspendido actividad o goza de licencia. |                             | Schema:Date                    | |
| Persona      | persona_horas_por_semana       | numerico     | Carga horaria de trabajo semanal.                            | 40                          | Schema:Thing                   | |
| Persona      | persona_es_proveedor           | alfanumérico | Indica si la persona es o fue proveedor, contratista, etc en los últimos 3 años. | No                          |                                | |
| Miembro      | miembro_organizacion_id        | alfanumérico | Identificador de la organización de la cual es miembro.      | 2                           | popolo:Membership              | |
| Miembro      | miembro_fecha_ingreso          | fecha        | Fecha de ingreso a la organización de la cual es miembro.    | 2002-31-08                  | popolo:Membership              | |
| Miembro      | puesto_nombre                  | alfanumérico |                                                              | Jefe                        | popolo:Post:label              | |
| Miembro      | puesto_rol                     | alfanumérico | La función que cumple el titular del puesto                  | Jefe de Sección             | popolo:Post                    | |
| Organización | organizacion_nombre            | alfanumérico | El nombre principal de la organización, por ejemplo su nombre legal | Ministerio de Modernización | popolo:Organization            | |
| Organización | organizacion_clasificacion     | alfanumérico | La clasificación de la organización, por ejemplo "Poder Ejecutivo" | Poder Ejecutivo             | popolo:Organization            | |

### Recurso: Declaración de Grupo Familiar

| clase       | titulo                         | tipo_dato    | descripcion                                                  | ejemplo     | estandar_mapeo                  | notas |
| ----------- | ------------------------------ | ------------ | ------------------------------------------------------------ | ----------- | ------------------------------- | ------------------------------------------------------------ |
| Declaración | declaracion_id                 | alfanumérico | Identificador de la declaración jurada                       | 2011889182  | Schema:Thing                    | |
| Persona     | persona_id                     | alfanumérico | Número de identificación de la persona según el sistema de identificación oficial principal en uso en el país donde reside. | 579129534   | popolo:Person                   | DNI |
| Persona     | persona_id_tipo                | alfanumérico | Tipo de identificación personal utilizado.                   | DNI         |                                 | |
| Persona     | persona_otro_id                | alfanumérico | Número de identificación de la persona según algún sistema de identificación oficial alternativo en uso en el país donde reside. | 27461236079 | popolo:Person                   | CUIT/CUIL |
| Persona     | persona_otro_id_tipo           | alfanumérico | Tipo de identificación personal alternativo utilizado.       | CUIL        |                                 | |
| Persona     | persona_nombre                 | alfanumérico | Nombre completo de la persona.                               | Ana Pérez   | popolo:Person                   | |
| Persona     | persona_genero                 | alfanumérico | Género según el cual se identifica la persona declarado según la normativa vigente para la presentación de declaraciones juradas en el país. | Femenino    | popolo:Person                   | |
| Persona     | persona_fecha_nacimiento       | fecha        | Fecha de nacimiento de la persona.                           | 1966-02-18  | popolo:Person                   | |
| Persona     | persona_nacionalidad           | numerico     | Nacionalidad de la persona.                                  | Argentina   | popolo:Person:national_identity | |
| Persona     | persona_relacionado_con_id     | alfanumérico | Identificador de la persona con la cual mantiene el vínculo. | 578379323   | vCard:related                   | |
| Persona     | persona_relacionado_con_nombre | alfanumérico | Nombre de la persona con la cual mantiene el vínculo.        | Juan Pérez  | foaf:knows                      | |
| Persona     | persona_tipo_relacion          | alfanumérico | Describe tipo de relación (Esposa/Esposo, Hija/Hijo, Madre/Padre, etc) | Hija        | vCard:related:type_value        | Tipo de vínculo (https://tools.ietf.org/html/rfc6350#section-6.6.6) |

### Recurso: Declaración de Bienes y deudas

| clase       | titulo         | tipo_dato    | descripcion                             | ejemplo    | estandar_mapeo | notas |
| ----------- | -------------- | ------------ | --------------------------------------- | ---------- | -------------- | ----- |
| Declaración | declaracion_id | alfanumérico | Identificador de la declaración jurada. | 2011889182 | Schema:Thing   | |

### Recurso: Declaración de Bienes y Deudas

| clase  | titulo                        | tipo_dato    | descripcion                                                  | ejemplo                    | estandar_mapeo        | notas |
| ------ | ----------------------------- | ------------ | ------------------------------------------------------------ | -------------------------- | --------------------- | ------------------------------------------------------------ |
| Bienes | bienes_momento                | numerico     | Describe el momento en el cual se declara el bien.           | Inicio del período         | Schema:Thing          | Momento en el que se declaran los bienes Inicio del período \| Fin del período |
| Bienes | bienes_tipo                   | alfanumérico | Tipo de bien.                                                | Inmueble                   | Schema:Thing          | |
| Bienes | bienes_descripcion            | texto        | Descripción del concepto declarado.                          | Apartamento de 300mts2     | Schema:Thing          | |
| Bienes | bienes_origen_fondos          | alfanumérico | Origen de los fondos Ingresos propios \| Donación, etc.      | Herencia                   | Schema:Thing          | |
| Bienes | bienes_porcentaje_titularidad | numerico     | Valor numérico que indica en que porcentaje se es titular del bien. 25, 50, 100, etc | 100                        | Schema:Thing          | |
| Bienes | bienes_moneda                 | alfanumérico | Tipo de moneda.                                              | USD                        | Schema:Thing          | Moneda en la cual se declara el importe. Campo opcional si solo se acepta en moneda nacional. https://www.currency-iso.org/en/home/tables/table-a1.html |
| Bienes | bienes_importe                | numerico     | Valor del bien en moneda.                                    | 450000                     | Schema:Thing          | |
| Deudas | deudas_momento                | alfanumérico | Describe el momento en el cual se declara la deuda.          | Inicio del período         | Schema:Thing          | |
| Deudas | deudas_tipo                   | alfanumérico | Tipo de deuda.                                               | Común                      | Schema:Thing          | |
| Deudas | deudas_descripcion            | texto        | Descripción de las dedudas declaradas.                       | Kooj S.A. CUIT 31579842356 | Schema:Thing          | |
| Deudas | deudas_clasificacion          | alfanumérico | Clasificación de las deudas declaradas.                      | Otras deudas               | Schema:Thing          | |
| Deudas | deudas_radicacion             | alfanumérico | Territorio donde se radica la deuda                          | Argentina                  | Schema:Thing          | País dónde se radica la deuda. |
| Deudas | deudas_moneda                 | alfanumérico | Tipo de moneda.                                              | USD                        | Schema:Currency       | Moneda en la cual se declara el importe. Campo opcional si solo se acepta en moneda nacional. https://www.currency-iso.org/en/home/tables/table-a1.html |
| Deudas | deudas_importe                | numerico     | Importe de las dedudas declaradas.                           | 25000                      | Schema:MonetaryAmount | |

### Recurso: Declaración de Postulaciones a Cargos Electivos

| clase       | titulo                  | tipo_dato    | descripcion                             | ejemplo                      | estandar_mapeo | notas |
| ----------- | ----------------------- | ------------ | --------------------------------------- | ---------------------------- | -------------- | -------------------------------------- |
| Declaración | declaracion_id          | alfanumérico | Identificador de la declaración jurada. | 2011889182                   | Schema:Thing   | Identificador de la declaración jurada |
| Postulación | postulacion_descripcion | alfanumérico | Describe el cargo al cual se postuló.   | Diputado periodo 2013 - 2017 | Schema:Thing   | |

### Recurso: Declaración de Patrimonio, Ingresos y Gastos

| clase       | titulo                               | tipo_dato    | descripcion                                                  | ejemplo                         | estandar_mapeo        | notas |
| ----------- | ------------------------------------ | ------------ | ------------------------------------------------------------ | ------------------------------- | --------------------- | ------------------------------------------------------------ |
| Declaración | declaracion_id                       | alfanumérico | Identificador de la declaración jurada.                      | 2011889182                      | Schema:Thing          | Identificador de la declaración jurada |
| Declaración | patrimonio_ingreso_gasto_tipo        | alfanumérico | Tipo del elemento partrimonial, ingreso o gasto declarado.   | Ingreso                         | Schema:Thing          | Lista de valores: Patrimonio \| Ingreso \| Gasto |
| Declaración | patrimonio_ingreso_gasto_descripcion | texto        | Descripción del elemento partrimonial, ingreso o gasto declarado. | Total de Ingresos 4ta categoría | Schema:Thing          | Descripción del concepto declarado |
| Declaración | patrimonio_ingreso_gasto_moneda      | alfanumérico | Moneda del elemento partrimonial, ingreso o gasto declarado. | ARS                             | Schema:Currency       | Tipo de moneda en que se declara. En caso de que sea siempre en moneda nacional, este campo es opcional. https://www.currency-iso.org/en/home/tables/table-a1.html |
| Declaración | patrimonio_ingreso_gasto_importe     | numerico     | Importe o valor del elemento partrimonial, ingreso o gasto declarado. | 2354169                         | Schema:MonetaryAmount | Importe en moneda nacional |

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
