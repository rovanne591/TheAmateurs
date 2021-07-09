LOGIC BRANCH

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

