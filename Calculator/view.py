from model import Calculator

class View:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def addition(self):
        operands = Calculator(self.x, self.y)
        print ("Sum of " + str(self.x) + " and " + str(self.y) + " = " + str(Calculator.addition(operands)))
    
    def subtraction(self):
        operands = Calculator(self.x, self.y)
        print ("Sum of " + str(self.x) + " and " + str(self.y) + " = " + str(Calculator.subtraction(operands)))

    def multiplication(self):
        operands = Calculator(self.x, self.y)
        print ("Sum of " + str(self.x) + " and " + str(self.y) + " = " + str(Calculator.multiplication(operands)))

    def division(self):
        operands = Calculator(self.x, self.y)
        if operands.y is not 0:
            print ("Sum of " + str(self.x) + " and " + str(self.y) + " = " + str(Calculator.division(operands)))
        else:
            print("Can not divide by zero!")