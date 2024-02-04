# Neurona de Muestra con Aprendizaje Supervisado

Este repositorio contiene una implementación en Python de una neurona simple con aprendizaje supervisado utilizando el algoritmo de perceptrón. La aplicación proporciona una interfaz gráfica de usuario (GUI) construida con la biblioteca `customtkinter`, lo que permite cargar un conjunto de datos en formato CSV para entrenar la neurona.

## Estructura del Proyecto

### Archivos Principales

1. **`main.py`**: Este archivo sirve como punto de entrada principal del programa. Instancia la aplicación principal `App` que contiene la GUI.

2. **`logic.py`**: Define la clase `Neuron`, que representa la neurona. Contiene métodos para calcular pesos, realizar la función de paso y llevar a cabo la optimización mediante el algoritmo de perceptrón.

3. **`Plots.py`**: Contiene la función `plot_data` que utiliza `seaborn` y `matplotlib` para visualizar los cambios en los pesos y la norma del error en cada iteración del entrenamiento.

## Uso de la Aplicación

1. Ejecute `main.py` para iniciar la aplicación.

2. Haga clic en el botón "Subir .CSV" para cargar un conjunto de datos en formato CSV.

3. Configure los parámetros de entrenamiento, como la tasa de aprendizaje (ETA) y el número de épocas.

4. Haga clic en el botón "Iniciar" para iniciar el entrenamiento de la neurona.

5. Los resultados, incluyendo la norma del error final, los pesos iniciales y finales, y la tasa de aprendizaje, se mostrarán en el área de resultados.

6. Además, se generará un gráfico que ilustra los cambios en los pesos y la norma del error en cada iteración.

## Requisitos

El código utiliza las bibliotecas estándar de Python, así como `customtkinter`, `pandas`, `seaborn` y `matplotlib`. Asegúrese de tener estas bibliotecas instaladas antes de ejecutar la aplicación:

```bash
pip install customtkinter pandas seaborn matplotlib
