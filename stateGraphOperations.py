import stateDoubleNode
import stateGraph
class StateGraphOperations:
    
    def __init__(self, nullSequenceSymbol, emptySequenceSymbol):
        self.nullSequenceSymbol = nullSequenceSymbol
        self.emptySequenceSymbol = emptySequenceSymbol
        
    def emptySequenceStateGraph(self):
        finalState = StateDoubleNode(None, None, None, None)
        initialState = StateDoubleNode(finalState, None, self.emptySequenceSymbol, None)
        return StateGraph(initialState, finalState)
    
    def nullSequenceStateGraph(self):
        finalState = StateDoubleNode(None, None, None, None)
        initialState = StateDoubleNode(None, None, None, None)
        return StateGraph(initialState, finalState)
    
    def symbolSequenceStateGraph(self, symbol):
        finalState = StateDoubleNode(None, None, None, None)
        initialState = StateDoubleNode(finalState, None, symbol, None)
        return StateGraph(initialState, finalState)
    
    def unionStateGraph(self, regExR, regExS):
        graphR = symbolSequenceStateGraph(regExR)
        graphS = symbolSequenceStateGraph(regExS)
        finalState = StateDoubleNode(None, None, None, None)
        initialState = StateDoubleNode(graphR.initialState, graphS.initialState,
                                       self.emptySequenceSymbol, self.emptySequenceSymbol)
        graphR.finalState.setLeftNode(finalState)
        graphR.finalState.setLeftLabel(self.emptySequenceSymbol)
        graphS.finalState.setLeftNode(finalState)
        graphS.finalState.setLeftLabel(self.emptySequenceSymbol)
        return StateGraph(initialState, finalState)
    
    def concatenationStateGraph(self, regExR, regExS):
        graphR = symbolSequenceStateGraph(regExR)
        graphS = symbolSequenceStateGraph(regExS)
        finalState = graphS.finalState
        initialState = graphR.initialState
        graphR.finalState.setLeftNode(graphS.initialState)
        graphR.finalState.setLeftLabel(self.emptySequenceSymbol)
        return StateGraph(initialState, finalState)
    
    def closureAsteriskStateGraph(self, regExR):
        graphR = symbolSequenceStateGraph(regExR)
        finalState = StateDoubleNode(None, None, None, None)
        initialState = StateDoubleNode(graphR.initialState, finalState,
                                       self.emptySequenceSymbol, self.emptySequenceSymbol)
        graphR.finalState.setLeftNode(graphR.initialState)
        graphR.finalState.setLeftLabel(self.emptySequenceSymbol)
        graphR.finalState.setRightNode(graphR.finalState)
        graphR.finalState.setRightLabel(self.emptySequenceSymbol)
        return StateGraph(initialState, finalState)
        
    def closurePlusStateGraph(self, regExR):
        graphR = symbolSequenceStateGraph(regExR)
        finalState = StateDoubleNode(None, None, None, None)
        initialState = StateDoubleNode(graphR.initialState, None,
                                       self.emptySequenceSymbol, None)
        graphR.finalState.setLeftNode(graphR.initialState)
        graphR.finalState.setLeftLabel(self.emptySequenceSymbol)
        graphR.finalState.setRightNode(graphR.finalState)
        graphR.finalState.setRightLabel(self.emptySequenceSymbol)
        return StateGraph(initialState, finalState)