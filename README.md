Initial Code/library BRANCH

from tkinter import*


#Initiate new window object
cal = Tk()
cal.title("TheAmateurs' Calculator")


#default value of answer button
default_answer = "No data"

#variable to be displayed in the calculator
text_input = StringVar()


#this holds all user inputs
user_input = []
display = ""

#make the window not resizable
cal.resizable(False, False)
cal["bg"]="lightgrey"

#USER INTERFACE BRANCH

#calculator display

txtDisplay = Entry(cal, font=("arial", 20, "bold"), textvariable=text_input, bd=

30, insertwidth=4, bg= "skyblue", justify="right", state=DISABLED, xscrollcommand='scrollbar').grid(columnspan=6)

#keypad of calculator

#row 1 (clear, del, percentage, divide)

clear= Button(cal, width=4, bd=8, fg="black", font=("arial", 20, "bold"),

text="C", bg="orange", command=lambda:btnClick("clear")).grid(row=1, column=1)

delete= Button(cal, width=4, bd=8, fg="black", font=("arial", 20, "bold"),

text="DEL", bg="orange", command=lambda:btnClick("delete")).grid(row=1, column=2)

percentage= Button(cal, width=4, bd=8, fg="black", font=("arial", 20, "bold"),

text="%", bg="orange", command=lambda:btnClick("%")).grid(row=1, column=3)

divide= Button(cal, width=4, bd=8, fg="white", font=("arial", 20, "bold"),

text="÷", bg="grey", command=lambda:btnClick("÷")).grid(row=1, column=4)

#row 2 (7,8,9, multiply)

btn7= Button(cal, width=4, bd=8, fg="white", font=("arial", 20, "bold"),

text="7", bg="black", command=lambda:btnClick(7)).grid(row=2, column=1)

btn8= Button(cal, width=4, bd=8, fg="white", font=("arial", 20, "bold"),

text="8", bg="black", command=lambda:btnClick(8)).grid(row=2, column=2)

btn9= Button(cal, width=4, bd=8, fg="white", font=("arial", 20, "bold"),

text="9", bg="black", command=lambda:btnClick(9)).grid(row=2, column=3)

multiply= Button(cal, width=4, bd=8, fg="white", font=("arial", 20, "bold"),

text="x", bg="grey", command=lambda:btnClick("x")).grid(row=2, column=4)

#row 3 (4,5,6, subtract)

btn4= Button(cal, width=4, bd=8, fg="white", font=("arial", 20, "bold"),

text="4", bg="black", command=lambda:btnClick(4)).grid(row=3, column=1)

btn5= Button(cal, width=4, bd=8, fg="white", font=("arial", 20, "bold"),

text="5", bg="black", command=lambda:btnClick(5)).grid(row=3, column=2)

btn6= Button(cal, width=4, bd=8, fg="white", font=("arial", 20, "bold"),

text="6", bg="black", command=lambda:btnClick(6)).grid(row=3, column=3)

subtract= Button(cal, width=4, bd=8, fg="white", font=("arial", 20, "bold"), 

text="-", bg="grey",command=lambda:btnClick("-")).grid(row=3,column=4)

#row 4 (1,2,3, add)

btn1= Button(cal, width=4, bd=8, fg="white", font=("arial", 20, "bold"),

text="1", bg="black", command=lambda:btnClick(1)).grid(row=4, column=1)

btn2= Button(cal, width=4, bd=8, fg="white", font=("arial", 20, "bold"),

text="2", bg="black", command=lambda:btnClick(2)).grid(row=4, column=2)

btn3= Button(cal, width=4, bd=8, fg="white", font=("arial", 20, "bold"),

text="3", bg="black", command=lambda:btnClick(3)).grid(row=4, column=3)

add= Button(cal, width=4, bd=8, fg="white", font=("arial", 20, "bold"),

text="+", bg="grey", command=lambda:btnClick("+")).grid(row=4, column=4)

#row 5 (0, decimal, equals)

answer= Button(cal, width=4, bd=8, fg="black", font=("arial", 20, "bold"),

text="Ans", bg="lightgreen", command=lambda:btnClick("ans")).grid(row=5, column=1)

btn0= Button(cal, width=4, bd=8, fg="white", font=("arial", 20, "bold"),

text="0", bg="black", command=lambda:btnClick(0)).grid(row=5, column=2)

decimal= Button(cal, width=4, bd=8, fg="white", font=("arial", 20, "bold"),

text=".", bg="black",command=lambda:btnClick(".")).grid(row=5, column=3)

equal= Button(cal, width=4, bd=8, fg="black", font=("arial", 20, "bold"),

text="=", bg="skyblue", command=lambda:evaluate(user_input)).grid(row=5, column=4)

cal.mainloop()
