class Number:
	def __init__(self, number = None):
		try:
			self.number = float(number)
			try:
				self.number = int(number)
			except:
				self.number = float(number)
				#print("Number is not Int nor Float")
		except:
			self.number = None
			if isinstance(self.number, int): pass
			else: print("Number is not Int nor Float")


	def printNumber(self):
		print(self.number)

	def getNumber(self):
		return self.number

	def isNumber(self):
		match self.number:
			case int() | float():
				return True;
			case _:
				return False;

	def setNumber(self, number):
		try:
			self.number = float(number)
			try:
				self.number = int(number)
			except:
				self.number = float(number)
				#print("Number is not Int nor Float")
		except:
			self.number = None
			if isinstance(self.number, int): pass
			else: print("Number is not Int nor Float")