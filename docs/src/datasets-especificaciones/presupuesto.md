# Presupuesto

El presupuesto asignado a cada área, programa o función, las modificaciones durante cada ejercicio anual y el estadode ejecución actualizado en forma trimestral hasta el último nivel de desagregación en que se procese.

* **Tema**: Economía y finanzas
* **Estándar referencia**: [Open Fiscal Data Package](https://docs.openspending.org/en/latest/contributors/package/)
* **Formatos**: CSV

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Presupuesto
**[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/presupuesto)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/presupuesto)**

<table>
    <tr>
        <th>organizacion_id</th>
        <th>organizacion_nombre</th>
        <th>organizacion_clasificacion</th>
        <th>gift_fecha</th>
        <th>gift_clasificacion_economica</th>
        <th>gift_clasificacion_funcional</th>
        <th>gift_descripción</th>
        <th>gift_actividad</th>
        <th>gift_administrador</th>
        <th>gift_procurador</th>
        <th>gift_destinatario</th>
        <th>gift_proveedor</th>
        <th>gift_transferencias</th>
        <th>gift_destino_presupestal</th>
        <th>gift_tipo_presupuesto</th>
        <th>gift_fuente_financiera</th>
        <th>gift_fase</th>
        <th>gift_informacion_geografica</th>
        <th>gift_identificador_línea_presupuestal</th>
        <th>gift_identificador_factura</th>
        <th>gift_importe</th>
        <th>gift_otros</th>
    </tr>

    <tr>
        <td>2</td>
        <td>Ministerio de Modernización</td>
        <td>Poder Ejecutivo</td>
        <td>2019-01-01</td>
        <td>Salarios</td>
        <td>Pago de salarios</td>
        <td>Pago de salarios Diciembre 2018</td>
        <td>Proyecto BID - 26548</td>
        <td>Ministerio de Modernización</td>
        <td></td>
        <td>Banco Nación</td>
        <td>SACE S.R.L</td>
        <td>No</td>
        <td>Egresos</td>
        <td>Gasto</td>
        <td>BID</td>
        <td>Aprobado</td>
        <td>Buenos Aires</td>
        <td>3427</td>
        <td>A32666</td>
        <td>1500000</td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Clases

Un item del `Presupuesto` es un gasto o ingreso asignado a una `Organización` para el financiamiento de sus misiones y funciones.

Descargar clases en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/presupuesto)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/presupuesto)**


<table>
    <tr>
        <th>nombre</th>
        <th>descripcion</th>
    </tr>

    <tr>
        <td>Organización</td>
        <td>Atributos que describen a las instituciones públicas que reciben, asignan y gastan presupuesto.</td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>Atributos que describen los flujos o partidas presupuestarias que son objeto de asignación y seguimiento para el financiamiento de las actividades de las organizaciones.</td>
    </tr>
        
</table>

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/presupuesto)** | **[XLSX](https://github.com/datosgobar/paquete-apertura-datos/raw/master/docs/datasets-especificaciones/presupuesto)**

### Recurso: Presupuesto

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
        <td>Organización</td>
        <td>organizacion_id</td>
        <td>alfanumérico</td>
        <td>Identificador único para la organización.</td>
        <td>2</td>
        <td>popolo:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre principal de la organización. Por ejemplo: su nombre legal u oficial.</td>
        <td>Ministerio de Modernización</td>
        <td>popolo:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_clasificacion</td>
        <td>alfanumérico</td>
        <td>La clasificación de la organización. Por ejemplo: "Poder Ejecutivo".</td>
        <td>Poder Ejecutivo</td>
        <td>popolo:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_fecha</td>
        <td>fecha</td>
        <td>Fecha de publicación del presupuesto o fecha en la que se aprueba el presupuesto.</td>
        <td>2019-01-01</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_clasificacion_economica</td>
        <td>alfanumérico</td>
        <td>Identifica el tipo de presupuesto e ingresos o gastos incurridos. Por ejemplo: salarios, bienes y servicios, transferencias y pagos de intereses, o gastos de capital.</td>
        <td>Salarios</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_clasificacion_funcional</td>
        <td>alfanumérico</td>
        <td>Gastos o ingresos según los fines y objetivos para los que están destinados.</td>
        <td>Pago de salarios</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_descripción</td>
        <td>alfanumérico</td>
        <td>Descripción o detalle del gasto, ingreso o partida presupuestaria.</td>
        <td>Pago de salarios Diciembre 2018</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_actividad</td>
        <td>alfanumérico</td>
        <td>Utilícela cuando tenga una columna de datos sobre el contrato / programa / proyecto que se está financiando.</td>
        <td>Proyecto BID - 26548</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_administrador</td>
        <td>alfanumérico</td>
        <td>Autoridad que gasta o a la que le ingresa el dinero.</td>
        <td>Ministerio de Modernización</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_procurador</td>
        <td>alfanumérico</td>
        <td>Entidad gubernamental que actúa como gestor de la transacción, si es diferente de la institución que controla el proyecto.</td>
        <td></td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_destinatario</td>
        <td>alfanumérico</td>
        <td>Destinatario (si existe) al que se dirige el elemento de ingreso.</td>
        <td>Banco Nación</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_proveedor</td>
        <td>alfanumérico</td>
        <td>Destinatario del gasto.</td>
        <td>SACE S.R.L</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_transferencias</td>
        <td>alfanumérico</td>
        <td>Propiedades adicionales con respecto a si el gasto o ingreso contiene transferencias presupuestarias.</td>
        <td>No</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_destino_presupestal</td>
        <td>alfanumérico</td>
        <td>Especifica si los valores en esta línea son egresos o ingresos.</td>
        <td>Egresos</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_tipo_presupuesto</td>
        <td>alfanumérico</td>
        <td>Atributos adicionales que proporcionan más propiedades.</td>
        <td>Gasto</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_fuente_financiera</td>
        <td>alfanumérico</td>
        <td>Fuente financiera de los fondos presupuestarios.</td>
        <td>BID</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_fase</td>
        <td>alfanumérico</td>
        <td>Identificador de fase para los valores en esta línea (por ejemplo, aprobado, ejecutado, etc.).</td>
        <td>Aprobado</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_informacion_geografica</td>
        <td>alfanumérico</td>
        <td>Puede ser una dirección, un código de área, una descripción, etc.</td>
        <td>Buenos Aires</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_identificador_línea_presupuestal</td>
        <td>alfanumérico</td>
        <td>Identificador único para esta línea de presupuesto.</td>
        <td>3427</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_identificador_factura</td>
        <td>alfanumérico</td>
        <td>Número de factura dado por el proveedor</td>
        <td>A32666</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_importe</td>
        <td>numerico</td>
        <td>Importe o valor del gasto o ingreso (obligatorio).</td>
        <td>1500000</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_otros</td>
        <td>texto</td>
        <td>Notas o comentarios adicionales.</td>
        <td></td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
