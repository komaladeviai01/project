import tkinter as tk
#from tkinter import *
win=tk.Tk()
win.title("computer security")
win.geometry("600x600")
#win.state("zoomed")

def Exitwindow():
    win.destroy()
menubar=tk.Menu(win)

filemenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu,  underline=0)
filemenu.add_command(label="New", underline=0,   accelerator="ctrl+N")
filemenu.add_command(label="New window", underline=3,   accelerator="ctrl+shift+N")
filemenu.add_command(label="Open", underline=0,   accelerator="ctrl+O")
filemenu.add_command(label="Save", underline=0,  accelerator="ctrl+S")
filemenu.add_command(label="Save as", underline=0,  accelerator="ctrl+shift+S")
filemenu.add_separator()
filemenu.add_command(label="Pagesetup", underline=0)
filemenu.add_command(label="print", underline=0,  accelerator="ctrl+P")
filemenu.add_separator()

filemenu.add_command(label="Exit", underline=0,command=Exitwindow,accelerator="ctrl+Q")

titleImageframe=tk.Frame(win,width=600,height=500,bg="black")
titleImageframe.pack(pady=200,fill="x")
lbltitleImage=tk.Label(titleImageframe,text="computer security")
lbltitleImage.pack(anchor="center")

Editmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit", menu=Editmenu, underline=0)
Editmenu.add_command(label="Undo", underline=0,  accelerator="ctrl+U")
Editmenu.add_command(label="Cut", underline=0,  accelerator="ctrl+X")
Editmenu.add_command(label="Paste", underline=0,  accelerator="ctrl+V")
Editmenu.add_command(label="Copy", underline=0,  accelerator="ctrl+C")
Editmenu.add_separator()
Editmenu.add_command(label="Select All", underline=0,  accelerator="ctrl+A")
Editmenu.add_command(label="Time/date", underline=0,  accelerator="F2")
Editmenu.add_separator()


formatmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="formate", menu=formatmenu,underline=0)
formatmenu.add_command(label="Word Wrab", underline=0)
formatmenu.add_command(label="Font..", underline=0)
formatmenu.add_separator()


Viewmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="View", menu=Viewmenu,underline=0)
submenulist=tk.Menu(menubar,tearoff=0)
submenulist.add_command(label="Zoom in")
submenulist.add_command(label="Zoom out")

Viewmenu.add_cascade(label="Zoom",menu=submenulist,underline=0)
Viewmenu.add_command(label="Status Bar",underline=0)

Helpmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help", menu=Helpmenu,underline=0)
Helpmenu.add_command(label="View",underline=0)
Helpmenu.add_command(label="Send Facebook",underline=0)
Helpmenu.add_separator()
Helpmenu.add_command(label="About Notepad",underline=0)


win.config(menu=menubar)
win.mainloop()
