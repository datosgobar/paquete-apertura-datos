# Contrataciones Públicas

Listado de todos los procesos de contratación, los procesos de contratación de obras deberían tener un enlace a sus obras, con el fin de poder agrupar todos los contratos de una obra dada (diseño, construccion, fiscalización).

* **Tema**: Gobierno y sector público
* **Estándar referencia**: [Open Contracting Data Standard]( http://standard.open-contracting.org/latest/en/)
* **Formatos**: JSON, XML, CSV
* **Ejemplo:**: http://standard.open-contracting.org/latest/en/schema/merging/, https://github.com/open-contracting/sample-data/blob/master/flat-template/template/

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Convocatorias
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/contrataciones-publicas/convocatorias.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/contrataciones-publicas/convocatorias.xlsx)**

| convocatoria_ocds_id | convocatoria_id | convocatoria_titulo       | convocatoria_descripcion                           | convocatoria_estado | convocatoria_entidad_compradora | convocatoria_valor | convocatoria_valor_minimo | convocatoria_metodo_compra | convocatoria_metodo_detalles                | convocatoria_metodo_justificacion | convocatoria_categoria_compra | convocatoria_categorias_adicionales | convocatoria_criterio_adjudicacion | convocatoria_criterio_adjudicacion_detalles   | convocatoria_recepcion  | convocatoria_recepcion_detalles                              | convocatoria_periodo_inicio | convocatoria_periodo_fin | convocatoria_fecha_limite | convocatoria_duracion_dias | convocatoria_consultas_inicio | convocatoria_consultas_fin | convocatoria_tiene_consultas | convocatoria_criterio_elegibilidad                           | convocatoria_periodo_evaluacion | convocatoria_periodo_contrato |
| -------------------- | --------------- | ------------------------- | -------------------------------------------------- | ------------------- | ------------------------------- | ------------------ | ------------------------- | -------------------------- | ------------------------------------------- | --------------------------------- | ----------------------------- | ----------------------------------- | ---------------------------------- | --------------------------------------------- | ----------------------- | ------------------------------------------------------------ | --------------------------- | ------------------------ | ------------------------- | -------------------------- | ----------------------------- | -------------------------- | ---------------------------- | ------------------------------------------------------------ | ------------------------------- | ----------------------------- |
| ocds-twb234-0005     | 3568999         | Licitación Pública 3/2019 | Servicio de soporte de infraestructura informática | Activa              | Ministerio de modernización     | 2000000            | 800000                    | Abierta                    | Todos los interesados pueden enviar ofertas |                                   | Servicios                     | Servicios de consultoria            | Mejor propuesta                    | 60% Propuesta Tecnica 40% Propuesta Económica | En persona, Electrónica | Las propuestas se reciben en Mesa de entrada de la calle ..... y por correo electrónico en la cuenta .... o puede ingresarlas al sistema ... | 2019-03-05                  | 2019-03-20               | 2019-03-25                | 15                         | 2019-03-05                    | 2019-03-15                 | Si                           | 10 puntos por experiencia empresarial 50 puntos por experiencia del equipo 40 puntos por precio | 2019-04-15                      | 2 años |

### Recurso: Adjudicaciones
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/contrataciones-publicas/adjudicaciones.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/contrataciones-publicas/adjudicaciones.xlsx)**

| adjudicacion_ocds_id | adjudicacion_id | adjudicacion_estado | adjudicacion_fecha | adjudicacion_proveedor_id | adjudicacion_proveedor_nombre | adjudicacion_moneda | adjudicacion_importe |
| -------------------- | --------------- | ------------------- | ------------------ | ------------------------- | ----------------------------- | ------------------- | -------------------- |
| ocds-twb234-0005     | 3568999         | Activo              | 2019-03-16         | 30628707093               | HAL2000                       | ARS                 | 2000000 |

### Recurso: Contratos 
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/contrataciones-publicas/contratos.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/contrataciones-publicas/contratos.xlsx)**

| contrato_id | contrato_adjudicacion_id | contrato_titulo           | contrato_descripcion                               | contrato_estado | contrato_periodo_inicio | contrato_periodo_fin | contrato_fecha_firma | adjudicacion_moneda | contrato_importe |
| ----------- | ------------------------ | ------------------------- | -------------------------------------------------- | --------------- | ----------------------- | -------------------- | -------------------- | ------------------- | ---------------- |
| 3568999-1   | 3568999                  | Licitación Pública 3/2019 | Servicio de soporte de infraestructura informática | Activa          | 2019-05-01              | 2021-04-30           | 2019-04-15           | ARS                 | 2000000 |

### Recurso: Transacciones
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/contrataciones-publicas/transacciones.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/contrataciones-publicas/transacciones.xlsx)**

| transaccion_id | transaccion_contrato_id | transaccion_adjudicacion_id | transaccion_fuente  | transaccion_fecha | transaccion_moneda | transaccion_importe | transaccion_origen          | transaccion_destino |
| -------------- | ----------------------- | --------------------------- | ------------------- | ----------------- | ------------------ | ------------------- | --------------------------- | ------------------- |
| 896655273      | 3568999-1               | 3568999                     | Prestamo BID AR1505 | 2019-05-31        | ARS                | 150000              | Ministerio de modernización | HAL2000 |

### Recurso: Items Adquiridos
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/contrataciones-publicas/items-adquiridos.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/contrataciones-publicas/items-adquiridos.xlsx)**

| convocatoria_ocds_id | item_etapa_id | item_id | item_descripcion        | item_clasificacion                  | item_cantidad | item_unidad |
| -------------------- | ------------- | ------- | ----------------------- | ----------------------------------- | ------------- | ----------- |
| ocds-twb234-0005     |               | 3245    | Servicio de consultoria | Soporte y mantenimiento de hardware | 1             | Cantidad |

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases

Una institución pública abre una `Convocatoria` para recibir ofertas de provisión de bienes y servicios. Una vez elegida una oferta realiza la `Adjudicación` al proveedor elegido con el que celebra un `Contrato` que marca las condiciones bajo las cuales se realiza una `Transacción` entre las partes mediante la cual se adquiere un `Item`.

Descargar clases en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/contrataciones-publicas-clases.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/contrataciones-publicas-clases.xlsx)**


| nombre       | descripcion |
| ------------ | ------------------------------------------------------------ |
| Convocatoria | Atributos del proceso que abre una institución pública en el que declara la necesidad de adquirir bienes o servicios y las condiciones para recibir ofertas de terceros que los provean. |
| Adjudicación | Atributos de la adjudicación del proceso de compra a un tercero que previamente ofertó en la etapa de convocatoria, y cuya oferta fue elegida. |
| Contrato     | Atributos del instrumento contractual firmado por las partes para legalizar las condiciones de provisión de los bienes o servicios adquiridos. |
| Transacción  | Atributos de las transacciones realizadas en el cumplimiento del contrato firmado para la provisión de bienes y servicios. |
| Item         | Atributos de los items adquiridos en las transacciones entre el proveedor y la institución pública compradora. |

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/contrataciones-publicas-campos.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/contrataciones-publicas-campos.xlsx)**

### Recurso: Convocatorias

| clase        | titulo                                      | tipo_dato    | descripcion                                                  | ejemplo                                                      | estandar_mapeo | notas |
| ------------ | ------------------------------------------- | ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------- | ----- |
| Convocatoria | convocatoria_ocds_id                        | alfanumérico | Identificador universal de open contracting.                 | ocds-twb234-0005                                             | ocds:Release   | |
| Convocatoria | convocatoria_id                             | alfanumérico | Identificador utilizado internamente para identificar la convocatoria. | 3568999                                                      | ocds:Release   | |
| Convocatoria | convocatoria_titulo                         | alfanumérico | Título de la convocatoria.                                   | Licitación Pública 3/2019                                    | ocds:Release   | |
| Convocatoria | convocatoria_descripcion                    | texto        | Detalle de lo que se desea adquirir.                         | Servicio de soporte de infraestructura informática           | ocds:Release   | |
| Convocatoria | convocatoria_estado                         | alfanumérico | Estado actual de la convocatoria.                            | Activa                                                       | ocds:Release   | |
| Convocatoria | convocatoria_entidad_compradora             | alfanumérico | Nombre de la organización responsable de la adquisición.     | Ministerio de modernización                                  | ocds:Release   | |
| Convocatoria | convocatoria_valor                          | numérico     | Valor máximo que se va a pagar por la compra.                | 2000000                                                      | ocds:Release   | |
| Convocatoria | convocatoria_valor_minimo                   | numérico     | Valor mínimo que se asegura se va a pagar por la compra.     | 800000                                                       | ocds:Release   | |
| Convocatoria | convocatoria_metodo_compra                  | alfanumérico | Método de compra.                                            | Abierta                                                      | ocds:Release   | |
| Convocatoria | convocatoria_metodo_detalles                | alfanumérico | Detalles adicionales sobre el método de adquisición utilizado. Este campo se puede usar para proporcionar el nombre local del método de adquisición particular utilizado. | Todos los interesados pueden enviar ofertas                  | ocds:Release   | |
| Convocatoria | convocatoria_metodo_justificacion           | alfanumérico | Justificación del método de contratación elegido. Es importante en caso de adjudicaciones directas o de ofertas limitadas. |                                                              | ocds:Release   | |
| Convocatoria | convocatoria_categoria_compra               | alfanumérico | Clasificación de la compra por su categoría principal.       | Servicios                                                    | ocds:Release   | |
| Convocatoria | convocatoria_categorias_adicionales         | alfanumérico | Clasificación de la compra por categorías secundarias.       | Servicios de consultoria                                     | ocds:Release   | |
| Convocatoria | convocatoria_criterio_adjudicacion          | alfanumérico | Nombre del criterio utilizado para adjudicar la compra.      | Mejor propuesta                                              | ocds:Release   | |
| Convocatoria | convocatoria_criterio_adjudicacion_detalles | alfanumérico | Detalle que permite operacionalizar el criterio para adjudicar la compra. | 60% Propuesta Tecnica 40% Propuesta Económica                | ocds:Release   | |
| Convocatoria | convocatoria_recepcion                      | alfanumérico | Modalidad o canal de recepción de una presentación o propuesta a la convocatoria. | En persona, Electrónica                                      | ocds:Release   | |
| Convocatoria | convocatoria_recepcion_detalles             | alfanumérico | Detalles o requisitos adicionales para la presentación o propuesta a la convocatoria. | Las propuestas se reciben en Mesa de entrada de la calle ..... y por correo electrónico en la cuenta .... o puede ingresarlas al sistema ... | ocds:Release   | |
| Convocatoria | convocatoria_periodo_inicio                 | fecha        | Fecha de inicio de recepción de ofertas.                     | 2019-03-05                                                   | ocds:Release   | |
| Convocatoria | convocatoria_periodo_fin                    | fecha        | Fecha de fin de recepción de ofertas.                        | 2019-03-20                                                   | ocds:Release   | |
| Convocatoria | convocatoria_fecha_limite                   | fecha        | Fecha de recepción máxima posible, en caso de extenderse la convocatoria. | 2019-03-25                                                   | ocds:Release   | |
| Convocatoria | convocatoria_duracion_dias                  | numérico     | Cantidad de dias e que la convocatoria permanecerá abierta.  | 15                                                           | ocds:Release   | |
| Convocatoria | convocatoria_consultas_inicio               | fecha        | Fecha a partir de la cual se pueden realizar consultas.      | 2019-03-05                                                   | ocds:Release   | |
| Convocatoria | convocatoria_consultas_fin                  | fecha        | Fecha a hasta la que se pueden realizar consultas.           | 2019-03-15                                                   | ocds:Release   | |
| Convocatoria | convocatoria_tiene_consultas                | booleano     | Indica si la convocatoria admite consultas o no.             | Si                                                           | ocds:Release   | |
| Convocatoria | convocatoria_criterio_elegibilidad          | alfanumérico | Descripción de cualquier criterio de elegibilidad para proveedores potenciales. | 10 puntos por experiencia empresarial 50 puntos por experiencia del equipo 40 puntos por precio | ocds:Release   | |
| Convocatoria | convocatoria_periodo_evaluacion             | alfanumérico | Cuanto tiempo toma el período de evaluación, se puede expresar en fecha de inicio y fecha de fin. | 2019-04-15                                                   | ocds:Release   | |
| Convocatoria | convocatoria_periodo_contrato               | alfanumérico | Duración estimada del contrato.                              | 2 años                                                       | ocds:Release   | |

### Recurso: Adjudicaciones

| clase        | titulo                        | tipo_dato    | descripcion                                                  | ejemplo          | estandar_mapeo | notas |
| ------------ | ----------------------------- | ------------ | ------------------------------------------------------------ | ---------------- | -------------- | ----- |
| Adjudicacion | adjudicacion_ocds_id          | alfanumérico | Identificador universal de open contracting.                 | ocds-twb234-0005 | ocds:Award     | |
| Adjudicacion | adjudicacion_id               | alfanumérico | Identificador utilizado internamente para identificar la adjudicación. | 3568999          | ocds:Award     | |
| Adjudicacion | adjudicacion_estado           | alfanumérico | Estado de la adjudicación.                                   | Activo           | ocds:Award     | |
| Adjudicacion | adjudicacion_fecha            | fecha        | Fecha de adjudicación.                                       | 2019-03-16       | ocds:Award     | |
| Adjudicacion | adjudicacion_proveedor_id     | alfanumérico | Identificación del proveedor adjudicatario.                  | 30628707093      | ocds:Award     | |
| Adjudicacion | adjudicacion_proveedor_nombre | alfanumérico | Nombre del proveedor adjudicatario.                          | HAL2000          | ocds:Award     | |
| Adjudicacion | adjudicacion_moneda           | alfanumérico | Moneda en que se adjudica el llamado.                        | ARS              | ocds:Award     | |
| Adjudicacion | adjudicacion_importe          | alfanumérico | Importe total adjudicado.                                    | 2000000          | ocds:Award     | |

### Recurso: Contratos 

| clase    | titulo                   | tipo_dato    | descripcion                                           | ejemplo                                            | estandar_mapeo | notas |
| -------- | ------------------------ | ------------ | ----------------------------------------------------- | -------------------------------------------------- | -------------- | ----- |
| Contrato | contrato_id              | alfanumérico | Identificación del contrato.                          | 3568999-1                                          | ocds:Contract  | |
| Contrato | contrato_adjudicacion_id | alfanumérico | Identificación de la adjudicación.                    | 3568999                                            | ocds:Contract  | |
| Contrato | contrato_titulo          | alfanumérico | Titulo o descripción breve objeto de la contratación. | Licitación Pública 3/2019                          | ocds:Contract  | |
| Contrato | contrato_descripcion     | alfanumérico | Descripción extendida del objeto de la contratación.  | Servicio de soporte de infraestructura informática | ocds:Contract  | |
| Contrato | contrato_estado          | alfanumérico | Estado del contrato.                                  | Activa                                             | ocds:Contract  | |
| Contrato | contrato_periodo_inicio  | fecha        | Fecha de inicio del contrato.                         | 2019-05-01                                         | ocds:Contract  | |
| Contrato | contrato_periodo_fin     | fecha        | Fecha de finalización del contrato.                   | 2021-04-30                                         | ocds:Contract  | |
| Contrato | contrato_fecha_firma     | alfanumérico | Fecha de firmado el contrato.                         | 2019-04-15                                         | ocds:Contract  | |
| Contrato | adjudicacion_moneda      | alfanumérico | Moneda en que se realiza el contrato.                 | ARS                                                | ocds:Contract  | |
| Contrato | contrato_importe         | numérico     | Importe total del contrato.                           | 2000000                                            | ocds:Contract  | |

### Recurso: Transacciones

| clase       | titulo                      | tipo_dato    | descripcion                                 | ejemplo                     | estandar_mapeo   | notas |
| ----------- | --------------------------- | ------------ | ------------------------------------------- | --------------------------- | ---------------- | ----- |
| Transaccion | transaccion_id              | alfanumérico | Identificación de la transacción.           | 896655273                   | ocds:Transaction | |
| Transaccion | transaccion_contrato_id     | alfanumérico | Identificación del contrato.                | 3568999-1                   | ocds:Transaction | |
| Transaccion | transaccion_adjudicacion_id | alfanumérico | Identificación de la adjudicación.          | 3568999                     | ocds:Transaction | |
| Transaccion | transaccion_fuente          | alfanumérico | Fuente de financiamiento de la transacción. | Prestamo BID AR1505         | ocds:Transaction | |
| Transaccion | transaccion_fecha           | fecha        | Fecha de realizada la transacción.          | 2019-05-31                  | ocds:Transaction | |
| Transaccion | transaccion_moneda          | alfanumérico | Moneda de la transacción.                   | ARS                         | ocds:Transaction | |
| Transaccion | transaccion_importe         | alfanumérico | Importe de la transacción.                  | 150000                      | ocds:Transaction | |
| Transaccion | transaccion_origen          | numérico     | Organización que realiza el pago.           | Ministerio de modernización | ocds:Transaction | |
| Transaccion | transaccion_destino         | alfanumérico | Organización que recibe el pago.            | HAL2000                     | ocds:Transaction | |

### Recurso: Items Adquiridos

| clase        | titulo               | tipo_dato    | descripcion                                           | ejemplo                             | estandar_mapeo | notas |
| ------------ | -------------------- | ------------ | ----------------------------------------------------- | ----------------------------------- | -------------- | ----- |
| Convocatoria | convocatoria_ocds_id | alfanumérico | Identificador universal de open contracting.          | ocds-twb234-0005                    | ocds:Release   | |
| <Etapa>_Item | item_etapa_id        | alfanumérico | Identificador de la etapa a la que pertenece el item. |                                     | ocds:Item      | |
| <Etapa>_Item | item_id              | alfanumérico | Identificación del item.                              | 3245                                | ocds:Item      | |
| <Etapa>_Item | item_descripcion     | alfanumérico | Descripción del item.                                 | Servicio de consultoria             | ocds:Item      | |
| <Etapa>_Item | item_clasificacion   | alfanumérico | Clasificación del item.                               | Soporte y mantenimiento de hardware | ocds:Item      | |
| <Etapa>_Item | item_cantidad        | numérico     | Cantidad de items.                                    | 1                                   | ocds:Item      | |
| <Etapa>_Item | item_unidad          | alfanumérico | Unidad de medida para cuantificar el item.            | Cantidad                            | ocds:Item      | |

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
