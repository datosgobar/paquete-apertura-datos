# Calidad del Agua

Listas de los funcionarios con referencia a la entidad a la que pertenecen, la categoría, el salario y el cargo, incluyendo pasantes y personal contratado en el marco de proyectos financiados por organismos multilaterales, detallando sus respectivas funciones y posición en el escalafón.

* **Tema**: Medio ambiente
* **Estándar referencia**: [Popolo](http://www.popoloproject.com/specs/)
* **Formatos**: JSON, XML, CSV
* **Ejemplo:**: http://www.popoloproject.com/examples/person.json

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Estaciones de Medición de la Calidad del Agua
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/calidad-agua/estaciones-medicion-calidad-agua.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/calidad-agua/estaciones-medicion-calidad-agua.xlsx)**

| estacion_id | estacion_nombre | estacion_region         | estacion_latitud | estacion_longitud | estacion_zonahoraria | estacion_tipo            | estacion_cuenca | estacion_subcuenca | estacion_fecha_desde | estacion_fecha_hasta | estacion_muestreos |
| ----------- | --------------- | ----------------------- | ---------------- | ----------------- | -------------------- | ------------------------ | --------------- | ------------------ | -------------------- | -------------------- | ------------------ |
| 1001        | Chapelco        | San Martin de Los Andes | -40.180854       | -71.318434        | UTC-3                | Agua Superficial - Fondo | Lago Lacar      |                    | 2010-01-06           | 2019-03-29           | 834 |

### Recurso: Elementos Contaminantes del Agua
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/calidad-agua/elementos-contaminantes-agua.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/calidad-agua/elementos-contaminantes-agua.xlsx)**

| contaminante_estacion_id | contaminante_cuenca | contaminante_subcuenca | contaminante_nombre    | contaminante_unidad | contaminante_actualizado | contaminante_valor | contaminante_validez |
| ------------------------ | ------------------- | ---------------------- | ---------------------- | ------------------- | ------------------------ | ------------------ | -------------------- |
| 1001                     | Lago Lacar          |                        | Potencial de hidrogeno |                     | 2019-03-29               | 7.1                | 5 días |

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases



Descargar clases en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/calidad-agua-clases.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/calidad-agua-clases.xlsx)**


| nombre       | descripcion |
| ------------ | ------------------------------------------------------------ |
| Estación     | Atributos del punto de medición de calidad del agua. |
| Contaminante | Atributos de la medición de un contaminante registrada en una estación. |

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/calidad-agua-campos.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/calidad-agua-campos.xlsx)**

### Recurso: Estaciones de Medición de la Calidad del Agua

| clase    | titulo               | tipo_dato    | descripcion                                              | ejemplo                  | estandar_mapeo          | notas |
| -------- | -------------------- | ------------ | -------------------------------------------------------- | ------------------------ | ----------------------- | ----------------------------------------- |
| Estación | estacion_id          | alfanumerico | Identificación de la estación.                           | 1001                     | schema:Thing            | |
| Estación | estacion_nombre      | alfanumerico | Nombre de la estación.                                   | Chapelco                 | schema:Thing            | |
| Estación | estacion_region      | alfanumerico | Nombre del país/provincia o localidad.                   | San Martin de Los Andes  | schema:Place            | |
| Estación | estacion_latitud     | fecha        | Coordenadas geograficas.                                 | -40.180854               | schema:GeoCoordinates   | Fecha de registro de la parcela |
| Estación | estacion_longitud    | numerico     | Coordenadas geograficas.                                 | -71.318434               | schema:GeoCoordinates   | |
| Estación | estacion_zonahoraria | texto        | Campo opcional para indicar la zona horaria.             | UTC-3                    | schema:BroadcastService | Descripción de las estructuras edificadas |
| Estación | estacion_tipo        | texto        | Describe si la estación es superficial o de profundidad. | Agua Superficial - Fondo | schema:Thing            | |
| Estación | estacion_cuenca      | alfanumerico | Nombre de la cuenca.                                     | Lago Lacar               | schema:Place            | |
| Estación | estacion_subcuenca   | alfanumerico | Nombre de la subcuenca.                                  |                          | schema:Place            | |
| Estación | estacion_fecha_desde | fecha        | Fecha de inicio de la medición.                          | 2010-01-06               | schema:Date             | |
| Estación | estacion_fecha_hasta | fecha        | Ultima fecha de medición.                                | 2019-03-29               | schema:Date             | |
| Estación | estacion_muestreos   | numerico     | Cantidad de muestreos realizados en el período.          | 834                      | schema:Thing            | |

### Recurso: Elementos Contaminantes del Agua

| clase        | titulo                   | tipo_dato    | descripcion                                    | ejemplo                | estandar_mapeo | notas |
| ------------ | ------------------------ | ------------ | ---------------------------------------------- | ---------------------- | -------------- | ----- |
| Contaminante | contaminante_estacion_id | alfanumerico | Identificación de la estación.                 | 1001                   | schema:Thing   | |
| Contaminante | contaminante_cuenca      | alfanumerico | Nombre de la cuenca.                           | Lago Lacar             | schema:Place   | |
| Contaminante | contaminante_subcuenca   | alfanumerico | Nombre de la subcuenca.                        |                        | schema:Place   | |
| Contaminante | contaminante_nombre      | alfanumerico | Nombre del contaminante que se esta midiendo.  | Potencial de hidrogeno | schema:Thing   | |
| Contaminante | contaminante_unidad      | alfanumerico | Unidad de medida en que se establece el valor. |                        | schema:Thing   | |
| Contaminante | contaminante_actualizado | fecha        | Fecha y hora de actualizado el valor.          | 2019-03-29             | schema:Date    | |
| Contaminante | contaminante_valor       | numerico     | Valor obtenido en la medición.                 | 7.1                    | schema:Thing   | |
| Contaminante | contaminante_validez     | alfanumerico | Indica la duración de validez del dato.        | 5 días                 | schema:Thing   | |

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
