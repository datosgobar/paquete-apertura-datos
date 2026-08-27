# Estadísticas del Crimen

Estadísticas sobre niveles de crimen o listado de los mismos.

* **Tema**: Justicia, seguridad y legales
* **Estándar referencia**: [Open Crime Data Standard](https://github.com/spotcrimebrit/SpotCrime-Open-Crime-Data-Standard)
* **Formatos**: JSON, CSV

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Crímenes  
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/crimen/crimenes.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/crimen/crimenes.xlsx)**

| crimen_fecha | crimen_hora | crimen_region | crimen_ciudad | crimen_barrio | crimen_codigo_postal | crimen_seccional | crimen_lugar           | crimen_latitud | crimen_longitud | crimen_tipo | crimen_descripcion | crimen_id_caso | crimen_id_incidente |
| ------------ | ----------- | ------------- | ------------- | ------------- | -------------------- | ---------------- | ---------------------- | -------------- | --------------- | ----------- | ------------------ | -------------- | ------------------- |
| 2018-02-02   | 22:35       | Buenos Aires  | Bahia Blanca  | Bella Vista   | B8000                | 5                | San Lorenzo esq. Garay | -38.7169673    | -62.2486776     | Homicidio   |                    | 865542         | 2336 |

### Recurso: Estadísticas Criminales
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/crimen/estadisticas-criminales.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/crimen/estadisticas-criminales.xlsx)**

| mes     | provincia_id | provincia_nombre | departamento_id | departamento_nombre | localidad_id | localidad_nombre | barrio_nombre | delito_tipo | victima_sexo | victimario_sexo | victima_edad | victimario_edad | vinculo_victima_victimario | situacion_victimario | casos_cantidad |
| ------- | ------------ | ---------------- | --------------- | ------------------- | ------------ | ---------------- | ------------- | ----------- | ------------ | --------------- | ------------ | --------------- | -------------------------- | -------------------- | -------------- |
| 2018-02 | Buenos Aires |                  | Bahia Blanca    |                     | Bahia Blanca |                  | Bella Vista   | Homicidio   | Mujer        | Varón           | 45           | 48              | Pareja                     | Suicidio             | 2 |

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases



Descargar clases en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/crimen-clases.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/crimen-clases.xlsx)**


| nombre             | descripcion |
| ------------------ | ------------------------------------------------------------ |
| Crimen             | Atributos de un hecho criminal determinado. |
| Indicador Criminal | Atributos de un indicador criminal que recoge una cantidad de casos de ocurrencia, con diversas dimensiones de apertura (que son sus atributos). |

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/crimen-campos.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/crimen-campos.xlsx)**

### Recurso: Crímenes  

| clase  | titulo               | tipo_dato    | descripcion                                                  | ejemplo                | estandar_mapeo        | notas |
| ------ | -------------------- | ------------ | ------------------------------------------------------------ | ---------------------- | --------------------- | ----- |
| Crimen | crimen_fecha         | fecha        | Fecha del crimen                                             | 2018-02-02             | Schema:DateTime       | |
| Crimen | crimen_hora          | hora         | Hora del crimen                                              | 22:35                  | Schema:DateTime       | |
| Crimen | crimen_region        | alfanumérico | Zona, región, provincia, departamento                        | Buenos Aires           | Schema:PostalAddress  | |
| Crimen | crimen_ciudad        | alfanumérico | Ciudad donde se perpetro el crimen                           | Bahia Blanca           | Schema:PostalAddress  | |
| Crimen | crimen_barrio        | alfanumérico | Nombre del barrio donde se produce el hecho                  | Bella Vista            | Schema:PostalAddress  | |
| Crimen | crimen_codigo_postal | alfanumérico | Codigo postal del lugar donde se produce el hecho            | B8000                  | Schema:PostalAddress  | |
| Crimen | crimen_seccional     | alfanumérico | Identificación de la sección policial donde ocurrió el hecho. | 5                      | Schema:Thing          | |
| Crimen | crimen_lugar         | alfanumérico | Dirección; calle, numero , esquinas                          | San Lorenzo esq. Garay | Schema:PostalAddress  | |
| Crimen | crimen_latitud       | numérico     | Coordenadas geograficas expresadas en latitud                | -38.7169673            | Schema:GeoCoordinates | |
| Crimen | crimen_longitud      | numérico     | Coordenadas geogrñaficas expresadas en longitud              | -62.2486776            | Schema:GeoCoordinates | |
| Crimen | crimen_tipo          | alfanumérico | Tipo de crimen                                               | Homicidio              | Schema:Thing          | |
| Crimen | crimen_descripcion   | texto        | Detalles del crimen                                          |                        | Schema:Thing          | |
| Crimen | crimen_id_caso       | alfanumérico | Identificación del caso. Puede haber un caso con muchos incidentes. | 865542                 | Schema:Thing          | |
| Crimen | crimen_id_incidente  | alfanumérico | Identificación del incidente                                 | 2336                   | Schema:Thing          | |

### Recurso: Estadísticas Criminales

| clase              | titulo                     | tipo_dato    | descripcion                                                  | ejemplo      | estandar_mapeo           | notas |
| ------------------ | -------------------------- | ------------ | ------------------------------------------------------------ | ------------ | ------------------------ | ----- |
| Indicador Criminal | mes                        | alfanumérico | Año y mes en que se recoge la información según ISO 8601 (YYYY-MM). | 2018-02      | Schema:Date              | |
| Indicador Criminal | provincia_id               | alfanumérico | Identificador oficial de la provincia donde de produce el hecho. | Buenos Aires | Schema:PostalAddress     | |
| Indicador Criminal | provincia_nombre           | alfanumérico | Nombre de la provincia donde se produce el hecho.            |              |                          | |
| Indicador Criminal | departamento_id            | alfanumérico | Identificador oficial del departamento donde de produce el hecho. | Bahia Blanca | Schema:PostalAddress     | |
| Indicador Criminal | departamento_nombre        | alfanumérico | Nombre del departamento donde se produce el hecho.           |              |                          | |
| Indicador Criminal | localidad_id               | alfanumérico | Identificador oficial de la localidad donde de produce el hecho. | Bahia Blanca | Schema:PostalAddress     | |
| Indicador Criminal | localidad_nombre           | alfanumérico | Nombre de la localidad donde se produce el hecho.            |              |                          | |
| Indicador Criminal | barrio_nombre              | alfanumérico | Nombre del barrio donde se produce el hecho.                 | Bella Vista  | Schema:PostalAddress     | |
| Indicador Criminal | delito_tipo                | alfanumérico | Tipificación del delito.                                     | Homicidio    | Schema:Thing             | |
| Indicador Criminal | victima_sexo               | alfanumérico | Genero de la victima.                                        | Mujer        | Schema:Person            | |
| Indicador Criminal | victimario_sexo            | alfanumérico | Genero del victimario.                                       | Varón        | Schema:Person            | |
| Indicador Criminal | victima_edad               | alfanumérico | Las edades pueden ser exactas 20, 25 o por rangos, entre 0 y 10; entre 10 y 25, etc. | 45           | Schema:Person            | |
| Indicador Criminal | victimario_edad            | alfanumérico | Las edades pueden ser exactas 20, 25 o por rangos, entre 0 y 10; entre 10 y 25, etc. | 48           | Schema:Person            | |
| Indicador Criminal | vinculo_victima_victimario | alfanumérico | Vinculo si existia entre la victima y el victimario, generalmente aplica a casos de violencia familiar o de genero. | Pareja       | vCard:related:type_value | |
| Indicador Criminal | situacion_victimario       | alfanumérico | Situación actual del victimario.                             | Suicidio     | Schema:Thing             | |
| Indicador Criminal | casos_cantidad             | alfanumérico | Cantidad en numeros de casos.                                | 2            | Schema:Thing             | |

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
