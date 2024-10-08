package inge2.dataflow;

public class Absoluto {

    // Calcula el valor absoluto de un número entero.
    // Si el número es negativo, devuelve el opuesto.
    //
    //@ requires Integer.MIN_VALUE < n;
    //@ ensures \result >=0 && Math.abs(n)==\result;
    public static int valorAbsoluto(int n) {
        if (n < 0) {
            return -n;
        } else {
            return n;
        }
    }
}