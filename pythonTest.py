
import unittest
from returnNumeros import Romannumerals

class test_basic(unittest.TestCase):
	def testresultforSum(self):
		classNumero = Romannumerals()
		assert classNumero.Sum('I','I') == 1

if __name__=='__main__':
	unittest.main()
		
