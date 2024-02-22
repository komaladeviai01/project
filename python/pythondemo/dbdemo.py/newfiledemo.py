import tkinter as tk
#from tkinter import *
win=tk.Tk()
win.title("computer security")
win.geometry("600x600")
#win.state("zoomed")

menubar=tk.Menu(win)
filemenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu,  underline=0)
filemenu.add_command(label="New", underline=0,   accelerator="ctrl+N")
filemenu.add_command(label="New window", underline=3,   accelerator="ctrl+W")
filemenu.add_command(label="Open", underline=0,   accelerator="ctrl+O")
filemenu.add_command(label="Save", underline=0,  accelerator="ctrl+S")
filemenu.add_command(label="Save as", underline=0,  accelerator="ctrl+A")
filemenu.add_separator()
filemenu.add_command(label="Pagesetup", underline=0)
filemenu.add_command(label="print", underline=0,  accelerator="ctrl+P")
filemenu.add_separator()
def Exitwindow():
    win.destroy()
filemenu.add_command(label="Exit", underline=0,command=Exitwindow,accelerator="ctrl+Q")


Editmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit", menu=Editmenu, underline=0)
Editmenu.add_cascade(label="undo", underline=0,  accelerator="ctrl+U")



formatmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="formate", menu=formatmenu,underline=0)

Viewmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="View", menu=Viewmenu,underline=0)

Helpmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help", menu=Helpmenu,underline=0)

win.config(menu=menubar)
win.mainloop()
