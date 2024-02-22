from tkinter import *
import mysql.connector
win =Tk()
win.config(bg="LightSeaGreen")
win.state("zoomed")
def MyDBConnection():
    dbcon=mysql.connector.connect(
    host="192.168.1.240",
    user="AIBATCH01",
    password="AI@123",
    database="ai_komathi"

)
    return dbcon
def insertvalues():
    Std_name=tbstd_name.get ()
    Tamil=tbtamil.get()
    English=tbenglish.get()
    Maths=tbmaths.get()
    Science=tbscience.get()
    Social=tbsocial.get()
    e_con=MyDBConnection()
    result=e_con.cursor()


    statement="insert into std_mark(Std_name,Tamil,English,Maths,Science,Social)value(%s,%s,%s,%s,%s,%s);"
    valuepass=(Std_name,Tamil,English,Maths,Science,Social)
    result.execute(statement,valuepass)
    print(result.rowcount,"row inserted")
    e_con.commit()

def updatevalues():
    Std_name=tbstd_name.get ()
    
    



std_name0msg=Label(win,text="Std_Name")
std_name0msg.grid(row=0,column=3,padx=200,pady=20)

tamil1msg=Label(win,text="Tamil:")
tamil1msg.grid(row=1,column=3,padx=200,pady=20)

english1msg=Label(win,text="English:")
english1msg.grid(row=2,column=3,padx=200,pady=20)

mathsl1msg=Label(win,text="maths:")
mathsl1msg.grid(row=3,column=3,padx=200,pady=20)

sciencel1msg=Label(win,text="science:")
sciencel1msg.grid(row=4,column=3,padx=200,pady=20)

sociall1msg=Label(win,text="social:")
sociall1msg.grid(row=5,column=3,padx=200,pady=20)

tbstd_name=Entry(win,width=60)
tbstd_name.grid(row=0,column=20)

tbtamil=Entry(win,width=60)
tbtamil.grid(row=1,column=20)

tbenglish=Entry(win,width=60)
tbenglish.grid(row=2,column=20)

tbmaths=Entry(win,width=60)
tbmaths.grid(row=3,column=20)

tbscience=Entry(win,width=60)
tbscience.grid(row=4,column=20)

tbsocial=Entry(win,width=60)
tbsocial.grid(row=5,column=20)

btnAdd=Button(win,text="INSERT",command=insertvalues,bg="Hotpink")
btnAdd.grid(row=9, column=22,padx=20,pady=20)

btnAdd=Button(win,text="UPDATE",bg="Hotpink")
btnAdd.grid(row=9, column=23,padx=20,pady=20)

btnAdd=Button(win,text="DELETE",bg="Hotpink")
btnAdd.grid(row=9, column=24,padx=20,pady=20)

btnAdd=Button(win,text="SUBMITE",bg="Hotpink")
btnAdd.grid(row=9, column=25,padx=20,pady=20)

win.mainloop()