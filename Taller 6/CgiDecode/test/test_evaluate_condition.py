#!./venv/bin/python
import unittest
from src.evaluate_condition import evaluate_condition


class TestEvaluateCondition(unittest.TestCase):

    def testEqChars(self):
       self.assertTrue(evaluate_condition(1, "Eq", 'a', 'a'))
       self.assertFalse(evaluate_condition(1, "Eq", 'a', 'b'))

    def testNe(self):
        self.assertTrue(evaluate_condition(1, "Ne", 'a', 'b'))
        self.assertFalse(evaluate_condition(1, "Ne", 'a', 'a'))

    def testLt(self):
        self.assertTrue(evaluate_condition(1, "Lt", 0, 1))
        self.assertFalse(evaluate_condition(1, "Lt", 1, 0))

    def testGt(self):
        self.assertTrue(evaluate_condition(1, "Gt", 'b', 'a'))
        self.assertFalse(evaluate_condition(1, "Gt", 'a', 'b'))

    def testLe(self):
        self.assertTrue(evaluate_condition(1, "Le", 1, 1))
        self.assertFalse(evaluate_condition(1, "Le", 1, 0))

    def testGe(self):
        self.assertTrue(evaluate_condition(1, "Ge", 1, 0))
        self.assertFalse(evaluate_condition(1, "Ge", 0, 1))

    def testIn(self):
        dic = {'a': 11, 'b': 12, 'c': 13}
        self.assertTrue(evaluate_condition(1, "In", 'a', dic))
        self.assertFalse(evaluate_condition(1, "In", 'd', dic))
        self.assertFalse(evaluate_condition(1, "In", 'e', {}))
