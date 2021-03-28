from enum import Enum

class CircuitElement(object):
    
    def __init__(self, m, n, id):
        self._num_ins = m
        self._num_outs = n

        self._ins = []
        self._outs = []
        self.name = None

    def update(self):
        pass

    def update_inputs(self):
        pass

    def update_outputs(self):
        pass
