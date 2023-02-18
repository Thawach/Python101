from tkinter import *
from tkinter import ttk
from tkinter import messagebox

gui = Tk()

gui.title('โปรแกรมบันทึกข้อมูล')

gui.geometry('800x600')

L1 = Label(gui, text='Program Money', font=('Angsana New',30), fg='Blue')
L1.pack()
##----------------------------##
def Button2():
    text = 'Money in account are 300 Bath' 
    messagebox.showinfo('Money',text)

FB1 = LabelFrame(gui, text ='Money')
FB1.place(x=100,y=100)
B2 = ttk.Button(FB1, text = 'How many money do you have?', command = Button2)
B2.pack(ipadx=20, ipady=20, padx = 30, pady = 20)

##----------------------------##

##----------------------------##
def Button3():
    text = 'Money in account are 300 Bath' 
    messagebox.showinfo('Money',text)

FB3 = LabelFrame(gui, text ='Study')
FB3.place(x=100,y=300)
B3 = ttk.Button(FB3, text = 'What do you study today?', command = Button2)
B3.pack(ipadx=20, ipady=20, padx = 30, pady = 20)

##----------------------------##


##----------------------------##
def Button4():
    text = 'Money in account are 300 Bath' 
    messagebox.showinfo('Money',text)

FB4 = LabelFrame(gui, text ='Hobby')
FB4.place(x=400,y=100)
B4 = ttk.Button(FB4, text = 'What do you do after study?', command = Button2)
B4.pack(ipadx=20, ipady=20, padx = 30, pady = 20)

##----------------------------##

##----------------------------##
def Butto5():
    text = 'Money in account are 300 Bath' 
    messagebox.showinfo('Money',text)

FB5 = LabelFrame(gui, text ='Plan')
FB5.place(x=400,y=300)
B5 = ttk.Button(FB5, text = 'What is you plan for tomorrow?', command = Button2)
B5.pack(ipadx=20, ipady=20, padx = 30, pady = 20)

##----------------------------##

gui.mainloop()
