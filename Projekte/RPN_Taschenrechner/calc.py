from stack import Stack

def calc(expr):
    """
        implements a postfix calculator
        
        see also here:
            https://www.geeksforgeeks.org/stack-set-4-evaluation-postfix-expression/
            https://de.wikipedia.org/wiki/Umgekehrte_polnische_Notation
    """
    s = Stack()
    
    # split the expression
    for e in expr.split(" "):        
        # check for number
        try:
            num = int(e)          
            s.push(num)            
        except:
            # it's not a number, so treat it as an operator
            op1 = s.pop()
            op2 = s.pop()            
            if e == "*":
                s.push(op2 * op1)
            elif e == "+":
                s.push(op2 + op1)
            elif e == "-":
                s.push(op2 - op1)
            elif e == ":":
                s.push(op2 / op1)
            else:
                print("Unknown operation")
                return
        
    return s.pop()
    
if __name__ == '__main__':
    print( calc("4 3 * 2 2 + :") )
    print( calc("2 3 1 * + 9 -") )
    