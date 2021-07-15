from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=10)
e.grid(row=0,column=0,columnspan=3,padx=5,pady=5)

#defined function for button
def buttonclick():
    return

#Buttons for numbers
button_1 = Button(root, text="1",padx=35,pady=20,command=buttonclick)
button_2 = Button(root, text="2",padx=35,pady=20,command=buttonclick)
button_3 = Button(root, text="3",padx=35,pady=20,command=buttonclick)
button_4 = Button(root, text="4",padx=35,pady=20,command=buttonclick)
button_5 = Button(root, text="5",padx=35,pady=20,command=buttonclick)
button_6 = Button(root, text="6",padx=35,pady=20,command=buttonclick)
button_7 = Button(root, text="7",padx=35,pady=20,command=buttonclick)
button_8 = Button(root, text="8",padx=35,pady=20,command=buttonclick)
button_9 = Button(root, text="9",padx=35,pady=20,command=buttonclick)
button_0 = Button(root, text="0",padx=35,pady=20,command=buttonclick)


#buttons for operations
plus = Button(root,text="+",padx=35,pady=20,command=buttonclick)
minus = Button(root,text="-",padx=35,pady=20,command=buttonclick)
product = Button(root,text="*",padx=35,pady=20,command=buttonclick)
clear = Button(root,text="C",padx=35,pady=20,command=buttonclick)
equal = Button(root,text="=",padx=35,pady=20,command=buttonclick)
divide = Button(root,text="/",padx=35,pady=20,command=buttonclick)

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