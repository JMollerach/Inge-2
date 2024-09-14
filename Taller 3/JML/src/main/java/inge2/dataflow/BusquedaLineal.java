package inge2.dataflow;

public class BusquedaLineal {

    // Busca un elemento en un arreglo de enteros.
    //@ requires arr != null;
    //@ ensures ((\exists int j; 0 <= j < arr.length; arr[j] == elem)  <==> \result);

    public static boolean busquedaLineal(int elem, int[] arr) {
        boolean result = false;
        //@ loop_invariant 0 <= i <= arr.length;
        //@ loop_invariant (result == false) ==> (\forall int j; 0<= j < i; arr[j] != elem);
        //@ loop_invariant (result == true) ==> (\exists int j; 0<= j < i; arr[j] == elem);
        //@ loop_decreases arr.length - i;
        for (int i = 0; i < arr.length; i++) {
            if (elem == arr[i]) {
                result = true;
            }
        }

        return result;
    }
}