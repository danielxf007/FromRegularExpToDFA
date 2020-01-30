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

def createNDFA(prefixRegEx):
    dividedRegEx = divideRegEx(prefixRegEx)
    if dividedRegEx[1] == None and dividedRegEx[2] == None:
        print("Atomic Expression:" + dividedRegEx[0])
    else:
        if dividedRegEx[2] == None:
            print("Operator: " + dividedRegEx[1] + " aplied to: " + dividedRegEx[0])
            createNDA(dividedRegEx[0])
        else:
            print("Operator: " + dividedRegEx[1] + " aplied to: " + dividedRegEx[0] + " and " + dividedRegEx[2])
            createNDA(dividedRegEx[0])
            createNDA(dividedRegEx[2])