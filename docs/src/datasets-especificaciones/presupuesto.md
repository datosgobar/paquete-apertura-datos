# Presupuesto

<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos
    
### Recurso: Presupuesto
**[CSV](presupuesto/presupuesto.csv)** | **[XLSX](presupuesto/presupuesto.xlsx)**

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
        <th>gift_Informacion_geografica</th>
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
        <td>1</td>
        <td>A32666</td>
        <td>1500000</td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](presupuesto-campos.csv)** | **[XLSX](presupuesto-campos.xlsx)**

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
        <td>Debe ser un identificador único para la organización</td>
        <td>2</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_nombre</td>
        <td>alfanumérico</td>
        <td>El nombre principal de la organización, por ejemplo su nombre legal</td>
        <td>Ministerio de Modernización</td>
        <td>popolo:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Organización</td>
        <td>organizacion_clasificacion</td>
        <td>alfanumérico</td>
        <td>La clasificación de la organización, por ejemplo "Poder Ejecutivo"</td>
        <td>Poder Ejecutivo</td>
        <td>popolo:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_fecha</td>
        <td>fecha</td>
        <td>Fecha de publicación del presupuesto o fecha en la que se aprueba el presupuesto</td>
        <td>2019-01-01</td>
        <td>popolo:Organization</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_clasificacion_economica</td>
        <td>alfanumérico</td>
        <td>identifica el tipo de presupuesto y gastos incurridos, por ejemplo, salarios, bienes y servicios, transferencias y pagos de intereses, o gastos de capital</td>
        <td>Salarios</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_clasificacion_funcional</td>
        <td>alfanumérico</td>
        <td>gastos según los fines y objetivos para los que están destinados</td>
        <td>Pago de salarios</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_descripción</td>
        <td>alfanumérico</td>
        <td></td>
        <td>Pago de salarios Diciembre 2018</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_actividad</td>
        <td>alfanumérico</td>
        <td>utilícela cuando tenga una columna de datos sobre el contrato / programa / proyecto que se está financiando</td>
        <td>Proyecto BID - 26548</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_administrador</td>
        <td>alfanumérico</td>
        <td>autoridad que gasta el dinero</td>
        <td>Ministerio de Modernización</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_procurador</td>
        <td>alfanumérico</td>
        <td>la entidad gubernamental que actúa como gestor de la transacción, si es diferente de la institución que controla el proyecto.</td>
        <td></td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_destinatario</td>
        <td>alfanumérico</td>
        <td>el destinatario (si existe) al que se dirige el elemento de ingresos.</td>
        <td>Banco Nación</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_proveedor</td>
        <td>alfanumérico</td>
        <td>el destinatario del gasto.</td>
        <td>SACE S.R.L</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_transferencias</td>
        <td>alfanumérico</td>
        <td>propiedades adicionales con respecto a si el gasto contiene transferencias presupuestarias</td>
        <td>No</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_destino_presupestal</td>
        <td>alfanumérico</td>
        <td>especifica si los valores en esta línea son egresos o ingresos</td>
        <td>Egresos</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_tipo_presupuesto</td>
        <td>alfanumérico</td>
        <td>atributos adicionales que proporcionan más propiedades</td>
        <td>Gasto</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_fuente_financiera</td>
        <td>alfanumérico</td>
        <td>la fuente financiera de los fondos presupuestarios</td>
        <td>BID</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_fase</td>
        <td>alfanumérico</td>
        <td>el identificador de fase para los valores en esta línea (por ejemplo, aprobado, ejecutado, etc.)</td>
        <td>Aprobado</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_Informacion_geografica</td>
        <td>alfanumérico</td>
        <td>puede ser una dirección, una código de área, una descripción, etc.</td>
        <td>Buenos Aires</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_identificador_línea_presupuestal</td>
        <td>alfanumérico</td>
        <td>este es simplemente el identificador único para esta línea de presupuesto.</td>
        <td>1</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_identificador_factura</td>
        <td>alfanumérico</td>
        <td>el número de factura dado por el proveedor</td>
        <td>A32666</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_importe</td>
        <td>numerico</td>
        <td>obligatorio para asignar un valor</td>
        <td>1500000</td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Presupuesto</td>
        <td>gift_otros</td>
        <td>texto</td>
        <td>campo adicional</td>
        <td></td>
        <td>gift - openspending</td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
