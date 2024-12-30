# Sentiment Analysis with Python

## Tarea del módulo de Linea de Comandos con Python

El presente proyecto fue realizado por Ernesto Cantú para el curso de Certificación ante Informs como
Python Data Engineering.

Realizado durante las fechas Diciembre 28 y Diciembre 30 del 2024.

### Documentación del Proyecto

#### Version 1
   ##### Crea el ambiente virtual 
    Para no afectar tu ambiente global python, crea tu virtual env e instala los requerimientos de librerías.

    1. python -m venv env
    2. env\Scripts\activate
    3. pip install -r requirements.txt

    ##### Descarga el modelo Bert por primera vez

    En el archivo Bert.py se encuentran comentadas las lineas 17 y 18.
    Estas lineas lo que hacen es descargar el modelo Bert entrenado para correr en local.
    
    A su vez, este archivo tiene un módulo de pruebas que puedes correr ejecutando este módulo 
    directo en el Python REPL. Al ejecutarlo, se generará una carpeta local llamada nlptown donde 
    se guardará el modelo y el tokenizer.

    Corre ahora si el archivo main.py con las lineas 17 y 18 comentadas del archvio Bert.py

    ##### Ejecuta el módulo main.py

    1. Desde VS Code, puedes abrir el archivo main.py y ejecutarlo con el run and debug.
    2. Desde linea de comandos, puedes correr con:
    
    > python main.py

#### Proceso

    1. Se lee el archivo Json de comentarios de un producto en Amazon
    2. Se inicializa una lista de objetos Review donde se guardan todos los JSON.
    3. Se aplican técnicas de limpieza de datos: Tokenización, eliminación de stopwords y normalización
    4. Se envian textos a Sentiment Analysis con Bert 
    5. Se crean gráficas para resultados Bert y Ratings


#### Resultados
    El modelo Bert no fue del todo efectivo, por esa razón creé 2 gráficas:

    1. Una con el modelo bert (BertRes.png)
    2. Otra utilizando los ratings (RatingRes.py) que se encontraban directo en el archivo JSON.