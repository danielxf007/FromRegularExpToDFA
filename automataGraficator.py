from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
f = Digraph('finite_state_machine', filename='fsm', format= "pdf")
f.attr(rankdir='LR', size='8,5')

def drawAcceptingStateList(diagraph, representation, nodeShape, stateNameList):
    diagraph.attr(representation, shape=nodeShape)
    for stateName in stateNameList:
        diagraph.node(stateName)

def drawEdgeList(diagraph, representation, nodeShape, edgeList):
    diagraph.attr(representation, shape=nodeShape)
    for element in edgeList:
        diagraph.edge(*element)

def drawFSM(diagraph, stateNameList, edgeList):
    drawAcceptingStateList(diagraph, "node", "doublecircle", stateNameList)
    drawEdgeList(diagraph, "node", "circle", edgeList)
    diagraph.view()
