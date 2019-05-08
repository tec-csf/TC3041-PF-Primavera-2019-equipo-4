# TC3041 Proyecto  Final Primavera 2019

Where to go now?
---

##### Integrantes:
1. Saúl Enrique Labra Cruz
2. Rodrigo García Mayo


---
## 1. Aspectos generales

### 1.1 Requerimientos técnicos

A continuación se mencionan los requerimientos técnicos mínimos del proyecto, favor de tenerlos presente para que cumpla con todos.

* El equipo tiene la libertad de elegir las tecnologías de desarrollo a utilizar en el proyecto, sin embargo, debe tener presente que la solución final se deberá ejecutar en una plataforma en la nube. Puede ser  [Google Cloud Platform](https://cloud.google.com/?hl=es), [Azure](https://azure.microsoft.com/en-us/) o AWS [AWS](https://aws.amazon.com/es/free/).
* El proyecto debe utilizar al menos dos modelos de bases de datos diferentes, de los estudiados en el curso.
* La solución debe utilizar una arquitectura de microservicios. Si no tiene conocimiento sobre este tema, le recomiendo la lectura [*Microservices*](https://martinfowler.com/articles/microservices.html) de [Martin Fowler](https://martinfowler.com).
* La arquitectura debe ser modular, escalable, con redundancia y alta disponibilidad.
* La arquitectura deberá estar separada claramente por capas (*frontend*, *backend*, *API RESTful*, datos y almacenamiento).
* Los diferentes componentes del proyecto (*frontend*, *backend*, *API RESTful*, bases de datos, entre otros) deberán ejecutarse sobre contenedores [Docker](https://www.docker.com/) y utilizar [Kubernetes](https://kubernetes.io/) como orquestador.
* Todo el código, *datasets* y la documentación del proyecto debe alojarse en un repositorio de GitHub siguiendo al estructura que aparece a continuación.

### 1.2 Estructura del repositorio
El proyecto debe seguir la siguiente estructura de carpetas:
```
- / 			        # Raíz de todo el proyecto
    - README.md			# Archivo con los datos del proyecto (este archivo)
    - frontend			# Carpeta con la solución del frontend (Web app)
    - backend			# Carpeta con la solución del backend (CMS)
    - api			# Carpeta con la solución de la API
    - datasets		        # Carpeta con los datasets y recursos utilizados (csv, json, audio, videos, entre otros)
    - dbs			# Carpeta con los modelos, catálogos y scripts necesarios para generar las bases de datos
    - models			# Carpeta donde se almacenarán los modelos de Machine Learning ya entrenados 
    - docs			# Carpeta con la documentación del proyecto
        - stage_f               # Documentos de la entrega final
        - manuals               # Manuales y guías
```

### 1.3 Documentación  del proyecto

Como parte de la entrega final del proyecto, se debe incluir la siguiente información:

* Justificación de los modelo de *bases de datos* que seleccionaron.
* Descripción del o los *datasets* y las fuentes de información utilizadas.
* Guía de configuración, instalación y despliegue de la solución en la plataforma en la nube  seleccionada.
* Documentación de la API. Puede ver un ejemplo en [Swagger](https://swagger.io/). 
* El código debe estar documentado siguiendo los estándares definidos para el lenguaje de programación seleccionado.

## 2. Descripción del proyecto

El proyecto consiste en una web app que con base en información almacenada en una base de datos "influxdb" ligaba datos de  la temperatura y el esetado del clima en diferentes ciudades con datos de atracciones públicas almacenadas en una base de datos mongodb utilizando como atributo discriminatorio el estado del clima. Es decir, el usuario tiene la posibilidad de seleccionar una fecha y hora determinada en una ciudad en específico y en respuesta obtiene una lista con las posibles atracciones a las que puede ir.

## 3. Solución

A continuación aparecen descritos los diferentes elementos que forman parte de la solución del proyecto.

### 3.1 Modelos de *bases de datos* utilizados

En la aplicación era necesario guardar información cada hora del clima de las diferentes ciudades en México, es por esto que se decidió utilizar InfluxDB. Ya que tiene una manejo bueno de series de tiempo y es utilizado para grandes volumenes de información.

En cuanto a MongoDB, se usó esta base de datos dada su facilidad para almacenar los atributos sin necesidad de definirlos en un inicio y tambien gracias a la facilidad de uso en conjunto de python para hacer consultas.

### 3.2 Arquitectura de la solución

![arquitectura.png](https://github.com/tec-csf/TC3041-PF-Primavera-2019-equipo-4/blob/master/arquitectura.png)

### 3.3 Frontend

El front-end fue desarrollado utilizando html, css y javascript regulares complementandolo con el uso de Jinja, un templating engine que mediante sintaxis especial reemplazaba en determinados lugares del html el contenido para presentar la informacion obtenida de los queries a las bases de datos implementadas.

#### 3.3.1 Lenguaje de programación

Python. Python se ocupó en conjunto con Flask utilizando la función render_template() para generar el html dinámico con la informacin necesaria

#### 3.3.2 Framework

Flask y Jinja

#### 3.3.3 Librerías de funciones o dependencias

Flask y Jinja

### 3.4 Backend

El backend está sobre las bases de datos:
-   InfluxDB
    -   Esta base permite guardar datos en determinados periodos de tiempos. Un modelo que permite el ingreso de información del clima, utilizado para esta aplicación.
-   MongoDB
    -   MongoDb es una base de datos no estructurada que tiene la ventaja de un facil almacenamiento de "documentos", siendo esta la unidad para almacenar registros ya que los atributos de los documentos no deben estar previamente definidos, es decir los atributos pueden variar conforme se insertan documentos

#### 3.4.1 Lenguaje de programación
Para lograr la comunicación a las bases de datos se utilizo python.

#### 3.4.2 Framework
-   InfluxDB
-   MongoDB
#### 3.4.3 Librerías de funciones o dependencias
-   MongoClient: pymongo
-   InfluxDBClient: influxdb

### 3.5 API

Para la comunicación entre frontend y back-end se utilizó el framework Flask para Python que con base en la url que se accedía desde el explorador detonaba la ejecución de los diferentes métodos especificados en el programa que podían a su vez llamar a la ejecución de queries específicos en las bases de datos.

#### 3.5.1 Lenguaje de programación

    Python
    
    Referencia: https://docs.python.org/3/
    
#### 3.5.2 Framework
        
    Flask
    
    Referencia: http://flask.pocoo.org/
    
#### 3.5.3 Librerías de funciones o dependencias

ENTRY POINT: "/"
* **Descripción**: solicita a la aplicación en python la lista de estados para popular la lista de estados a seleccionar por el usuario y hace "render_template()" al html de la página principal
* **URL**: "/"

END POINT: "/city_select"
* **Descripción**: solicita a la aplicación en python un render_template() con el html de la página de selección de ciudad utilizando los datos seleccionados por la "form" en la página principal. El paso de la información seleccionada por el usuario en la "form" se hace mediante POST
* **URL**: "/city_select"

END POINT: "/query_atractions"
* **Descripción**: solicita a la aplicación en python un render_template() con el html de las atracciones posibles con base en la selección de la ciudad
* **URL**: "/query_atractions"

## 3.6 Pasos a seguir para utilizar el proyecto

*[Incluya aquí una guía paso a paso para poder utilizar el proyecto, desde la clonación del repositorio hasta el despliegue de la solución en una plataforma en la nube.]*

Ejecucion local en docker:

*Clonar el repositorio de GitHub:
git clone https://github.com/tec-csf/TC3041-PF-Primavera-2019-equipo-4.git

Cambiarse a la carpeta de app y compilar la imagen personalizada de la aplicación: 
cd app/
docker build -t flaskpf .

Verifique que la imagen fue creada correctamente con el siguiente comando:
docker images | grep app

Iniciar el contenedor:
docker run --rm --name app -p 8080:8080 flaskpf

Acceder al http://localhost:8080

Ejecución en GCP:

## 4. Referencias

*[Incluya aquí las referencias a sitios de interés, datasets y cualquier otra información que haya utilizado para realizar el proyecto y que le puedan ser de utilidad a otras personas que quieran usarlo como referencia]*
