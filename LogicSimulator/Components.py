from CircuitElement import CircuitElement

class LogicGate(CircuitElement):

    def __init__(self, m):
        super().__init__(m, 1)
    
    def logic_function(self):
        pass

class AndGate(LogicGate):
    
    def logic_function(self):
        return all

class OrGate(LogicGate):
    
    def logic_function(self):
        return any

class NotGate(LogicGate):
    
    def logic_function(self):
        def logical_not(bools):
            return [not x for x in bools]
        return logical_not

class NullElement(CircuitElement):
    
    def __init__(self):
        super().__init__(0, 0)

class InputElement(CircuitElement):
    pass

class OutputElement(CircuitElement):
    pass


def calculate_output(gate, inputs):
    func = gate.logic_function()
    return func(inputs)
