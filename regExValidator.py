def isOperator(symbol):
    return symbol in ")|.*+("

def isUnary(operator):
    return operator in "*+"

def isBinary(operator):
    return operator in "|."

def isEndOfSequence(symbol, endSequence):
    return symbol == endSequence

def getTopElement(_list):
    if len(_list) == 0:
        return None
    return _list[len(_list)-1]

def countOpenAndCloseParenthesis(symbols):
    counterOpenPar = 0
    counterClosePar = 0
    for element in symbols:
        if element == "(":
            counterOpenPar +=1
        if element == ")":
            counterClosePar += 1
    return (counterOpenPar, counterClosePar)

def validRegEx(string, endSequence):
    symbols = []
    valid = True
    if len(string) == 0:
        return not valid
    if (isUnary(string[0]) or isBinary(string[0]) 
        or isEndOfSequence(string[0], endSequence) or string[0] == ")"):
        return not valid
    if not endSequence in string:
        return not valid
    symbols.append(string[0])
    regEx = string[1:]
    index = 1
    for symbol in regEx:
        if isEndOfSequence(symbol, endSequence):
            break
        if not isOperator(symbol):
            if getTopElement(symbols) == "(" or isBinary(getTopElement(symbols)):
                symbols.append(symbol)
            else:
                return not valid
        else:
            if isUnary(symbol):
                if (getTopElement(symbols) == ")" or
                    not isOperator(getTopElement(symbols)) or
                   isUnary(getTopElement(symbols))):
                    symbols.append(symbol)
                else:
                    return not valid
            if isBinary(symbol):
                if (getTopElement(symbols) == ")" or
                    not isOperator(getTopElement(symbols)) or
                   isUnary(getTopElement(symbols))):
                    symbols.append(symbol)
                else:
                    return not valid
            if symbol == ")":
                if getTopElement(symbols) == "(" or isBinary(getTopElement(symbols)):
                    return not valid
                counter = countOpenAndCloseParenthesis(symbols)
                if counter[0] >= counter[1]+1:
                    symbols.append(symbol)
                else:
                    return not valid
            if symbol == "(":
                if getTopElement(symbols) == "(" or isBinary(getTopElement(symbols)):
                    symbols.append(symbol)
                else:
                    return not valid
        index +=1
    counter = countOpenAndCloseParenthesis(symbols)
    if counter[0] != counter[1]:
        return not valid
    if index == len(string)-1:
        return valid
    return not valid