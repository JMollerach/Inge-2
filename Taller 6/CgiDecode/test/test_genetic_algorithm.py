#!./venv/bin/python
import unittest

from random import seed
from src.genetic_algorithm import GeneticAlgorithm


class TestGeneticAlgorithm(unittest.TestCase):
    def test1(self):
        # TODO COMPLETAR
        seed(1)
        ga = GeneticAlgorithm()
        result = ga.run()
        self.assertEqual(ga.get_generation(), 4)
        self.assertEqual(ga.covered_all_branches(ga.fitness_best_individual),True)

    def test2(self):
        # TODO COMPLETAR
        seed(2)
        ga = GeneticAlgorithm()
        result = ga.run()
        self.assertEqual(ga.get_generation(), 23)
        self.assertEqual(ga.covered_all_branches(ga.fitness_best_individual),True)


    def test3(self):
        # TODO COMPLETAR
        seed(4)
        ga = GeneticAlgorithm()
        result = ga.run()
        self.assertEqual(ga.get_generation(), 6)
        self.assertEqual(ga.covered_all_branches(ga.fitness_best_individual),True)
