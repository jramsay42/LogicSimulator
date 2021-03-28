import os
import sys


class Circuit(object):
    
    def __init__(self):
        self._adjacency_list = list()

    def build_circuit(self, circuit_file):
        """ Parses given circuit_file and constructs the data structure. """
        with open(circuit_file, "r") as f:
            print(f.readlines())


    def save_circuit(self, circuit_file):
        pass