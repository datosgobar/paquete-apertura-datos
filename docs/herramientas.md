# Herramientas

Índice de herramientas desarrolladas para potenciar la apertura y consumo de datos públicos.

## Apertura

* **Portal Andino** ([Landing de producto](http://andino.datos.gob.ar/) | [Ejemplo desarrollo](http://portal-andino.datos.gob.ar/) | [Documentación](http://portal-andino.readthedocs.io/) | [Github](http://github.com/datosgobar/portal-andino)). Distribución de CKAN desarrollada por la República Argentina dockerizada, fácil de instalar y compatible con el Perfil Nacional de Metadatos de la Política de Apertura de Datos.

* Herramientas para la apertura de datos
    - **pydatajson** ([Documentación](https://pydatajson.readthedocs.io/) | [Github](https://github.com/datosgobar/pydatajson)). Librería en python para analizar, generar y validar metadatos en formato data.json.
    - **monitoreo-apertura** ([Github](https://github.com/datosgobar/monitoreo-apertura)). Aplicación web para monitoreo de la red de nodos de datos abiertos de la Administración Pública Nacional.
    - **data-cleaner** ([Documentación](https://data-cleaner.readthedocs.io/) | [Github](https://github.com/datosgobar/data-cleaner)). Librería en python para para limpieza de datos, según estándares del Equipo de Datos Argentina.
    - **django-datajsonar** ([Github](https://github.com/datosgobar/django-datajsonar)). Aplicación en _Django_ para administrar acciones sobre la red de nodos de catálogos, basada en el Perfil Nacional de Metadatos de la Política de Apertura de Datos.

## Servicios

* Georef
    - **API del Servicio de Normalización de Datos Geográficos de Argentina** ([Documentación](http://apis.datos.gob.ar/georef/) | [Github](https://github.com/datosgobar/georef-ar-api )). Normaliza nombres de provincias, departamentos, municipios, otras unidades territoriales de la Argentina, calles y direcciones. Enriquece datasets con coordenadas agregando las unidades territoriales que las contienen.

* Series de Tiempo
    - **API de Series de Tiempo de la República Argentina** ([Documentación](https://apis.datos.gob.ar/series) | [Github](https://github.com/datosgobar/series-tiempo-ar-api)). Expone recursos para buscar y consultar indicadores con evolución temporal de organismos de la Administración Pública Nacional, realizando filtros y operaciones sobre ellos.
    - [**Explorador de Series de Tiempo**](http://datos.gob.ar/series) ([Ejemplo desarrollo](https://datosgobar.github.io/series-tiempo-ar-explorer/) | [Github](https://github.com/datosgobar/series-tiempo-ar-explorer)). Interfaz web para buscar, visualizar y compartir indicadores disponibles en la API de Series de Tiempo.
    - **Landing de Series de Tiempo** ([Ministerio de Hacienda](https://www.minhacienda.gob.ar/datos/) | [Ejemplo desarrollo](https://datosgobar.github.io/series-tiempo-ar-landing/) | [Github](https://github.com/datosgobar/series-tiempo-ar-landing)). Tablero de indicadores y gráficos de la API de Series de Tiempo, fácil de configurar y personalizar para crear diferentes instancias.
    - **Scraper de Series de Tiempo en Excel** ([Github](https://github.com/datosgobar/series-tiempo-ar-scraping)). Rutina para la extracción y transformación de series de tiempo desde Excels semi-estructurados hacia distribuciones de formato abierto, basado en una extensión experimental del Perfil Nacional de Metadatos de la política de apertura de datos de la APN.
    - [**Generador de Llamadas a la API**](https://datosgobar.github.io/series-tiempo-ar-call-generator/) ([Github](https://github.com/datosgobar/series-tiempo-ar-call-generator)). Interfaz web para buscar series de tiempo de la API y construir URLs de consulta.

* **API Gateway** ([Github](https://github.com/datosgobar/api-gateway)). Aplicación en Django y Kong para administrar cuotas y ruteo de APIs.
