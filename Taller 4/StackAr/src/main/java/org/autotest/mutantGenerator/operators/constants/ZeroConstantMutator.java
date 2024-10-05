package org.autotest.mutantGenerator.operators.constants;

import org.autotest.mutantGenerator.operators.MutationOperator;
import spoon.reflect.code.CtLiteral;
import spoon.reflect.declaration.CtElement;

import java.util.Arrays;
import java.util.List;

/**
 * Operador de mutación basado en https://pitest.org/quickstart/mutators/#EXPERIMENTAL_CRCR
 *
 * Este operador reemplaza los valores de las constantes por cero.
 */
public class ZeroConstantMutator extends MutationOperator {
    @Override
    public boolean isToBeProcessed(CtElement candidate) {
        // llamo al método super para verificar que el candidato no es parte de randoop.CheckRep: repOK method
        if (!super.isToBeProcessed(candidate)) {
            return false;
        }
        // COMPLETAR
        if (!(candidate instanceof CtLiteral)) {
            return false;
        }

        CtLiteral op = (CtLiteral)candidate;
        if(op.getValue()!=null) {
            String type = op.getType().toString();
            List<String> targetTypes = Arrays.asList(
                    "int"
            );

            if(op.getValue().toString().equals("0")){
                return false;
            }

            if (targetTypes.contains(type)) {
                return true;
            }
        }
        return false;
    }

    @Override
    public void process(CtElement candidate) {
        // COMPLETAR
        CtLiteral op = (CtLiteral)candidate;
        op.setValue(op.getFactory().Code().createLiteral(0));
    }

    @Override
    public String describeMutation(CtElement candidate) {
        CtLiteral op = (CtLiteral)candidate;
        return this.getClass().getSimpleName() + ": Se reemplazó " +
                op.getValue().toString() + " por 0" +
                " en la línea " + op.getPosition().getLine() + ".";
    }
}
