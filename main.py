from tkinter import *
from create import *
from search import *

root=Tk()
root.title("Novel blood pressure")
root.geometry("500x500")
labelfont = ('times', 15, 'bold')
photo1= PhotoImage(file = r"/home/vignesh/Desktop/modules/2.png")
photo2= PhotoImage(file = r"/home/vignesh/Desktop/modules/download.png")
photoimage1 = photo1.subsample(7,7)
photoimage2 = photo2.subsample(7,7)
label1=Label(root,text="Select option:")
button1=Button(root,text="Search record",font=('Helvetica', '9'),image=photoimage2,compound=LEFT,command=search)
button2=Button(root,text="Create New",font=('Helvetica', '9'),image=photoimage1,compound=LEFT,command=create)
label1.config(font=labelfont)
label1.place(x=80,y=10,width=300,height=100)
button1.place(x=60,y=110,width=130,height=50)
button2.place(x=200,y=110,width=120,height=50)
root.mainloop()
