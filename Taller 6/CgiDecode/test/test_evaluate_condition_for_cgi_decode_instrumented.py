#!./venv/bin/python
import unittest
from src.cgi_decode import cgi_decode
from src.cgi_decode_instrumented import cgi_decode_instrumented
from src.evaluate_condition import clear_maps, get_true_distance, get_false_distance, distances_true, distances_false


class TestEvaluateConditionForCgiDecodeInstrumented(unittest.TestCase):
    def testHelloWorld(self):
        clear_maps()
        t = cgi_decode_instrumented("Hello+World")
        self.assertEqual(t, cgi_decode("Hello+World"))
        self.assertEqual(distances_true, {1: 0, 2: 0, 3: 35})
        self.assertEqual(distances_false, {1: 0, 2: 0, 3: 0})

    def testEspacio(self):
        clear_maps()
        t = cgi_decode_instrumented("+")
        self.assertEqual(" ", t)
        self.assertEqual(distances_true, {1: 0, 2: 0})
        self.assertEqual(distances_false, {1: 0, 2: 1})

    def testVariableHex(self):
        clear_maps()
        t = cgi_decode_instrumented("%01")
        self.assertEqual("\x01", t)
        self.assertEqual(distances_true, {1: 0, 2: abs(ord('%')-ord('+')), 3:0, 4:0, 5:0})
        self.assertEqual(distances_false, {1: 0, 2: 0, 3:1, 4:1, 5:1})

    def testVariableDigitoAltoNoHex(self):
        clear_maps()
        self.assertRaises(ValueError, cgi_decode_instrumented, "%GG")
        self.assertEqual(distances_true, {1: 0, 2: abs(ord('%') - ord('+')), 3: 0, 4: abs(ord('G')-ord('F'))})
        self.assertEqual(distances_false, {1: 3, 2: 0, 3: 1, 4: 0})

    def testVariableDigitoBajoNoHex(self):
        clear_maps()
        self.assertRaises(ValueError, cgi_decode_instrumented, "%1G")
        self.assertEqual(distances_true, {1: 0, 2: abs(ord('%') - ord('+')), 3: 0, 4: 0, 5: abs(ord('G')-ord('F'))})
        self.assertEqual(distances_false, {1: 3, 2: 0, 3: 1, 4:1, 5:0})

    def testMensajeNoCodificado(self):
        clear_maps()
        t = cgi_decode("Hello World")
        self.assertEqual("Hello World", t)
