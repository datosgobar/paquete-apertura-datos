# Organigrama

Organismos y entidades del estado con su estructura orgánica y funciones.

* **Tema**: Gobierno y sector público
* **Estándar referencia**: [Organizaciones de Popolo](http://www.popoloproject.com/specs/organization.html)
* **Formatos**: JSON, XML, CSV
* **Ejemplo:**: http://www.popoloproject.com/examples/organization.json

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Organigrama
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/organigrama/organigrama.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/organigrama/organigrama.xlsx)**

| organizacion_id | organizacion_nombre         | organizacion_clasificacion | organizacion_padre_id | organizacion_area | organizacion_fecha_creacion | organizacion_fecha_final | organizacion_imagen                                          | organizacion_contactos         | organizacion_direccion                      | organizacion_latitud | organizacion_longitud | organizacion_enlaces |
| --------------- | --------------------------- | -------------------------- | --------------------- | ----------------- | --------------------------- | ------------------------ | ------------------------------------------------------------ | ------------------------------ | ------------------------------------------- | -------------------- | --------------------- | ------------------------------------------ |
| 2               | Ministerio de Modernización | Poder Ejecutivo            | 1                     | ARG               | 2015-06-01                  |                          | https://www.argentina.gob.ar/profiles/argentinagobar/themes/argentinagobar/argentinagobar_theme/logo.svg | (54-011) 5985-8700 / 4343-9001 | Av. Roque Sáenz Peña 511 (Entrepiso) - CABA | -34.607617           | -58.373771            | https://www.argentina.gob.ar/modernizacion |

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases



Descargar clases en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/organigrama-clases.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/organigrama-clases.xlsx)**


| nombre       | descripcion |
| ------------ | ------------------------------------------------------------ |
| Organización | Atributos que describen a las instituciones públicas que componen el organigrama. |

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/organigrama-campos.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/organigrama-campos.xlsx)**

### Recurso: Organigrama

| clase        | titulo                      | tipo_dato    | descripcion                                                  | ejemplo                                                      | estandar_mapeo        | notas |
| ------------ | --------------------------- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------- | ------------------------------------------------------------ |
| Organización | organizacion_id             | alfanumérico | Identificador único para la organización.                    | 2                                                            | popolo:Organization   | Se puede utilizar una codificacion en base al presupuesto; ej: Código jurisdicccion:+código sub jurisdicción:+ ... |
| Organización | organizacion_nombre         | alfanumérico | El nombre principal de la organización, por ejemplo su nombre legal. | Ministerio de Modernización                                  | popolo:Organization   | |
| Organización | organizacion_clasificacion  | alfanumérico | La clasificación de la organización, por ejemplo "Poder Ejecutivo" | Poder Ejecutivo                                              | popolo:Organization   | Ej: Poder Ejecutivo / Poder Judicial / Empresa Publica / etc. |
| Organización | organizacion_padre_id       | alfanumérico | Debe referenciar al id de la organización de la cual esta depende. Por ejemplo la Presidencia de la Nación depende del Poder Ejecutivo. | 1                                                            | popolo:Organization   | |
| Organización | organizacion_area           | alfanumérico | Indica el área geografica donde se ubica la organizacion, utilizando el código ISO alpha 3 para país ("ARG") o los códigos oficiales de INDEC para provincias ("06") o municipios ("822931"). | ARG                                                          | popolo:Organization   | Se podría ampliar este campo a Provincia, Localidad o Codigo Postal |
| Organización | organizacion_fecha_creacion | fecha        | Fecha en que fue creada la organización.                     | 2015-06-01                                                   | popolo:Organization   | |
| Organización | organizacion_fecha_final    | fecha        | Fecha en que dejo de existir la organización.                |                                                              | popolo:Organization   | |
| Organización | organizacion_imagen         | uri          | Logo de la organización, url a la imagen de la organización. | https://www.argentina.gob.ar/profiles/argentinagobar/themes/argentinagobar/argentinagobar_theme/logo.svg | popolo:Organization   | URL a logo o imagen que identifica a la organización |
| Organización | organizacion_contactos      | alfanumérico | Datos de contacto de la organización.                        | (54-011) 5985-8700 / 4343-9001                               | popolo:Organization   | |
| Organización | organizacion_direccion      | alfanumérico | Dirección de la organización.                                | Av. Roque Sáenz Peña 511 (Entrepiso) - CABA                  | schema:PostalAddress  | Calle, Nro utilizar combinado con organizacion_area |
| Organización | organizacion_latitud        | numerico     | Coordenadas geográficas de la ubicación de la organización (latitud). | -34.607617                                                   | schema:GeoCoordinates | Opcional |
| Organización | organizacion_longitud       | numerico     | Coordenadas geográficas de la ubicación de la organización (longitud). | -58.373771                                                   | schema:GeoCoordinates | Opcional |
| Organización | organizacion_enlaces        | uri          | Elaces externos que contengan información sobre la organización. Se puede tener mas de un enlace, por lo que se podria diferenciar cada campo con una secuencia de numeros; ej: organización_enlaces_1, … , organización_enlaces_n | https://www.argentina.gob.ar/modernizacion                   | popolo:Organization   | |

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
