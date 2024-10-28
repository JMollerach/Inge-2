from random import sample
from typing import Tuple, List


def selection(fitness_by_individual: dict, tournament_size: int) -> Tuple[int, float]:
    """
    fitness_by_individual: Diccionario que contiene a los individuos de la población como keys y su fitness como valores.
    tournament_size: Tamaño del torneo (entero positivo).
    """
    seleccionados = sample(fitness_by_individual.keys(), tournament_size)
    winner = min(seleccionados, key=fitness_by_individual.get)
    return winner, fitness_by_individual[winner]
