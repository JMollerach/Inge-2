package inge2.dataflow.zeroanalysis;

/**
 * This enum represents the possible values of the zero analysis for a variable.
 */
public enum ZeroAbstractValue {

    /**
     * We don't have information about the variable.
     */
    BOTTOM("bottom"),

    /**
     * The variable is not zero.
     */
    NOT_ZERO("not-zero"),

    /**
     * The variable is zero.
     */
    ZERO("zero"),

    /**
     * The variable may be (or not) zero.
     */
    MAYBE_ZERO("maybe-zero");

    /**
     * The name of the ZeroAbstractValue.
     */
    private final String name;

    @Override
    public String toString() {
        return this.name;
    }

    ZeroAbstractValue(String name) {
        this.name = name;
    }

    /**
     * Returns the result of the addition between this ZeroAbstractValue and another.
     * @param another the other ZeroAbstractValue.
     * @return the result of the addition.
     */
    public ZeroAbstractValue add(ZeroAbstractValue another) {
        // TODO: IMPLEMENTAR
        if (this == BOTTOM || another == BOTTOM) {
            return BOTTOM;
        }else if (this == ZERO) {
            return another;
        } else if (another == ZERO) {
            return this;
        } else {
            return MAYBE_ZERO;
        }

       // throw new UnsupportedOperationException();
    }

    /**
     * Returns the result of the division between this ZeroAbstractValue and another.
     * @param another the other ZeroAbstractValue.
     * @return the result of the division.
     */
    public ZeroAbstractValue divideBy(ZeroAbstractValue another) {
        // TODO: IMPLEMENTAR
        if (this == BOTTOM || another == BOTTOM || another == ZERO) {
            return BOTTOM;
        } else if (this == ZERO) {
            return ZERO;
        } else {
            return MAYBE_ZERO;
        }
        //throw new UnsupportedOperationException();
    }

    /**
     * Returns the result of the multiplication between this ZeroAbstractValue and another.
     * @param another the other ZeroAbstractValue.
     * @return the result of the multiplication.
     */
    public ZeroAbstractValue multiplyBy(ZeroAbstractValue another) {
        // TODO: IMPLEMENTAR
        if (this == BOTTOM || another == BOTTOM) {
            return BOTTOM;
        } else if (this == ZERO || another == ZERO) {
            return ZERO;
        } else if (this == NOT_ZERO && another == NOT_ZERO){
            return NOT_ZERO;
        } else {
            return MAYBE_ZERO;
        }
        //throw new UnsupportedOperationException();
    }

    /**
     * Returns the result of the subtraction between this ZeroAbstractValue and another.
     * @param another the other ZeroAbstractValue.
     * @return the result of the subtraction.
     */
    public ZeroAbstractValue subtract(ZeroAbstractValue another) {
        // TODO: IMPLEMENTAR
        if (this == BOTTOM || another == BOTTOM) {
            return BOTTOM;
        } else if (this == ZERO) {
            return another;
        } else if (another == ZERO) {
            return this;
        } else {
            return MAYBE_ZERO;
        }
        //throw new UnsupportedOperationException();
    }

    /**
     * Returns the result of the merge between this ZeroAbstractValue and another.
     * @param another the other ZeroAbstractValue.
     * @return the result of the merge.
     */
    public ZeroAbstractValue merge(ZeroAbstractValue another) {
        // TODO: IMPLEMENTAR
        if(this==MAYBE_ZERO|| another == MAYBE_ZERO){
            return MAYBE_ZERO;
        } else if (this== BOTTOM) {
            return another;
        } else if (another== BOTTOM || this==another) {
            return this;
        } else {
            return MAYBE_ZERO;
        }
        // throw new UnsupportedOperationException();
    }

}
