# Prototipo académico para el monitoreo y detección de lenguaje agresivo multimodal para prevenir el maltrato a Adultos Mayores.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HuggingFace](https://img.shields.io/badge/huggingface-%23FFD21E.svg?style=for-the-badge&logo=huggingface&logoColor=white)


Este repositorio forma parte del trabajo 
"Monitoreo y detección de lenguaje agresivo multimodal para prevenir el maltrato a Adultos Mayores." del Equipo 3004H para la asignatura de Seminario de Innovación en Inteligencia Artificial (SIIA) de la Maestría en Inteligencia Artificial de UNIR México. El trabajo tiene como objetivo desarrollar una herramienta tecnológica basada en Inteligencia Artificial (IA) capaz de detectar el lenguaje agresivo en conversaciones mediante un enfoque multimodal que integra:

- Análisis de la tonalidad del audio.
- Análisis semántico del texto transcrito.
- Ensamble de modelos para la decision final.

La finalidad es contribuir a la detección temprana de posibles situaciones de maltrato psicológico hacia adultos mayores, facilitando un envejecimiento saludable de los mismos. 


### DEMO técnico del prototipo desplegado en Render
|Componente|Url|
|--|--|
|Frontend (Client)|https://prototipo-siia-9elu.onrender.com/ |
|Backend (API)|https://prototipo-siia.onrender.com/|
|Swagger (API docs)|https://prototipo-siia.onrender.com/docs|
|Documentación técnica (ReDoc)|https://prototipo-siia.onrender.com/|



## Tabla de contenido

- [1. Autores](#1-autores)
- [2. Objetivos](#2-objetivos)
- [3. Características](#3-caracteristicas)
- [4. Arquitectura](#4-arquitectura-del-sistema)
- [5. Tecnologías](#5-tecnologías)
- [6. Estructura del repositorio](#6-estructura-del-repositorio)
- [7. Requisitos](#7-requisitos)
- [8. Instalación](#8-instalación)
- [9. Uso](#9-uso)
- [10. Datasets](#10-datasets)

### 1. Autores

| Apellidos            | Nombres         |
| -------------------- | --------------- |
| Martínez Cruz        | Luis Arturo.    |
| Rentería Ramírez     | Mariana Jazmín. |
| Rodríguez Valladares | Olga Sarahi.    |

### 2. Objetivos

#### Objetivo general:
Implementar una solución de IA multimodal que permita identificar lenguaje agresivo mediante análisis de audio y texto en conversaciones casi en tiempo real.

#### Objetivos específicos 

- Capturar y transcribir conversaciones de dos personas casi en tiempo real.
  - Mantener una latencia de máximo 500ms.
  - Mantener una Word Error Rate de entre 0 y15%.
- Analizar el audio para clasificar tonalidades de agresividad en la voz.
- Analizar el texto para clasificación de palabras agresivas.
- Combinar ambos análisis bajo un ensamble para determinar la presencia de lenguaje agresivo.
- Obtener métricas de F1 Score en los modelos de clasificación y ensamble iguales o mayores a 0.85, dando prioridad al recall para minimizar los falso negativos; es decir:
  - Valores de recall y precisiones superiores a 0.85
  - Mayor prioridad a valores de recall alto vs precisión.
- Desarrollar un prototipo mínimo viable (MVP) con los puntos anteriores.

### 3. Características

- Capturar audio de forma estable.
- Generar y almacenar correctamente los archivos creados.
- Transcribir conversaciones, mostrar el texto en pantalla y almacenarlo en un archivo.
- Realizar análisis prosódico (volumen y tonos agresivos) del audio y mostrar una señal visual en pantalla cuando detecte patrones agresivos.
- Identificar palabras agresivas en la transcripción y resaltarlas al mostrar en pantalla.
- Mostrar en pantalla los resultados integrados de los modelos prosódico y léxico.

### 4. Arquitectura del sistema

Arquitectura cliente servidor desacoplada
<!-- ![Diagrama de la solución](/resources/diagrama_solucion.png) -->

#### Frontend
- Captura audio.
- Envía el audio al backend.
- Muestra la transcripción y resultados en pantalla.

#### Backend
- Recibe el audio.
- Realiza el proceso de transcripción.
- Clasifica el audio con el modelo de análisis prosódico.
- Clasifica el texto transcrito utilizando el modelo de análisis de sentimientos.
- Ejecuta el ensamble de modelos.
- Devuelve los resultados al frontend.

### 5. CI/CD
El proyecto implementa Integracion Continua, Despliegie Continuo (CI/CD) utilizando GitHub y Rendeer.
Se utiliza un modelo de despliegue automatico, donde cada actualizacion en la rama configurada activa el proceso de construccion y publicacion de los servicios web para frontend y backend.

Flujo de despliegue
1. Push a repositorio GitHub.
2. Render detecta cambios en la rama configurada.
3. Instalación automática de dependencias.
4. Construcción del servicio.
5. Despliegue automático del servicio en la nube.

Esto permite mantener el prototipo disponible en una URL publica sin intervención manual.

### 5. Tecnologías

Lenguaje de programación
- Python 3.9

Frontend

| Herramienta/librería | Version | Uso dentro del proyecto |
| -------------------- | --------------- | --------------- |
|   streamlit       | 1.50.0 | Interfaz gráfica    | 
|         |   | 
|  |    |
 

Backend

| Herramienta/librería | Version | Uso dentro del proyecto |
| -------------------- | --------------- | --------------- |
| Fastapi        |0.128.0| Exposición de endpoints Rest del backend   |
| uvicorn     | 0.40.0 | Ejecuta la api como servidor web
|  |    |
 

### 6. Estructura del repositorio
<p>El proyecto se divide en dos carpetas principales Frontend (Cliente) y Backend (Servidor)  </p>

<!-- Front -->

<!-- Back -->
<!-- 195 ├, 192 └  ── -->
```
Repositorio

├── prototipo-client/
|   ├──app.py
|   ├──.python-version
|   └──requirements.txt
|
├── prototipo-api/
|   ├──main.py
|   ├──.python-version
|   └──requirements.txt
|
├── README.md
└── resources
```

- **prototipo-client/**: contiene la aplicación cliente encargada de la captura de audio y visualización de resultados.
 - `app.py`: pagina principal del cliente de streamlit.  
  - `.python-version`: especifica la versión de Python utilizada en el entorno.  
  - `requirements.txt`: lista las dependencias necesarias para ejecutar el frontend.
- **prototipo-api/**: implementa el backend del sistema utilizando FastAPI para exponer los servicios del proyecto.  
  - `main.py`: punto de entrada donde se definen los endpoints del servicio.  
  - `.python-version`: especifica la versión de Python utilizada en el entorno.  
  - `requirements.txt`: lista las dependencias necesarias para ejecutar el backend.
- **resources/**: almacena archivos estáticos como diagramas e imágenes del proyecto.
- **README.md**: documentación principal del repositorio.

### 7. Requisitos

- Git bash / Git Desktop
- Python 3.9
- Entorno virtual (venv o conda)
- Visual Studio Code o terminal

### 8. Instalación

#### 8.1 Clonar repositorio 
Para clonar el repositorio de manera local se utiliza el siguiente código:

````bash
git clone https://github.com/Equipo-3004H/Prototipo-SIIA.git 
cd Prototipo-SIIA
````

#### 8.2 Crear entorno virtual

```
python -m venv venv
source venv/bin/activate   # mac/linux
venv\Scripts\activate      # windows
```


#### 8.3 Instalar dependencias 

Tanto el frontend como el backend cuentan con un archivo `requirements` el cual contiene todas las dependencias necesarias para levantar cada solución 

````
pip install -r requirements.txt
````


### 9. Uso

#### Backend

Para levantar el repositorio del backend se ejecuta el siguiente comando en la terminal 

<!-- #fastapi dev main.py -->

``` 
uvicorn main:app --reload
```
Accesos:
- Api local: http://127.0.0.1:8000/
- Swagger: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

#### Frontend
Para levantar el repositorio del frontend se ejecuta el siguiente comando en la terminal

``` 
streamlit run app.py
```
Streamlit se levanta en la siguiente direccion 
 
Acceso local: http://localhost:8501/


### 10. Datasets

Para el entrenamiento de los modelos se utilizan datasets publicos

|Dataset|Tipo|Descripción|
|--|--|--|
||||
||||
||||
<!-- para entrenamiento -->
<!--  -->

### 11. Estado del proyecto

Actualmente el prototipo académico se encuentra en fase de desarrollo.
