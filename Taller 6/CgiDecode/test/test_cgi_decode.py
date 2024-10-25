#!./venv/bin/python
import unittest
from src.cgi_decode import cgi_decode


class TestCgiDecode(unittest.TestCase):
    def testEspacio(self):
        t = cgi_decode("+")
        self.assertEqual(" ", t)

    def testVariableHex(self):
        t = cgi_decode("%01")
        self.assertEqual("\x01", t)

    def testVariableDigitoAltoNoHex(self):
        self.assertRaises(ValueError, cgi_decode, "%GG")

    def testVariableDigitoBajoNoHex(self):
        self.assertRaises(ValueError, cgi_decode, "%1G")

    def testMensajeNoCodificado(self):
        t = cgi_decode("Hello World")
        self.assertEqual("Hello World", t)

