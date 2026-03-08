class Number:
	def __init__(self, number = ""):
		if not number == "":
			match number:
				case int() | float():
					self.number = number
				case _:
					print("Number is not Int nor Float")

	def printNumber(self):
		print(self.number)

	def getNumber(self):
		return self.number

	def setNumber(self, number):
		match number:
			case int() | float():
				self.number = number
			case _:
				print("Number is not Int nor Float")