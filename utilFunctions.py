from toolz import curry

@curry
def isOperator(operators, symbol):
    return symbol in operators

@curry
def isUnary(unaryOperators, operator):
    return operator in unaryOperators

@curry
def isBinary(binaryOperators, operator):
    return operator in binaryOperators

@curry
def isEndOfSequence(endSequence, symbol):
    return symbol == endSequence

@curry
def isNullSequence(nullSequence, sequence):
    return sequence == nullSequence

@curry
def isSymbolSequence(endSequence, nullSequence, operators, sequence):
    return not (isEmptySequence(endSequence)(sequence) or
                isNullSequence(nullSequence)(sequence) or
                isOperator(operators)(sequence))
@curry
def isAtomicSequence(endSequence, nullSequence, operators, sequence):
    return (isEmptySequence(endSequence)(sequence) or
            isNullSequence(nullSequence)(sequence) or
            isSymbolSequence(endSequence)(nullSequence)(operators)(sequence))

def combineToRegularEx(dividedRegEx):
    if dividedRegEx[1] == None and dividedRegEx[2] == None:
        return dividedRegEx[0]
    if dividedRegEx[2] == None:
        return dividedRegEx[1] + dividedRegEx[0]
    return dividedRegEx[1] + dividedRegEx[0] + dividedRegEx[2]

@curry
def getStateGraphOperation(starOp, crossOp, unionOp,
    concatOp, emptySequence, nullSequence, operations, symbol):  
    if symbol == starOp:
        return operations.closureAsteriskStateGraph
    if symbol == crossOp:
        return operations.closurePlusStateGraph
    if symbol == unionOp:
        return operations.unionStateGraph
    if symbol == concatOp:
        return operations.concatenationStateGraph
    if symbol == emptySequence:
        return operations.emptySequenceStateGraph
    if symbol == nullSequence:
        return operations.nullSequenceStateGraph
    return operations.symbolSequenceStateGraph

def getTopElement(_list):
    if len(_list) == 0:
        return None
    return _list[len(_list)-1]

@curry
def countOpenAndCloseParenthesis(openPar, closePar, symbols):
    counterOpenPar = 0
    counterClosePar = 0
    for element in symbols:
        if element == openPar:
            counterOpenPar +=1
        if element == closePar:
            counterClosePar += 1
    return (counterOpenPar, counterClosePar)