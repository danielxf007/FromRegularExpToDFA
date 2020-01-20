def getWeigth(operator):
    cases = {")": 0, "|": 1, ".": 2, "*": 3, "+": 3, "(": 4}
    return cases[operator]

def isOperator(symbol):
    return symbol in ")|.*+("

def hasGreaterEqWeigth(operatorR, operatorS):
    return getWeigth(operatorR) >= getWeigth(operatorS)

def listIsEmpty(_list):
    return len(_list) == 0

def condInsertOperators(operator, _list):
    return (listIsEmpty(_list) or _list[len(_list)-1] == "(" or
            hasGreaterEqWeigth(operator, _list[len(_list)-1]))

def canInsert(cond, element, _list):
    return cond(element, _list)

def isUnary(operator):
    return operator in "*+"

def accumulate(symbols, operators):
    accumulation = symbols.copy()
    operatorsLeft = operators.copy()
    while not listIsEmpty(operatorsLeft):
        operator = operatorsLeft.pop()
        if operator == "(":
            break
        else:
            symbolj = ""
            symbolk = ""
            if isUnary(operator):
                symbolj = accumulation.pop()
                accumulation.append(operator + " " + symbolj)
            else:
                symbolk = accumulation.pop()
                symbolj = accumulation.pop()
                accumulation.append(operator + " " + symbolj + " " + symbolk)
    return (accumulation, operatorsLeft)
                
def fromInfixToPrefix(regExR):
    if len(regExR) == 1:
        return regExR
    symbols = []
    operators = []
    for element in regExR:
        if not isOperator(element):
            symbols.append(element)
        else:
            if canInsert(condInsertOperators, element, operators):
                operators.append(element)
            else:
                accumulated = accumulate(symbols, operators)
                symbols = accumulated[0]
                operators = accumulated[1]
                if element != ")":
                    operators.append(element)
    while not listIsEmpty(operators):
        accumulated = accumulate(symbols, operators)
        symbols = accumulated[0]
        operators = accumulated[1]
    return symbols[0]