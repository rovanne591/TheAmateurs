# TheAmateurs
Project 1 Calculator Second Semester S.Y. 2020-2021

start the code for logic here!!

>>
# TheAmateurs
Project 1 Calculator Second Semester S.Y. 2020-2021

start the code for logic here!!

>>
#LOGIC

def btnClick(value):
global display
global user_input

#clear the textbox when clear btn is clicked
if value == "clear":
    text_input.set("")
    user_input.clear()
    print(user_input)
#delete the last character
elif value == "delete" and len(user_input) == 0:
    #to prevent IndexError
    pass
elif value == "delete":
    del user_input[-1]
    display = display[:-1]
    text_input.set(display)
#append to display
else:
    user_input.append(value)

    #removes the unneccessary spaces in display while the user enters the data
    display = ' '.join([str(elem) for elem in user_input])
    display = display.replace(" ", "")

    text_input.set(display)
#equal button function
def evaluate(input):
global answer
global user_input
global default_answer

index = 0
err_math = "Math Error"
err_syntax = "Syntax Error"


#scans for potential syntax errors due to trailing decimals
for x in user_input:
    #duplicate decimals [index must start at least 1 onwards or else IndexError results]
    if index > 0 and user_input[index] == user_input[index-1] == ".":
        text_input.set(err_syntax)

        #clear user_input
        user_input.clear()
        break
    else:
        pass
    index += 1

#convert user_input list as string
val_string = ' '.join([str(elem) for elem in user_input])

#preparation before parsing
for x in val_string:

    #make multiple "x" and "÷" button presses invalid
    val_string = val_string.replace("**", "invalid")
    val_string = val_string.replace("//", "invalid")
