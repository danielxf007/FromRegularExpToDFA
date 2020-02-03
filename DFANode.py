class DFANode:
    def __init__(self, nodeName, dfaNodeList):
        self.nodeName = nodeName
        self.dfaNodeList = dfaNodeList
        
    def setVariableValue(self, variableName, value):
        if variableName in vars(self).keys():
            vars(self)[variableName] = value