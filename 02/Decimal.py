#Created by:Nicholas Brean
#Created On:Nov 2017
#This program moves tge decimal place of a number


import ui


def procedure(input_number):
    #long number they inout 
    input_number = float(view['number_textfield'].text)
    #how many numbers they move
    decimal_point_moving = float(view['moving_decimal_point_textfield'].text)
    #Calculate moving the decimal point 
    output_number = input_number/10**decimal_point_moving
    #output after moving the decimal
    view['answer_label'].text = 'the nunber is: ' + str(output_number)
view = ui.load_view()
view.present('sheet')
