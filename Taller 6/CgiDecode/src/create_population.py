from random import choice, randint
from string import printable
from typing import List


def get_random_character():
    char=choice(printable)
    return char


def create_test_case() -> str:
    test = ''
    for _ in range(randint(0,10)):
        char = get_random_character()
        test+= char
    return test


def create_individual() -> List[str]:
    individuo = []
    for _ in range(randint(1,15)):
        individuo.append(create_test_case())
    return individuo


def create_population(population_size) -> List[List[str]]:
    population = []
    for _ in range(population_size):
        population.append(create_individual())
    return population
