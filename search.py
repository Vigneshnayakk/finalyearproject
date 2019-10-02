from tkinter import *
from tkcalendar import Calendar, DateEntry

def search():
    def clear():
        text_userid.delete(0,END)
    root1=Tk()
    root1.title("Search record")
    labelfont = ('times', 13, 'bold')
    root1.geometry("500x500")
    label_userid=Label(root1,text="Enter ID")
    buttonid=Button(root1,text="Search",bg='brown',fg='white',activebackground="green")
    buttonclear=Button(root1,text="Clear",bg='brown',fg='white',activebackground="grey",command=clear)
    buttonquit=Button(root1,text="Quit",bg='brown',fg='white',activebackground="red",command=root1.destroy)
    text_userid=Entry(root1)
    label_userid.place(x=80,y=135)
    label_userid.config(font=labelfont)
    text_userid.place(x=200,y=125,width=220,height=40)
    buttonid.place(x=80,y=210,width=100,height=50)
    buttonclear.place(x=200,y=210,width=100,height=50)
    buttonquit.place(x=320,y=210,width=100,height=50)
    root1.mainloop()
