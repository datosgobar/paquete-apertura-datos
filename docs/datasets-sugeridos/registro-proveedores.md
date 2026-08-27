# Registro de Proveedores

Nombre de proveedores adjudicados en contrataciones públicas, así como los socios y accionistas principales, de las sociedades o empresas proveedoras.

* **Tema**: Gobierno y sector público
* **Estándar referencia**: [Beneficial Ownership](http://standard.openownership.org/en/master/)
* **Formatos**: JSON, XML, CSV

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Declaraciones de Proveedores
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/registro-proveedores/declaraciones-proveedores.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/registro-proveedores/declaraciones-proveedores.xlsx)**

| declaracion_id | declaracion_fecha | declaracion_documentacion     | entidad_id  | entidad_fecha_preinscripcion | entidad_tipo | entidad_nombre | entidad_jurisdiccion | entidad_correo   | entidad_telefono | entidad_domicilio_legal | entidad_estado |
| -------------- | ----------------- | ----------------------------- | ----------- | ---------------------------- | ------------ | -------------- | -------------------- | ---------------- | ---------------- | ----------------------- | -------------- |
| 10529          | 2020-12-31        | Declaración Jurada de Interes | 30628707093 | 2018-01-01                   | SRL          | HAL2000        | CABA                 | info@hal2000.com | +541152864897    | Av. Cordoba 1555        | Inscripto |

### Recurso: Apoderados o Referentes Legales de Proveedores
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/registro-proveedores/apoderados-o-referentes-legales-proveedores.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/registro-proveedores/apoderados-o-referentes-legales-proveedores.xlsx)**

| declaracion_id | persona_id | persona_tipo | persona_nombre  | persona_identificador_otro_id | persona_limite_oferta |
| -------------- | ---------- | ------------ | --------------- | ----------------------------- | --------------------- |
| 10529          | 579320998  | Socio        | Andrea Martinez | 30-62870709-3                 | |

### Recurso: Intereses Declarados por los Proveedores
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/registro-proveedores/intereses-declarados-por-proveedores.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/registro-proveedores/intereses-declarados-por-proveedores.xlsx)**

| declaracion_id | clase_id | clase_descripcion        | clase_rubro_id | clase_rubro_descripcion |
| -------------- | -------- | ------------------------ | -------------- | ----------------------- |
| 10529          | 584798   | Serv. Detección Incendio | 58             | Serv. Profesional |

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases



Descargar clases en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/registro-proveedores-clases.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/registro-proveedores-clases.xlsx)**


| nombre       | descripcion |
| ------------ | ------------------------------------------------------------ |
| Declaración  | Atributos de la declaración de una organización al momento de consignarse como proveedora. |
| Organización | Atributos de una empresa u organización que se constituye en un registro de proveedores. |
| Persona      | Atributos de las personas físicas responsables o representantes de la organización que se constituye en proveedora. |
| Intereses    | Atributos de los intereses declarados por la organización respecto de los rubros o áreas en las cuales puede prestar servicios como proveedor. |

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/registro-proveedores-campos.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/registro-proveedores-campos.xlsx)**

### Recurso: Declaraciones de Proveedores

| clase        | titulo                       | tipo_dato    | descripcion                                                  | ejemplo                       | estandar_mapeo      | notas |
| ------------ | ---------------------------- | ------------ | ------------------------------------------------------------ | ----------------------------- | ------------------- | ----- |
| Declaración  | declaracion_id               | alfanumérico | Identificador único de la declaración, número de inscripción. | 10529                         | BO:EntityStatement  | |
| Declaración  | declaracion_fecha            | fecha        | Fecha de vencimiento de la declaración                       | 2020-12-31                    | BO:EntityStatement  | |
| Declaración  | declaracion_documentacion    | alfanumérico | Descripción del conjunto de documentos que tiene la parte interesada. Ver interes. | Declaración Jurada de Interes | BO:EntityStatement  | |
| Organización | entidad_id                   | alfanumérico | Identificadores oficiales para la entidad (CUIT/CUIL)        | 30628707093                   | BO:EntityStatement  | |
| Organización | entidad_fecha_preinscripcion | alfanumérico | Fecha de registro                                            | 2018-01-01                    | BO:EntityStatement  | |
| Organización | entidad_tipo                 | alfanumérico | Tipo de entidad (SA / SRL / etc)                             | SRL                           | BO:EntityStatement  | |
| Organización | entidad_nombre               | alfanumérico | Nombre de la entidad o Razón social                          | HAL2000                       | BO:EntityStatement  | |
| Organización | entidad_jurisdiccion         | alfanumérico | Jurisdicción expresada utilizando la codificación ISO_3166-2 | CABA                          | BO:EntityStatement  | |
| Organización | entidad_correo               | alfanumérico | Correo electronico de la entidad                             | info@hal2000.com              | Schema:ContactPoint | |
| Organización | entidad_telefono             | alfanumérico | Telefono de contacto de la entidad                           | +541152864897                 | Schema:ContactPoint | |
| Organización | entidad_domicilio_legal      | alfanumérico | Domicilio leglamente establecido por la entidad              | Av. Cordoba 1555              | BO:EntityStatement  | |
| Organización | entidad_estado               | alfanumérico | Estado de la entidad                                         | Inscripto                     | No estandarizado    | |

### Recurso: Apoderados o Referentes Legales de Proveedores

| clase       | titulo                        | tipo_dato    | descripcion                                                  | ejemplo         | estandar_mapeo     | notas |
| ----------- | ----------------------------- | ------------ | ------------------------------------------------------------ | --------------- | ------------------ | ----- |
| Declaración | declaracion_id                | alfanumérico | Identificador único de la declaración, número de inscripción. | 10529           | BO:EntityStatement | |
| Persona     | persona_id                    | alfanumérico | DNI                                                          | 579320998       | Bo:PersonStatement | |
| Persona     | persona_tipo                  | alfanumérico | Se utiliza a la persona para registrar a representate legal, apoderado o cargo. | Socio           | Bo:PersonStatement | |
| Persona     | persona_nombre                | alfanumérico | Nombre completo habitual                                     | Andrea Martinez | Bo:PersonStatement | |
| Persona     | persona_identificador_otro_id | alfanumérico | CUIT / NIT                                                   | 30-62870709-3   | Bo:PersonStatement | |
| Persona     | persona_limite_oferta         | alfanumérico | Monto límite por oferta electronica, solo aplica a representates legales o apoderados |                 | No estandarizado   | |

### Recurso: Intereses Declarados por los Proveedores

| clase       | titulo                  | tipo_dato    | descripcion                                                  | ejemplo                  | estandar_mapeo     | notas |
| ----------- | ----------------------- | ------------ | ------------------------------------------------------------ | ------------------------ | ------------------ | ----- |
| Declaración | declaracion_id          | alfanumérico | Identificador único de la declaración, número de inscripción. | 10529                    | BO:EntityStatement | |
| Intereses   | clase_id                | alfanumérico | Identificador de la clase de interes                         | 584798                   | Schema:Product     | |
| Intereses   | clase_descripcion       | alfanumérico | Descripción de la clase de interes o tipo de interes         | Serv. Detección Incendio | Schema:Thing       | |
| Intereses   | clase_rubro_id          | alfanumérico | Identificador del rubro asociado a la clase                  | 58                       | Schema:Product     | |
| Intereses   | clase_rubro_descripcion | alfanumérico | Descripción del rubro asociado a la clase                    | Serv. Profesional        | Schema:Thing       | |

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
