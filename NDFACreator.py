import stateOperations
def isEmptySequence(sequence):
    return sequence == "$"

def isNullSequence(sequence):
    return sequence == "¬"
	
def isUnary(operator):
    return operator in "*+"

def isSymbolSequence(sequence):
    return not (isEmptySequence(sequence) or
                isEmptySequence(sequence) or
                isOperator(sequence))

def isAtomicSequence(sequence):
    return (isEmptySequence(sequence) or
            isNullSequence(sequence) or
            isSymbolSequence(sequence))

def combineToRegularEx(dividedRegEx):
    if dividedRegEx[1] == None and dividedRegEx[2] == None:
        return dividedRegEx[0]
    if dividedRegEx[2] == None:
        return dividedRegEx[1] + dividedRegEx[0]
    return dividedRegEx[1] + dividedRegEx[0] + dividedRegEx[2]

def divideRegEx(prefixRegEx):
    if isAtomicSequence(prefixRegEx[0]):
        return (prefixRegEx[0], None, None)
    operator = prefixRegEx[0]
    if isUnary(operator):
        regEx = divideRegEx(prefixRegEx[1:])
        leftRegEx = combineToRegularEx(regEx)
        return (leftRegEx, operator, None)
    regEx = divideRegEx(prefixRegEx[1:])
    leftRegEx = combineToRegularEx(regEx)
    regEx = divideRegEx(prefixRegEx[len(leftRegEx)+1:])
    rightRegEx = combineToRegularEx(regEx)
    return (leftRegEx, operator, rightRegEx)
	
operations = StateGraphOperations("¬", "$")

def simplifyRegEx(prefixRegEx):
    if isAtomicSequence(prefixRegEx[0]):
        return prefixRegEx[0]
    dividedRegEx = divideRegEx(prefixRegEx)
    if isUnary(dividedRegEx[1]):
        regEx = None
        if dividedRegEx[0][0] == "*":
            regEx = simplifyRegEx(dividedRegEx[0][1:])
            return  regEx
        else:
            regEx = simplifyRegEx(dividedRegEx[0])
        if isEmptySequence(regEx):
            return "$"
        if isNullSequence(regEx):
            return "$"
        return dividedRegEx[1]+regEx
    leftRegEx = simplifyRegEx(dividedRegEx[0])
    rightRegEx = simplifyRegEx(dividedRegEx[2])
    if dividedRegEx[1] == "|":
        if leftRegEx == rightRegEx:
            return leftRegEx
    if dividedRegEx[1] == ".":
        if isNullSequence(leftRegEx) or isNullSequence(rightRegEx):
            return "¬"
        if isEmptySequence(leftRegEx):
            return rightRegEx
        if isEmptySequence(rightRegEx):
            return leftRegEx
    return dividedRegEx[1] + leftRegEx + rightRegEx

def getStateGraphOperation(symbol):
    if symbol == "*":
        return operations.closureAsteriskStateGraph
    if symbol == "+":
        return operations.closurePlusStateGraph
    if symbol == "|":
        return operations.unionStateGraph
    if symbol == ".":
        return operations.concatenationStateGraph
    if symbol == "$":
        return operations.emptySequenceStateGraph
    if symbol == "¬":
        return operations.nullSequenceStateGraph
    return operations.symbolSequenceStateGraph

def createNDFA(prefixRegEx):
    dividedRegEx = divideRegEx(prefixRegEx)
    if dividedRegEx[1] == None and dividedRegEx[2] == None:
        return getStateGraphOperation(dividedRegEx[0])(dividedRegEx[0])
    else:
        if dividedRegEx[2] == None:
            unaryOperator = getStateGraphOperation(dividedRegEx[1])
            return unaryOperator(createNDFA(dividedRegEx[0]))
        else:
            binaryOperator = getStateGraphOperation(dividedRegEx[1])
            graphR = createNDFA(dividedRegEx[0])
            graphS = createNDFA(dividedRegEx[2])
            return binaryOperator(graphR, graphS)