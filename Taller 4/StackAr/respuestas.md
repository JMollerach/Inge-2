# Ejercicio 1
1. ¿Cuántos mutantes se generaron en total?

En total se generaron 72 mutantes.

2. ¿Qué operador de mutación generó más mutantes? ¿Cuántos y por qué? 

False Conditional y True conditional fueron los operadores que más mutantes generaron. Esto es porque hay más 
condicionales que otro tipo de elementos en el código analizado.

3.  ¿Qué operador de mutación generó menos mutantes? ¿Cuántos y por qué?

Null Return y Empty Return fueron los oepradores que menos mutantes generaron. Esto ocurre porque en el código 
analizado hay pocas funciones que devuelven enteros, string u objetos no primitivos.

# Ejercicio 2
1. ¿Cuántos mutantes vivos y muertos encontraron cada uno de los test suites provistos por la cátedra?

En StackTests1, se eliminaron 18 mutantes y quedaron 54. Tanto en StackTests2 como en StackTests3 se 
eliminaron 34 mutantes y quedaron 38 vivos.
    
2. ¿Cuál es el mutation score de cada test suite?

En StackTests1 el mutation score es de 25%. En StackTests2 y StackTests3 el mutation score fue de 47%.

# Ejercicio 3
1.  ¿Cuál es el mutation score logrado para los tests del 
StackTests2 mejorado (i.e. StackTests3)?

El mutation score logrado fue del 81%.

2. ¿Cuántos mutantes vivos y muertos encontraron?

Encontramos 13 mutantes vivos y 59 muertos.

3. Comente cuáles son todos los mutantes vivos que quedaron y 
justifique por qué son mutantes equivalentes al programa original.

   Los mutantes vivos que quedaron son:
    - Un mutante que altera la función pop de manera que no entra nunca al código 
que tira la excepción cuando se llama sobre un stack vacío. Este mutante es equivalente al código original ya que después del chequeo de la excepción se llama a la función 
top, que sí tira la excepción correcta. Es decir, a pesar de que, en principio, no hay error al ejecutar pop en un stack vacío, la excepción se genera de todas formas por el llamado a la función top y el comportamiento es equivalente.
    - Un mutante que altera la función equals de manera que nunca entra a la cláusula
que define que si llamás a la función con 2 stacks de igual hashCode devuelva true. 
Pero como cuando es el mismo stack el resto de las condiciones necesarias para 
determinar que son iguales se cumplen, no afecta el comportamiento final de la función.
    - Un mutante que altera la función equals de manera que no se verifique que 2 stacks tienen el mismo readIndex. 
Sin embargo, 2 instancias construidas legalmente no podrían tener un distinto readIndex para 2 stacks con los mismos elementos
    - Un mutante que altera la función equals de manera que 2 stacks con distintos readIndexes sean considerados iguales. 
Sin embargo por cómo está ordenado el código esto no altera el funcionamiento del método ya que
antes de comparar readIndexes se verifica que tengan los mismos elementos y esto retornará falso ya que 2 stacks construidos legalmente no pueden tener 
la misma cantidad de elementos y un distinto readIndex.
    - El resto de los mutantes vivos son equivalentes al programa original porque sólo 
afectan la función de hash.

4. ¿Cuál es el instruction coverage promedio que lograron para las clases mutadas? 

El instruction coverage promedio fue de 53%

5. ¿Cuál es el peor instruction coverage que lograron para una clase 
mutada? ¿Por qué creen que sucede esto?

El peor instruction coverage logrado fue del 3%. Esto se debe a que se modificó la condición 
de una guarda por true muy temprano en el código por lo que en la siempre entra a esa guarda
cuando se construye un stack de capacidad no default. Como el cuerpo de la guarda tiene la única 
instrucción de arrojar una excepción el programa termina muy rápido y no ejecuta el resto de las instrucciones.

# Ejercicio 4
1. ¿Cuántos casos de test produjo Randoop? 

Randoop produjo 610 tests.

2. ¿Alguno de los tests generados falló?

Ninguno de los tests genrados falló.

3. ¿Cuál es el instruction coverage alcanzado por los tests generados para la clase StackAr?

El instruction coverage alcanzado es del 83%.

# Ejercicio 5
1. ¿Qué fallas fueron detectadas por los tests producidos por Randoop?

Se detectó que cuando se popeaba un elemento la posición en el que este estaba no pasaba a ser null.

2. ¿Cuál es el instruction coverage alcanzado por el último test suite generado (aquel que 
no encontró nuevas fallas en StackAr)?

El nuevo instruction coverage alcanzado es del 86%.

# Ejercicio 6
1. Ejecutar el nuevo archivo RegressionTest.java (sin número) generado y reportar cuál es este
   mutation score obtenido por los tests generados sobre al clase StackAr reparada.

El mutation score obtenido (luego de agregar la linea args('--omit-methods', 'getClass')) fue del 79%.