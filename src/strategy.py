import math
import random
import numpy as np
import matplotlib.pyplot as plt
import scipy
from abc import ABC, abstractmethod


class Strategy:
    def __init__(self, verbal=True, parameter_verbal=False, **kwargs) -> None:
        self.parameters = kwargs

        self.verbal = verbal
        self.parameter_verbal = parameter_verbal    
    
    def simulate(self):
        return
    
    def parameters(self):
        return self.parameters
    
    def add_parameter(self, new_parameter, value):
        self.parameters[new_parameter] = value

    def remove_parameter(self, removed_parameter):
        self.parameters.pop(removed_parameter, None)

    @abstractmethod
    def eval():
        return
    

if __name__ == "__main__":
    strategy = Strategy(hi=True, hello=True)
    print(strategy.parameters)