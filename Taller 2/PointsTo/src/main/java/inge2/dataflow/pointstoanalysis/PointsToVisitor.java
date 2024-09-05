package inge2.dataflow.pointstoanalysis;

import soot.jimple.*;
import soot.jimple.internal.JInstanceFieldRef;
import soot.jimple.internal.JimpleLocal;

import java.util.HashSet;
import java.util.Set;

public class PointsToVisitor extends AbstractStmtSwitch<Void> {

    private final PointsToGraph pointsToGraph;

    public PointsToVisitor(PointsToGraph pointsToGraph) {
        this.pointsToGraph = pointsToGraph;
    }

    @Override
    public void caseAssignStmt(AssignStmt stmt) {
        boolean isLeftLocal = stmt.getLeftOp() instanceof JimpleLocal;
        boolean isRightLocal = stmt.getRightOp() instanceof JimpleLocal;

        boolean isLeftField = stmt.getLeftOp() instanceof JInstanceFieldRef;
        boolean isRightField = stmt.getRightOp() instanceof JInstanceFieldRef;

        boolean isRightNew = stmt.getRightOp() instanceof AnyNewExpr;

        if (isRightNew) { // x = new A()
            processNewObject(stmt);
        } else if (isLeftLocal && isRightLocal) { // x = y
            processCopy(stmt);
        } else if (isLeftField && isRightLocal) { // x.f = y
            processStore(stmt);
        } else if (isLeftLocal && isRightField) { // x = y.f
            processLoad(stmt);
        }
    }

    private void processNewObject(AssignStmt stmt) {
        String leftVariableName = stmt.getLeftOp().toString();
        Node nodeName = pointsToGraph.getNodeName(stmt);

        this.pointsToGraph.nodes.add(nodeName);
        Set<Node> set = new HashSet<Node>();
        set.add(nodeName);
        this.pointsToGraph.mapping.put(leftVariableName, set);
    }

    private void processCopy(AssignStmt stmt) {
        String leftVariableName = stmt.getLeftOp().toString();
        String rightVariableName = stmt.getRightOp().toString();

        Set<Node> nodes = this.pointsToGraph.getNodesForVariable(rightVariableName);
        this.pointsToGraph.mapping.put(leftVariableName, nodes);
    }

    private void processStore(AssignStmt stmt) { // x.f = y
        JInstanceFieldRef leftFieldRef = (JInstanceFieldRef) stmt.getLeftOp();
        String leftVariableName = leftFieldRef.getBase().toString();
        String fieldName = leftFieldRef.getField().getName();
        String rightVariableName = stmt.getRightOp().toString();

        Set<Node> nodes = this.pointsToGraph.getNodesForVariable(leftVariableName);
        Set<Node> pointedTo = this.pointsToGraph.getNodesForVariable(rightVariableName);

        for (Node x : nodes){
            for (Node y : pointedTo) {
                Axis a = new Axis(x, fieldName, y);
                this.pointsToGraph.axis.add(a);
            }
        }
    }

    private void processLoad(AssignStmt stmt) { // x = y.f
        String leftVariableName = stmt.getLeftOp().toString();
        JInstanceFieldRef rightFieldRef = (JInstanceFieldRef) stmt.getRightOp();
        String rightVariableName = rightFieldRef.getBase().toString();
        String fieldName = rightFieldRef.getField().getName();

        Set<Node> nodes = this.pointsToGraph.getNodesForVariable(rightVariableName);
        Set<Node> f = new HashSet<Node>();

        for (Node y : nodes){
            f.addAll(this.pointsToGraph.getReachableNodesByField(y, fieldName));
        }

        this.pointsToGraph.mapping.put(leftVariableName, f);
    }
}
