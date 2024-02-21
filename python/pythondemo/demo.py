from tkinter import *

app=Tk()
app.title("my first python gui app")
app.geometry("500x500+500+100")
app.config(bg="gray")
# app.state("zoomed")

def clickresult():
    a=10
    b=10
    c=a+b
    lblTitle.config(text=c, fg="red")


lblTitle=Label(app,text="Arithmatic Operations")
lblTitle.grid(row=0, column=1, padx=40, pady=40)

inputbox1=Entry(app,width=30)
inputbox1.grid(row=0, column=2)


lblTitle1=Label(app,text="Arithmatic Operations")
lblTitle1.grid(row=1, column=1, padx=40, pady=40)

inputbox2=Entry(app,width=30)
inputbox2.grid(row=1, column=2)


clickme=Button(app, text="addition", command=clickresult, )
clickme.grid(row=2, column=8, padx=40, pady=40)



app.mainloop()

# def clickresult():
#     a=10
#     b=10

#     print("added value is ", a+b)

# clickresult()
