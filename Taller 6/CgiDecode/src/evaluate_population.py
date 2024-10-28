from typing import List

from src.get_fitness_cgi_decode import get_fitness_cgi_decode

def evaluate_population(population: List[List[str]]) -> dict:
    fitness = {}
    index = 0
    for individuo in population:
        fitness[index] = get_fitness_cgi_decode(individuo)
        index+=1
    return fitness
