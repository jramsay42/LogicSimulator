import os

import pytest
from LogicSimulator import Circuit

PROJECT_PATH = os.getcwd()

def test_read_circuit():
    test = Circuit.Circuit()
    test.build_circuit(os.path.join(PROJECT_PATH, "tests\\good_circuit_1.txt"))