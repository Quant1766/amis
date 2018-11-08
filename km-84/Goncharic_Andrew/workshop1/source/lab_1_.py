import re


def get_float(input_str="",text="", format_=float):
    while not re.match(r'^[+-]?\d{0,}\.?\d+$', input_str):
        # use construction try, except  for
        input_str = input('Enter the value {0}: '.format(text))

        if input_str == "" or input_str == " " or len(input_str) <= 0 or 'exit' in input_str:
            exit()

    return format_(input_str)



def division(a,b):
    return a/b

