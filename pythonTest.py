
import unittest
from returnNumeros import returnNumeros

class test_basic(unittest.TestCase):
	def testNumeroUno(self):
		classNumero = returnNumeros(None)
		assert classNumero.numeroUno == 1

	def testNumeroDos(self):
		classNumero = returnNumeros(None)
		assert classNumero.numeroDos == 2	
						
if __name__=='__main__':
	unittest.main()
	print __name__
		
