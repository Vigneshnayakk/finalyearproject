from tkinter import *
from tkcalendar import Calendar, DateEntry
from tkinter import filedialog
from tkinter import messagebox
import mysql.connector
#from databaseconnect import *
import os
def create():
    def clearall():
        entry_1.delete(0,END)
        entry_2.delete(0,END)
        entry_3.delete(0,END)
        entry_4.delete(0,END)
        entry_9.delete(0,END)
        entry_11.delete(0,END)

    def browse():
        currdir = os.getcwd()
        tempdir = filedialog.askopenfilename(parent=root2, initialdir="/home/vignesh/Desktop/",title='Please select a directory',filetypes=(("Excel files","*.xls"),("All files","*.*")))
        if len(tempdir) > 0:
            entry_11.insert(10,tempdir)

    def createdata():
        user_id=entry_1.get()
        print(user_id)
        full_name=entry_2.get()
        em=entry_3.get()
        mob=entry_4.get()
        #gen=var.get()
        #print(gen)
        d=cal.get()
        print(d)
        a=entry_9.get()
        #an=ana.get()
        br=entry_11.get()
        #tablename=str(fullname)+str(user_id)
        config={
        'user':'root',
        'password':'root',
        'host':'localhost',
        'database':'project',
        'raise_on_warnings':True,
        }
        cn=mysql.connector.connect(**config)
        print("connected to database")
        cr=cn.cursor()

        s='''create table if not exists %s(
        userid char(5) primary key,
        fullname char(30),
        email char(50),
        mobile char(15),
        gender char(8),
        date char(10),
        age char(5),
        analysis char(4),
        brdata char(50)
        )''' %(full_name+user_id)
        s1='''INSERT INTO %s (userid,fullname,email,mobile,date,age,brdata) values('%s','%s','%s','%s','%s','%s','%s')''' %((full_name+user_id),user_id,full_name,em,mob,d,a,br)

        try:
            cr.execute(s)

        except mysql.connector.Error:
            messagebox.showwarning("WARNING","Table already exists",parent=root2)

        else:
            messagebox.showinfo("SUCCESS","Table created",parent=root2)
            try:
                cr.execute(s1)
            except mysql.connector.Error:
                messagebox.showwarning("WARNING","Data insertion failed",parent=root2)
                cn.rollback()
            else:
                cn.commit()
                messagebox.showinfo("SUCCESS","Data inserted into Database",parent=root2)
        cn.close()


    var=StringVar()
    ana=StringVar()

    root2 = Tk()
    root2.geometry('680x600')
    root2.title("Create New")


    label_1 = Label(root2, text="User ID",width=20,anchor="w",font=("bold", 10))
    label_1.place(x=80,y=40)

    entry_1 = Entry(root2)
    entry_1.place(x=240,y=40)

    label_2 = Label(root2,text="FullName",width=20,anchor="w",font=("bold", 10))
    label_2.place(x=80,y=90)

    entry_2 = Entry(root2)
    entry_2.place(x=240,y=90)

    label_3 = Label(root2,text="Email",width=20,anchor="w",font=("bold", 10))
    label_3.place(x=80,y=140)

    entry_3 = Entry(root2)
    entry_3.place(x=240,y=140)

    label_4 = Label(root2, text="Mobile Number",width=20,anchor="w",font=("bold", 10))
    label_4.place(x=80,y=190)

    entry_4 = Entry(root2)
    entry_4.place(x=240,y=190)

    label_5 = Label(root2, text="Gender",width=20,anchor="w",font=("bold", 10))
    label_5.place(x=80,y=240)

    Radiobutton(root2, text="Male ",padx=20 ,variable=var,value="MALE").place(x=235,y=240)
    Radiobutton(root2, text="Female", padx=20,variable=var,value="FEMALE").place(x=235,y=270)

    label_6 = Label(root2, text="DOB",width=20,anchor="w",font=("bold", 10))
    label_6.place(x=80,y=320)
    cal = DateEntry(root2, width=12, background='darkblue',foreground='white', borderwidth=2)
    cal.place(x=240,y=320)


    label_9 = Label(root2, text="Age",width=20,anchor="w",font=("bold", 10))
    label_9.place(x=80,y=370)

    entry_9 = Entry(root2)
    entry_9.place(x=240,y=370)

    label_10= Label(root2, text="Analysis",width=20,anchor="w",font=("bold", 10))
    label_10.place(x=80,y=420)

    Radiobutton(root2, text="X",padx = 5,variable=ana, value="X").place(x=240,y=420)
    Radiobutton(root2, text="Y",padx = 5,variable=ana, value="Y").place(x=300,y=420)
    Radiobutton(root2, text="Z",padx = 5,variable=ana, value="Z").place(x=360,y=420)

    label_11= Label(root2, text="Select File",width=20,anchor="w",font=("bold", 10))
    label_11.place(x=80,y=470)

    entry_11 = Entry(root2)
    entry_11.place(x=240,y=470)

    browse1=Button(root2,text='Browse',width=7,command=browse)
    browse1.place(x=420,y=470)

    submit1=Button(root2,text='Submit',width=20,bg='brown',activebackground='green',fg='white',command=createdata)
    submit1.place(x=80,y=520)
    clear_a=Button(root2,text='Clear all',width=20,bg='brown',activebackground="grey",fg='white',command=clearall)
    clear_a.place(x=240,y=520)
    quit_1=Button(root2,text='Quit',width=20,bg='brown',activebackground='red',fg='white',command=root2.destroy)
    quit_1.place(x=420,y=520)

    root2.mainloop()
