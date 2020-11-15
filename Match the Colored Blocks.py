from tkinter import *
from random import choice


colors_list = ["red", "blue", "green", "yellow", "purple", "cyan"]
button_number = 0
total_colors = []
stored_colors = []
row = 0
column = 0
difficulty = 1

class main_window:
    def __init__(self):
        self.root = Tk()
        self.root.title("Main Window")

    def button(self, column, row, button_number, color, stored):

        button = Button(text= ("Button", button_number), bg = "black",
                        width = 20, height = 10, command = lambda : [self.canvas(column, row, color, stored)
                                                                        ], activebackground = color)
        button.grid(column = column, row = row)

    def no_more_than_two_colors(self, color):

        while total_colors.count(color) >= (2 * difficulty):
            color = choice(colors_list)
        return color

    def canvas(self, column, row, color, stored):
        canvas = Canvas(self.root,bg = color, width = 145, height = 150)
        canvas.grid(column = column, row = row)
        stored += [color]
        print(stored)
        return stored

window = main_window()

for color in colors_list*2 * difficulty:
    color = choice(colors_list)
    color = window.no_more_than_two_colors(color)
    if button_number%3 == 0:
        row += 1
        column = 0
    window.button(row, column, button_number, color, stored_colors)

    column +=1
    total_colors += [color]
    button_number += 1

print(total_colors)
window.root.mainloop()
