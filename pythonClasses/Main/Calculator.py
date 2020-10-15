from CalcFunct.fractionalConverter import fractionalConverter
from MathOperations.subtraction import Subtraction

from yahoo_fin import stock_info as si

class Calculator:

    Result = 0

    def __init__(self):
        pass

    def Sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result