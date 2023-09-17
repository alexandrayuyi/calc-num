# Evaluación 2 Calculo Numérico

## Descripción

El siguiente proyecto consiste en el desarrollo de 1 tema de las siguientes unidades: II,III y IV.


## Temas Elegidos

Los temas a tratar en la evaluación son los siguientes:

- Unidad II: Resolución de Sistemas de Ecuaciones por el Método de Cramer.

- Unidad III: Método de las Potencias.

- Unidad IV: Interpolación de Lagrange.


## Interfaz Gráfica

Decidimos desarrollarla con Flet, una librería para construir aplicaciones web, de escritorio y móviles basada en Flutter.
La elegimos por encima de Django porque quisimos crear una aplicación de escritorio, ya que no vimos la necesidad de que nuestra aplicación acceda a los servicios web,
otra razón es por la simplicidad y pulcritud de los componentes de Flet, y por la sencillez en la integración y desarrollo del frontend y backend de Flet con Python. Sin embargo, Flet es una librería prácticamente nueva y aún necesita integrar ciertas características y optimizarse. Por ejemplo, durante el desarrollo nos encontramos con
un problema con un tipo de botón, en dónde el estilo deshabilitado no funcionaba correctamente, pero en otros tipos de botones si funcionaba el estilo correctamente.


## Posibles mejoras
- La razón por la que no hay espacios entre los outputs en las operaciones y los resultados es porque el control de tipo texto
- en flet no tiene la propiedad de margen, y por otro lado, la asignacion de los valores de los outputs en los eventos de clickear algún botón,
- los hacemos en simultáneo. Es decir, que con una sola función para mostrar, retornamos todas las strings necesarias, y las asignamos en una
- sola línea de código. Esto lo decidimos hacer así por practicidad y optimización de tiempo, pero no nos permitió concatenar saltos de línea en
- las strings para agregar espacio entre los outputs.

- Por otro lado, nuestro diseño de algoritmos es completamente funcional, pero en los modulos de Potencias y Cramer, la randomnización en una misma
- sesión se limita sólo a los elementos del operando, y no al tamaño del mismo.
