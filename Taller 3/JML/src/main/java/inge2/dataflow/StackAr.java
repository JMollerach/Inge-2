package inge2.dataflow;

public class StackAr {

    /**
     * Capacidad por defecto de la pila.
     */
    private final static int DEFAULT_CAPACITY = 10;

    /**
     * Arreglo que contiene los elementos de la pila.
     */
    //@ spec_public
    private final int[] elems;

    /**
     * Indice del tope de la pila.
     */
    //@ spec_public
    private int top = -1;

    //@ public invariant -1 <= top <= (elems.length-1);

    //@ ensures elems.length == 10;
    //@ ensures top == -1;
    public StackAr() {
        this(DEFAULT_CAPACITY);
    }

    //@ requires capacity >= 0;
    //@ ensures elems.length == capacity;
    //@ ensures top == -1;
    public StackAr(int capacity) {
        this.elems = new int[capacity];
    }

    //@ ensures (\result <==> top == -1);
    public /*@ pure */ boolean isEmpty() {
        return top == -1;
    }

    //@ ensures (\result <==> top == elems.length-1);
    public /*@ pure */ boolean isFull() {
        return top == elems.length-1;
    }

    //@ ensures \result == top+1;
    public /*@ pure */ int size() {
        return top + 1;
    }

    //@ requires top < elems.length-1;
    //@ ensures elems[top] == o;
    //@ ensures top == \old (top+1);
    //@ ensures (\forall int j; 0 <= j <= \old (top); elems[j] == \old (elems[j]));
    public void push(int o) {
        top++;
        elems[top] = o;
    }

    //@ requires top > -1;
    //@ ensures \result == \old(elems[\old(top)]);
    //@ ensures top == \old (top-1);
    //@ ensures (\forall int j; 0 <= j < \old (top); elems[j] == \old (elems[j]));
    public int pop() {
      int o = elems[top];
      top --;
      return o;
    }

    //@ requires top > -1;
    //@ ensures \result == elems[top];
    public /*@ pure */ int peek() {
        return elems[top];
    }
}

