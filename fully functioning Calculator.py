from sys import flags
from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=10)
e.grid(row=0,column=0,columnspan=3,padx=5,pady=5)

#defined function for button
def buttonclick(num):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(num))
    return


def clearbutton():
    e.delete(0,END)
    return

def add():
    firstnum = e.get()
    global f_num
    global flag
    flag = "addition"
    f_num = int(firstnum)
    e.delete(0,END)


def subtract():
    firstnum = e.get()
    global f_num
    global flag
    flag = "subtract"
    f_num = int(firstnum)
    e.delete(0,END)


def product():
    firstnum = e.get()
    global f_num
    global flag
    flag = "product"
    f_num = int(firstnum)
    e.delete(0,END)


def divide():
    firstnum = e.get()
    global f_num
    global flag
    flag = "divide"
    f_num = int(firstnum)
    e.delete(0,END)


def equal():
    secondnum = e.get()
    e.delete(0,END)
    if(flag=="addition"):
        e.insert(0, f_num + int(secondnum))
    if(flag=="subtract"):
        e.insert(0,f_num - int(secondnum))
    if(flag=="product"):
        e.insert(0, f_num * int(secondnum))
    if(flag=="divide"):
        e.insert(0,f_num / int(secondnum))
#Buttons for numbers
button_1 = Button(root, text="1",padx=35,pady=20,command=lambda: buttonclick(1))
button_2 = Button(root, text="2",padx=35,pady=20,command=lambda: buttonclick(2))
button_3 = Button(root, text="3",padx=35,pady=20,command=lambda: buttonclick(3))
button_4 = Button(root, text="4",padx=35,pady=20,command=lambda: buttonclick(4))
button_5 = Button(root, text="5",padx=35,pady=20,command=lambda: buttonclick(5))
button_6 = Button(root, text="6",padx=35,pady=20,command=lambda: buttonclick(6))
button_7 = Button(root, text="7",padx=35,pady=20,command=lambda: buttonclick(7))
button_8 = Button(root, text="8",padx=35,pady=20,command=lambda: buttonclick(8))
button_9 = Button(root, text="9",padx=35,pady=20,command=lambda: buttonclick(9))
button_0 = Button(root, text="0",padx=35,pady=20,command=lambda: buttonclick(0))


#buttons for operations
plus = Button(root,text="+",padx=35,pady=20,command=add)
minus = Button(root,text="-",padx=35,pady=20,command=subtract)
product = Button(root,text="*",padx=35,pady=20,command=product)
clear = Button(root,text="C",padx=35,pady=20,command=clearbutton)
equal = Button(root,text="=",padx=35,pady=20,command=equal)
divide = Button(root,text="/",padx=35,pady=20,command=divide)

#placing buttons for numbers

button_1.grid(row=5,column=0)
button_2.grid(row=5,column=1)
button_3.grid(row=5,column=2)
button_4.grid(row=4,column=0)
button_5.grid(row=4,column=1)
button_6.grid(row=4,column=2)
button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_0.grid(row=6,column=1)



#placing buttons for operations
plus.grid(row=5,column=3)
minus.grid(row=4,column=3)
product.grid(row=3,column=3)
equal.grid(row=6,column=3)
clear.grid(row=6,column=0)
divide.grid(row=6,column=2)
root.mainloop()