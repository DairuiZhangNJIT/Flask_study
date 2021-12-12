"""Multiplication Class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """subtraction calculation object"""
    def get_result(self):
        """get the multiplication results"""
        result = self.values[0] / self.values[1]
        return result
