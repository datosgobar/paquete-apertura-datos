# Permisos

Los permisos, concesiones y autorizaciones otorgados y sus titulares.

* **Tema**: Gobierno y sector público
* **Estándar referencia**: https://schema.org/
* **Formatos**: CSV

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Permisos  
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/permisos/permisos.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/permisos/permisos.xlsx)**

| entidad_id    | entidad_nombre   | permiso_id | permiso_tipo       | permiso_subtipo     | permiso_inicio | permiso_fin | permiso_detalles                         | permiso_area      | permiso_geo                                                  | permiso_provincia | permiso_localidad | permiso_resolucion_enlace | permiso_es_prorroga | permiso_id_padre | participacion_exacta |
| ------------- | ---------------- | ---------- | ------------------ | ------------------- | -------------- | ----------- | ---------------------------------------- | ----------------- | ------------------------------------------------------------ | ----------------- | ----------------- | ------------------------- | ------------------- | ---------------- | -------------------- |
| 30-70911317-2 | Minera del Plata | 112440     | Explotación Minera | Extracción de plata | 2019-06-01     | 2029-06-01  | Con fecha .... se otorga el permiso .... | RP4 - RP50 - RP49 | {"type":"FeatureCollection","features":[{"type":"Feature","properties":{},"geometry":{"type":"Polygon","coordinates":[[[-69.19189453125,-42.48830197960225],[-68.97216796875,-42.48830197960225],[-68.97216796875,-42.35854391749705],[-69.19189453125,-42.35854391749705],[-69.19189453125,-42.48830197960225]]]}}]} | Chubut            | Gastre            |                           | No                  |                  | 40 |

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases



Descargar clases en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/permisos-clases.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/permisos-clases.xlsx)**


| nombre       | descripcion |
| ------------ | ------------------------------------------------------------ |
| Organización | Atributos de la organización o empresa que obtiene el permiso o concesión. |
| Permiso      | Atributos de un permiso o concesión otorgado a una organización o empresa. |

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/permisos-campos.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/permisos-campos.xlsx)**

### Recurso: Permisos  

| clase         | titulo                    | tipo_dato    | descripcion                                                  | ejemplo                                                      | estandar_mapeo                          | notas |
| ------------- | ------------------------- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------------------------- | ------------------------------------------- |
| Organización  | entidad_id                | alfanumerico | Identificacion de la organización/empresa que obtiene el permiso. | 30-70911317-2                                                | popolo:Organization schema:Organization | |
| Organización  | entidad_nombre            | alfanumerico | Nombre de la organización/empresa que tiene el permiso.      | Minera del Plata                                             | popolo:Organization schema:Organization | |
| Permiso       | permiso_id                | alfanumerico | Identificación del permiso.                                  | 112440                                                       | schema:GovernmentPermit                 | |
| Permiso       | permiso_tipo              | alfanumerico | Tipo de permiso.                                             | Explotación Minera                                           | schema:Thing                            | |
| Permiso       | permiso_subtipo           | alfanumerico | Otras clasificaciones.                                       | Extracción de plata                                          | schema:Thing                            | Categorizar dependiendo del tipo de permiso |
| Permiso       | permiso_inicio            | fecha        | Fecha de inicio del permiso/concesión.                       | 2019-06-01                                                   | schema:GovernmentPermit                 | |
| Permiso       | permiso_fin               | fecha        | Fecha de fin del permiso/concesión.                          | 2029-06-01                                                   | schema:GovernmentPermit                 | |
| Permiso       | permiso_detalles          | texto        | Descripción al detalle del permiso/concesión.                | Con fecha .... se otorga el permiso ....                     | schema:Thing                            | |
| Permiso       | permiso_area              | alfanumerico | Area dónde se realiza la actividad.                          | RP4 - RP50 - RP49                                            | schema:Place                            | |
| Permiso       | permiso_geo               | geografico   | geoJson u otro formato de georeferenciación del área geográfica donde se realiza la actividad. | {"type":"FeatureCollection","features":[{"type":"Feature","properties":{},"geometry":{"type":"Polygon","coordinates":[[[-69.19189453125,-42.48830197960225],[-68.97216796875,-42.48830197960225],[-68.97216796875,-42.35854391749705],[-69.19189453125,-42.35854391749705],[-69.19189453125,-42.48830197960225]]]}}]} | schema:Place                            | |
| Permiso       | permiso_provincia         | alfanumerico | Provincia dónde se realiza la actividad.                     | Chubut                                                       | schema:PostalAddress                    | |
| Permiso       | permiso_localidad         | alfanumerico | Localidad dónde se realiza la actividad.                     | Gastre                                                       | schema:PostalAddress                    | |
| Permiso       | permiso_resolucion_enlace | url          | Enlace a la resolución que otorga el permiso/concesión/autorización. |                                                              | schema:Permit                           | |
| Permiso       | permiso_es_prorroga       | booleano     | Indica si los datos corresponden a una prórroga o al permiso/concesión original. | No                                                           |                                         | |
| Permiso       | permiso_id_padre          | alfanumerico | En caso de ser una prorroga, el Id de la concesión original. |                                                              | schema:GovernmentPermit                 | |
| Participacion | participacion_exacta      | numerico     | Porcentaje exacto de la participación.                       | 40                                                           | BO:Share                                | |

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
