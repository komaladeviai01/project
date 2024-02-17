from tkinter import *
#app=Tk()
win=Tk()

#app.title("The first python change work")
#app.geometry("200x400+500+100")
#app.config(bg='red')



win.title("Arithmatic Operations")
win.geometry("500x500+500+100")
win.config(bg="lightseaGreen")
win.state("zoomed")

def addition():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    #print(a+b)
    c=a+b
    labelouptut.config(text=c)

def Subtraction():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    #print(a+b)
    c=a-b
    labelouptut.config(text=c)

def multipule():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    #print(a*b)
    c=a*b
    labelouptut.config(text=c)

def division():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    #print(a/b)
    c=a/b
    labelouptut.config(text=c)



def modules():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    #print(a/b)
    c=a%b
    labelouptut.config(text=c)


def exponentiation():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    #print(a/b)
    c=a**b
    labelouptut.config(text=c)




labelTitle=Label(win,text="Arithmatic Operations",font=("clarion",15))
labelTitle.grid(row=0,column=20,padx=200, pady=30)

label1msg=Label(win,text="Enter value a :")
label1msg.grid(row=1,column=20)

tbEntrya=Entry(win,width=60)
tbEntrya.grid(row=1,column=25)


label2msg=Label(win,text="Enter value b :")
label2msg.grid(row=2,column=20, pady=20)

tbEntryb=Entry(win,width=60)
tbEntryb.grid(row=2,column=25,pady=20)


labelouptut=Label(win,text="values:")
labelouptut.grid(row=3,column=30, pady=20)


btnAdd=Button(win,text="Addition", command=addition,bg="Hotpink")
btnAdd.grid(row=4, column=1)

btnSubtract=Button(win,text="Subtraction",command=Subtraction,bg="Hotpink")
btnSubtract.grid(row=4,column=2)

btnmultipule=Button(win,text="multipule",command=multipule,bg="Hotpink")
btnmultipule.grid(row=4,column=3)

btndivision=Button(win,text="division",command=division,bg="Hotpink")
btndivision.grid(row=4,column=4)

btndivision=Button(win,text="modules",command=modules,bg="Hotpink")
btndivision.grid(row=4,column=4)

btndivision=Button(win,text="exponentiation",command=exponentiation,bg="Hotpink")
btndivision.grid(row=4,column=5)


win.mainloop()