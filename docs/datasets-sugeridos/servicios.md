# Servicios

Los servicios que brinda el organismo directamente al público, incluyendo normas, cartas y protocolos de atención al cliente.

* **Tema**: Gobierno y sector público
* **Estándar referencia**: https://schema.org/
* **Formatos**: JSON, XML, CSV

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Servicios 
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/servicios/servicios.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/servicios/servicios.xlsx)**

| organizacion_id | organizacion_nombre       | servicio_id | servicio_nombre | servicio_proveedor | servicio_contacto               | servicio_descripcion                                         | servicio_fecha_inicio | servicio_fecha_fin | servicio_dias_semana | servicio_hora_inicio | servicio_hora_fin | servicio_costo | servicio_enlace                         | servicio_enlace_descripcion             | servicio_tramite_inicio_id | servicio_tramite_nombre |
| --------------- | ------------------------- | ----------- | --------------- | ------------------ | ------------------------------- | ------------------------------------------------------------ | --------------------- | ------------------ | -------------------- | -------------------- | ----------------- | -------------- | --------------------------------------- | --------------------------------------- | -------------------------- | --------------------------------------------------- |
| 325             | Municipio de Bahia Blanca |             | Poda            | Arbolado urbano    | Parque de Mayo s/n - 2914880350 | Los vecinos deben solicitar al municipio autorización para podar o extraer un árbol. Para ello, ingresando al Centro de Atención al Vecino en la web del Municipio de Bahía Blanca, el vecino puede solicitar un turno para la realización del trabajo, justificando los motivos de la solicitud (interferencia peatonal, interferencia vehicular, interferencia con luminarias o carteles, riesgo de caída de ramas, etc.), indicando, además, la dirección de referencia para intervención, las observaciones que quiera formular e, incluso, puede adjuntar una foto del árbol a intervenir. | 2019-03-01            | 2019-09-30         | Lunes a Viernes      | 8:00                 | 17:00             | Sin costo      | https://www.bahia.gob.ar/arbolado/poda/ | https://www.bahia.gob.ar/arbolado/poda/ | 333                        | Poda de árbol, extracción de árbol o corte de raíz. |

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases



Descargar clases en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/servicios-clases.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/servicios-clases.xlsx)**


| nombre       | descripcion |
| ------------ | ---------------------------------------------------- |
| Organización | Atributos de la organización que presta el servicio. |
| Servicio     | Atributos del servicio prestado. |

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/servicios-campos.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/servicios-campos.xlsx)**

### Recurso: Servicios 

| clase        | titulo                      | tipo_dato    | descripcion                                                  | ejemplo                                                      | estandar_mapeo                          | notas |
| ------------ | --------------------------- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------------------------- | ------------------------------------------------------------ |
| Organización | organizacion_id             | alfanumerico | Debe ser un identificador único para la organización. Se puede utilizar una codificacion en base al presupuesto; ej: Código jurisdicccion:+código sub jurisdicción:+ ... | 325                                                          | popolo:Organization schema:Organization | |
| Organización | organizacion_nombre         | alfanumerico | El nombre principal de la organización, por ejemplo su nombre legal | Municipio de Bahia Blanca                                    | popolo:Organization schema:Organization | |
| Servicio     | servicio_id                 | alfanumerico | Identificador del servicio                                   |                                                              | schema:Thing                            | |
| Servicio     | servicio_nombre             | alfanumerico | Nombre del servicio                                          | Poda                                                         | schema:Thing                            | |
| Servicio     | servicio_proveedor          | alfanumerico | Area que brinda el servicio dentro de la organización        | Arbolado urbano                                              | schema:Service                          | |
| Servicio     | servicio_contacto           | alfanumerico | Punto de contacto del area que brinda el servicio dentro de la organización | Parque de Mayo s/n - 2914880350                              | schema:Organization                     | |
| Servicio     | servicio_descripcion        | texto        | Descripción del servicio                                     | Los vecinos deben solicitar al municipio autorización para podar o extraer un árbol. Para ello, ingresando al Centro de Atención al Vecino en la web del Municipio de Bahía Blanca, el vecino puede solicitar un turno para la realización del trabajo, justificando los motivos de la solicitud (interferencia peatonal, interferencia vehicular, interferencia con luminarias o carteles, riesgo de caída de ramas, etc.), indicando, además, la dirección de referencia para intervención, las observaciones que quiera formular e, incluso, puede adjuntar una foto del árbol a intervenir. | schema:Thing                            | |
| Servicio     | servicio_fecha_inicio       | fecha        | Fecha de inicio servicio                                     | 2019-03-01                                                   | schema:Demand:availabilityStarts        | |
| Servicio     | servicio_fecha_fin          | fecha        | Fecha de fin del servicio                                    | 2019-09-30                                                   | schema:Demand:availabilityEnds          | |
| Servicio     | servicio_dias_semana        | alfanumerico | Dias de la semana en que se brinda el servicio               | Lunes a Viernes                                              | schema:OpeningHours                     | |
| Servicio     | servicio_hora_inicio        | hora         | Hora de inicio del servicio.                                 | 8:00                                                         | schema:OpeningHours                     | |
| Servicio     | servicio_hora_fin           | hora         | Hora de cierre del servicio.                                 | 17:00                                                        | schema:OpeningHours                     | |
| Servicio     | servicio_costo              | alfanumerico | Costo asociado al servicio                                   | Sin costo                                                    | schema:QuantitativeValue                | |
| Servicio     | servicio_enlace             | URI          | URL a sitio web con información adicional o dónde se puede solicitar el servicio | https://www.bahia.gob.ar/arbolado/poda/                      | schema:Thing                            | |
| Servicio     | servicio_enlace_descripcion | texto        | Descripción del contenido a obtener del enlace               | https://www.bahia.gob.ar/arbolado/poda/                      | schema:Thing                            | |
| Servicio     | servicio_tramite_inicio_id  | alfanumerico | Identificación del trámite que asociado al servicio          | 333                                                          | schema:Thing                            | En caso de que el servicio requiera el inicio de un tramite se identifica el tramite relacionado |
| Servicio     | servicio_tramite_nombre     | alfanumerico | Nombre o descripción del servicio.                           | Poda de árbol, extracción de árbol o corte de raíz.          | schema:Thing                            | |

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
