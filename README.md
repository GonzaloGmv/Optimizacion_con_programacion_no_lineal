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


Para continuar hemos utilizado la biblioteca CVXPY. Este modelo emplea esta librería para abordar la tarea de optimización. Con CVXPY, se busca la asignación más eficiente de recursos presupuestarios que maximice el retorno de inversión (ROI) dentro de los límites establecidos.

![image](https://github.com/GonzaloGmv/Optimizacion_con_programacion_no_lineal/assets/91721237/d308c893-27b8-474a-8ebd-a7137b848e5d)

Después de ejecutar nuestros cálculos, encontramos que nuestro rendimiento total es de $135,845. Y la asginación óptima es $33,090 para los anuncios de hamburguesas, $42,580 para los anuncios de patatas y $24,330 para los anuncios de croissants.

Este modelo aborda el problema de los rendimientos decrecientes al considerar las curvas de respuesta no lineales y busca maximizar el ROI al encontrar la asignación de presupuesto óptima. Al asignar más presupuesto a los canales que tienen un mejor rendimiento relativo y un menor impacto de rendimientos decrecientes, se logra una eficiencia máxima en la inversión en marketing. Esto permite que la hamburguesería obtenga el máximo retorno posible de su presupuesto de marketing limitado.
