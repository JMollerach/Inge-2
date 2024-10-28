from random import choice
from typing import List

from src.create_population import create_test_case, get_random_character


def add_character(test_case: str) -> str:
    test_case += get_random_character()
    return test_case


def remove_character(test_case: str) -> str:
    index = choice(range(len(test_case)-1))
    return test_case[:index] + test_case[index+1:]


def modify_character(test_case: str) -> str:
    index = choice(range(len(test_case) - 1))
    return test_case[:index] + get_random_character() + test_case[index + 1:]


def add_test_case(individual: List[str]) -> List[str]:
    test_case = create_test_case()
    individual.append(test_case)
    return individual


def remove_test_case(individual: List[str]) -> List[str]:
    individual.remove(choice(individual))
    return individual


def modify_test_case(individual: List[str]) -> List[str]:
    index_case = choice(range(len(individual)-1))
    test_case = individual[index_case]
    se_muto = False

    while not se_muto:
        modificacion = choice([1, 2, 3])

        if modificacion == 1 and len(test_case) < 10:
            test_case = add_character(test_case)
            se_muto = True

        elif modificacion == 2 and len(test_case) > 1:
            test_case = remove_character(test_case)
            se_muto = True

        elif modificacion == 3 and len(test_case) > 1:
            test_case = modify_character(test_case)
            se_muto = True

    individual[index_case] = test_case
    return individual


def mutate(individual: List[str]) -> List[str]:
    #Hacemos una copia, quizás no es necesario
    individual = individual[:]
    #Si la mutacion no es viable, volvemos a intentar hasta lograr mutar
    se_muto = False

    while not se_muto:
        mutacion = choice([1, 2, 3])

        if mutacion == 1 and len(individual) < 15:
            individual = add_test_case(individual)
            se_muto = True

        elif mutacion == 2 and len(individual) > 1:
            individual = remove_test_case(individual)
            se_muto = True

        elif mutacion == 3 and len(individual) > 1:
            individual = modify_test_case(individual)
            se_muto = True

    return individual

