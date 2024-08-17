import sys, os
from tkinter import *


def main():
    root = Tk()
    root.title("Project Kitty")
    root.geometry("400x400")
    w = Label(root, text="Hello World!")
    w.pack()
    inp =  Entry(root, width=50)
    inp.pack()
    btn = Button(root, text="Execute", width=20)
    btn.pack()
    output = Label(root, width=50, height=10, text="Output")
    output.pack()
    root.mainloop()

if __name__ == "__main__":
    main()