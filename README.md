# TheAmateurs
Project 1 Calculator Second Semester S.Y. 2020-2021

from tkinter import*

#GRAPHIC CODE

cal = Tk()

cal.title("TheAmateurs' Calculator")

operator =""

text_input = StringVar()

#upper part of calculator where text is displayed 

txtDisplay = Entry(cal, font=("arial", 20, "bold"), textvariable=text_input, bd=

30, insertwidth=4, bg= "pink", justify="right").grid(columnspan=4)

#keypad of calculator

#row number 1

btn7= Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),

text="7", bg="pink", command=lambda:btnClick(7)).grid(row=1, column=1)

btn8= Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),

text="8", bg="pink", command=lambda:btnClick(8)).grid(row=1, column=2)

btn9= Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),

text="9", bg="pink", command=lambda:btnClick(9)).grid(row=1, column=3)

clear= Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),

text="C", bg="pink").grid(row=1, column=4)

#row number 2

btn4= Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),

text="4", bg="pink", command=lambda:btnClick(4)).grid(row=2, column=1)

btn5= Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),

text="5", bg="pink", command=lambda:btnClick(5)).grid(row=2, column=2)

btn6= Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),

text="6", bg="pink", command=lambda:btnClick(6)).grid(row=2, column=3)

dividesign= Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="%", bg="pink",command=lambda:btnClick("/")).grid(row=2,column=4)

#row number 3

btn1= Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),

text="1", bg="pink", command=lambda:btnClick(1)).grid(row=3, column=1)

btn2= Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),

text="2", bg="pink", command=lambda:btnClick(2)).grid(row=3, column=2)

btn3= Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),

text="3", bg="pink", command=lambda:btnClick(3)).grid(row=3, column=3)

minussign= Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),

text="-", bg="pink", command=lambda:btnClick("-")).grid(row=3, column=4)

#row number 4

btn0= Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),

text="0", bg="pink", command=lambda:btnClick(0)).grid(row=4, column=1)

dotsign= Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),

text=".", bg="pink",command=lambda:btnClick(".")).grid(row=4, column=2)

timessign= Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),

text="x", bg="pink", command=lambda:btnClick("x")).grid(row=4, column=3)

equalsign= Button(cal, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),

text="=", bg="pink").grid(row=4, column=4)

cal.mainloop()

#trialkopalangto
