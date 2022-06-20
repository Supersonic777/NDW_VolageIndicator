import tkinter as tk

mineWindow = tk.Tk()

def WindowCreator():
    mineWindow.title("VOLTTERA - помошник №1 в индикации напряжения")

    mineWindow.geometry("1280x720")

    mineWindow.config(bg="mediumslateblue")

    mineWindow.mainloop()

def Main():
    WindowCreator()

Main()