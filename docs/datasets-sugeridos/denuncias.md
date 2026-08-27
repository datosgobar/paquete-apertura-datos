# Denuncias

Mecanismos de presentación directa de solicitudes o denuncias a disposición del público en relación a acciones u omisiones del sujeto obligado.

* **Tema**: Gobierno y sector público
* **Estándar referencia**: https://schema.org/
* **Formatos**: JSON, XML, CSV
* **Ejemplo:**: http://www.popoloproject.com/examples/person.json

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Denuncias 
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/denuncias/denuncias.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/denuncias/denuncias.xlsx)**

| organizacion_id | organizacion_nombre       | denuncia_id | denuncia_fecha | denuncia_hora | denuncia_medio | denuncia_lugar_radicacion | denuncia_enlace_seguimiento       | denuncia_estado_actual | denuncia_direccion | denuncia_latitud | denuncia_longitud | denuncia_detalle                                           | denuncia_categoria | denuncia_tipo | denuncia_subtipo | denuncia_otra_clasificacion | denuncia_fecha_ultimo_cambio | denuncia_comentario_ultimo_cambio |
| --------------- | ------------------------- | ----------- | -------------- | ------------- | -------------- | ------------------------- | --------------------------------- | ---------------------- | ------------------ | ---------------- | ----------------- | ---------------------------------------------------------- | ------------------ | ------------- | ---------------- | --------------------------- | ---------------------------- | ---------------------------------- |
| 325             | Municipio de Bahia Blanca | 3384556     | 2019-03-12     | 14:45         | Página web     |                           | https://www.bahia.gob.ar/vecinos/ | Activo                 | Alsina 1600        | -38.705048       | -62.250596        | Cable se encuentra colgando desde la columna de alumbrado. | Alumbrado          | Cable Suelto  |                  |                             | 2019-03-15                   | Se envió equipo a reparar el cable |

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases



Descargar clases en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/denuncias-clases.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/denuncias-clases.xlsx)**


| nombre       | descripcion |
| ------------ | ------------------------------------------------------------ |
| Organización | Atributos de una organización a la cual o donde se realiza la denuncia. |
| Denuncia     | Atributos de la denuncia realizada por la persona en la organización. |

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/denuncias-campos.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/denuncias-campos.xlsx)**

### Recurso: Denuncias 

| clase        | titulo                            | tipo_dato    | descripcion                                                  | ejemplo                                                    | estandar_mapeo                          | notas |
| ------------ | --------------------------------- | ------------ | ------------------------------------------------------------ | ---------------------------------------------------------- | --------------------------------------- | ----- |
| Organización | organizacion_id                   | alfanumerico | Debe ser un identificador único para la organización. Se puede utilizar una codificacion en base al presupuesto; ej: Código jurisdicccion:+código sub jurisdicción:+ ... | 325                                                        | popolo:Organization schema:Organization | |
| Organización | organizacion_nombre               | alfanumerio  | El nombre principal de la organización, por ejemplo su nombre legal. | Municipio de Bahia Blanca                                  | popolo:Organization schema:Organization | |
| Denuncia     | denuncia_id                       | alfanumerico | Identificador de la denuncia realizada.                      | 3384556                                                    | schema:Thing                            | |
| Denuncia     | denuncia_fecha                    | fecha        | Fecha de la denuncia.                                        | 2019-03-12                                                 | schema:Thing                            | |
| Denuncia     | denuncia_hora                     | fecha        | Hora de la denuncia.                                         | 14:45                                                      | schema:Thing                            | |
| Denuncia     | denuncia_medio                    | alfanumerico | Indica de que forma fue realizada la denuncia                | Página web                                                 |                                         | |
| Denuncia     | denuncia_lugar_radicacion         | alfanumerico | Oficina o dependencia que recepciono la denuncia ya sea presencial, electrónica, telefónica u otro medio. |                                                            | schema:Thing                            | |
| Denuncia     | denuncia_enlace_seguimiento       | url          | De existir un enlace para hacer seguimiento a la denuncia, opcional | https://www.bahia.gob.ar/vecinos/                          | schema:Thing                            | |
| Denuncia     | denuncia_estado_actual            | alfanumerico | Ultimo estado de la denuncia                                 | Activo                                                     |                                         | |
| Denuncia     | denuncia_direccion                | alfanumerico | Dirección donde sucedió el hecho denunciado.                 | Alsina 1600                                                | schema:PostalAddress                    | |
| Denuncia     | denuncia_latitud                  | numerico     | Latitud donde sucedió el hecho denunciado.                   | -38.705048                                                 | schema:GeoCoordinates                   | |
| Denuncia     | denuncia_longitud                 | numerico     | Longitud donde sucedió el hecho denunciado.                  | -62.250596                                                 | schema:GeoCoordinates                   | |
| Denuncia     | denuncia_detalle                  | texto        | Detalle brindado por el denunciante al realizar la denuncia. | Cable se encuentra colgando desde la columna de alumbrado. | schema:Thing                            | |
| Denuncia     | denuncia_categoria                | alfanumerico | Categoría o clasificación del hecho denunciado.              | Alumbrado                                                  | schema:Thing                            | |
| Denuncia     | denuncia_tipo                     | alfanumerico | Tipo de denuncia (esto es una clasificación más específica que "categoría"). | Cable Suelto                                               | schema:Thing                            | |
| Denuncia     | denuncia_subtipo                  | alfanumerico | Subtipo de denuncia (esto es una clasificación más específica que "tipo", si aplica). |                                                            | schema:Thing                            | |
| Denuncia     | denuncia_otra_clasificacion       | alfanumerico | Categoría o clasificación alternativa del hecho denunciado.  |                                                            | schema:Thing                            | |
| Denuncia     | denuncia_fecha_ultimo_cambio      | fecha        | Fecha de la última modificación que sufrió la denuncia.      | 2019-03-15                                                 | schema:Date                             | |
| Denuncia     | denuncia_comentario_ultimo_cambio | texto        | Comentario agregado a la denuncia en el último cambio.       | Se envió equipo a reparar el cable                         | schema:Thing                            | |

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
