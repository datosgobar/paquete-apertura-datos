# Normativa

Todas las leyes, decretos, resoluciones, ordenanzas, acordadas y estatutos estatutos municipales sancionados por el Honorable Concejo Deliberante.

* **Tema**: Justicia, seguridad y legales
* **Estándar referencia**: Akoma Ntoso
* **Formatos**: XML
* **Ejemplo:**: http://docs.oasis-open.org/legaldocml/akn-nc/v1.0/akn-nc-v1.0.html, http://docs.oasis-open.org/legaldocml/akn-core/v1.0/akn-core-v1.0-part2-specs.html

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Normas    
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/normativa/normas.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/normativa/normas.xlsx)**

| norma_id | norma_tipo | norma_numero | norma_nombre | norma_organismo_origen | norma_fecha_sancion | norma_fecha_boletin | norma_numero_boletin | norma_pagina_boletin | norma_texto_resumido | norma_observaciones | norma_url_original | norma_url_texto_actual | norma_modificada_por | norma_modifica_a | norma_region |
| -------- | ---------- | ------------ | ------------ | ---------------------- | ------------------- | ------------------- | -------------------- | -------------------- | -------------------- | ------------------- | ------------------ | ---------------------- | -------------------- | ---------------- | ------------ |
|          |            |              |              |                        |                     |                     |                      |                      |                      |                     |                    |                        |                      |                  | |

### Recurso: Artículos 
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/normativa/articulos.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/normativa/articulos.xlsx)**

| articulo_norma_id | articulo_norma_fecha_sancion | articulo_numero | articulo_secuencia | articulo_titulo | articulo_texto | articulo_notas |
| ----------------- | ---------------------------- | --------------- | ------------------ | --------------- | -------------- | -------------- |
|                   |                              |                 |                    |                 |                | |

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases



Descargar clases en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/normativa-clases.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/normativa-clases.xlsx)**


| nombre   | descripcion |
| -------- | ------------------------------------------------------------ |
| Norma    | Atributos de un elemento normativo (ley, decreto, disposición, etc). |
| Artículo | Atributos de un artículo perteneciente al cuerpo de un elemento normativo. |

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/normativa-campos.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/normativa-campos.xlsx)**

### Recurso: Normas    

| clase | titulo                 | tipo_dato    | descripcion                                                | ejemplo | estandar_mapeo      | notas |
| ----- | ---------------------- | ------------ | ---------------------------------------------------------- | ------- | ------------------- | ----- |
| Norma | norma_id               | numérico     | Identificador único de la norma                            |         | akn:identification  | |
| Norma | norma_tipo             | alfanumérico | Tipo de norma                                              |         | akn:akomantosoType  | |
| Norma | norma_numero           | numérico     | Número asignado a la norma                                 |         | akn:FRBRnumber      | |
| Norma | norma_nombre           | alfanumérico | Nombre o título resumido                                   |         | akn:docTitle        | |
| Norma | norma_organismo_origen | alfanumérico | Nombre del organismo que la origina                        |         | akn:TLCorganization | |
| Norma | norma_fecha_sancion    | fecha        | Fecha en la que se sanciona la norma                       |         | akn:docDate         | |
| Norma | norma_fecha_boletin    | fecha        | Fecha de publicación en el boletón oficial                 |         | akn:docDate         | |
| Norma | norma_numero_boletin   | numérico     | Numero del boletín en el cual se publica la norma          |         | akn:num             | |
| Norma | norma_pagina_boletin   | numérico     | Página del boletin en el cual se publica la norma          |         | akn:num             | |
| Norma | norma_texto_resumido   | texto        | Resumen del texto de la norma para el boletín              |         | akn:paragraph       | |
| Norma | norma_observaciones    | texto        | Texto con información adicional sobre la norma             |         | akn:summary         | |
| Norma | norma_url_original     | url          | Enlace al texto original de la norma                       |         | akn:linkType        | |
| Norma | norma_url_texto_actual | url          | Enlace al texto actual modificado de la norma              |         | akn:linkType        | |
| Norma | norma_modificada_por   | numérico     | Identificador de la norma que modifica a esta              |         | akn:overrules       | |
| Norma | norma_modifica_a       | numérico     | Identificador de la norma a la cual se modifica            |         | akn:afectedDocument | |
| Norma | norma_region           | alfanumérico | Nombre de la provincia / ciudad donde se promulga la norma |         | akn:TLClocation     | |

### Recurso: Artículos 

| clase    | titulo                       | tipo_dato    | descripcion                          | ejemplo | estandar_mapeo       | notas |
| -------- | ---------------------------- | ------------ | ------------------------------------ | ------- | -------------------- | ----- |
| Articulo | articulo_norma_id            | numérico     | Identificador único de la norma      |         | akn:identification   | |
| Articulo | articulo_norma_fecha_sancion | fecha        | Fecha en la que se sanciona la norma |         | akn:docDate          | |
| Articulo | articulo_numero              | numérico     | Numero del articulo                  |         | akn:FRBRnumber       | |
| Articulo | articulo_secuencia           | alfanumerico | Secuencia del articulo               |         | akn:num              | |
| Articulo | articulo_titulo              | alfanumerico | Titulo del artículo                  |         | akn:docTitle         | |
| Articulo | articulo_texto               | texto        | Texto del artículo                   |         | akn:amendmentContent | |
| Articulo | articulo_notas               | texto        | Notas del artículo                   |         | akn:summary          | |

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
