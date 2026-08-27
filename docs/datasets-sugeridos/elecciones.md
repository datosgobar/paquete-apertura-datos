# Resultados Electorales

Resultados de las últimas elecciones municipales o provinciales desagregadas por mesas electorales.

* **Tema**: Gobierno y sector público
* **Estándar referencia**: Election data format (Open Data Institute)
* **Formatos**: CSV
* **Ejemplo:**: https://github.com/theodi/election-data-format/blob/gh-pages/tables/index.md


<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Elecciones
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/elecciones/elecciones.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/elecciones/elecciones.xlsx)**

| eleccion_id | eleccion_nombre                                 | eleccion_tipo                | eleccion_fecha_inicio | elección_fecha_fin |
| ----------- | ----------------------------------------------- | ---------------------------- | --------------------- | ------------------ |
| GenCor2019  | Elecciones Generales de la Provincia de Córdoba | Gobernador y Vice Gobernador | 2019-05-12            | 2019-05-12 |

### Recurso: Resultados Electorales por Opción Elegible Disponible
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/elecciones/resultados-electorales-por-opcion-elegible-disponible.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/elecciones/resultados-electorales-por-opcion-elegible-disponible.xlsx)**

| opcion_eleccion_id | opcion_region_id | opcion_region_nombre | opcion_partido_id | opcion_partido_nombre | opcion_candidato_id | opcion_candidato_nombre | opcion_candidato_votos | resultado_elegido | resultado_orden |
| ------------------ | ---------------- | -------------------- | ----------------- | --------------------- | ------------------- | ----------------------- | ---------------------- | ----------------- | --------------- |
| GenCor2019         | AR-X             | Provincia de Córdoba | 4                 | Encuentro por Córdoba | 1                   | Juan Martinez           | 5000                   | No                | 10 |

### Recurso: Resultados Electorales por Mesa y Opción Elegible Disponible
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/elecciones/resultados-electorales-por-mesa-opcion-elegible-disponible.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/elecciones/resultados-electorales-por-mesa-opcion-elegible-disponible.xlsx)**

| resultado_eleccion_id | resultado_region_id | resultado_circuito_id | resultado_mesa_id | resultado_partido_id | resultado_candidato_id | resultado_opcion_candidato_id | resultado_votos_obtenidos |
| --------------------- | ------------------- | --------------------- | ----------------- | -------------------- | ---------------------- | ----------------------------- | ------------------------- |
| GenCor2019            | AR-X                | 32                    | 1                 | 4                    | 1                      | 9009                          | 26 |

### Recurso: Resumen de Resultados Electorales por Mesa
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/elecciones/resumen-resultados-electorales-por-mesa.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/elecciones/resumen-resultados-electorales-por-mesa.xlsx)**

| resumen_eleccion_id | resumen_region_id | resultado_circuito_id | resumen_mesa_id | resumen_votos_anulados | resumen_votos_en_blanco | resumen_votos_otro_estado | resumen_votos_emitidos |
| ------------------- | ----------------- | --------------------- | --------------- | ---------------------- | ----------------------- | ------------------------- | ---------------------- |
| GenCor2019          | AR-X              | 32                    | 1               | 25                     | 180                     |                           | 1207 |

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases



Descargar clases en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/elecciones-clases.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/elecciones-clases.xlsx)**


| nombre           | descripcion |
| ---------------- | ------------------------------------------------------------ |
| Elección         | Atributos de un ejercicio electoral determinado. |
| Opción           | Atributos de una opción elegible disponible en un ejercicio electoral determinado. |
| Resultado        | Atributos del resultado electoral sobre una opción elegible disponible en un ejercicio electoral determinado. |
| Resumen por mesa | Atributos del resumen de una mesa electoral (que incluye la cantidad de votantes que asistieron, votos positivos, votos en blanco, etc pero no incluye los resultados electorales por opción elegible disponible). |

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/elecciones-campos.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/elecciones-campos.xlsx)**

### Recurso: Elecciones

| clase    | titulo                | tipo_dato    | descripcion                               | ejemplo                                         | estandar_mapeo | notas |
| -------- | --------------------- | ------------ | ----------------------------------------- | ----------------------------------------------- | -------------- | ----- |
| Eleccion | eleccion_id           | alfanumérico | Identificacón única del acto eleccionario | GenCor2019                                      | edf:Contest    | |
| Eleccion | eleccion_nombre       | alfanumérico | Nombre de la elección                     | Elecciones Generales de la Provincia de Córdoba | edf:Contest    | |
| Eleccion | eleccion_tipo         | alfanumérico | Tipo de elección                          | Gobernador y Vice Gobernador                    | edf:Contest    | |
| Eleccion | eleccion_fecha_inicio | fecha        | Fecha de inicio de la elección            | 2019-05-12                                      | edf:Contest    | |
| Eleccion | elección_fecha_fin    | fecha        | Fecha de fin de la elección               | 2019-05-12                                      | edf:Contest    | |

### Recurso: Resultados Electorales por Opción Elegible Disponible

| clase     | titulo                  | tipo_dato    | descripcion                                                  | ejemplo               | estandar_mapeo | notas |
| --------- | ----------------------- | ------------ | ------------------------------------------------------------ | --------------------- | -------------- | ------------------------------------------------------------ |
| Opcion    | opcion_eleccion_id      | alfanumérico | URI unica que identifique el acto eleccionario               | GenCor2019            | edf:Choices    | |
| Opcion    | opcion_region_id        | alfanumérico | URI que identifica la region donde se realiza la elección. xx:yy:zzzz donde xx corresponde al codigo de provincia, yy corresponde al código de departamento, zzzz corresponde al codigo de localidad. En caso de no existir un codigo electoral se puede usar la codificación ISO 3166-2 | AR-X                  | edf:Choices    | |
| Opcion    | opcion_region_nombre    | alfanumérico | Nombre de la región                                          | Provincia de Córdoba  | edf:Choices    | |
| Opcion    | opcion_partido_id       | alfanumérico | URI identificando al partido                                 | 4                     | edf:Choices    | |
| Opcion    | opcion_partido_nombre   | alfanumérico | Nombre del partido                                           | Encuentro por Córdoba | edf:Choices    | |
| Opcion    | opcion_candidato_id     | alfanumérico | URI identificando al candidato                               | 1                     | edf:Choices    | |
| Opcion    | opcion_candidato_nombre | alfanumérico | Nombre del candidato                                         | Juan Martinez         | edf:Choices    | |
| Opcion    | opcion_candidato_votos  | numérico     | Cantidad de votos obtenidos por el candidato.                | 5000                  | edf:Choices    | |
| Resultado | resultado_elegido       | booleano     | Indica si el candidato fue elegido o no                      | No                    | edf:Results    | Este valor en el estandar se ubica dentro del resultado, pero a los efectos de esta propuesta corresponde que se ubique a nivel del candidato |
| Resultado | resultado_orden         | numérico     | Campo que permite ordenar el resultado de la elección        | 10                    | edf:Results    | Este valor en el estandar se ubica dentro del resultado, pero a los efectos de esta propuesta corresponde que se ubique a nivel del candidato |

### Recurso: Resultados Electorales por Mesa y Opción Elegible Disponible

| clase     | titulo                        | tipo_dato    | descripcion                                                  | ejemplo    | estandar_mapeo | notas |
| --------- | ----------------------------- | ------------ | ------------------------------------------------------------ | ---------- | -------------- | ------------------------------------------------------------ |
| Resultado | resultado_eleccion_id         | alfanumérico | Identificacón única del acto eleccionario                    | GenCor2019 | edf:Results    | |
| Resultado | resultado_region_id           | alfanumérico | Identifica la region donde se realiza la elección. xx:yy:zzzz donde xx corresponde al codigo de provincia, yy corresponde al código de departamento, zzzz corresponde al codigo de localidad. | AR-X       | edf:Results    | |
| Resultado | resultado_circuito_id         | alfanumérico | Indica circuito de votación                                  | 32         | schema:Thing   | |
| Resultado | resultado_mesa_id             | alfanumérico | Indica la mesa de votación                                   | 1          | schema:Thing   | Se agrega la mesa de votación para conocer los resultados a un nivel mas desagregado. |
| Resultado | resultado_partido_id          | alfanumérico | Identificación única del partido                             | 4          | edf:Results    | |
| Resultado | resultado_candidato_id        | alfanumérico | Identificación única del candidato                           | 1          | edf:Results    | |
| Resultado | resultado_opcion_candidato_id | alfanumérico | Identifica la hoja de votación o lista a la que pertenece el candidato | 9009       | edf:Results    | |
| Resultado | resultado_votos_obtenidos     | numérico     | Cantidad de votos obtenidos por el candidato en esa lista    | 26         | edf:Results    | |

### Recurso: Resumen de Resultados Electorales por Mesa

| clase            | titulo                    | tipo_dato    | descripcion                                                  | ejemplo    | estandar_mapeo | notas |
| ---------------- | ------------------------- | ------------ | ------------------------------------------------------------ | ---------- | -------------- | ----- |
| Resultado        | resumen_eleccion_id       | alfanumérico | Identificacón única del acto eleccionario                    | GenCor2019 | schema:Thing   | |
| Resultado        | resumen_region_id         | alfanumérico | Identifica la region donde se realiza la elección. xx:yy:zzzz donde xx corresponde al codigo de provincia, yy corresponde al código de departamento, zzzz corresponde al codigo de localidad. | AR-X       | schema:Thing   | |
| Resultado        | resultado_circuito_id     | alfanumérico | Indica circuito de votación                                  | 32         | schema:Thing   | |
| Resultado        | resumen_mesa_id           | alfanumérico | Indica la mesa de votación                                   | 1          | schema:Thing   | |
| Resumen por mesa | resumen_votos_anulados    | numérico     | Cantidad de votos anulados en la mesa receptora de votos     | 25         | schema:Thing   | |
| Resumen por mesa | resumen_votos_en_blanco   | numérico     | Cantidad de votos en blanco en la mesa receptora de votos    | 180        | schema:Thing   | |
| Resumen por mesa | resumen_votos_otro_estado | numérico     | Cantidad de votos con otro estado en la mesa receptora de votos |            | schema:Thing   | |
| Resumen por mesa | resumen_votos_emitidos    | alfanumérico | Total de votos emitidos se compone del total de los votos del resumen por mesa mas los votos obtenidos por cada opcion | 1207       | schema:Thing   | |

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
