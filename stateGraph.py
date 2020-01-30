class StateGraph:
    def __init__(self, initialState, finalState):
        self.initialState = initialState
        self.finalState = finalState
        
    def setVariableValue(self, variableName, value):
        if variableName in vars(self).keys():
            vars(self)[variableName] = value