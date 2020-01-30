import stateDoubleNode
import stateGraph
class StateGraphOperations:
    
    def __init__(self, nullSequenceSymbol, emptySequenceSymbol):
        self.nullSequenceSymbol = nullSequenceSymbol
        self.emptySequenceSymbol = emptySequenceSymbol
        
    def emptySequenceStateGraph(self):
        finalState = StateDoubleNode(None, None, None, None, None)
        initialState = StateDoubleNode(finalState, None, self.emptySequenceSymbol, None,
                                       None)
        return StateGraph(initialState, finalState)
    
    def nullSequenceStateGraph(self):
        finalState = StateDoubleNode(None, None, None, None, None)
        initialState = StateDoubleNode(None, None, None, None, None)
        return StateGraph(initialState, finalState)
    
    def symbolSequenceStateGraph(self, symbol):
        finalState = StateDoubleNode(None, None, None, None, None)
        initialState = StateDoubleNode(finalState, None, symbol, None, None)
        return StateGraph(initialState, finalState)
    
    def unionStateGraph(self, graphR, graphS):
        finalState = StateDoubleNode(None, None, None, None, None)
        initialState = StateDoubleNode(graphR.initialState, graphS.initialState,
                                       self.emptySequenceSymbol, self.emptySequenceSymbol, None)
        graphR.finalState.setVariableValue("leftNode", finalState)
        graphR.finalState.setVariableValue("leftLabel", self.emptySequenceSymbol)
        graphS.finalState.setVariableValue("leftNode", finalState)
        graphS.finalState.setVariableValue("leftLabel", self.emptySequenceSymbol)
        return StateGraph(initialState, finalState)
    
    def concatenationStateGraph(self, graphR, graphS):
        finalState = graphS.finalState
        initialState = graphR.initialState
        graphR.finalState.setVariableValue("leftNode", graphS.initialState)
        graphR.finalState.setVariableValue("leftLabel", self.emptySequenceSymbol)
        return StateGraph(initialState, finalState)
    
    def closureAsteriskStateGraph(self, graphR):
        finalState = StateDoubleNode(None, None, None, None, None)
        initialState = StateDoubleNode(graphR.initialState, finalState,
                                       self.emptySequenceSymbol, self.emptySequenceSymbol)
        graphR.finalState.setVariableValue("leftNode", graphR.initialState)
        graphR.finalState.setVariableValue("leftLabel", self.emptySequenceSymbol)
        graphR.finalState.setVariableValue("rightNode", graphR.finalState)
        graphR.finalState.setVariableValue("rightLabel", self.emptySequenceSymbol)
        return StateGraph(initialState, finalState)
        
    def closurePlusStateGraph(self, graphR):
        finalState = StateDoubleNode(None, None, None, None, None)
        initialState = StateDoubleNode(graphR.initialState, None,
                                       self.emptySequenceSymbol, None, None)
        graphR.finalState.setVariableValue("leftNode", graphR.initialState)
        graphR.finalState.setVariableValue("leftLabel", self.emptySequenceSymbol)
        graphR.finalState.setVariableValue("rightNode", graphR.finalState)
        graphR.finalState.setVariableValue("rightLabel", self.emptySequenceSymbol)
        return StateGraph(initialState, finalState)