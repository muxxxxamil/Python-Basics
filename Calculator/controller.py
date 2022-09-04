from view import View

class Controller: 
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def operations(op, operands):
        if op == '+':
            Controller.addition(operands)
        elif op == '-':
            Controller.subtraction(operands)
        elif op == '*':
            Controller.multiplication(operands)
        elif op == '/':
            Controller.division(operands)
        else:
            print("Choose one of the following operator : +, -, *, /")

    def addition(self):
        return View.addition(self)
    
    def subtraction(self):
        return View.subtraction(self)

    def multiplication(self):
        return View.multiplication(self)
    
    def division(self):
        return View.division(self)

    def startCalculator(self):
        x = int(input("Enter first number : "))
        y = int(input("Enter second number : "))
        operands = Controller(x, y)
        operators = input("Chose operators from (+, -, /, *) : ")
        Controller.operations(operators, operands) 


if __name__ == '__main__':
    print("Loading calculator....")
    calculator = Controller()
    calculator.startCalculator() 