'''
Author: Sai Uday Bhaskar Mudivarty
Program: Hash Table
Process: Expression should have operands and operators seperated by a space ' '
         We require stack to solve this problem
         1.If input is operand(digit) we simple push them on stack.
         2.If the input is operator we pop two operands and do the required 
         operation (operand2 operator operand1)
         Note: Order should be follow operand2 operator operand1
         Let say 2 3 -
         so we push 2(operand1) then 3(operand2) when -(operator). if we can 
         have two answers 1 or -1. But correct one is -1 (2 - 3 = -1).
         3.Then after solving Push the result into stack.
'''

def performOperation(op1,op,op2):
    op1, op2 = int(op1), int(op2)
    if op =='+':
        return op2+op1
    elif op =='-':
        return op2-op1
    elif op=='*':
        return op2*op1
    elif op=='/':
        return op2/op1
    return None

def postfixEval(expression):
    operators = set('+-*/')
    s = expression.split(' ')
    evallist = list()
    for i in s:
        if i.isdigit():
            evallist.append(i)
        elif i in operators:
            evallist.append(performOperation(evallist.pop(),i,evallist.pop()))
    return evallist.pop()

if __name__ == "__main__":
    expression = "10 2 8 * + 3 -"
    print(postfixEval(expression))


