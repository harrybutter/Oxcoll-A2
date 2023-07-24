"""Creating an RPN expression evaluator"""


class Stack:

    def __init__(self, size):
        self.array = []
        self.size = size
        for _ in range(self.size):
            self.array.append('')
        self.pointer = -1
        self.maxInt = 99999

    def show(self):
        return self.array, self.pointer

    def push(self, value):
        if self.pointer < self.size - 1:
            self.pointer += 1
            self.array[self.pointer] = value
            status = value
        else:
            print('Stack overflow')
            status = self.maxInt
        return status

    def pop(self):
        if self.pointer >= 0:
            value = self.array[self.pointer]
            self.array[self.pointer] = ''
            self.pointer -= 1
        else:
            print("Stack underflow")
            value = self.maxInt
        return value


def evaluateRPN(expression):
    stack = Stack(10)
    operator = ['+', '-', '/', '*']
    for char in expression:
        if char not in operator:  # push into the Stack
            stack.push(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.push(arithmetic_operation(operand1, operand2, char))
    print('end')
    return stack.pop()


def arithmetic_operation(a, b, operator):
    match operator:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b
        case _:
            print('Undefined operator')
            return 99999


def main():
    expression = input('Input expression: ')
    print(evaluateRPN(expression))


if __name__ == '__main__':
    main()
