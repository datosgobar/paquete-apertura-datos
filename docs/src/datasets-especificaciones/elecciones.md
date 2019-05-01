# Resultados Electorales

Resultados de las últimas elecciones municipales o provinciales desagregadas por mesas electorales.

* **Tema**: Gobierno y sector público
* **Estándar referencia**: Election data format (Open Data Institute)
* **Formatos**: CSV
* **Ejemplo:**: https://github.com/theodi/election-data-format/blob/gh-pages/tables/index.md


<!-- COMIENZO TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Ejemplos

### Recurso: Eleccion  
**[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/elecciones/eleccion.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/elecciones/eleccion.xlsx)**

<table>
    <tr>
        <th>eleccion_id</th>
        <th>eleccion_nombre</th>
        <th>eleccion_tipo</th>
        <th>eleccion_fecha_inicio</th>
        <th>elección_fecha_fin</th>
    </tr>

    <tr>
        <td>GenCor2019</td>
        <td>Elecciones Generales de la Provincia de Córdoba</td>
        <td>Gobernador y Vice Gobernador</td>
        <td>2019-05-12</td>
        <td>2019-05-12</td>
    </tr>
        
</table>
### Recurso: ResultadoOpcion
**[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/elecciones/resultadoopcion.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/elecciones/resultadoopcion.xlsx)**

<table>
    <tr>
        <th>opcion_eleccion_id</th>
        <th>opcion_region_id</th>
        <th>opcion_region_nombre</th>
        <th>opcion_partido_id</th>
        <th>opcion_partido_nombre</th>
        <th>opcion_candidato_id</th>
        <th>opcion_candidato_nombre</th>
        <th>opcion_candidato_votos</th>
        <th>resultado_elegido</th>
        <th>resultado_orden</th>
    </tr>

    <tr>
        <td>GenCor2019</td>
        <td>AR-X</td>
        <td>Provincia de Córdoba</td>
        <td>4</td>
        <td>Encuentro por Córdoba</td>
        <td>1</td>
        <td>Juan Martinez</td>
        <td>5000</td>
        <td>No</td>
        <td>10</td>
    </tr>
        
</table>
### Recurso: ResultadoMesa
**[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/elecciones/resultadomesa.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/elecciones/resultadomesa.xlsx)**

<table>
    <tr>
        <th>resultado_eleccion_id</th>
        <th>resultado_region_id</th>
        <th>resultado_circuito_id</th>
        <th>resultado_mesa_id</th>
        <th>resultado_partido_id</th>
        <th>resultado_candidato_id</th>
        <th>resultado_opcion_candidato_id</th>
        <th>resultado_votos_obtenidos</th>
    </tr>

    <tr>
        <td>GenCor2019</td>
        <td>AR-X</td>
        <td>32</td>
        <td>1</td>
        <td>4</td>
        <td>1</td>
        <td>9009</td>
        <td>26</td>
    </tr>
        
</table>
### Recurso: ResumenMesa
**[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/elecciones/resumenmesa.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/elecciones/resumenmesa.xlsx)**

<table>
    <tr>
        <th>resumen_eleccion_id</th>
        <th>resumen_region_id</th>
        <th>resultado_circuito_id</th>
        <th>resumen_mesa_id</th>
        <th>resumen_votos_anulados</th>
        <th>resumen_votos_en_blanco</th>
        <th>resumen_votos_otro_estado</th>
        <th>resumen_votos_emitidos</th>
    </tr>

    <tr>
        <td>GenCor2019</td>
        <td>AR-X</td>
        <td>32</td>
        <td>1</td>
        <td>25</td>
        <td>180</td>
        <td></td>
        <td>1207</td>
    </tr>
        
</table>

<!-- FIN TABLA DE EJEMPLO. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

<!-- FIN TABLA DE CLASES. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->


<!-- COMIENZO TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->

## Campos

Descargar campos en **[CSV](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/elecciones-campos.csv)** | **[XLSX](/Users/abenassi/github/paquete-apertura-datos/docs/src/datasets-especificaciones/elecciones-campos.xlsx)**

### Recurso: Eleccion  

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
        <td>Eleccion</td>
        <td>eleccion_id</td>
        <td>alfanumérico</td>
        <td>Identificacón única del acto eleccionario</td>
        <td>GenCor2019</td>
        <td>edf:Contest</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Eleccion</td>
        <td>eleccion_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre de la elección</td>
        <td>Elecciones Generales de la Provincia de Córdoba</td>
        <td>edf:Contest</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Eleccion</td>
        <td>eleccion_tipo</td>
        <td>alfanumérico</td>
        <td>Tipo de elección</td>
        <td>Gobernador y Vice Gobernador</td>
        <td>edf:Contest</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Eleccion</td>
        <td>eleccion_fecha_inicio</td>
        <td>fecha</td>
        <td>Fecha de inicio de la elección</td>
        <td>2019-05-12</td>
        <td>edf:Contest</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Eleccion</td>
        <td>elección_fecha_fin</td>
        <td>fecha</td>
        <td>Fecha de fin de la elección</td>
        <td>2019-05-12</td>
        <td>edf:Contest</td>
        <td></td>
    </tr>
        
</table>
### Recurso: ResultadoOpcion

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
        <td>Opcion</td>
        <td>opcion_eleccion_id</td>
        <td>alfanumérico</td>
        <td>URI unica que identifique el acto eleccionario</td>
        <td>GenCor2019</td>
        <td>edf:Choices</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Opcion</td>
        <td>opcion_region_id</td>
        <td>alfanumérico</td>
        <td>URI que identifica la region donde se realiza la elección. xx:yy:zzzz donde xx corresponde al codigo de provincia, yy corresponde al código de departamento, zzzz corresponde al codigo de localidad. En caso de no existir un codigo electoral se puede usar la codificación ISO 3166-2</td>
        <td>AR-X</td>
        <td>edf:Choices</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Opcion</td>
        <td>opcion_region_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre de la región</td>
        <td>Provincia de Córdoba</td>
        <td>edf:Choices</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Opcion</td>
        <td>opcion_partido_id</td>
        <td>alfanumérico</td>
        <td>URI identificando al partido</td>
        <td>4</td>
        <td>edf:Choices</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Opcion</td>
        <td>opcion_partido_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre del partido</td>
        <td>Encuentro por Córdoba</td>
        <td>edf:Choices</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Opcion</td>
        <td>opcion_candidato_id</td>
        <td>alfanumérico</td>
        <td>URI identificando al candidato</td>
        <td>1</td>
        <td>edf:Choices</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Opcion</td>
        <td>opcion_candidato_nombre</td>
        <td>alfanumérico</td>
        <td>Nombre del candidato</td>
        <td>Juan Martinez</td>
        <td>edf:Choices</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Opcion</td>
        <td>opcion_candidato_votos</td>
        <td>numérico</td>
        <td></td>
        <td>5000</td>
        <td>edf:Choices</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Resultado</td>
        <td>resultado_elegido</td>
        <td>booleano</td>
        <td>Indica si el candidato fue elegido o no</td>
        <td>No</td>
        <td>edf:Results</td>
        <td>Este valor en el estandar se ubica dentro del resultado, pero a los efectos de esta propuesta corresponde que se ubique a nivel del candidato</td>
    </tr>
        
    <tr>
        <td>Resultado</td>
        <td>resultado_orden</td>
        <td>numérico</td>
        <td>Campo que permite ordenar el resultado de la elección</td>
        <td>10</td>
        <td>edf:Results</td>
        <td>Este valor en el estandar se ubica dentro del resultado, pero a los efectos de esta propuesta corresponde que se ubique a nivel del candidato</td>
    </tr>
        
</table>
### Recurso: ResultadoMesa

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
        <td>Resultado</td>
        <td>resultado_eleccion_id</td>
        <td>alfanumérico</td>
        <td>Identificacón única del acto eleccionario</td>
        <td>GenCor2019</td>
        <td>edf:Results</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Resultado</td>
        <td>resultado_region_id</td>
        <td>alfanumérico</td>
        <td>Identifica la region donde se realiza la elección. xx:yy:zzzz donde xx corresponde al codigo de provincia, yy corresponde al código de departamento, zzzz corresponde al codigo de localidad.</td>
        <td>AR-X</td>
        <td>edf:Results</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Resultado</td>
        <td>resultado_circuito_id</td>
        <td>alfanumérico</td>
        <td>Indica circuito de votación</td>
        <td>32</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Resultado</td>
        <td>resultado_mesa_id</td>
        <td>alfanumérico</td>
        <td>Indica la mesa de votación</td>
        <td>1</td>
        <td>schema:Thing</td>
        <td>Se agrega la mesa de votación para conocer los resultados a un nivel mas desagregado.</td>
    </tr>
        
    <tr>
        <td>Resultado</td>
        <td>resultado_partido_id</td>
        <td>alfanumérico</td>
        <td>Identificación única del partido</td>
        <td>4</td>
        <td>edf:Results</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Resultado</td>
        <td>resultado_candidato_id</td>
        <td>alfanumérico</td>
        <td>Identificación única del candidato</td>
        <td>1</td>
        <td>edf:Results</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Resultado</td>
        <td>resultado_opcion_candidato_id</td>
        <td>alfanumérico</td>
        <td>Identifica la hoja de votación o lista a la que pertenece el candidato</td>
        <td>9009</td>
        <td>edf:Results</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Resultado</td>
        <td>resultado_votos_obtenidos</td>
        <td>numérico</td>
        <td>Cantidad de votos obtenidos por el candidato en esa lista</td>
        <td>26</td>
        <td>edf:Results</td>
        <td></td>
    </tr>
        
</table>
### Recurso: ResumenMesa

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
        <td>Resultado</td>
        <td>resumen_eleccion_id</td>
        <td>alfanumérico</td>
        <td>Identificacón única del acto eleccionario</td>
        <td>GenCor2019</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Resultado</td>
        <td>resumen_region_id</td>
        <td>alfanumérico</td>
        <td>Identifica la region donde se realiza la elección. xx:yy:zzzz donde xx corresponde al codigo de provincia, yy corresponde al código de departamento, zzzz corresponde al codigo de localidad.</td>
        <td>AR-X</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Resultado</td>
        <td>resultado_circuito_id</td>
        <td>alfanumérico</td>
        <td>Indica circuito de votación</td>
        <td>32</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Resultado</td>
        <td>resumen_mesa_id</td>
        <td>alfanumérico</td>
        <td>Indica la mesa de votación</td>
        <td>1</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Resumen por mesa</td>
        <td>resumen_votos_anulados</td>
        <td>numérico</td>
        <td>Cantidad de votos anulados en la mesa receptora de votos</td>
        <td>25</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Resumen por mesa</td>
        <td>resumen_votos_en_blanco</td>
        <td>numérico</td>
        <td>Cantidad de votos en blanco en la mesa receptora de votos</td>
        <td>180</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Resumen por mesa</td>
        <td>resumen_votos_otro_estado</td>
        <td>numérico</td>
        <td>Cantidad de votos con otro estado en la mesa receptora de votos</td>
        <td></td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
    <tr>
        <td>Resumen por mesa</td>
        <td>resumen_votos_emitidos</td>
        <td>alfanumérico</td>
        <td>Total de votos emitidos se compone del total de los votos del resumen por mesa mas los votos obtenidos por cada opcion</td>
        <td>1207</td>
        <td>schema:Thing</td>
        <td></td>
    </tr>
        
</table>

<!-- FIN TABLA DE CAMPOS POR CLASE. Dejar este comentario para edicion automatica. No editar manualmente el contenido, usar el script.  -->
