
import unittest
from returnNumeros import Romannumerals

class test_basic(unittest.TestCase):
	def testNumeroDos(self):
		classNumero = Romannumerals()
		assert classNumero.Sum('I','I') == 2

	def testNumeroTres(self):
		classNumero = Romannumerals()
		assert classNumero.Sum('I','II') == 3

	def testNumeroTresInverso(self):
		classNumero = Romannumerals()
		assert classNumero.Sum('II','I') == 3

	def testNumeroCuatro(self):
		classNumero = Romannumerals()
		assert classNumero.Sum('III','I') == 4

	def testNumeroCuatroInverso(self):
		classNumero = Romannumerals()
		assert classNumero.Sum('I','III') == 4

	def testNumeroCinco(self):
		classNumero = Romannumerals()
		assert classNumero.Sum('IV','I') == 5

	def testNumeroCincoInverso(self):
		classNumero = Romannumerals()
		assert classNumero.Sum('I','IV') == 5	

	def testNumeroSeis(self):
		classNumero = Romannumerals()
		assert classNumero.Sum('I','V') == 6

	def testNumeroSeisInverso(self):
		classNumero = Romannumerals()
		assert classNumero.Sum('V','I') == 6

	def testNumeroSiete(self):
		classNumero = Romannumerals()
		assert classNumero.Sum('II','V') == 7

	def testNumeroSieteInverso(self):
		classNumero = Romannumerals()
		assert classNumero.Sum('V','II') == 7

	def testNumeroOcho(self):
		classNumero = Romannumerals()
		assert classNumero.Sum('III','V') == 8

	def testNumeroOchoInverso(self):
		classNumero = Romannumerals()
		assert classNumero.Sum('V','III') == 8

	def testNumeroNueve(self):
		classNumero = Romannumerals()
		assert classNumero.Sum('IV','V') == 9

	def testNumeroNueveInverso(self):
		classNumero = Romannumerals()
		assert classNumero.Sum('V','IV') == 9

	def testNumeroDiez(self):
		classNumero = Romannumerals()
		assert classNumero.Sum('I','IX') == 10

	def testNumeroDiezInverso(self):
		classNumero = Romannumerals()
		assert classNumero.Sum('IX','I') == 10 

if __name__=='__main__':
	unittest.main()
		
