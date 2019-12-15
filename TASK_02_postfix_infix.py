#GIVEN CODE
class Expression:
    pass

class Operation(Expression):
    def __init__(self, op, arg1, arg2):
        self.op = op                # a string; always one of '+' '-' '*' '/'
        self.arg1 = arg1        # an Expression
        self.arg2 = arg2        # an Expression

class Value(Expression):
    def __init__(self, value):
        self.value = value    # an integer; always positive

#MY CODE
def postfixRepr(e):
    returnString=""
    def postfixRepr2(e):
        nonlocal returnString

        if e.arg1.__class__.__name__ =="Operation":
            postfixRepr2(e.arg1)
        else:
            returnString+= str(e.arg1.value)+" "

        if e.arg2.__class__.__name__=="Operation":
            postfixRepr2(e.arg2)
        else:
            returnString+= str(e.arg2.value)+" "
        

        returnString+=e.op+" "

        return returnString

    return postfixRepr2(e)

def infixRepr(e):
    #"global" variables
    returnString=""             #this is the string we construct durting the recursive iteration to return
    returnStack=[]              #this is where we save the right side of the brackets ")"
    operationHolder=list()      #this list holds all the operation of the given expression
    operationHolderIndex=-1     #this is the previous operation used (before the current operation was called)
    
    #make a list of all the operations
    def listOperations(e):
        nonlocal operationHolder
        operationHolder.append(e.op)
        if e.arg1.__class__.__name__ =="Operation":
            listOperations(e.arg1)
        if e.arg2.__class__.__name__ =="Operation":
            listOperations(e.arg2)
    
    #create the list of operations
    listOperations(e)

    def infixRepr2(e):
        #"global" variables which do not lose value during recursive iteration
        nonlocal operationHolder
        nonlocal returnString
        nonlocal returnStack
        nonlocal operationHolderIndex

        #check if we need to use brackets, the very first time we should not check
        if operationHolderIndex!=-1:
            prev_op=operationHolder[operationHolderIndex]
            if (e.op =="+" or e.op=="-") and (prev_op=="*" or prev_op=="/") or \
                    (e.op =="-" and prev_op=="-") or \
                        (e.op =="*" or e.op=="/") and (prev_op=="+" or prev_op=="-"):
                returnString+="("
                returnStack.append(")")
        

        #check if the first argument is an operation, if yes, we do a recursive call, and step to the next operation index
            #else we add the arg1 to our returning string 
        if e.arg1.__class__.__name__ =="Operation":
            operationHolderIndex=operationHolderIndex+1
            infixRepr2(e.arg1)
        else:
            returnString+= str(e.arg1.value)
        
        #add the operator to our recursive string
        returnString+= e.op

        #check if the second argument is an operation, if yes, we do a recursive call, and step to the next operation index
            #else we add the arg2 to our returning string 
        if e.arg2.__class__.__name__=="Operation":
            operationHolderIndex=operationHolderIndex+1
            infixRepr2(e.arg2)
        else:
            returnString+= str(e.arg2.value)

        #if we have right-side brackets if our stack, we add them to our returning string
        try:
            returnString+=returnStack.pop()
        except:
            pass

        #as we step out of the operation, we reduce the operation index
        operationHolderIndex=operationHolderIndex-1

        return returnString


    return infixRepr2(e)

if __name__ == "__main__":

    #GIVEN EXAMPLES
    EXAMPLE_1 = Operation('*',Value(2),Operation('+',Value(5),Value(7)))
    EXAMPLE_2 = Operation('/',Operation('*', Value(2),Operation('+',Value(3),Operation('-',Operation('-',Value(4),Value(5)),Operation('-',Value(1),Value(2))))),Operation('*',Value(3),Value(4)))

    #(1+2)*(3+4)*5
    OWN_EXAMPLE_1=Operation("*",Operation("*",Operation("+",Value(1),Value(2)),Operation("+",Value(3),Value(4))),Value(5))
    #((12-5)*6)-3
    OWN_EXAMPLE_2=Operation("-",Operation("*",Operation("-",Value(12),Value(5)),Value(6)),Value(3))

    print("EXAPLE_1:")
    print("The infix representation:    {}".format(infixRepr(EXAMPLE_1)))
    print("The postfix representation:  {}".format(postfixRepr(EXAMPLE_1)))

    print("EXAPLE_2")
    print("The infix representation:    {}".format(infixRepr(EXAMPLE_2)))
    print("The postfix representation:  {}".format(postfixRepr(EXAMPLE_2)))

    print("OWN_EXAPLE_1")
    print("The infix representation:    {}".format(infixRepr(OWN_EXAMPLE_1)))
    print("The postfix representation:  {}".format(postfixRepr(OWN_EXAMPLE_1)))

    print("OWN_EXAPLE_2")
    print("The infix representation:    {}".format(infixRepr(OWN_EXAMPLE_2)))
    print("The postfix representation:  {}".format(postfixRepr(OWN_EXAMPLE_2)))



