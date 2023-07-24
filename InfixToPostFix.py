"""Converting expressions from infix to postfix"""

import RPN as rpn


def infix_to_postfix(infix):
    stack = rpn.Stack(20)
    operator = {'+': 0, '-': 0, '*': 1, '/': 1, '(': -1, ')': -1}
    postfix = ''
    for token in infix:
        if token not in operator:
            postfix += token
        elif token == '(':
            stack.push(token)
        elif token == ')':  # if token is closing bracket,
            operatorB = stack.pop()
            while operatorB != '(':
                postfix += operatorB
                operatorB = stack.pop()
        else: # if token is one of the arithmetic operator,
            if stack.pointer < 0:
                stack.push(token)
                continue
            operatorB = stack.pop()
            if operator[operatorB] >= operator[token]:  # if optB is priortised over token
                postfix += operatorB
                stack.push(token)
            else:
                stack.push(operatorB)
                stack.push(token)
    while stack.pointer != -1:
        postfix += stack.pop()
    print(stack.show())
    print('done')
    return postfix


def main():
    expressions = ['5+8*9-(7/2)']
    for expression in expressions:
        # infix = input("Input infix expression: ")
        postfix = infix_to_postfix(expression)
        print(rpn.evaluateRPN(postfix))


if __name__ == '__main__':
    main()
