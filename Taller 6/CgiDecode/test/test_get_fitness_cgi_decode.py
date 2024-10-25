#!./venv/bin/python
import unittest

from src.evaluate_condition import clear_maps
from src.get_fitness_cgi_decode import get_fitness_cgi_decode


class TestGetFitnessCgiDecode(unittest.TestCase):
    def test1(self):
        clear_maps()
        self.assertEqual(get_fitness_cgi_decode(["%AA"]), 2.357142857142857)

    def test2(self):
        clear_maps()
        self.assertEqual(get_fitness_cgi_decode(["\%AA"]), 1.8571428571428572)

    def test3(self):
        clear_maps()
        self.assertEqual( get_fitness_cgi_decode(["\%AU"]), 3.03021978021978)

    def test4(self):
        clear_maps()
        self.assertEqual(get_fitness_cgi_decode(["\%UU"]), 4.53021978021978)

    def test5(self):
        clear_maps()
        self.assertEqual(get_fitness_cgi_decode(["Hello+Reader"]), 4.972222222222222)

    def test6(self):
        clear_maps()
        self.assertEqual(get_fitness_cgi_decode([""]), 8.5)

    def test7(self):
        clear_maps()
        self.assertEqual(get_fitness_cgi_decode(["\%"]), 5.357142857142858)

    def test8(self):
        clear_maps()
        self.assertEqual(get_fitness_cgi_decode(["\%1"]), 5.523809523809524)

    def test9(self):
        clear_maps()
        self.assertEqual(get_fitness_cgi_decode(["+"]), 6.5)

    def test10(self):
        clear_maps()
        self.assertEqual(get_fitness_cgi_decode(["+\%1"]), 4.666666666666666)


    def test11(self):
        clear_maps()
        self.assertEqual(get_fitness_cgi_decode(["\%1+", "%+1", "a+%AA"]), 0)


        # get_fitness_cgi_decode(["\%1+"]) = 2.9404761904761907
        # get_fitness_cgi_decode(["\%1+", "%+1", "a+%AA"]) = 0