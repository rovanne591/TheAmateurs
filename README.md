from tkinter import*


#Initiate new window object
cal = Tk()
cal.title("TheAmateurs' Calculator")


#default value of answer button
default_answer = "No record"

#variable to be displayed in the calculator
text_input = StringVar()


#this holds all user inputs
user_input = []
display = ""

#make the window not resizable
cal.resizable(False, False)
cal["bg"]="lightgrey"
