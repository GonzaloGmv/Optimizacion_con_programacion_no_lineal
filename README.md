# Optimizacion_con_programacion_no_lineal

El link al repositorio es: [github](https://github.com/GonzaloGmv/Optimizacion_con_programacion_no_lineal)

Los participantes son:

Gonzalo Martínez

José Luis Rodríguez

Alexandre Muñoz

## Modelo de marketing

Hemos realizado un modelo de marketing para una hamburguesería. Queríamos ver cuánto presupuesto asignarle a publicitar la hamburguesa, las patatas y los corissants, basándonos en los  los retornos para cada canal de marketing (curva de respuesta), que son los siguientes:

Hamburguesas = -3300 + 4533 Ln(budget1)

Patatas = -1233 + 5833 Ln(budget2)

Croissants = -2633 + 3333 Ln(budget2)

Ahora con estos datos podemos trazar las curvas de respuesta de cada canal de marketing usando matplotlib.

![Figure_1](https://github.com/GonzaloGmv/Optimizacion_con_programacion_no_lineal/assets/91721237/ccb2da9a-c5c3-4c74-80d9-f0f675f9d993)


Para continuar hemos utilizado la biblioteca CVXPY para resolver el problema de optimización. Y los resultados obtenidos son:

![image](https://github.com/GonzaloGmv/Optimizacion_con_programacion_no_lineal/assets/91721237/d308c893-27b8-474a-8ebd-a7137b848e5d)

Después de ejecutar nuestros cálculos, encontramos que nuestro rendimiento total es de $135,845. Y la asginación óptima es $33,090 para los anuncios de hamburguesas, $42,580 para los anuncios de patatas y $24,330 para los anuncios de croissants.
