package org.autotest;

import java.lang.reflect.Array;
import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.*;

public class StackTests3 extends MutationAnalysisRunner {
    @Override
    protected boolean useVerboseMode() {
        return false;
    }

    // Tests de StackTests2

    public void testSizeIncreasesByOne() throws Exception {
        Stack stack = createStack();
        assertEquals(0, stack.size());
        stack.push(42);
        assertEquals(1, stack.size());
    }

    public void testDefaultConstructor() throws Exception {
        Stack stack = createStack();
        assertTrue(stack.isEmpty());
    }

    public void testConstructorWithSpecifiedCapacity() throws Exception {
        Stack stack = createStack(5);
    }

    public void testConstructorWithNegativeCapacity() {
        assertThrows(IllegalArgumentException.class, () -> {
            Stack stack = createStack(-1);
        });
    }

    public void testIsEmptyMethod() throws Exception {
        Stack stack = createStack();
        assertTrue(stack.isEmpty());
        stack.push(42);
        assertFalse(stack.isEmpty());
        stack.pop();
        assertTrue(stack.isEmpty());
    }

    public void testIsFullMethod() throws Exception {
        Stack stack = createStack(1);
        assertFalse(stack.isFull());
        stack.push(42);
        assertTrue(stack.isFull());
        stack.pop();
        assertFalse(stack.isFull());
    }

    public void testToStringMethod() throws Exception {
        Stack stack = createStack(2);
        assertEquals("[]", stack.toString());
        stack.push(42);
        assertEquals("[42]", stack.toString());
        stack.push(43);
        assertEquals("[42,43]", stack.toString());
    }

    // COMPLETAR
    public void testEqualsMethod() throws Exception {
        Stack stack = createStack(2);
        // un stack vacío no es null
        assertNotEquals(stack, null);
        stack.push(42);
        Stack stack2 = createStack(2);
        stack2.push(42);
        //stacks iguales
        assertEquals(stack, stack2);
        stack2.pop();
        assertNotEquals(stack, stack2);
        //un stack es igual a si mismo
        assertEquals(stack,stack);
        stack2.push(43);
        //stacks diferentes no son iguales
        assertNotEquals(stack,stack2);
    }

    public void testCreateStackWithCapacity0() throws Exception {
        Stack stack = createStack(0);
    }

    public void testCantPushOnFullStack() throws Exception {
        Stack stack = createStack(1);
        stack.push(42);
        assertThrows(IllegalStateException.class, () -> {
            stack.push(43);
        });
    }

    public void testTopMethod() throws Exception {
        Stack stack = createStack(1);
        stack.push(42);
        Object top = stack.top();
        assertEquals(top, 42);
        assertEquals(stack.top(), 42);
    }

    public void testCantTopOnEmptyStack() throws Exception {
        assertThrows(IllegalStateException.class, () -> {
            Stack stack = createStack();
            stack.top();
        });
    }

    public void testPopMethod() throws Exception {
        Stack stack = createStack(1);
        stack.push(42);
        Object pop = stack.pop();
        assertEquals(pop, 42);
        assertTrue(stack.isEmpty());
    }

    public void testCantPopOnEmptyStack() throws Exception {
        assertThrows(IllegalStateException.class, () -> {
            Stack stack = createStack();
            stack.pop();
        });
        // no funciona para eliminar pop en stack vacío porque este llama a top que tira la excepción igualmente
    }

    public void testHashMetod() throws Exception {
        Stack stack = createStack(1);
        stack.push(42);
        Stack stack2 = createStack(1);
        assertNotEquals(stack.hashCode(),stack2.hashCode());

    }

    public void testDefaultCapacityStack() throws Exception {
        Stack stack = createStack();
        stack.push(42);
        assertFalse(stack.isFull());
    }

    public void testEqualsDifferentClass() throws Exception {
        Stack stack = createStack();
        int arr=1;
        assertNotEquals(stack,arr);
    }

}
