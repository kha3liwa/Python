from tkinter import *
from tkinter import ttk
win=Tk()
win.geometry('960x500+100+100')
win.resizable(0,0) # منع التحريك 
win.configure(bg='#d9d9d9')
khat=font=('arial',12,'bold')
khat1=font=('arial',40,'bold')
khat2=font=('arial',90,'bold')
var = IntVar()
#----------------------- code ------------------------
def zakat():
    try:
        label_1.configure(text='الرجاء ادخال اي قيمة ذهب بالجرام:',fg='green')
        lab.configure(fg='black')
        global zaka
        mony=float(en.get())
        ayar=var.get()
        zaka=float(mony*ayar/24) 
        label_2.configure(text=zaka)   
    except :# Exception:
        label_1.configure(text=" الرجاء ادخال اي قيمة ذهب بالجرام:->  ",fg='red')
        lab.configure(fg='red')
# -------------- Designer -----------------------------
ntb = ttk.Notebook(win)
ntb.grid()

fm1 = Frame(ntb)
fm2 = Frame(ntb)
fm3 = Frame(ntb)
ntb.add(fm1, text='frame 1')

#-------------- Combobox ------------------------------
cb = ttk.Combobox(fm1,values=(18,21,24),textvariable=var,font=khat)
cb.grid(row=6,column=1)
lab=Label(fm1,text="اختر العيار للذهب")
lab.grid(row=6,column=2)
# ------------- label Designer ------------------------
label_1 = Label(fm1,text='الرجاء ادخال اي قيمة بالجرام:',
               bg='#d9d9d9',
               fg='green',
               font=khat                
               )
label_1.grid(row=5,column=0)
# ------------- Entry Designer ------------------------
en=Entry(fm1,bg='cyan',bd=9,relief='groove',cursor='heart',
         font=khat,
         fg='black',
         justify='left',
         width=19,
         selectbackground='pink',
         selectforeground='red'
         )
en.grid(row=5,column=1)
label_2 = Label(fm1,text='<.....>',
               bg='#d9d9d9',
               fg='lime',
               font=khat2,
               state='disabled'
               )
label_2.grid(row=8,column=1)

showButton = Button(fm1, text="اظهر نصابه ",font=khat1,
                    fg='grey',bg='powder blue',command=zakat)
showButton.grid(row=7,column=0)

win.mainloop()
