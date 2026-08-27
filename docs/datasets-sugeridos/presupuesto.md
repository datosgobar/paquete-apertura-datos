# Presupuesto

El presupuesto asignado a cada área, programa o función, las modificaciones durante cada ejercicio anual y el estadode ejecución actualizado en forma trimestral hasta el último nivel de desagregación en que se procese.

* **Tema**: Economía y finanzas
* **Estándar referencia**: [Open Fiscal Data Package](https://docs.openspending.org/en/latest/contributors/package/)
* **Formatos**: CSV

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Presupuesto
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/presupuesto/presupuesto.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/presupuesto/presupuesto.xlsx)**

| organizacion_id | organizacion_nombre         | organizacion_clasificacion | gift_fecha | gift_clasificacion_economica | gift_clasificacion_funcional | gift_descripción                | gift_actividad       | gift_administrador          | gift_procurador | gift_destinatario | gift_proveedor | gift_transferencias | gift_destino_presupestal | gift_tipo_presupuesto | gift_fuente_financiera | gift_fase | gift_informacion_geografica | gift_identificador_línea_presupuestal | gift_identificador_factura | gift_importe | gift_otros |
| --------------- | --------------------------- | -------------------------- | ---------- | ---------------------------- | ---------------------------- | ------------------------------- | -------------------- | --------------------------- | --------------- | ----------------- | -------------- | ------------------- | ------------------------ | --------------------- | ---------------------- | --------- | --------------------------- | ------------------------------------- | -------------------------- | ------------ | ---------- |
| 2               | Ministerio de Modernización | Poder Ejecutivo            | 2019-01-01 | Salarios                     | Pago de salarios             | Pago de salarios Diciembre 2018 | Proyecto BID - 26548 | Ministerio de Modernización |                 | Banco Nación      | SACE S.R.L     | No                  | Egresos                  | Gasto                 | BID                    | Aprobado  | Buenos Aires                | 3427                                  | A32666                     | 1500000      | |

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases

Un item del `Presupuesto` es un gasto o ingreso asignado a una `Organización` para el financiamiento de sus misiones y funciones.

Descargar clases en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/presupuesto-clases.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/presupuesto-clases.xlsx)**


| nombre       | descripcion |
| ------------ | ------------------------------------------------------------ |
| Organización | Atributos que describen a las instituciones públicas que reciben, asignan y gastan presupuesto. |
| Presupuesto  | Atributos que describen los flujos o partidas presupuestarias que son objeto de asignación y seguimiento para el financiamiento de las actividades de las organizaciones. |

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/presupuesto-campos.csv)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-sugeridos/presupuesto-campos.xlsx)**

### Recurso: Presupuesto

| clase        | titulo                                | tipo_dato    | descripcion                                                  | ejemplo                         | estandar_mapeo      | notas |
| ------------ | ------------------------------------- | ------------ | ------------------------------------------------------------ | ------------------------------- | ------------------- | ----- |
| Organización | organizacion_id                       | alfanumérico | Identificador único para la organización.                    | 2                               | popolo:Organization | |
| Organización | organizacion_nombre                   | alfanumérico | Nombre principal de la organización. Por ejemplo: su nombre legal u oficial. | Ministerio de Modernización     | popolo:Organization | |
| Organización | organizacion_clasificacion            | alfanumérico | La clasificación de la organización. Por ejemplo: "Poder Ejecutivo". | Poder Ejecutivo                 | popolo:Organization | |
| Presupuesto  | gift_fecha                            | fecha        | Fecha de publicación del presupuesto o fecha en la que se aprueba el presupuesto. | 2019-01-01                      | gift - openspending | |
| Presupuesto  | gift_clasificacion_economica          | alfanumérico | Identifica el tipo de presupuesto e ingresos o gastos incurridos. Por ejemplo: salarios, bienes y servicios, transferencias y pagos de intereses, o gastos de capital. | Salarios                        | gift - openspending | |
| Presupuesto  | gift_clasificacion_funcional          | alfanumérico | Gastos o ingresos según los fines y objetivos para los que están destinados. | Pago de salarios                | gift - openspending | |
| Presupuesto  | gift_descripción                      | alfanumérico | Descripción o detalle del gasto, ingreso o partida presupuestaria. | Pago de salarios Diciembre 2018 | gift - openspending | |
| Presupuesto  | gift_actividad                        | alfanumérico | Utilícela cuando tenga una columna de datos sobre el contrato / programa / proyecto que se está financiando. | Proyecto BID - 26548            | gift - openspending | |
| Presupuesto  | gift_administrador                    | alfanumérico | Autoridad que gasta o a la que le ingresa el dinero.         | Ministerio de Modernización     | gift - openspending | |
| Presupuesto  | gift_procurador                       | alfanumérico | Entidad gubernamental que actúa como gestor de la transacción, si es diferente de la institución que controla el proyecto. |                                 | gift - openspending | |
| Presupuesto  | gift_destinatario                     | alfanumérico | Destinatario (si existe) al que se dirige el elemento de ingreso. | Banco Nación                    | gift - openspending | |
| Presupuesto  | gift_proveedor                        | alfanumérico | Destinatario del gasto.                                      | SACE S.R.L                      | gift - openspending | |
| Presupuesto  | gift_transferencias                   | alfanumérico | Propiedades adicionales con respecto a si el gasto o ingreso contiene transferencias presupuestarias. | No                              | gift - openspending | |
| Presupuesto  | gift_destino_presupestal              | alfanumérico | Especifica si los valores en esta línea son egresos o ingresos. | Egresos                         | gift - openspending | |
| Presupuesto  | gift_tipo_presupuesto                 | alfanumérico | Atributos adicionales que proporcionan más propiedades.      | Gasto                           | gift - openspending | |
| Presupuesto  | gift_fuente_financiera                | alfanumérico | Fuente financiera de los fondos presupuestarios.             | BID                             | gift - openspending | |
| Presupuesto  | gift_fase                             | alfanumérico | Identificador de fase para los valores en esta línea (por ejemplo, aprobado, ejecutado, etc.). | Aprobado                        | gift - openspending | |
| Presupuesto  | gift_informacion_geografica           | alfanumérico | Puede ser una dirección, un código de área, una descripción, etc. | Buenos Aires                    | gift - openspending | |
| Presupuesto  | gift_identificador_línea_presupuestal | alfanumérico | Identificador único para esta línea de presupuesto.          | 3427                            | gift - openspending | |
| Presupuesto  | gift_identificador_factura            | alfanumérico | Número de factura dado por el proveedor                      | A32666                          | gift - openspending | |
| Presupuesto  | gift_importe                          | numerico     | Importe o valor del gasto o ingreso (obligatorio).           | 1500000                         | gift - openspending | |
| Presupuesto  | gift_otros                            | texto        | Notas o comentarios adicionales.                             |                                 | gift - openspending | |

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
