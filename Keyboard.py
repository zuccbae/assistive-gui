import tkinter as tk

from tkinter import *
import tkinter


Keyboard = tk.Tk()
Keyboard.geometry("1600x958+455+30")


def select(value):
    if value == "     Space     ":
        entry.insert(tkinter.END, ' ')
    elif value == "Tab":
        entry.insert(tkinter.END, '       ')
    elif value == "Shift":
        entry.insert(tkinter.END, )
    elif value == "Caps":
        entry.insert(tkinter.END, )
    elif value == "Bkspace":
        entry.insert(tkinter.END, '')
    elif value == "Enter":
        entry.insert(tkinter.END, '\n')
    else:
        entry.insert(tkinter.END, value)


# def autocapitalize(*arg):
# var.set(var.get().capitalize())

# var.trace("Caps", autocapitalize)

Keyboard.title("Vertigo Assistive Eye: Keyboard and Mouse")
Keyboard['bg'] = 'black'
label1 = Label(Keyboard, text="Vertigo Assistive Eye: Keyboard and Mouse", font=('times new roman', 16, 'normal'),
               bg='black', fg="#000000").grid(row=1, columnspan=40)
entry = Text(Keyboard, wrap=WORD,  #textvariable=var, #yscrollcommand=scrollBar.set,
             width=100, height=32, font=('times new roman', 16, 'normal'))
entry.grid(row=1, columnspan=60)
# entry.pack(side=LEFT, fill=BOTH)
# scrollBar.config(command=entry.yview)

buttons = ['!', '"', '£', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', 'Bkspace', '/', '7', '8', '9',
           'Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '{', '}', '[', ']', 'Enter', '4', '5', '6',
           'Caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', ':', '@', '''''', '#', '~', '1', '2', '3',
           'Shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '<', '>', ',', '.', '?', '|', '\'', '¬', '`', '0', '',

           '     Space     '

           ]
varRow = 2
varColumn = 0


for button in buttons:
    command = lambda x=button: select(x)
    if button != "     Space     ":
        tkinter.Button(Keyboard, text=button, width=6, padx=0.5, pady=0.5, bd=9,
                       font=('times new roman', 12, 'normal'), bg='white',
                       activebackground='green', activeforeground='#FFFFFF', relief='raised',
                       command=command).grid(row=varRow, column=varColumn)
    if button == "     Space     ":
        tkinter.Button(Keyboard, text=button, width= 100, padx=1, pady=1, bd=2,
                       font=('times new roman', 12, 'normal'), bg='white',
                       activebackground='green', activeforeground='#FFFFFF', relief='raised',
                       command=command).grid(row=7, columnspan=20)
    varColumn += 1

    if varColumn > 18 and varRow == 2:
        varColumn = 0
        varRow += 1
    if varColumn > 18 and varRow == 3:
        varColumn = 0
        varRow += 1
    if varColumn > 18 and varRow == 4:
        varColumn = 0
        varRow += 1

Keyboard.mainloop()
