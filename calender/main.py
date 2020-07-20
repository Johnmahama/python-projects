from tkinter import *
import calendar


#initialization
cal = Tk()
cal.title("Calender")
cal.geometry("250x240")
cal.resizable(False,False)

#show fucntion
def show():
    a=spin1.get()
    b = spin2.get()
    a = int(a)
    b = int(b)
    cale = calendar.month(b, a)
    txt.delete(0.0, END)
    txt.insert(INSERT, cale)

#graphical user interfaces

lbl1= Label(cal,text="Month",font=("aerial",9,'bold')).place(x=15,y=0)
spin1= Spinbox(cal,values=(1,2,3,4,5,6,7,8,9,10,11,12),width=4)
spin1.place(x=60,y=0)
lbl2 =Label(cal,text="Year",font=("arial",9,'bold')).place(x=115,y=0)
spin2=Spinbox(cal,from_=1980,to=2100,width=4)
spin2.place(x=150,y=0)
btn=Button(cal,text="Show",font=("arial",9,'bold'),command=show).place(x=100,y=30)
txt=Text(cal,width=24,height=8)
txt.place(x=20,y=57)


cal.mainloop()
