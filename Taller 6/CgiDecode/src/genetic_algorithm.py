from operator import concat
from random import random, choice
from typing import List

from src.create_population import create_population
from src.crossover import crossover
from src.evaluate_population import evaluate_population
from src.mutate import mutate
from src.selection import selection

class GeneticAlgorithm():
    def __init__(self):
        self.population_size = 100
        self.tournament_size = 5
        self.p_crossover = 0.70
        self.p_mutation = 0.20

        self.generation = 0
        self.best_individual = None
        self.fitness_best_individual = None

    def get_best_individual(self):
        return self.best_individual
    
    def get_fitness_best_individual(self):
        return self.fitness_best_individual
    
    def get_generation(self):
        return self.generation

    def generate_crossovers(self, population: List[List[str]], fitness_by_individual: dict) -> List[List[str]]:
        # TODO COMPLETAR
        # Pista: no olvidarse de usar selection, deben crear una nueva poblacion
        parent1 = selection(fitness_by_individual,self.tournament_size)
        parent2 = selection(fitness_by_individual,self.tournament_size)
        if random() <= self.p_crossover:
            hijos = crossover(population[parent1[0]], population[parent2[0]])
        else:
            hijos = [population[parent1[0]], population[parent2[0]]]
        return hijos

    def generate_mutations(self, population: List[List[str]]) -> List[List[str]]:
        # TODO COMPLETAR
        ##tirar 2 veces 1 por cada individuo
        if random() <= self.p_mutation:
            population= [mutate(population[0]),population[1]]
        if random() <= self.p_mutation:
            population = [population[0],mutate(population[1])]
        return population

    def covered_all_branches(self, fitness_individual: float) -> bool:
        # TODO COMPLETAR
        return fitness_individual == 0

    def run(self):
        # Generar y evaluar la poblacion inicial
        population = create_population(self.population_size)
        fitness_by_individual = evaluate_population(population)

        # Imprimir el mejor valor de fitness encontrado
        index_best_individual = min(fitness_by_individual, key=fitness_by_individual.get)
        self.best_individual = population[index_best_individual]
        self.fitness_best_individual = fitness_by_individual[index_best_individual]

        # Continuar mientras la cantidad de generaciones es menor que 1000
        # y no haya ningun individuo que cubra todos los objetivos

        while self.generation < 1000 and self.fitness_best_individual != 0:

            # Producir una nueva poblacion en base a la anterior.
            # Usar selection, crossover y mutation.
            new_population = []
            while len(new_population) < self.population_size:
                crossovers = self.generate_crossovers(population, fitness_by_individual)
                mutations = self.generate_mutations(crossovers) #4ta it acá
                new_population.append(mutations[0])
                new_population.append(mutations[1])

            # Una vez creada, reemplazar la poblacion anterior con la nueva
            self.generation += 1
            population = new_population
            fitness_by_individual = evaluate_population(population)

            # Evaluar la nueva poblacion e imprimir el mejor valor de fitness
            index_best_individual = min(fitness_by_individual, key=fitness_by_individual.get)
            if fitness_by_individual[index_best_individual] < self.fitness_best_individual:
                self.best_individual = population[index_best_individual]
                self.fitness_best_individual = fitness_by_individual[index_best_individual]

        # retornar el mejor individuo de la ultima generacion
        return self.best_individual