"""Subtraction Class"""
import pprint

from calc.calculations.calculation import Calculation

class Subtraction(Calculation):
    """subtraction calculation object"""
    def get_result(self):
        """get the subtraction results"""
        # difference_of_values = 0.0
        # for value in self.values:
        #     difference_of_values =   difference_of_values - value
        difference_of_values = self.values[0] - self.values[1]
        return difference_of_values
