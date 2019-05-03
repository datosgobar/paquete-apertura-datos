# Contrataciones Públicas

Listado de todos los procesos de contratación, los procesos de contratación de obras deberían tener un enlace a sus obras, con el fin de poder agrupar todos los contratos de una obra dada (diseño, construccion, fiscalización).

* **Tema**: Gobierno y sector público
* **Estándar referencia**: [Open Contracting Data Standard]( http://standard.open-contracting.org/latest/en/)
* **Formatos**: JSON, XML, CSV
* **Ejemplo:**: http://standard.open-contracting.org/latest/en/schema/merging/, https://github.com/open-contracting/sample-data/blob/master/flat-template/template/

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Convocatorias
**[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/contrataciones-publicas/convocatorias.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/contrataciones-publicas/convocatorias.xlsx)**

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
        <th>convocatoria_duracion_dias</th>
        <th>convocatoria_consultas_inicio</th>
        <th>convocatoria_consultas_fin</th>
        <th>convocatoria_tiene_consultas</th>
        <th>convocatoria_criterio_elegibilidad</th>
        <th>convocatoria_periodo_evaluacion</th>
        <th>convocatoria_periodo_contrato</th>
    </tr>

    <tr>
        <td>ocds-twb234-0005</td>
        <td>3568999</td>
        <td>Licitación Pública 3/2019</td>
        <td>Servicio de soporte de infraestructura informática</td>
        <td>Activa</td>
        <td>Ministerio de modernización</td>
        <td>2000000</td>
        <td>800000</td>
        <td>Abierta</td>
        <td>Todos los interesados pueden enviar ofertas</td>
        <td></td>
        <td>Servicios</td>
        <td>Servicios de consultoria</td>
        <td>Mejor propuesta</td>
        <td>60% Propuesta Tecnica
40% Propuesta Económica</td>
        <td>En persona, Electrónica</td>
        <td>Las propuestas se reciben en Mesa de entrada de la calle ..... y por correo electrónico en la cuenta .... o puede ingresarlas al sistema ...</td>
        <td>2019-03-05</td>
        <td>2019-03-20</td>
        <td>2019-03-25</td>
        <td>15</td>
        <td>2019-03-05</td>
        <td>2019-03-15</td>
        <td>Si</td>
        <td>10 puntos por experiencia empresarial
50 puntos por experiencia del equipo
40 puntos por precio</td>
        <td>2019-04-15</td>
        <td>2 años</td>
    </tr>
        
</table>
### Recurso: Adjudicaciones
**[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/contrataciones-publicas/adjudicaciones.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/contrataciones-publicas/adjudicaciones.xlsx)**

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
        <td>ocds-twb234-0005</td>
        <td>3568999</td>
        <td>Activo</td>
        <td>2019-03-16</td>
        <td>30628707093</td>
        <td>HAL2000</td>
        <td>ARS</td>
        <td>2000000</td>
    </tr>
        
</table>
### Recurso: Contratos 
**[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/contrataciones-publicas/contratos.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/contrataciones-publicas/contratos.xlsx)**

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
        <td>3568999-1</td>
        <td>3568999</td>
        <td>Licitación Pública 3/2019</td>
        <td>Servicio de soporte de infraestructura informática</td>
        <td>Activa</td>
        <td>2019-05-01</td>
        <td>2021-04-30</td>
        <td>2019-04-15</td>
        <td>ARS</td>
        <td>2000000</td>
    </tr>
        
</table>
### Recurso: Transacciones
**[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/contrataciones-publicas/transacciones.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/contrataciones-publicas/transacciones.xlsx)**

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
        <td>896655273</td>
        <td>3568999-1</td>
        <td>3568999</td>
        <td>Prestamo BID AR1505</td>
        <td>2019-05-31</td>
        <td>ARS</td>
        <td>150000</td>
        <td>Ministerio de modernización</td>
        <td>HAL2000</td>
    </tr>
        
</table>
### Recurso: Items Adquiridos
**[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/contrataciones-publicas/items-adquiridos.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/contrataciones-publicas/items-adquiridos.xlsx)**

<table>
    <tr>
        <th>convocatoria_ocds_id</th>
        <th>item_etapa_id</th>
        <th>item_id</th>
        <th>item_descripcion</th>
        <th>item_clasificacion</th>
        <th>item_cantidad</th>
        <th>item_unidad</th>
    </tr>

    <tr>
        <td>ocds-twb234-0005</td>
        <td></td>
        <td>3245</td>
        <td>Servicio de consultoria</td>
        <td>Soporte y mantenimiento de hardware</td>
        <td>1</td>
        <td>Cantidad</td>
    </tr>
        
</table>

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases

Una institución pública abre una `Convocatoria` para recibir ofertas de provisión de bienes y servicios. Una vez elegida una oferta realiza la `Adjudicación` al proveedor elegido con el que celebra un `Contrato` que marca las condiciones bajo las cuales se realiza una `Transacción` entre las partes mediante la cual se adquiere un `Item`.

Descargar clases en **[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/contrataciones-publicas-clases.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/contrataciones-publicas-clases.xlsx)**


<table>
    <tr>
        <th>recurso</th>
        <th>clase</th>
        <th>titulo</th>
        <th>tipo_dato</th>
        <th>descripcion</th>
        <th>ejemplo</th>
        <th>estandar_mapeo</th>
        <th>notas</th>
    </tr>

    <tr>
        <td>Estaciones de Medición de la Calidad del Aire</td>
        <td>Estacion</td>
        <td>estacion_id</td>
        <td>alfanumerico</td>
        <td>Identificación de la estación</td>
        <td>1001</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estaciones de Medición de la Calidad del Aire</td>
        <td>Estacion</td>
        <td>estacion_nombre</td>
        <td>alfanumerico</td>
        <td>Nombre de la estación</td>
        <td>Chapelco</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estaciones de Medición de la Calidad del Aire</td>
        <td>Estacion</td>
        <td>estacion_region</td>
        <td>alfanumerico</td>
        <td>Nombre del país/provincia o localidad</td>
        <td>San Martin de Los Andes</td>
        <td>schema:Place</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estaciones de Medición de la Calidad del Aire</td>
        <td>Estacion</td>
        <td>estacion_latitud</td>
        <td>numerico</td>
        <td>Coordenadas geograficas</td>
        <td>-40.1808541022993</td>
        <td>schema:GeoCoordinates</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estaciones de Medición de la Calidad del Aire</td>
        <td>Estacion</td>
        <td>estacion_longitud</td>
        <td>numerico</td>
        <td>Coordenadas geograficas</td>
        <td>-71.31843</td>
        <td>schema:GeoCoordinates</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Estaciones de Medición de la Calidad del Aire</td>
        <td>Estacion</td>
        <td>estacion_zonahoraria</td>
        <td>alfanumerico</td>
        <td>Campo opcional para indicar la zona horaria</td>
        <td>UTC-3</td>
        <td>schema:BroadcastService</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Elementos Contaminantes del Aire</td>
        <td>Contaminante</td>
        <td>contaminante_estacion_id</td>
        <td>alfanumerico</td>
        <td>Identificación de la estación</td>
        <td>1001</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Elementos Contaminantes del Aire</td>
        <td>Contaminante</td>
        <td>contaminante_nombre</td>
        <td>alfanumerico</td>
        <td>Nombre del contaminante que se esta midiendo</td>
        <td>Dióxido de azufre</td>
        <td>schema:GeoCoordinates</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Elementos Contaminantes del Aire</td>
        <td>Contaminante</td>
        <td>contaminante_unidad</td>
        <td>alfanumerico</td>
        <td>Unidad de medida en que se establece el valor</td>
        <td>µg/m3</td>
        <td>schema:GeoCoordinates</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Elementos Contaminantes del Aire</td>
        <td>Contaminante</td>
        <td>contaminante_actualizado</td>
        <td>fecha</td>
        <td>Fecha y hora de actualizado el valor</td>
        <td>2019-02-26 0:00:00</td>
        <td>schema:Date</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Elementos Contaminantes del Aire</td>
        <td>Contaminante</td>
        <td>contaminante_valor</td>
        <td>numerico</td>
        <td>Valor obtenido en la medición</td>
        <td>0.27</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Elementos Contaminantes del Aire</td>
        <td>Contaminante</td>
        <td>contaminante_validez</td>
        <td>alfanumerico</td>
        <td>Indica la duración de validez del dato</td>
        <td>1 hora</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/contrataciones-publicas-campos.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/contrataciones-publicas-campos.xlsx)**

### Recurso: Convocatorias

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
        <td>Identificador universal de open contracting.</td>
        <td>ocds-twb234-0005</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_id</td>
        <td>alfanumérico</td>
        <td>Identificador utilizado internamente para identificar la convocatoria.</td>
        <td>3568999</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_titulo</td>
        <td>alfanumérico</td>
        <td>Título de la convocatoria.</td>
        <td>Licitación Pública 3/2019</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_descripcion</td>
        <td>texto</td>
        <td>Detalle de lo que se desea adquirir.</td>
        <td>Servicio de soporte de infraestructura informática</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_estado</td>
        <td>alfanumérico</td>
        <td>Estado actual de la convocatoria.</td>
        <td>Activa</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_entidad_compradora</td>
        <td>alfanumérico</td>
        <td>Nombre de la organización responsable de la adquisición.</td>
        <td>Ministerio de modernización</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_valor</td>
        <td>numérico</td>
        <td>Valor máximo que se va a pagar por la compra.</td>
        <td>2000000</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_valor_minimo</td>
        <td>numérico</td>
        <td>Valor mínimo que se asegura se va a pagar por la compra.</td>
        <td>800000</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_metodo_compra</td>
        <td>alfanumérico</td>
        <td>Método de compra.</td>
        <td>Abierta</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_metodo_detalles</td>
        <td>alfanumérico</td>
        <td>Detalles adicionales sobre el método de adquisición utilizado. Este campo se puede usar para proporcionar el nombre local del método de adquisición particular utilizado.</td>
        <td>Todos los interesados pueden enviar ofertas</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_metodo_justificacion</td>
        <td>alfanumérico</td>
        <td>Justificación del método de contratación elegido. Es importante en caso de adjudicaciones directas o de ofertas limitadas.</td>
        <td></td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_categoria_compra</td>
        <td>alfanumérico</td>
        <td>Clasificación de la compra por su categoría principal.</td>
        <td>Servicios</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_categorias_adicionales</td>
        <td>alfanumérico</td>
        <td>Clasificación de la compra por categorías secundarias.</td>
        <td>Servicios de consultoria</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_criterio_adjudicacion</td>
        <td>alfanumérico</td>
        <td>Nombre del criterio utilizado para adjudicar la compra.</td>
        <td>Mejor propuesta</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_criterio_adjudicacion_detalles</td>
        <td>alfanumérico</td>
        <td>Detalle que permite operacionalizar el criterio para adjudicar la compra.</td>
        <td>60% Propuesta Tecnica
40% Propuesta Económica</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_recepcion</td>
        <td>alfanumérico</td>
        <td>Modalidad o canal de recepción de una presentación o propuesta a la convocatoria.</td>
        <td>En persona, Electrónica</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_recepcion_detalles</td>
        <td>alfanumérico</td>
        <td>Detalles o requisitos adicionales para la presentación o propuesta a la convocatoria.</td>
        <td>Las propuestas se reciben en Mesa de entrada de la calle ..... y por correo electrónico en la cuenta .... o puede ingresarlas al sistema ...</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_periodo_inicio</td>
        <td>fecha</td>
        <td>Fecha de inicio de recepción de ofertas.</td>
        <td>2019-03-05</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_periodo_fin</td>
        <td>fecha</td>
        <td>Fecha de fin de recepción de ofertas.</td>
        <td>2019-03-20</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_fecha_limite</td>
        <td>fecha</td>
        <td>Fecha de recepción máxima posible, en caso de extenderse la convocatoria.</td>
        <td>2019-03-25</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_duracion_dias</td>
        <td>numérico</td>
        <td>Cantidad de dias e que la convocatoria permanecerá abierta.</td>
        <td>15</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_consultas_inicio</td>
        <td>fecha</td>
        <td>Fecha a partir de la cual se pueden realizar consultas.</td>
        <td>2019-03-05</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_consultas_fin</td>
        <td>fecha</td>
        <td>Fecha a hasta la que se pueden realizar consultas.</td>
        <td>2019-03-15</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_tiene_consultas</td>
        <td>booleano</td>
        <td>Indica si la convocatoria admite consultas o no.</td>
        <td>Si</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_criterio_elegibilidad</td>
        <td>alfanumérico</td>
        <td>Descripción de cualquier criterio de elegibilidad para proveedores potenciales.</td>
        <td>10 puntos por experiencia empresarial
50 puntos por experiencia del equipo
40 puntos por precio</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_periodo_evaluacion</td>
        <td>alfanumérico</td>
        <td>Cuanto tiempo toma el período de evaluación, se puede expresar en fecha de inicio y fecha de fin.</td>
        <td>2019-04-15</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Convocatoria</td>
        <td>convocatoria_periodo_contrato</td>
        <td>alfanumérico</td>
        <td>Duración estimada del contrato.</td>
        <td>2 años</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
</table>
### Recurso: Adjudicaciones

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
        <td>Identificador universal de open contracting.</td>
        <td>ocds-twb234-0005</td>
        <td>ocds:Award</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Adjudicacion</td>
        <td>adjudicacion_id</td>
        <td>alfanumérico</td>
        <td>Identificador utilizado internamente para identificar la adjudicación.</td>
        <td>3568999</td>
        <td>ocds:Award</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Adjudicacion</td>
        <td>adjudicacion_estado</td>
        <td>alfanumérico</td>
        <td>Estado de la adjudicación.</td>
        <td>Activo</td>
        <td>ocds:Award</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Adjudicacion</td>
        <td>adjudicacion_fecha</td>
        <td>fecha</td>
        <td>Fecha de adjudicación.</td>
        <td>2019-03-16</td>
        <td>ocds:Award</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Adjudicacion</td>
        <td>adjudicacion_proveedor_id</td>
        <td>alfanumérico</td>
        <td>Identificación del proveedor adjudicatario.</td>
        <td>30628707093</td>
        <td>ocds:Award</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Adjudicacion</td>
        <td>adjudicacion_proveedor_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre del proveedor adjudicatario.</td>
        <td>HAL2000</td>
        <td>ocds:Award</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Adjudicacion</td>
        <td>adjudicacion_moneda</td>
        <td>alfanumérico</td>
        <td>Moneda en que se adjudica el llamado.</td>
        <td>ARS</td>
        <td>ocds:Award</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Adjudicacion</td>
        <td>adjudicacion_importe</td>
        <td>alfanumérico</td>
        <td>Importe total adjudicado.</td>
        <td>2000000</td>
        <td>ocds:Award</td>
        <td></td>
    </tr>
        
</table>
### Recurso: Contratos 

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
        <td>Identificación del contrato.</td>
        <td>3568999-1</td>
        <td>ocds:Contract</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contrato</td>
        <td>contrato_adjudicacion_id</td>
        <td>alfanumérico</td>
        <td>Identificación de la adjudicación.</td>
        <td>3568999</td>
        <td>ocds:Contract</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contrato</td>
        <td>contrato_titulo</td>
        <td>alfanumérico</td>
        <td>Titulo o descripción breve objeto de la contratación.</td>
        <td>Licitación Pública 3/2019</td>
        <td>ocds:Contract</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contrato</td>
        <td>contrato_descripcion</td>
        <td>alfanumérico</td>
        <td>Descripción extendida del objeto de la contratación.</td>
        <td>Servicio de soporte de infraestructura informática</td>
        <td>ocds:Contract</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contrato</td>
        <td>contrato_estado</td>
        <td>alfanumérico</td>
        <td>Estado del contrato.</td>
        <td>Activa</td>
        <td>ocds:Contract</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contrato</td>
        <td>contrato_periodo_inicio</td>
        <td>fecha</td>
        <td>Fecha de inicio del contrato.</td>
        <td>2019-05-01</td>
        <td>ocds:Contract</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contrato</td>
        <td>contrato_periodo_fin</td>
        <td>fecha</td>
        <td>Fecha de finalización del contrato.</td>
        <td>2021-04-30</td>
        <td>ocds:Contract</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contrato</td>
        <td>contrato_fecha_firma</td>
        <td>alfanumérico</td>
        <td>Fecha de firmado el contrato.</td>
        <td>2019-04-15</td>
        <td>ocds:Contract</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contrato</td>
        <td>adjudicacion_moneda</td>
        <td>alfanumérico</td>
        <td>Moneda en que se realiza el contrato.</td>
        <td>ARS</td>
        <td>ocds:Contract</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Contrato</td>
        <td>contrato_importe</td>
        <td>numérico</td>
        <td>Importe total del contrato.</td>
        <td>2000000</td>
        <td>ocds:Contract</td>
        <td></td>
    </tr>
        
</table>
### Recurso: Transacciones

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
        <td>Identificación de la transacción.</td>
        <td>896655273</td>
        <td>ocds:Transaction</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Transaccion</td>
        <td>transaccion_contrato_id</td>
        <td>alfanumérico</td>
        <td>Identificación del contrato.</td>
        <td>3568999-1</td>
        <td>ocds:Transaction</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Transaccion</td>
        <td>transaccion_adjudicacion_id</td>
        <td>alfanumérico</td>
        <td>Identificación de la adjudicación.</td>
        <td>3568999</td>
        <td>ocds:Transaction</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Transaccion</td>
        <td>transaccion_fuente</td>
        <td>alfanumérico</td>
        <td>Fuente de financiamiento de la transacción.</td>
        <td>Prestamo BID AR1505</td>
        <td>ocds:Transaction</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Transaccion</td>
        <td>transaccion_fecha</td>
        <td>fecha</td>
        <td>Fecha de realizada la transacción.</td>
        <td>2019-05-31</td>
        <td>ocds:Transaction</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Transaccion</td>
        <td>transaccion_moneda</td>
        <td>alfanumérico</td>
        <td>Moneda de la transacción.</td>
        <td>ARS</td>
        <td>ocds:Transaction</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Transaccion</td>
        <td>transaccion_importe</td>
        <td>alfanumérico</td>
        <td>Importe de la transacción.</td>
        <td>150000</td>
        <td>ocds:Transaction</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Transaccion</td>
        <td>transaccion_origen</td>
        <td>numérico</td>
        <td>Organización que realiza el pago.</td>
        <td>Ministerio de modernización</td>
        <td>ocds:Transaction</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Transaccion</td>
        <td>transaccion_destino</td>
        <td>alfanumérico</td>
        <td>Organización que recibe el pago.</td>
        <td>HAL2000</td>
        <td>ocds:Transaction</td>
        <td></td>
    </tr>
        
</table>
### Recurso: Items Adquiridos

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
        <td>Identificador universal de open contracting.</td>
        <td>ocds-twb234-0005</td>
        <td>ocds:Release</td>
        <td></td>
    </tr>
        
    <tr>
        <td><Etapa>_Item</td>
        <td>item_etapa_id</td>
        <td>alfanumérico</td>
        <td>Identificador de la etapa a la que pertenece el item.</td>
        <td></td>
        <td>ocds:Item</td>
        <td></td>
    </tr>
        
    <tr>
        <td><Etapa>_Item</td>
        <td>item_id</td>
        <td>alfanumérico</td>
        <td>Identificación del item.</td>
        <td>3245</td>
        <td>ocds:Item</td>
        <td></td>
    </tr>
        
    <tr>
        <td><Etapa>_Item</td>
        <td>item_descripcion</td>
        <td>alfanumérico</td>
        <td>Descripción del item.</td>
        <td>Servicio de consultoria</td>
        <td>ocds:Item</td>
        <td></td>
    </tr>
        
    <tr>
        <td><Etapa>_Item</td>
        <td>item_clasificacion</td>
        <td>alfanumérico</td>
        <td>Clasificación del item.</td>
        <td>Soporte y mantenimiento de hardware</td>
        <td>ocds:Item</td>
        <td></td>
    </tr>
        
    <tr>
        <td><Etapa>_Item</td>
        <td>item_cantidad</td>
        <td>numérico</td>
        <td>Cantidad de items.</td>
        <td>1</td>
        <td>ocds:Item</td>
        <td></td>
    </tr>
        
    <tr>
        <td><Etapa>_Item</td>
        <td>item_unidad</td>
        <td>alfanumérico</td>
        <td>Unidad de medida para cuantificar el item.</td>
        <td>Cantidad</td>
        <td>ocds:Item</td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
