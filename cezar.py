#/usr/bin/python
#-*- coding: utf-8 -*-
#Графический интерфейс, шифр Цезаря

from tkinter import *
import tkinter.ttk as ttk
N = 27 # сдвиг

root = Tk()

label_input = Label(root, text='Введите сообщение', font='Arial 14')
label_output = Label(root, text='Результат', font='Arial 14')
label_input.grid(row=0, column=0, sticky='w')
label_output.grid(row=0, column=2, sticky='w')

mode = ttk.Combobox(root, values=[u'Зашифровываем', u'Расшифровываем'], height=3, font='Arial 14')
mode.set(u'Зашифровываем')
mode.grid(row=0, column=1)

text_input = Text(root, width=25, height=15, font='Arial 14', wrap=WORD)
text_input.grid(row=1, column=0)

button = Button(root, text='Code/deCode', width=15, height=14, font='Arial 14')
button.grid(row=1, column=1)

text_output = Text(root, width=25, height=15, font='Arial 14', wrap=WORD)
text_output.grid(row=1, column=2)

def coding(string):
    global N
    text_output.delete(1.0, END)
    output = ""

    for letter in string:
        if letter == "\n":
            output = output + letter
        elif letter == " ":
            pass
        else:
            value = ord(letter) + N

            if letter.islower() and value > 1103:
                value = value - 32
                letter = chr(value)

            elif letter.isupper() and value > 1071:
                value = value - 32
                letter = chr(value)
            else:
                letter = chr(value)



        output = output + letter

    text_output.insert(1.0, output)




def decoding(string):
    global N
    text_output.delete(1.0, END)
    output = ""

    for letter in string:
        if letter == "\n":
            output = output + letter
        elif letter == " ":
            pass
        else:

            value = ord(letter) - N
            if value < 1040 and letter.isupper():
                value = value + 32
                letter = chr(value)
            elif  value < 1072 and letter.islower():
                value = value + 32
                letter = chr(value)

            else:

                letter = chr(value)



        output = output + letter

    text_output.insert(1.0, output)




def main_func(event):
    text = text_input.get(1.0, END)
    if mode.get() == 'Расшифровываем':
        decoding(text)
    else:
        coding(text)

def pr_str(event):
    text = text_input.get(1.0, END)
    for letter in text:
        print(1, "-", letter)
        if letter == '\n':
            print("пробел")


button.bind('<Button-1>', main_func)
root.mainloop()
