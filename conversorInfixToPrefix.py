from toolz import curry
@curry
def getWeigth(openPar, unionOp, concatOp, starOp,
    crossOp, closePar, operator):
    cases = {openPar: 0, unionOp: 1, concatOp: 2, starOp: 3,
	crossOp: 3, closePar: 4}
    return cases[operator]

def isOperator(symbol):
    return symbol in ")|.*+("

@curry
def hasGreaterEqWeigth(weightF, operatorR, operatorS):
    return weightF(operatorR) >= weightF(operatorS)

def listIsEmpty(_list):
    return len(_list) == 0

@curry
def condInsertOperators(weightF, openPar, operator, _list):
    return (listIsEmpty(_list) or _list[len(_list)-1] == openPar or
            hasGreaterEqWeigth(weightF)(operator)(_list[len(_list)-1]))
@curry
def canInsert(cond, element, _list):
    return cond(element)(list)

def isUnary(operator):
    return operator in "*+"

@curry
def accumulate(openPar, symbols, operators):
    accumulation = symbols.copy()
    operatorsLeft = operators.copy()
    while not listIsEmpty(operatorsLeft):
        operator = operatorsLeft.pop()
        if operator == openPar:
            break
        else:
            symbolj = ""
            symbolk = ""
            if isUnary(operator):
                symbolj = accumulation.pop()
                accumulation.append(operator + symbolj)
            else:
                symbolk = accumulation.pop()
                symbolj = accumulation.pop()
                accumulation.append(operator + symbolj + symbolk)
    return (accumulation, operatorsLeft)
                
def fromInfixToPrefix(openPar, closePar, regExR):
    if len(regExR) == 1:
        return regExR
    symbols = []
    operators = []
    for element in regExR:
        if not isOperator(element):
            symbols.append(element)
        else:
            if element == closePar:
                accumulated = accumulate(symbols, operators)
                symbols = accumulated[0]
                operators = accumulated[1]
            else:
                if canInsert(condInsertOperators, element, operators):
                    operators.append(element)
                else:
                    accumulated = accumulate(symbols, operators)
                    symbols = accumulated[0]
                    operators = accumulated[1]
                    if element != openPar:
                        operators.append(element)
    while not listIsEmpty(operators):
        accumulated = accumulate(symbols, operators)
        symbols = accumulated[0]
        operators = accumulated[1]
    return symbols[0]
