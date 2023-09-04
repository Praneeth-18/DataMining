from tkinter import *
from math import sin, cos, tan, log, exp, sqrt, factorial

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Scientific Calculator")
        self.master.geometry("400x600")
        self.equation = StringVar()
        self.entry_field = Entry(self.master, textvariable=self.equation)
        self.entry_field.grid(row=0, column=0, columnspan=4)
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 'sin',
            '4', '5', '6', '*', 'cos',
            '1', '2', '3', '-', 'tan',
            '0', '.', '=', '+', 'log',
            'exp', 'sqrt', '!', '(', ')'
        ]
        row_val = 1
        col_val = 0
        for button in buttons:
            Button(self.master, text=button, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

    def click_button(self, button):
        current_equation = str(self.equation.get())
        if button == '=':
            try:
                self.equation.set(eval(current_equation))
            except:
                self.equation.set("Error")
        elif button in ['sin', 'cos', 'tan', 'log', 'exp', 'sqrt', 'factorial']:
            try:
                self.equation.set(eval(button + '(' + current_equation + ')'))
            except:
                self.equation.set("Error")
        else:
            self.equation.set(current_equation + button)
