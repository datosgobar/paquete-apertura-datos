---
title: "Calidad del Aire"
---

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Estaciones de Medición de la Calidad del Aire
**[CSV](/paquete-apertura-datos/datasets-sugeridos/calidad-aire/estaciones-medicion-calidad-aire.csv)** | **[XLSX](/paquete-apertura-datos/datasets-sugeridos/calidad-aire/estaciones-medicion-calidad-aire.xlsx)**

| estacion_id | estacion_nombre | estacion_region         | estacion_latitud  | estacion_longitud | estacion_zonahoraria |
| ----------- | --------------- | ----------------------- | ----------------- | ----------------- | -------------------- |
| 1001        | Chapelco        | San Martin de Los Andes | -40.1808541022993 | -71.31843         | UTC-3 |

### Recurso: Elementos Contaminantes del Aire
**[CSV](/paquete-apertura-datos/datasets-sugeridos/calidad-aire/elementos-contaminantes-aire.csv)** | **[XLSX](/paquete-apertura-datos/datasets-sugeridos/calidad-aire/elementos-contaminantes-aire.xlsx)**

| contaminante_estacion_id | contaminante_nombre | contaminante_unidad | contaminante_actualizado | contaminante_valor | contaminante_validez |
| ------------------------ | ------------------- | ------------------- | ------------------------ | ------------------ | -------------------- |
| 1001                     | Dióxido de azufre   | µg/m3               | 2019-02-26 0:00:00       | 0.27               | 1 hora |

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases



Descargar clases en **[CSV](/paquete-apertura-datos/datasets-sugeridos/calidad-aire-clases.csv)** | **[XLSX](/paquete-apertura-datos/datasets-sugeridos/calidad-aire-clases.xlsx)**


| nombre       | descripcion |
| ------------ | ------------------------------------------------------------ |
| Estación     | Atributos del punto de medición de calidad del aire. |
| Contaminante | Atributos de la medición de un contaminante registrada en una estación. |

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](/paquete-apertura-datos/datasets-sugeridos/calidad-aire-campos.csv)** | **[XLSX](/paquete-apertura-datos/datasets-sugeridos/calidad-aire-campos.xlsx)**

### Recurso: Estaciones de Medición de la Calidad del Aire

| clase    | titulo               | tipo_dato    | descripcion                                 | ejemplo                 | estandar_mapeo          | notas |
| -------- | -------------------- | ------------ | ------------------------------------------- | ----------------------- | ----------------------- | ----- |
| Estacion | estacion_id          | alfanumerico | Identificación de la estación               | 1001                    | schema:Thing            | |
| Estacion | estacion_nombre      | alfanumerico | Nombre de la estación                       | Chapelco                | schema:Thing            | |
| Estacion | estacion_region      | alfanumerico | Nombre del país/provincia o localidad       | San Martin de Los Andes | schema:Place            | |
| Estacion | estacion_latitud     | numerico     | Coordenadas geograficas                     | -40.1808541022993       | schema:GeoCoordinates   | |
| Estacion | estacion_longitud    | numerico     | Coordenadas geograficas                     | -71.31843               | schema:GeoCoordinates   | |
| Estacion | estacion_zonahoraria | alfanumerico | Campo opcional para indicar la zona horaria | UTC-3                   | schema:BroadcastService | |

### Recurso: Elementos Contaminantes del Aire

| clase        | titulo                   | tipo_dato    | descripcion                                   | ejemplo            | estandar_mapeo        | notas |
| ------------ | ------------------------ | ------------ | --------------------------------------------- | ------------------ | --------------------- | ----- |
| Contaminante | contaminante_estacion_id | alfanumerico | Identificación de la estación                 | 1001               | schema:Thing          | |
| Contaminante | contaminante_nombre      | alfanumerico | Nombre del contaminante que se esta midiendo  | Dióxido de azufre  | schema:GeoCoordinates | |
| Contaminante | contaminante_unidad      | alfanumerico | Unidad de medida en que se establece el valor | µg/m3              | schema:GeoCoordinates | |
| Contaminante | contaminante_actualizado | fecha        | Fecha y hora de actualizado el valor          | 2019-02-26 0:00:00 | schema:Date           | |
| Contaminante | contaminante_valor       | numerico     | Valor obtenido en la medición                 | 0.27               | schema:Thing          | |
| Contaminante | contaminante_validez     | alfanumerico | Indica la duración de validez del dato        | 1 hora             | schema:Thing          | |

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
