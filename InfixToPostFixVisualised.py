"""Converting expressions from infix to postfix"""

import RPN as rpn
from tkinter import *

global cb


class control_block:  # To store global control variables
    def __init__(self):
        self.infix_input = ''
        self.root = None
        self.cv = None


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
        else:  # if token is one of the arithmetic operator,
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


def handle_boxes(index, colour, value):
    global cb
    boxindex = [100, 150, 200, 250, 300, 450, 500, 550, 600, 650]
    box = boxindex[index]
    cb.cv.create_rectangle((200, box, 350, box + 50),
                           width=2, fill=colour)
    cb.cv.create_text(272, box + 25, text=value)


def evaluating_infix(infix):
    # infix = input("Input infix expression: ")
    postfix = infix_to_postfix(infix)
    print(rpn.evaluateRPN(postfix))


def infix_submit():
    global cb
    from tkinter.messagebox import showinfo

    msg = f"Infix '{cb.infix_input.get()}' has been submitted"
    showinfo(
        title="Information",
        message=msg
    )
    postfix_label = Label(cb.root, text=infix_to_postfix(cb.infix_input.get()))
    cb.cv.create_window(500, 80, window=postfix_label)
    #  cb.cv.create_text(500, 100, text=infix_to_postfix(cb.infix_input.get()))


def main():
    global cb
    #  expression = '5+8*9-(7/2)'
    cb = control_block()

    root = Tk()
    cb.root = root
    root.title("Postfix calculation process simulator")
    cv = Canvas(root, width=900, height=700, bg="white")
    cb.cv = cv
    cv.pack()

    # Input box for infix
    # cv.create_rectangle((460, 35, 700, 65), width=1, fill="blue")
    cb.infix_input = StringVar()
    infix_label = Label(root, text="Infix Input")
    cv.create_window(500, 50, window=infix_label)
    infix_entry = Entry(root, textvariable=cb.infix_input)
    cv.create_window(610, 50, window=infix_entry)
    infix_entry.focus()

    sumbitbtn = Button(root, text="Submit", width=5, height=1, bd='2', command=lambda: infix_submit())
    sumbitbtn.place(x=700, y=35)



    btn = Button(root, text="Oh yeah", width=8, height=2, bd='3', command=lambda: handle_boxes(3, 'red', 56),
                 font=('Arial', 10))
    btn.place(x=500, y=500)

    start_box = 100
    for _ in range(10):  # creating 10 boxes for the stack
        cv.create_rectangle((200, start_box, 350, start_box + 50), width=2, fill="light green")
        start_box += 50

    root.mainloop()


if __name__ == '__main__':
    main()
