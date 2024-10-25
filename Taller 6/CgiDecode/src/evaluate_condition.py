import sys
from typing import Dict, Union

# Inicializar mappings globales
distances_true: Dict[int, int] = {}
distances_false: Dict[int, int] = {}


def update_maps(condition_num: int, d_true: int, d_false: int):
    global distances_true, distances_false

    if condition_num in distances_true.keys():
        distances_true[condition_num] = min(
            distances_true[condition_num], d_true)
    else:
        distances_true[condition_num] = d_true

    if condition_num in distances_false.keys():
        distances_false[condition_num] = min(
            distances_false[condition_num], d_false)
    else:
        distances_false[condition_num] = d_false


def clear_maps():
    global distances_true, distances_false
    distances_true.clear()
    distances_false.clear()


def get_true_distance(condition_num: int) -> Union[int, None]:
    global distances_true
    if condition_num in distances_true.keys():
        return distances_true[condition_num]
    else:
        return None


def get_false_distance(condition_num: int) -> Union[int, None]:
    global distances_false
    if condition_num in distances_false.keys():
        return distances_false[condition_num]
    else:
        return None


def has_reached_condition(condition_num: int) -> bool:
    global distances_true, distances_false
    return condition_num in distances_true.keys() or condition_num in distances_false.keys()


def evaluate_condition(condition_num: int, op: str, lhs: Union[int, str, Dict], rhs: Union[int, str, Dict]) -> bool:
    if type(lhs) == str:
        numLhs = ord(lhs)
        if type(rhs) == str:
            numRhs = ord(rhs)
    else:
        numLhs = lhs
        numRhs = rhs

    if op == "Eq":
        if numLhs == numRhs:
            update_maps(condition_num, 0, 1)
            return True
        else:
            update_maps(condition_num, abs(numLhs - numRhs), 0)
            return False
    elif op == "Ne":
        if numLhs != numRhs:
            update_maps(condition_num, 0, 1)
            return True
        else:
            update_maps(condition_num, abs(numLhs - numRhs), 0)
            return False
    elif op == "Lt":
        if (numLhs < numRhs):
            update_maps(condition_num, 0, numRhs - numLhs)
            return True
        else:
            update_maps(condition_num, numLhs - numRhs + 1, 0)
            return False
    elif op == "Gt":
        if (numLhs > numRhs):
            update_maps(condition_num, 0,  numLhs - numRhs)
            return True
        else:
            update_maps(condition_num,  numRhs - numLhs + 1, 0)
            return False
    elif op == "Le":
        if (numLhs <= numRhs):
            update_maps(condition_num, 0, numRhs - numLhs + 1)
            return True
        else:
            update_maps(condition_num, numLhs - numRhs, 0)
            return False
    elif op == "Ge":
        if (numLhs >= numRhs):
            update_maps(condition_num, 0,  numLhs - numRhs + 1)
            return True
        else:
            update_maps(condition_num,  numRhs - numLhs, 0)
            return False
    elif op == "In":
        claves = list(rhs.keys())
        if len(claves) == 0:
            update_maps(condition_num, sys.maxsize, 0)
            return False
        minDistance = abs(numLhs - ord(claves[0]))
        for clave in claves:
            if numLhs == ord(clave):
                update_maps(condition_num, 0, 1)
                return True
            minDistance = min(minDistance, abs(numLhs - ord(clave)))
        update_maps(condition_num, minDistance, 0)
        return False

