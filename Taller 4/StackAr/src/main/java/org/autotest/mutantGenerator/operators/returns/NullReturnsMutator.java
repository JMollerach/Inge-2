package org.autotest.mutantGenerator.operators.returns;

import org.autotest.mutantGenerator.operators.MutationOperator;
import spoon.reflect.code.CtExpression;
import spoon.reflect.code.CtReturn;
import spoon.reflect.declaration.CtElement;
import spoon.reflect.reference.CtTypeReference;

import java.util.Arrays;
import java.util.List;

/**
 * Operador de mutación basado en https://pitest.org/quickstart/mutators/#NULL_RETURNS
 *
 * Este operador reemplaza los valores de retorno de las funciones que devuelven un Object por null.
 */
public class NullReturnsMutator extends MutationOperator {
    @Override
    public boolean isToBeProcessed(CtElement candidate) {
        // llamo al método super para verificar que el candidato no es parte de randoop.CheckRep: repOK method
        if (!super.isToBeProcessed(candidate)) {
            return false;
        }

        if (!(candidate instanceof CtReturn)) {
            return false;
        }
        // COMPLETAR
        CtReturn op = (CtReturn)candidate;

        CtTypeReference type = getReturnedExpressionType(op);
        return !type.isPrimitive();
    }

    @Override
    public void process(CtElement candidate) {
        // COMPLETAR
        CtReturn op = (CtReturn)candidate;
        op.setReturnedExpression(getNullValueForReturnExpression(op));
    }

    private static CtTypeReference getReturnedExpressionType(CtReturn op) {
        return op.getReturnedExpression().getType();
    }

    private CtExpression getNullValueForReturnExpression(CtReturn op) {
        // COMPLETAR
        return op.getFactory().Code().createLiteral(null);
    }

    @Override
    public String describeMutation(CtElement candidate) {
        CtReturn op = (CtReturn)candidate;
        return this.getClass().getSimpleName() + ": Se reemplazó " +
                op.getReturnedExpression().toString() + " por " + getNullValueForReturnExpression(op).toString() +
                " en la línea " + op.getPosition().getLine() + ".";
    }
}
