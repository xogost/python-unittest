#Calculadora de numeros romanos
#Juan Camilo Martinez
#Para Codindojo Bogota

class Romannumerals(object):
	"""Roman numerals class"""
	def __init__(self):
		super(Romannumerals, self).__init__()
		self.numbers = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
		_numberOne = 0
		_numberTwo = 0
	
	def Sum(self,numberOne,numberTwo):
		self._numberOne = self.convertToNumber(numberOne)
		self._numberTwo = self.convertToNumber(numberTwo)
		result = self._numberOne + self._numberTwo
		return(result)
	
	def convertToNumber(self, number):
		_number = str(number)		

		one = 0

		for x in xrange(0,len(_number)):
			if len(_number) == 2 and _number != 'II':
				if _number[x+1] == 'V' and _number[x] == 'I':
					_number = self.numbers['V'] -1 
					break
				elif _number[x+1] == 'X' and _number[x] == 'I':
					  _number = self.numbers['X'] - 1
					  break
			elif _number[x] == 'V':
				_number = self.numbers['V']
			elif _number[x] == 'I':
				one = one + 1

		if one != 0:
			_number = one

		return int(_number)
		
