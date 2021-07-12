class Calculator:
    def btnClick(self, value):
        global display
        global user_input

        #clear the textbox when clear btn is clicked
        if value == "clear":
            text_input.set("")
            user_input.clear()


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
    def evaluate(self, input):
        global answer
        global user_input
        global default_answer

        index = 0
        err_math = "Math Error"
        err_syntax = "Syntax Error"
        err_empty = "No record"


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

            #remove the spaces between each characters
            val_string = val_string.replace(" ", "")
            #change "x" to "*" for multiplication
            val_string = val_string.replace("x", "*")
            #change "÷" to "/"
            val_string = val_string.replace("÷", "/")
            #change "%" to "/100"
            val_string = val_string.replace("%", "/100")
            #change "ans" to data in default answer
            val_string = val_string.replace("ans", str(default_answer))



        #main logic part here
        #try the expression first
        try:
            #show the stored answer
            if val_string == "ans":
                text_input.set(default_answer)
                return default_answer
            #when the user keeps pressing the equals button after a calculation was made
            elif val_string == "":
                pass
            #raise an error for multiple "x" and "÷" button presses
            elif "invalid"  in val_string == True or val_string == "invalid":
                raise SyntaxError
            else:
                #evaluate the string
                answer = eval(val_string)
                #copy the calculated data for Ans button
                default_answer = answer
                
                #pass the answer to calculator display
                #and clear the user_input and val_string
                text_input.set(answer)
                user_input.clear()
                val_string = ""


                return answer

        #zero / zero error
        except ZeroDivisionError:
            text_input.set(err_math)
            user_input.clear()
            val_string = ""
            answer = 0
            default_answer = err_math

            return err_math
        
        #syntax error
        except SyntaxError:
            text_input.set(err_syntax)
            user_input.clear()
            val_string = ""

            default_answer = err_syntax
            return err_syntax

        #no data (when Ans button is clicked with no previous calculations made)
        except NameError:
            text_input.set(err_empty)
            user_input.clear()
            val_string = ""
            default_answer = err_empty
            return err_empty
        

        return default_answer