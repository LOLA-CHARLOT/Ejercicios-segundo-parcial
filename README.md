# Ejercicios-segundo-parcial

La simulación de sistemas con variables aleatorias de distribución discreta o continua es una técnica muy útil en muchas situaciones en las que es necesario analizar el comportamiento de sistemas complejos en los que algunas variables tienen una distribución de probabilidad y se comportan de forma aleatoria. Esta técnica permite a los usuarios evaluar diferentes escenarios, reducir riesgos, identificar problemas, mejorar el rendimiento y tomar decisiones basadas en datos.

Comenzando el segundo parcial, realizamos varios ejercicios de predicción utilizando números aleatorios de referencia (segunda columna). Por ejemplo la siguiente tabla:

No.	r (aleatorio)	Datos 1
1	0,296067098	0,444100647
2	0,314047234	0,47107085
3	0,657737102	0,986605653
4	0,129856981	0,194785472
5	0,339754128	0,509631192
6	0,274366072	0,411549108
7	0,568234451	0,852351677
8	0,994945014	1,876853922
9	0,903508223	1,461970882
10	0,093736884	0,140605325
11	0,34373528	0,51560292
12	0,390893427	0,586340141
13	0,658480874	0,987721311
14	0,869335996	1,373907345
15	0,246771426	0,370157139

<img width="262" height="321" alt="image" src="https://github.com/user-attachments/assets/034e6d6f-a6c6-434f-9ed9-4ea5781e1e8e" />

Se realizó en excel. En la tercera columna se utilizó la siguiente fórmula: =SI(C5<(2/3);(3/2)*C5;2-RAIZ(3*(1-C5)))
Dando como resultado el siguiente gráfico:

<img width="531" height="317" alt="image" src="https://github.com/user-attachments/assets/97a29a5a-fa0c-4b43-be87-7a1b786370e0" />

Por otro lado, haciendo uso del formulario de Distribuciones y variables procedimos a graficar cada una utilizando siempre la fórmula correcta:

<img width="860" height="528" alt="image" src="https://github.com/user-attachments/assets/924f1e69-9f1d-4591-841b-202f3d1f0faf" />

Distribuciones discretas:

<img width="847" height="378" alt="image" src="https://github.com/user-attachments/assets/e6dc7c1a-8d2c-4c70-8696-c1c72acd1039" />

VARIABLE UNIFORME:

Utilizando la siguiente fórmula en excel:

=$C$5+($C$4-$C$5)*ALEATORIO()

<img width="402" height="185" alt="image" src="https://github.com/user-attachments/assets/1f5080a0-c5ad-482e-898f-d17a03360c57" />

VARIABLE K*ERLANG:

Utilizando la siguiente fórmula en excel:

=INV.GAMMA(ALEATORIO();$F$4;$F$5/$F$4)

<img width="428" height="253" alt="image" src="https://github.com/user-attachments/assets/9c18f111-188a-41a0-b46e-f4d42e75d335" />

VARIABLE EXPONENTE:

Utilizando la siguiente fórmula en excel:

=INV.GAMMA(ALEATORIO();1;$I$5)

<img width="370" height="259" alt="image" src="https://github.com/user-attachments/assets/449a3d1f-edcc-4aa4-8c69-cda5ee7b6bf5" />

VARIABLE GAMMA:

Utilizando la siguiente fórmula en excel:

=INV.GAMMA(ALEATORIO();L$4^2/L$5;L$5/L$4)

<img width="372" height="267" alt="image" src="https://github.com/user-attachments/assets/636b90e0-0f19-42aa-a4fc-8a7b30f6598e" />

VARIABLE NORMAL:

Utilizando la siguiente fórmula en excel:

=INV.NORM(ALEATORIO();$O$4;RAIZ($O$5))

<img width="424" height="258" alt="image" src="https://github.com/user-attachments/assets/b00e4130-b377-4876-819a-e7cea0603be6" />

VARIABLE WEIBULL:

Utilizando la siguiente fórmula en excel:

=$R$6+($R$5^2)*POTENCIA(-LN(1-ALEATORIO());1/$R$4)

<img width="390" height="253" alt="image" src="https://github.com/user-attachments/assets/ab438f98-a4ff-4f9e-9306-d4e899fe6aa4" />

VARIABLE BERNOULLI:

Utilizando la siguiente fórmula en excel:

=SI(ALEATORIO()<1-X$5;0;1)

<img width="467" height="279" alt="image" src="https://github.com/user-attachments/assets/d2047dd2-0480-4175-9f94-042cd63eccf6" />

VARIABLE BINOMIAL:

Utilizando la siguiente fórmula en excel:

=INV.BINOM(AA$4; AA$5; ALEATORIO())

<img width="349" height="223" alt="image" src="https://github.com/user-attachments/assets/0833e29d-d1c9-4980-9d52-6c9a08995701" />




# Juego de la vida

El "Juego de la Vida" de Conway es un autómata celular con cuatro reglas simples que determinan la evolución de una cuadrícula de celdas vivas y muertas. Las reglas son: 1) una célula viva con menos de dos vecinos vivos muere por soledad; 2) una célula viva con más de tres vecinos vivos muere por sobrepoblación; 3) una célula viva con dos o tres vecinos vivos sobrevive; y 4) una célula muerta con exactamente tres vecinos vivos nace.

<img width="158" height="349" alt="image" src="https://github.com/user-attachments/assets/2a292a11-e848-44a6-bfad-9468dc16a164" />

El Juego de la Vida de Conway es un autómata celular de cero jugadores, un modelo matemático discreto inventado por el matemático John Horton Conway en 1970, y es famoso por demostrar cómo la complejidad emergente puede surgir de la simplicidad. Se desarrolla sobre una cuadrícula bidimensional infinita, donde cada célula puede estar en uno de dos estados: viva (1) o muerta (0). La evolución del sistema se determina enteramente por su configuración inicial y se produce en pasos de tiempo discretos llamados generaciones. En cada generación, todas las células se actualizan simultáneamente según cuatro reglas locales y deterministas, basadas en el número de sus ocho vecinas adyacentes: una célula viva sobrevive si tiene dos o tres vecinas vivas; muere por sobrepoblación si tiene más de tres, o por soledad si tiene menos de dos; y una célula muerta nace (se activa) si tiene exactamente tres vecinas vivas. A pesar de estas reglas mínimas, la iteración produce patrones que pueden ser estáticos, oscilantes (que repiten un ciclo) o viajeros (que se mueven por el tablero), e incluso se ha demostrado que el juego es Turing completo, lo que significa que es teóricamente capaz de simular cualquier cálculo.

<img width="668" height="592" alt="image" src="https://github.com/user-attachments/assets/4fb3253e-340f-4ff8-aebe-c6d690cce308" />

En este ejercicio representamos la estructura conocida como "nave espacial" (spaceship), que ilustra la emergencia de un sistema dinámico y autoorganizado. Se trata de una secuencia temporal que muestra el movimiento de una nave espacial (spaceship), donde las filas (numeradas del 0 al 33) representan generaciones sucesivas (pasos discretos en el tiempo) y las columnas indican las coordenadas espaciales. El estado '1' (amarillo) denota una célula viva, y '0' (naranja) una célula muerta. Este patrón demuestra la capacidad del sistema para la complejidad emergente: a partir de un conjunto de reglas locales y deterministas, surge una estructura global que se propaga periódicamente a través del plano sin cambiar su forma, un fenómeno clave en el estudio de los sistemas dinámicos y la teoría de la computación.

<img width="1219" height="607" alt="image" src="https://github.com/user-attachments/assets/dc4f4334-fce5-48e7-acba-026c8be11e4d" />

En el ejercicio detallado arriba se muestra un patrón de crecimiento que no es una simple nave espacial, sino un objeto más complejo. En este caso, las filas indexan generaciones temporales y las columnas denotan la configuración espacial del patrón en cada instante. Los valores '1' (amarillo) y '0' (naranja) corresponden, respectivamente, a células en estado activo (vivas) o inactivo (muertas). Este patrón exhibe una dinámica de crecimiento exponencial o pseudoexponencial, caracterizada por la proliferación de células vivas a través del espacio-tiempo simulado. A diferencia de las "naves espaciales" que mantienen una forma constante mientras se desplazan, esta configuración ilustra un comportamiento de auto-reproducción o expansión descontrolada (al menos en las primeras etapas mostradas), lo que resalta la capacidad del Juego de la Vida para generar comportamientos complejos y no triviales a partir de interacciones locales simples. Es un ejemplo vívido de cómo reglas básicas pueden dar lugar a patrones complejos y sistemas emergentes.

