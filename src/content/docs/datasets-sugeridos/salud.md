---
title: "Salud"
---

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Establecimientos de Salud
**[CSV](/paquete-apertura-datos/datasets-sugeridos/salud/establecimientos-salud.csv)** | **[XLSX](/paquete-apertura-datos/datasets-sugeridos/salud/establecimientos-salud.xlsx)**

| organizacion_id | organizacion_nombre | organizacion_clasificacion | organizacion_padre_id | organizacion_area         | organizacion_fecha_creacion | organizacion_imagen | organizacion_contactos        | organizacion_direccion | organizacion_enlaces                            | organizacion_latitud | organizacion_longitud |
| --------------- | ------------------- | -------------------------- | --------------------- | ------------------------- | --------------------------- | ------------------- | ----------------------------- | ---------------------- | ----------------------------------------------- | -------------------- | --------------------- |
| 2222            | Hospital Pirovano   | Hospital General           | 0                     | CABA, Republica Argentina | 1896-07-12                  |                     | contacto@hospitalpirovano.org | Av. Monroe 3555        | https://www.buenosaires.gob.ar/hospitalpirovano |                      | |

### Recurso: Estadísticas de Salud
**[CSV](/paquete-apertura-datos/datasets-sugeridos/salud/estadisticas-salud.csv)** | **[XLSX](/paquete-apertura-datos/datasets-sugeridos/salud/estadisticas-salud.xlsx)**

| indicador_anio | indicador_organizacion_id | indicador_nombre  | indicador_descripcion                | indicador_periodicidad | indicador_ultima_medicion | indicador_unidad_medida | indicador_valor | indicador_forma_calculo |
| -------------- | ------------------------- | ----------------- | ------------------------------------ | ---------------------- | ------------------------- | ----------------------- | --------------- | ------------------------------------------------------------ |
| 2018           | 2222                      | Cantidad de camas | Cantidad de camas cada 1000 personas | Anual                  | 2018-12-31                | Cantidad de camas       | 5               | Se calcula la cantidad de camas disponibles de acuerdo a la cantidad de afiliados y se pondera el resultado para llevarlo a un valor equivalente sobre una poblacion de 1000 personas. |

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases



Descargar clases en **[CSV](/paquete-apertura-datos/datasets-sugeridos/salud-clases.csv)** | **[XLSX](/paquete-apertura-datos/datasets-sugeridos/salud-clases.xlsx)**


| nombre             | descripcion |
| ------------------ | ----------------------------------------- |
| Organización       | Atributos de un establecimiento de salud. |
| Indicador de Salud | Atributos de un indicador de salud. |

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](/paquete-apertura-datos/datasets-sugeridos/salud-campos.csv)** | **[XLSX](/paquete-apertura-datos/datasets-sugeridos/salud-campos.xlsx)**

### Recurso: Establecimientos de Salud

| clase        | titulo                      | tipo_dato    | descripcion                                                  | ejemplo                                         | estandar_mapeo        | notas |
| ------------ | --------------------------- | ------------ | ------------------------------------------------------------ | ----------------------------------------------- | --------------------- | ------------------------------------------------------------ |
| Organización | organizacion_id             | alfanumerico | Debe ser un identificador único para la organización         | 2222                                            | popolo:Organization   | Se puede utilizar una codificacion en base al presupuesto; ej: Código jurisdicccion:+código sub jurisdicción:+ ... |
| Organización | organizacion_nombre         | alfanumerico | El nombre principal de la organización, por ejemplo su nombre legal | Hospital Pirovano                               | popolo:Organization   | |
| Organización | organizacion_clasificacion  | alfanumerico | La clasificación de la organización                          | Hospital General                                | popolo:Organization   | Indicar la especialidad del centro de salud |
| Organización | organizacion_padre_id       | alfanumerico | Debe referenciar al id de la organización de la cual esta depende. Por ejemplo si es un sanatorio que depende de otra institución mayor | 0                                               | popolo:Organization   | |
| Organización | organizacion_area           | alfanumerico | Indica el área geografica donde se ubica la organizacion     | CABA, Republica Argentina                       | popolo:Organization   | Se podría ampliar este campo a Provincia, Localidad o Codigo Postal |
| Organización | organizacion_fecha_creacion | fecha        | Fecha en que fue creada la organización                      | 1896-07-12                                      | popolo:Organization   | |
| Organización | organizacion_imagen         | uri          |                                                              |                                                 | popolo:Organization   | URL a logo o imagen que identifica a la organización |
| Organización | organizacion_contactos      | alfanumerico | Mecanismos de contacto con las institución                   | contacto@hospitalpirovano.org                   | popolo:Organization   | |
| Organización | organizacion_direccion      | uri          |                                                              | Av. Monroe 3555                                 | popolo:Organization   | |
| Organización | organizacion_enlaces        | alfanumerico | URL a la pagina web del centro educativo                     | https://www.buenosaires.gob.ar/hospitalpirovano | schema:PostalAddress  | Calle, Nro utilizar combinado con organizacion_area |
| Organización | organizacion_latitud        | numerico     | Telefono del centro educativo                                |                                                 | schema:GeoCoordinates | Opcional |
| Organización | organizacion_longitud       | numerico     | Correo electronico institucional del establecimiento         |                                                 | schema:GeoCoordinates | Opcional |

### Recurso: Estadísticas de Salud

| clase              | titulo                    | tipo_dato    | descripcion                                                  | ejemplo                                                      | estandar_mapeo                       | notas |
| ------------------ | ------------------------- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------ | ----- |
| Indicador de Salud | indicador_anio            | numerico     | Año en el cual se registra el indicador                      | 2018                                                         | schema:Date                          | |
| Indicador de Salud | indicador_organizacion_id | alfanumérico | Identificación del establecimiento de salud                  | 2222                                                         | popolo:Organization                  | |
| Indicador de Salud | indicador_nombre          | alfanumérico | Identificación del indicador                                 | Cantidad de camas                                            | schema:QuantitativeValueDistribution | |
| Indicador de Salud | indicador_descripcion     | texto        | Descripción de indicador, se puede complementar con información sobre como se relevan los datos. | Cantidad de camas cada 1000 personas                         | schema:QuantitativeValueDistribution | |
| Indicador de Salud | indicador_periodicidad    | alfanumérico | Cada cuanto tiempo se releva el indicador                    | Anual                                                        | schema:QuantitativeValueDistribution | |
| Indicador de Salud | indicador_ultima_medicion | fecha        | Ultima fecha en que se obtuvo el indicador                   | 2018-12-31                                                   | schema:Date                          | |
| Indicador de Salud | indicador_unidad_medida   | alfanumérico | Unidad de medida                                             | Cantidad de camas                                            | schema:QuantitativeValueDistribution | |
| Indicador de Salud | indicador_valor           | numerico     | Valor en numeros del indicador                               | 5                                                            | schema:QuantitativeValueDistribution | |
| Indicador de Salud | indicador_forma_calculo   | alfanumérico | Especificar como se calcula el indicador, si se calcula en base a datos de otras fuentes. | Se calcula la cantidad de camas disponibles de acuerdo a la cantidad de afiliados y se pondera el resultado para llevarlo a un valor equivalente sobre una poblacion de 1000 personas. | schema:QuantitativeValueDistribution | |

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
