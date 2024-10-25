from random import randint
from typing import List, Tuple


def crossover(parent1: List[str], parent2: List[str]) -> Tuple[List[str], List[str]]:
    offspring1 = None
    offspring2 = None

    single_point = randint(0, len(parent1) - 1)
    offspring1 = parent1[:single_point] + parent2[single_point:]
    offspring2 = parent2[:single_point] + parent1[single_point:]

    return offspring1, offspring2
