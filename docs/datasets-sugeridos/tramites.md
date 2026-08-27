# Trámites

Un índice de trámites y procedimientos que se realicen ante el organismo, así como los requisitos y criterios de asignación para acceder a las prestaciones.

* **Tema**: Gobierno y sector público
* **Estándar referencia**: https://schema.org/
* **Formatos**: JSON, XML, CSV

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Trámites  
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/tramites/tramites.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/tramites/tramites.xlsx)**

| organizacion_id | organizacion_nombre       | tramite_id | tramite_nombre    | tramite_descripcion                                          | tramite_area_depende                | tramite_dias_semana | tramite_hora inicio | tramite_hora_fin | tramite_prerequisitos                                        | tramite_costo | tramite_area_direccion | tramite_web |
| --------------- | ------------------------- | ---------- | ----------------- | ------------------------------------------------------------ | ----------------------------------- | ------------------- | ------------------- | ---------------- | ------------------------------------------------------------ | ------------- | ---------------------- | ---------------------------------------------------- |
| 325             | Municipio de Bahia Blanca | 76         | Licencia Original | Si tramitás por primera vez una licencia, o se te venció hace más de 90 días, tenés que hacer el siguiente trámite. | Dirección de Tránsito y Transporte, | Lunes a Viernes     | 7:45                | 16:00            | Sacar turno para el Curso de Seguridad Vial ingresando a “Capacitación”. Solo principiantes o quienes tengan licencias vencidas hace más de 5 años. (Ingresar a Turnos de Licencia). Sacar turno para iniciar el trámite ingresando a “Solicitar Turno”. (Ingresar a Turnos de Licencia) Documento de Identidad: original y copia, con domicilio en el partido de Bahía Blanca. En caso de no tener el DNI, presentar constancia de DNI en trámite, con todos los datos, incluso el domicilio. Menores de 18 años: Deben tener autorización de padre y madre, o tutor, certificada por un Juez de Paz o un Escribano Público. Si alguno de los padres hubiera fallecido, hay que adjuntar el Certificado o partida de defunción, y la Partida de nacimiento o Libreta de Familia. El siguiente formulario debe completarse por duplicado. (Descargar formulario) Las fotos se toman en la Dirección General de Tránsito y Transporte al momento de presentación para sacar la licencia. Presentar la constancia de grupo sanguíneo, la cual podrá ser emitida por hospital público, o por un laboratorio privado. Abonar los sellados correspondientes. Licencias de clase C,D y E: El solicitante debe tener entre 21 y 65 años y un año de antigüedad con licencia clase B. en este caso se debe presentar un audiometría actualizada y certificado de antecedentes penales. | 1364          | Undiano 1165           | https://www.bahia.gob.ar/tramites/conducir/original/ |

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases



Descargar clases en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/tramites-clases.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/tramites-clases.xlsx)**


| nombre       | descripcion |
| ------------ | ---------------------------------------------------- |
| Organización | Atributos de la organización que presta el servicio. |
| Trámite      | Atributos del trámite disponible en la organización. |

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/tramites-campos.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/tramites-campos.xlsx)**

### Recurso: Trámites  

| clase        | titulo                 | tipo_dato    | descripcion                                                  | ejemplo                                                      | estandar_mapeo                          | notas |
| ------------ | ---------------------- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------------------------- | ----- |
| Organización | organizacion_id        | alfanumerico | Debe ser un identificador único para la organización. Se puede utilizar una codificacion en base al presupuesto; ej: Código jurisdicccion:+código sub jurisdicción:+ ... | 325                                                          | popolo:Organization schema:Organization | |
| Organización | organizacion_nombre    | alfanumerico | El nombre principal de la organización, por ejemplo su nombre legal | Municipio de Bahia Blanca                                    | popolo:Organization schema:Organization | |
| Trámite      | tramite_id             | alfanumerico | Un identificador único para el trámite                       | 76                                                           | schema:Thing                            | |
| Trámite      | tramite_nombre         | alfanumerico | Nombre del trámite                                           | Licencia Original                                            | schema:Thing                            | |
| Trámite      | tramite_descripcion    | texto        | Descripción del trámite                                      | Si tramitás por primera vez una licencia, o se te venció hace más de 90 días, tenés que hacer el siguiente trámite. | schema:Thing                            | |
| Trámite      | tramite_area_depende   | alfanumerico | Nombre del área de quien depende el trámite                  | Dirección de Tránsito y Transporte,                          | popolo:Organization schema:Organization | |
| Trámite      | tramite_dias_semana    | alfanumerico | Dias de la semana en que se puede realizar el tramite        | Lunes a Viernes                                              | schema:OpeningHours                     | |
| Trámite      | tramite_hora inicio    | hora         | Hora de inicio de atencion                                   | 7:45                                                         | schema:OpeningHours                     | |
| Trámite      | tramite_hora_fin       | hora         | Hora de cierre de atención                                   | 16:00                                                        | schema:OpeningHours                     | |
| Trámite      | tramite_prerequisitos  | texto        | Detalle de prerequisitos para realizar el trámite            | Sacar turno para el Curso de Seguridad Vial ingresando a “Capacitación”. Solo principiantes o quienes tengan licencias vencidas hace más de 5 años. (Ingresar a Turnos de Licencia). Sacar turno para iniciar el trámite ingresando a “Solicitar Turno”. (Ingresar a Turnos de Licencia) Documento de Identidad: original y copia, con domicilio en el partido de Bahía Blanca. En caso de no tener el DNI, presentar constancia de DNI en trámite, con todos los datos, incluso el domicilio. Menores de 18 años: Deben tener autorización de padre y madre, o tutor, certificada por un Juez de Paz o un Escribano Público. Si alguno de los padres hubiera fallecido, hay que adjuntar el Certificado o partida de defunción, y la Partida de nacimiento o Libreta de Familia. El siguiente formulario debe completarse por duplicado. (Descargar formulario) Las fotos se toman en la Dirección General de Tránsito y Transporte al momento de presentación para sacar la licencia. Presentar la constancia de grupo sanguíneo, la cual podrá ser emitida por hospital público, o por un laboratorio privado. Abonar los sellados correspondientes. Licencias de clase C,D y E: El solicitante debe tener entre 21 y 65 años y un año de antigüedad con licencia clase B. en este caso se debe presentar un audiometría actualizada y certificado de antecedentes penales. | schema:Thing:description                | |
| Trámite      | tramite_costo          | texto        | Detalles sobre el costo del tramite                          | 1364                                                         | schema:QuantitativeValue                | |
| Trámite      | tramite_area_direccion | alfanumerico | Dirección dónde se puede iniciar o consultar el trámite en persona | Undiano 1165                                                 | popolo:Organization schema:Organization | |
| Trámite      | tramite_web            | URI          | URL al sitio web dónde se puede iniciar y/o dar seguimiento al tramite | https://www.bahia.gob.ar/tramites/conducir/original/         | schema:Thing                            | |

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
