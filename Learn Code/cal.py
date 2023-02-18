from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()

GUI.geometry('500x300')
GUI.title('โปรแกรมจัดการ Layout')

L1 = Label(GUI,text ='กรอกจำนวนกุ้ง (กิโลกรัม)',font=('Angsana New',25))
L1.pack()

v_kilo = StringVar()

E1 = ttk.Entry(GUI, textvariable = v_kilo, width = 10,justify='right',font=('impact', 30))
E1.pack(pady=20)

def Calc():
    print('กำลังคิดราคา....รอสักครู่')
    kilo = float(v_kilo.get())
    print(kilo*10)
    messagebox.showinfo('รวมราคาทั้งหมด',f'ลูกค้าต้องต้องจ่ายเงินทั้งหมด: {kilo*299:.2f}')

B1 = ttk.Button(GUI, text ='คำนวณราคา',command = Calc)
B1.pack(ipadx=40,ipady=30)

E1.bind('<Return>', Calc)


GUI.mainloop()
