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
        label_1.configure(text='الرجاء ادخال اي قيمة بالجرام:',fg='green')
        lab.configure(fg='black')
        global zaka
        mony=float(en.get())
        ayar=var.get()
        zaka=float(mony*ayar/24) 
        label_2.configure(text=zaka)
        canvas0.configure(bg='#d9d9d9')
    except :# Exception:
        label_1.configure(text=" الرجاء ادخال اي قيمة بالجرام:->  ",fg='red')
        lab.configure(fg='red')
        canvas0.configure(bg='red')
# -------------- Designer -----------------------------
canvas0 = Canvas(win,bg='#AAAAFF')
canvas0.place( x=20,y=20,width = 930, height = 460 )

canvas1 = Canvas(canvas0,bg='#AAAAFF')
canvas1.place( x=15,y=5,width = 900, height = 450 )

#-------------- Combobox ------------------------------
cb = ttk.Combobox(canvas1,font=khat,values=(18,21,24),textvariable=var)
cb.grid(row=7,column=1)
lab=Label(canvas1,text="اختر العيار للذهب",font=khat)
lab.grid(row=7,column=2)
# ------------- label Designer ------------------------
label_1 = Label(canvas1,text='الرجاء ادخال اي قيمة بالجرام:',
               bg='#d9d9d9',
               fg='green',
               font=khat                
               )
label_1.grid(row=6,column=2)
# ------------- Entry Designer ------------------------
en=Entry(canvas1,bg='cyan',bd=6,relief='groove',cursor='heart',
         font=khat,
         fg='black',
         justify='left',
         width=20,
         selectbackground='pink',
         selectforeground='red'
         )
en.grid(row=6,column=1)
label_2 = Label(canvas1,text='<.....>',
               bg='#AAAAFF',
               fg='lime',
               font=khat2,
               state='disabled'
               )
label_2.grid(row=8,column=1)

showButton = Button(canvas1, text="اظهر نصابه ",font=('arial',25,'bold'),
                    fg='grey',bg='powder blue',command=zakat)
showButton.grid(row=0,column=0)

win.mainloop()
