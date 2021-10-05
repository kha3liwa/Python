import tkinter as tk
import datetime

dt = datetime.datetime.now()

root = tk.Tk()
root.geometry('450x370')
bgcolor = '#AAAAFF'
actbgcolor = '#CCCCFF'
fgcolor = '#884400'
root.title("Find Birth Year or your age")
khat = font = ("Time", 22, "bold")

var = tk.StringVar()
# ---------------- coding --------------
def values():
    try:
        thisyear = dt.strftime('%Y')
        sta = entry1.get()
        year_you = int(thisyear)-int(sta)
        hi = str("Your birth year is :  , [OR] \n your age is : \n") + str(year_you)
        label2.configure(text=hi, bg='powder blue', fg='black')
    except:
        err="------- Error Entry ---------\n ---Most be int number entry--- "
        label2.configure(fg='red', text=err)
def clickexit():
    root.destroy()
def newtype():
    label2.configure(bg=bgcolor)
    label2.configure(text="")
    var.set("")


# --------------- designer ---------------
canvas1 = tk.Canvas(root, bg=bgcolor)
canvas1.place(x=15, y=5, width=420, height=350)

label = tk.Label(root, text="Find your birth year \n ابحث عن سنة ميلادك", bg=bgcolor, fg='blue', font=khat)
canvas1.create_window(250, 40, window=label)

label1 = tk.Label(root, bg=bgcolor, text='Type your Age or year:\n  اكتب عمرك او سنة ميلادك: ')
canvas1.create_window(80, 100, window=label1)

entry1 = tk.Entry(root, textvariable=var)
canvas1.create_window(220, 100, window=entry1)

button1 = tk.Button(root, text='push here ', bd=10, command=values, bg='orange')
canvas1.create_window(200, 150, window=button1)

label2 = tk.Label(canvas1, text=' ', bg=bgcolor, font=('Market', 14, 'bold'))
canvas1.create_window(200, 220, window=label2)

bt1 = tk.Button(canvas1, text="Exit", fg='red', bg='orange', bd=10, command=clickexit)
bt1.place(x=330, y=100)
bt2 = tk.Button(canvas1, text="clear", bg='orange', bd=8, command=newtype)
bt2.place(x=330, y=150)

var.set(" ")
root.mainloop()
