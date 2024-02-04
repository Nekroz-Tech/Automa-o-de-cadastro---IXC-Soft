from imports import *

def input_dados(janela, text, row, column):
    Label(janela, text = text).grid(column=column, row=row)
    entry = Entry(janela)
    entry.grid(column=column+1, row=row)
    return entry
