from toolz import curry
from functools import reduce
import DFANode
@curry
def eTransitionFENDFA(symbol, stateNode):
    states = set()
    if stateNode.leftNode != None and  stateNode.leftLabel == symbol:
        states.add(stateNode.leftNode)
    if stateNode.rightNode != None and  stateNode.rightLabel == symbol:
        states.add(stateNode.rightNode)
    return states
@curry
def eClosure(emptySequence, stateNode):
    currentVisitedNodes = []
    currentVisitedNodes.append(stateNode)
    closure = {stateNode}
    for element in currentVisitedNodes:
        if (element.leftNode != None and element.leftLabel == emptySequence and
            not element.leftNode in currentVisitedNodes):
            currentVisitedNodes.append(element.leftNode)
            closure.add(element.leftNode)
        if (element.rightNode != None and element.rightLabel == emptySequence and
            not element.rightNode in currentVisitedNodes):
            currentVisitedNodes.append(element.rightNode)
            closure.add(element.rightNode)
    return closure

@curry
def getNameStateSet(startStr, endStr, separator, stateSet):
    name = ""
    for element in stateSet:
        name = element.stateName + ", "+ name
    name = name[0: len(name)-2]
    return startStr + name + endStr

@curry
def fromNDFAToDFAList(NDFAListInitialState, NDFGraph, symbolSet, emptySequence,
    startStr, endStr, separator):
    currentStates = [eClosure(emptySequence)(NDFAListInitialState)]
    DFANodes = []
    for stateSet in currentStates:
        currentDFANode =  DFANode(getNameStateSet(startStr)(endStr)(separator)(stateSet),
		[])
        DFATransitions = []
        for symbol in symbolSet:
            states = reduce(lambda x, y: x.union(y),
                            map(eClosure(emptySequence),
                               reduce(lambda x, y: x.union(y), 
                                      map(eTransitionFENDFA(symbol), stateSet),
                                      set())), 
                           set())
            if len(states) > 0 and not states in currentStates:
                DFANodeStateName = getNameStateSet(startStr)(endStr)(separator)(states)
                currentStates.append(states)
                DFATransitions.append((DFANodeStateName, symbol))
        if len(DFATransitions) > 0:
            currentDFANode.setVariableValue("dfaNodeList", DFATransitions)
        if NDFGraph.finalState in stateSet:
            DFANodes.append((currentDFANode, True))
        else:
            DFANodes.append((currentDFANode, False))
    return DFANodes

def getAcceptanceStatesFromDFAList(DFAList):
    return list(filter(lambda x: x[1] == True, DFAList))

def getEdgesFromDFAList(DFAList):
    edges = []
    for dfaNode in DFAList:
        for element in dfaNode[0].dfaNodeList:
            edges.append((dfaNode[0].nodeName, *element))
    return edges

def getAcceptanceStatesNameList(acceptanceStatesList):
    names = []
    for element in acceptanceStatesList:
        names.append(element[0].nodeName)
    return names