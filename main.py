from tkinter import *
import tkinter as tk

class UI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Hi')
        self.initcomponent()

    def initcomponent(self):
        text = tk.Text(self)
        button = self.create_button()
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        # text.grid(padx=5, pady=5)
        text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        button.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)


    def create_text(self):
        pass

    def create_button(self):
        button = tk.Button(self, text="test")
        button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        return button


if __name__ == '__main__':
    play = UI()
    play.mainloop()