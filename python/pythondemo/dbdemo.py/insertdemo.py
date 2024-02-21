from tkinter import *
import mysql.connector

win=Tk()

win.title("Insert into Mysql DB Demo")
win.geometry("500x500")
win.state("zoomed")
class development:
    def __init__(self):

        frametop=Frame(win,bg="black",width=500,height=500,padx=30,pady=20)
        frametop.pack(side=TOP)
        btninsert=Button(frametop,text="Insert",command=self.frameleft).pack(padx=10,pady=10)
        
        btninsert=Button(frametop,text="update",command=self.rightFrame).pack(padx=10,pady=10)
        
        btninsert=Button(frametop,text="delete").pack(padx=10,pady=10)

        

    def frameleft(self):
        newtap=Tk()
        newtap.title("Insert into Mysql DB demo")
        newtap.geometry("500x500")
        
        frameleft=Frame(newtap,bg="red",width=500,height=500,padx=20,pady=20)
        frameleft.pack(side=LEFT)



    #frameright=Frame(win,bg="black",width=200,height=200)
    #frameright.pack(side=RIGHT)

        lbl_title_of_operation=Label(frameleft,text="Insert into Mysql DB Demo")
        lbl_title_of_operation.grid(row=0,columnspan=5)

        lblname=Label(frameleft,text="name")
        lblname.grid(row=1,column=1,padx=30,pady=20)

        lbltamil=Label(frameleft,text="Tamil")
        lbltamil.grid(row=2,column=1,padx=30,pady=20)

        newtap.mainloop()

    def rightFrame(self):

        neww=Tk()
        neww.title("update into Mysql DB demo")
        neww.geometry("500x500")

        frameright=Frame(neww,bg="blue",width=500,height=500,padx=30,pady=30)
        frameright.pack(side=RIGHT)

        lbl_title_of_operation1=Label(frameright,text="update into Mysql DB Demo")
        lbl_title_of_operation1.grid(row=0,columnspan=5)

        lblname=Label(frameright,text="name")
        lblname.grid(row=1,column=1,padx=30,pady=20)

        lbltamil=Label(frameright,text="Tamil")
        lbltamil.grid(row=2,column=1,padx=30,pady=20)

        neww.mainloop()        

        


run=development()


win.mainloop()
