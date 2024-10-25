from typing import List

from src.get_fitness_cgi_decode import get_fitness_cgi_decode

def evaluate_population(population: List[List[str]]) -> dict:
    fitness = {}
    for individuo in population:
        fitness[individuo] = get_fitness_cgi_decode(individuo)
    return fitness
