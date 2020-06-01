from tkinter import *
from tkinter import ttk
win=Tk()
win.geometry('960x500+100+100')
win.resizable(0,0) # منع التحريك 
win.configure(bg='#d9d9d9')
khat=font=('arial',22,'bold')
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
#-------------- Combobox ------------------------------
cb = ttk.Combobox(win,values=(18,21,24),textvariable=var)
cb.grid(row=6,column=1)
lab=Label(win,text="اختر العيار للذهب")
lab.grid(row=6,column=2)
# ------------- label Designer ------------------------
label_1 = Label(win,text='الرجاء ادخال اي قيمة بالجرام:',
               bg='#d9d9d9',
               fg='green',
               font=khat                
               )
label_1.grid(row=5,column=0)
# ------------- Entry Designer ------------------------
en=Entry(win,bg='cyan',bd=6,relief='groove',cursor='heart',
         font=khat,
         fg='black',
         justify='left',
         width=20,
         selectbackground='pink',
         selectforeground='red'
         )
en.grid(row=5,column=1)
label_2 = Label(win,text='<.....>',
               bg='#d9d9d9',
               fg='lime',
               font=khat2,
               state='disabled'
               )
label_2.grid(row=8,column=1)

showButton = Button(win, text="اظهر نصابه ",font=khat1,
                    fg='grey',bg='powder blue',command=zakat)
showButton.grid(row=7,column=0)

win.mainloop()
