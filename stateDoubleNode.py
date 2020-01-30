class StateDoubleNode:
    def __init__(self, leftNode, rightNode, leftLabel, rightLabel, stateName):
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.leftLabel = leftLabel
        self.rightLabel = rightLabel
        self.stateName = stateName

    def setVariableValue(self, variableName, value):
        if variableName in vars(self).keys():
            vars(self)[variableName] = value