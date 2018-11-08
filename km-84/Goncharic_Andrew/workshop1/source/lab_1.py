import re
# -*- coding: utf-8 -*-
# """- номер варіанта і повідомлення про призначення програми;
# - прізвище та ініціали автора програми, групу;
# - інформаційні повідомлення про необхідність введення даних;
# - повідомлення з результатами, отриманими в ході роботи програми; при
# """
print('Лабораторна робота № 1')
print('Варіант № 6')
print('Автор - Гончарик Андрій Валентинович КМ-84')

#function get_num take text for derivation to console and return real number
#if user to press symbol the program to return error and call
#For quit program press enter or space enter

def get_numb(text="",input_str="",qunty=1,format_=float):
    if qunty == 1:
        while not re.match(r'^[+-]?\d{0,}\.?\d+$',input_str):
            # use construction try, except  for
            input_str = input('Enter the value {0} or press <Enter> for quit: '.format(text))  # RETURN TEXT DATA

            if input_str == "" or input_str == " " or len(input_str) <= 0 or 'exit' in input_str:
                exit()

        return format_(input_str)
    else:
        input_str = input('Enter the value {0} or press <Enter> for quit: '.format(text)).split()

# function tr_temp return calculated temperature the fahrenheit from celsius
def tr_temp(celsius):
    return celsius*1.8+32




# Find max value  assign this value for any element
# If values equivalent the return 0,0
def rechange_numb(a,b):
    #a,b = tuple(map(lambda x: get_numb(text="value {0} ".format(x)), ["a", "b"])))
    try:
        assert a == b # assert that <a> equivalent <b>
        return 0,0
    # if <a> not equivalent <b> find max value
    except:
        max_ = max([a,b])
        return max_, max_


# question 3
# function func_y return
def func_y(x):
    if x <= 7:
        y =  3*x-9
    elif x > 7 :
        y = round(1/(x**2-4),2)
    else:
        y = None
    return y


def select_function(func='tr_temp'):
    if func == "tr_temp":
        return tr_temp(celsius=get_numb(text="of celsius temperature"))


    elif func == "rechange_numb":
        return rechange_numb(a=get_numb(text="a"),
                       b=get_numb(text="b")
                        )
    elif func == "func_y":
        return func_y(x=get_numb("x"))

    else:
        return None
