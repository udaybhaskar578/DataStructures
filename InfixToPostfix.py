'''
Author: Sai Uday Bhaskar Mudivarty
Program: Infix => Postfix 
Process: Expression should have operands and operators seperated by a space ' '
         Create an empty stack called opstack for keeping operators.
         Create an empty list for output.
         Convert the input infix string to a list by using the string method split.
         Scan the expression list from left to right.
         1.If the token is an operand, append it to the end of the output list.
         2.If the token is a left parenthesis, push it on the opstack.
         3.If the token is a right parenthesis, pop the opstack until the 
           corresponding left parenthesis is removed. Append each operator to 
           the end of the output list.
        4.If the token is an operator, *, /, +, or -, push it on the opstack.
          However, first remove any operators already on the opstack that have
          higher or equal precedence and append them to the output list.
        5.When the input expression has been completely processed, check the 
          opstack. Any operators still on the stack can be removed and appended
          to the end of the output list.
'''

from Stack import *
def convertInfixToPostfix(infixexpr):
    #Defining operator precedence
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token.isalpha() or token.isdigit():
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

if __name__ == '__main__':
    print(convertInfixToPostfix("A * B + C * D"))
    print(convertInfixToPostfix("(2 + 3) * 15 - (18 - 22) * (9 / 10)"))
