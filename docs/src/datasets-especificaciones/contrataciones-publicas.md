# Contrataciones Públicas

Listado de todos los procesos de contratación, los procesos de contratación de obras deberían tener un enlace a sus obras, con el fin de poder agrupar todos los contratos de una obra dada (diseño, construccion, fiscalización).

* **Tema**: Gobierno y sector público
* **Estándar referencia**: [Open Contracting Data Standard]( http://standard.open-contracting.org/latest/en/)
* **Formatos**: JSON, XML, CSV
* **Ejemplo:**: http://standard.open-contracting.org/latest/en/schema/merging/, https://github.com/open-contracting/sample-data/blob/master/flat-template/template/

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos
    
### Recurso: Convocatoria
**[CSV](contrataciones-publicas/convocatoria.csv)** | **[XLSX](contrataciones-publicas/convocatoria.xlsx)**

<table>
    <tr>
        <th>convocatoria_ocds_id</th>
        <th>convocatoria_id</th>
        <th>convocatoria_titulo</th>
        <th>convocatoria_descripcion</th>
        <th>convocatoria_estado</th>
        <th>convocatoria_entidad_compradora</th>
        <th>convocatoria_valor</th>
        <th>convocatoria_valor_minimo</th>
        <th>convocatoria_metodo_compra</th>
        <th>convocatoria_metodo_detalles</th>
        <th>convocatoria_metodo_justificacion</th>
        <th>convocatoria_categoria_compra</th>
        <th>convocatoria_categorias_adicionales</th>
        <th>convocatoria_criterio_adjudicacion</th>
        <th>convocatoria_criterio_adjudicacion_detalles</th>
        <th>convocatoria_recepcion</th>
        <th>convocatoria_recepcion_detalles</th>
        <th>convocatoria_periodo_inicio</th>
        <th>convocatoria_periodo_fin</th>
        <th>convocatoria_fecha_limite</th>
        <th>convocatoria_duracion_en_dias</th>
        <th>convocatoria_consultas_inicio</th>
        <th>convocatoria_consultas_fin</th>
        <th>convocatoria_tiene_consultas</th>
        <th>convocatoria_criterio_elegibilidad</th>
        <th>convocatoria_periodo_evaluacion</th>
        <th>convocatoria_periodo_contrato</th>
    </tr>

    <tr>
        <td>ocds-twb234-0005</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>Abierta/Selectiva/Limitad/Directa
 http://standard.open-contracting.org/latest/en/schema/codelists/#method</td>
        <td></td>
        <td></td>
        <td>Bienes
 Trabajos
 Servicios</td>
        <td>http://standard.open-contracting.org/latest/en/schema/codelists/#extended-procurement-category</td>
        <td>http://standard.open-contracting.org/latest/en/schema/codelists/#award-criteria</td>
        <td></td>
        <td>En persona/Envío electronico/Escrito/Plataforma para postulación de ofertas</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>Si/No</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
        
</table>
### Recurso: Adjudicacion
**[CSV](contrataciones-publicas/adjudicacion.csv)** | **[XLSX](contrataciones-publicas/adjudicacion.xlsx)**

<table>
    <tr>
        <th>adjudicacion_ocds_id</th>
        <th>adjudicacion_id</th>
        <th>adjudicacion_estado</th>
        <th>adjudicacion_fecha</th>
        <th>adjudicacion_proveedor_id</th>
        <th>adjudicacion_proveedor_nombre</th>
        <th>adjudicacion_moneda</th>
        <th>adjudicacion_importe</th>
    </tr>

    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
        
</table>
### Recurso: Contrato  
**[CSV](contrataciones-publicas/contrato.csv)** | **[XLSX](contrataciones-publicas/contrato.xlsx)**

<table>
    <tr>
        <th>contrato_id</th>
        <th>contrato_adjudicacion_id</th>
        <th>contrato_titulo</th>
        <th>contrato_descripcion</th>
        <th>contrato_estado</th>
        <th>contrato_periodo_inicio</th>
        <th>contrato_periodo_fin</th>
        <th>contrato_fecha_firma</th>
        <th>adjudicacion_moneda</th>
        <th>contrato_importe</th>
    </tr>

    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td>Pendiente
 Activo
 Cancelado
 Finalizado</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
        
</table>
### Recurso: Transaccion
**[CSV](contrataciones-publicas/transaccion.csv)** | **[XLSX](contrataciones-publicas/transaccion.xlsx)**

<table>
    <tr>
        <th>transaccion_id</th>
        <th>transaccion_contrato_id</th>
        <th>transaccion_adjudicacion_id</th>
        <th>transaccion_fuente</th>
        <th>transaccion_fecha</th>
        <th>transaccion_moneda</th>
        <th>transaccion_importe</th>
        <th>transaccion_origen</th>
        <th>transaccion_destino</th>
    </tr>

    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
        
</table>
### Recurso: <Etapa>_Item
**[CSV](contrataciones-publicas/etapaitem.csv)** | **[XLSX](contrataciones-publicas/etapaitem.xlsx)**

<table>
    <tr>
        <th>item_id</th>
        <th>item_descripcion</th>
        <th>item_clasificacion</th>
        <th>item_cantidad</th>
        <th>item_unidad</th>
    </tr>

    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](contrataciones-publicas-campos.csv)** | **[XLSX](contrataciones-publicas-campos.xlsx)**

### Recurso: Convocatoria

<table>
    <tr>
        <th>clase</th>
        <th>titulo</th>
        <th>tipo_dato</th>
        <th>descripcion</th>
        <th>ejemplo</th>
        <th>estandar_mapeo</th>
        <th>notas</th>
    </tr>

    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_ocds_id</td>
        <td>alfanumérico</td>
        <td>Identificador universal de open contracting</td>
        <td>ocds-twb234-0005</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_id</td>
        <td>alfanumérico</td>
        <td>Identificador utilizado internamente a la organización para identificar la convocatoria</td>
        <td></td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_titulo</td>
        <td>alfanumérico</td>
        <td>Titulo de la convocatoria</td>
        <td></td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_descripcion</td>
        <td>texto</td>
        <td>Detalle de lo que se desea adquirir</td>
        <td></td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_estado</td>
        <td>alfanumérico</td>
        <td>Estado actual de la convocatoria</td>
        <td></td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_entidad_compradora</td>
        <td>alfanumérico</td>
        <td>Nombre de la organización responsable de la adquisición</td>
        <td></td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_valor</td>
        <td>numérico</td>
        <td>Valor máximo que se va a pagar por la compra</td>
        <td></td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_valor_minimo</td>
        <td>numérico</td>
        <td>Valor mínimo que se asegura se va a pagar</td>
        <td></td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_metodo_compra</td>
        <td>alfanumérico</td>
        <td>Metodo de compra</td>
        <td>Abierta/Selectiva/Limitad/Directa
 http://standard.open-contracting.org/latest/en/schema/codelists/#method</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_metodo_detalles</td>
        <td>alfanumérico</td>
        <td>Detalles adicionales sobre el método de adquisición utilizado. Este campo se puede usar para proporcionar el nombre local del método de adquisición particular utilizado.</td>
        <td></td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_metodo_justificacion</td>
        <td>alfanumérico</td>
        <td>Justificación del método de contratación elegido, es importante en caso de adjudicaciones directas o de ofertas limitadas</td>
        <td></td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_categoria_compra</td>
        <td>alfanumérico</td>
        <td></td>
        <td>Bienes
 Trabajos
 Servicios</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_categorias_adicionales</td>
        <td>alfanumérico</td>
        <td></td>
        <td>http://standard.open-contracting.org/latest/en/schema/codelists/#extended-procurement-category</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_criterio_adjudicacion</td>
        <td>alfanumérico</td>
        <td></td>
        <td>http://standard.open-contracting.org/latest/en/schema/codelists/#award-criteria</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_criterio_adjudicacion_detalles</td>
        <td>alfanumérico</td>
        <td></td>
        <td></td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_recepcion</td>
        <td>alfanumérico</td>
        <td></td>
        <td>En persona/Envío electronico/Escrito/Plataforma para postulación de ofertas</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_recepcion_detalles</td>
        <td>alfanumérico</td>
        <td></td>
        <td></td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_periodo_inicio</td>
        <td>fecha</td>
        <td>Inicio de recepción de ofertas</td>
        <td></td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_periodo_fin</td>
        <td>fecha</td>
        <td>Fin de recepción de ofertas</td>
        <td></td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_fecha_limite</td>
        <td>fecha</td>
        <td>En caso de extenderse la convocatoria cual sería la fecha maxima posible</td>
        <td></td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_duracion_en_dias</td>
        <td>numérico</td>
        <td>Duración en cantidad de dias de abierta la convocatoria</td>
        <td></td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_consultas_inicio</td>
        <td>fecha</td>
        <td>Cuando se pueden realizar consultas</td>
        <td></td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_consultas_fin</td>
        <td>fecha</td>
        <td>Hasta cuando se pueden realizar consultas</td>
        <td></td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_tiene_consultas</td>
        <td>booleano</td>
        <td></td>
        <td>Si/No</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_criterio_elegibilidad</td>
        <td>alfanumérico</td>
        <td>Descripción de cualquier criterio de elegibilidad para proveedores potenciales.</td>
        <td></td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_periodo_evaluacion</td>
        <td>alfanumérico</td>
        <td>Cuanto tiempo toma el período de evaluación, se puede expresar en fecha de inicio y fecha de fin</td>
        <td></td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_periodo_contrato</td>
        <td>alfanumérico</td>
        <td>Duración estimada del contrato</td>
        <td></td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
</table>
### Recurso: Adjudicacion

<table>
    <tr>
        <th>clase</th>
        <th>titulo</th>
        <th>tipo_dato</th>
        <th>descripcion</th>
        <th>ejemplo</th>
        <th>estandar_mapeo</th>
        <th>notas</th>
    </tr>

    <tr>
        <td>Adjudicacion</td>
        <td>adjudicacion_ocds_id</td>
        <td>alfanumérico</td>
        <td>Numero de Open contracting asignado</td>
        <td></td>
        <td>ocds:Award</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Adjudicacion</td>
        <td>adjudicacion_id</td>
        <td>alfanumérico</td>
        <td>Identificación de la adjudicación</td>
        <td></td>
        <td>ocds:Award</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Adjudicacion</td>
        <td>adjudicacion_estado</td>
        <td>alfanumérico</td>
        <td>Estado de la adjudicación</td>
        <td></td>
        <td>ocds:Award</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Adjudicacion</td>
        <td>adjudicacion_fecha</td>
        <td>fecha</td>
        <td>Fecha de adjudicación</td>
        <td></td>
        <td>ocds:Award</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Adjudicacion</td>
        <td>adjudicacion_proveedor_id</td>
        <td>alfanumérico</td>
        <td>Identificación del proveedor adjudicatario</td>
        <td></td>
        <td>ocds:Award</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Adjudicacion</td>
        <td>adjudicacion_proveedor_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre del proveedor adjudicatario</td>
        <td></td>
        <td>ocds:Award</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Adjudicacion</td>
        <td>adjudicacion_moneda</td>
        <td>alfanumérico</td>
        <td>Moneda en que se adjudica el llamado</td>
        <td></td>
        <td>ocds:Award</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Adjudicacion</td>
        <td>adjudicacion_importe</td>
        <td>alfanumérico</td>
        <td>Importe total adjudicado</td>
        <td></td>
        <td>ocds:Award</td>
        <td></td>
    </tr>
        
</table>
### Recurso: Contrato  

<table>
    <tr>
        <th>clase</th>
        <th>titulo</th>
        <th>tipo_dato</th>
        <th>descripcion</th>
        <th>ejemplo</th>
        <th>estandar_mapeo</th>
        <th>notas</th>
    </tr>

    <tr>
        <td>Contrato</td>
        <td>contrato_id</td>
        <td>alfanumérico</td>
        <td>Identificación del contrato</td>
        <td></td>
        <td>ocds:Contract</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contrato</td>
        <td>contrato_adjudicacion_id</td>
        <td>alfanumérico</td>
        <td>Identificación de la adjudicación</td>
        <td></td>
        <td>ocds:Contract</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contrato</td>
        <td>contrato_titulo</td>
        <td>alfanumérico</td>
        <td>Titulo o descripción breve objeto de la contratación</td>
        <td></td>
        <td>ocds:Contract</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contrato</td>
        <td>contrato_descripcion</td>
        <td>alfanumérico</td>
        <td>Descripción extendida del objeto de la contratación</td>
        <td></td>
        <td>ocds:Contract</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contrato</td>
        <td>contrato_estado</td>
        <td>alfanumérico</td>
        <td>Estado del contrato.</td>
        <td>Pendiente
 Activo
 Cancelado
 Finalizado</td>
        <td>ocds:Contract</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contrato</td>
        <td>contrato_periodo_inicio</td>
        <td>fecha</td>
        <td>Fecha de inicio del contrato</td>
        <td></td>
        <td>ocds:Contract</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contrato</td>
        <td>contrato_periodo_fin</td>
        <td>fecha</td>
        <td>Fecha de finalización del contrato</td>
        <td></td>
        <td>ocds:Contract</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contrato</td>
        <td>contrato_fecha_firma</td>
        <td>alfanumérico</td>
        <td>Fecha de firmado el contrato</td>
        <td></td>
        <td>ocds:Contract</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contrato</td>
        <td>adjudicacion_moneda</td>
        <td>alfanumérico</td>
        <td>Moneda en que se realiza el contrato</td>
        <td></td>
        <td>ocds:Contract</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contrato</td>
        <td>contrato_importe</td>
        <td>numérico</td>
        <td>Importe total del contrato</td>
        <td></td>
        <td>ocds:Contract</td>
        <td></td>
    </tr>
        
</table>
### Recurso: Transaccion

<table>
    <tr>
        <th>clase</th>
        <th>titulo</th>
        <th>tipo_dato</th>
        <th>descripcion</th>
        <th>ejemplo</th>
        <th>estandar_mapeo</th>
        <th>notas</th>
    </tr>

    <tr>
        <td>Transaccion</td>
        <td>transaccion_id</td>
        <td>alfanumérico</td>
        <td>Identificación de la transacción</td>
        <td></td>
        <td>ocds:Transaction</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Transaccion</td>
        <td>transaccion_contrato_id</td>
        <td>alfanumérico</td>
        <td>Identificación del contrato</td>
        <td></td>
        <td>ocds:Transaction</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Transaccion</td>
        <td>transaccion_adjudicacion_id</td>
        <td>alfanumérico</td>
        <td>Identificación de la adjudicación</td>
        <td></td>
        <td>ocds:Transaction</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Transaccion</td>
        <td>transaccion_fuente</td>
        <td>alfanumérico</td>
        <td>Fuente de financiamiento de la transacción</td>
        <td></td>
        <td>ocds:Transaction</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Transaccion</td>
        <td>transaccion_fecha</td>
        <td>fecha</td>
        <td>Fecha de realizada la transacción</td>
        <td></td>
        <td>ocds:Transaction</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Transaccion</td>
        <td>transaccion_moneda</td>
        <td>alfanumérico</td>
        <td>Moneda de la transacción</td>
        <td></td>
        <td>ocds:Transaction</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Transaccion</td>
        <td>transaccion_importe</td>
        <td>alfanumérico</td>
        <td>Importe de la transacción</td>
        <td></td>
        <td>ocds:Transaction</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Transaccion</td>
        <td>transaccion_origen</td>
        <td>numérico</td>
        <td>Organización que realiza el pago</td>
        <td></td>
        <td>ocds:Transaction</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Transaccion</td>
        <td>transaccion_destino</td>
        <td>alfanumérico</td>
        <td>Organización que recibe el pago</td>
        <td></td>
        <td>ocds:Transaction</td>
        <td></td>
    </tr>
        
</table>
### Recurso: <Etapa>_Item

<table>
    <tr>
        <th>clase</th>
        <th>titulo</th>
        <th>tipo_dato</th>
        <th>descripcion</th>
        <th>ejemplo</th>
        <th>estandar_mapeo</th>
        <th>notas</th>
    </tr>

    <tr>
        <td><Etapa>_Item</td>
        <td>item_id</td>
        <td>alfanumérico</td>
        <td>Identificación del item</td>
        <td></td>
        <td>ocds:Item</td>
        <td></td>
    </tr>
        
    <tr>
        <td><Etapa>_Item</td>
        <td>item_descripcion</td>
        <td>alfanumérico</td>
        <td>Descripción del item</td>
        <td></td>
        <td>ocds:Item</td>
        <td></td>
    </tr>
        
    <tr>
        <td><Etapa>_Item</td>
        <td>item_clasificacion</td>
        <td>alfanumérico</td>
        <td>Clasificación del item</td>
        <td></td>
        <td>ocds:Item</td>
        <td></td>
    </tr>
        
    <tr>
        <td><Etapa>_Item</td>
        <td>item_cantidad</td>
        <td>numérico</td>
        <td>Cantidad de items</td>
        <td></td>
        <td>ocds:Item</td>
        <td></td>
    </tr>
        
    <tr>
        <td><Etapa>_Item</td>
        <td>item_unidad</td>
        <td>alfanumérico</td>
        <td>Unidad de medida para cuantificar el item</td>
        <td></td>
        <td>ocds:Item</td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
