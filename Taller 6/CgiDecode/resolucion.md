# Ejercicio 1
En este ejercicio generamos casos de test con el objetivo de
cubrir todas las líneas y branches del programa cgi_decode. Para eso, consideramos los casos contemplados en las condiciones del programa como el string vacío, o strings con caracteres especiales como '+', '%' o aquellos no definidos en el mapeo hex_values.

# Ejercicio 2
En este ejercicio completamos la implementación de evaluate_condition de acuerdo a las condiciones y ejemplos provistos en el enunciado del taller.
Como decisiones tomadas podemos mencionar que no consideramos 
los casos en los que lhs y rhs toman valores no permitidos, 
además de que modificamos el tipado original de la función 
evaluate_condition que no contemplaba que lhs y rhs podían ser enteros.

Finalmente, creamos casos de test que cubran el total de la líneas y branches
de la función evaluate_condition. Sin embargo, en el reporte 
de coverage generado por coverage.py se puede observar que no 
tenemos un 100% de cobertura en este archivo ya que había funciones útiles no implementadas por nosotras
como get_true_distance ó has_reached_condition que no usamos para la resolución del taller.

# Ejercicio 3
En este punto del taller completamos la función cgi_decode_instrumented(test_case) manteniendo su implementación original
pero instrumentando las condiciones con su evaluación con el objetivo de realizar el cálculo de los branch distances del test en observación.

Luego, reescribimos los casos de test que implementamos en el ejercicio anterior aprovechando su 100% de cobertura para testear esta nueva implementación instrumentada.
Los tests pasaron con éxito y obtuvimos nuevamente 100% de cobertura. Agregamos además el test de ejemplo del enunciado del taller.

# Ejercicio 4
Hicimos el cómputo de la función de fitness de un test suite del programa cgi_decode. Para eso, primero calculamos sus branch distances
con cgi_decode_instrumented. Si la ejecución de ese programa generaba una excepción, continuamos con la ejecución normal del fitness con 
los condicionales alcanzados hasta ese momento.
Primero para cada objetivo sumamos su branch distance normalizado si se se alcanzó el branch, y 1 si no como se pide en el enunciado del taller.
Luego, sumamos el approach level considerando aquellas condiciones no alcanzadas en la ejecución del programa.

Para testear usamos los ejemplos provistos por la cátedra.

# Ejercicio 5
Completamos la función create_population(size) que genera un test suite de una 
cantidad determinada de test cases de entre 0 y 10 caracteres aleatorios.

# Ejericio 6
Para cada individuo de un test suite, calculamos su fitness y devolvemos todos los resultados en un diccionario. Dado que estamos considerando las keys como 
índices de la lista original, quizás podríamos haber usado otro tipo de datos como una lista.

# Ejercicio 7
La función selection hace un tournament selection de los individuos según su fitness. Consideramos las keys del diccionario índices de los individuos en la población y cambiamos levemente el tipado de la función para que
devuelva una tupla [int,float] en vez de [str,float] como decía originalmente.
También, a diferencia de lo visto en la teórica en este caso nos interesa minimizar la función de fitness y no maximizarla, por lo que para elegir el ganador consideramos aquel con fitness más cercano a 0.

# Ejercicio 8
Calculamos el single-point crossover entre 2 padres tal cual vimos en la teórica.

# Ejercicio 9
En este ejercicio, implementamos un operador de mutación que puede, con igual probabilidad agregar un test case ó eliminar o modificar uno existente. Para eso
chequeamos no sobrepasar el límite de 15 casos de test al agregar, ni bajar de 1 caso al eliminar o modificar. En el caso de hacer una modificación podemos nuevamente con igual probabilidad
agregar, eliminar o modificar un caracter del caso de test considerado. 
Decidimos para cada iteración hacer sí o sí una mutación, es decir, si al tirar la moneda
saliera elegido un caso no viable (ej. agregar un test case a un test suite lleno) la volvemos a tirar hasta lograr una mutación pertinente.

# Ejercicio 10
En este ejercicio usamos todas las funciones definidad en los ejercicios anteriores e implementamos un algoritmo genético standard para la función de decodificación.
Empezamos creando una población aleatoria, y a partir de la misma obtenemos una segunda generación como resultado del crossover y mutación de los mejores individuos de la población anterior.
Finalmente, nos quedamos con el mejor individuo de la última generación.
Podemos observar que como este algoritmo no considera elitismo, el mejor individuo de una generación a la otra podría empeorar.
Pensando cómo calcular el branch coverage, notamos que en los 3 casos de test implementados se consigue un individuo con fitness mínimo (=0) bastante rápido. Donde
el peor caso fue la generación 23 para el test2. Por lo que siempre conseguimos un individuo con 100% de branch coverage.