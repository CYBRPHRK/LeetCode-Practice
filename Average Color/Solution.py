# Python 3.9.4 IDLE
# Install colour library using 'pip install colour'. I am using this library for color conversion.
from colour import Color

'''
Name        : average_color
Description : A function that takes 2 colors as arguments and returns the average color.
    * The hexadecimal strings represent colors in RGB, much like in CSS.
    * The average color is to be determined by taking the arithmetic mean for each component: red, green and blue.
Parameters  : Two 6-digit hexadecimal strings (Non-validated).
Returns     : value should be a 6-digit hexadecimal string.
'''

def average_color(color1, color2):
    # Taking the arithmetic mean for each component: red, green and blue
    mean_red = (color1.red + color2.red)/2
    mean_green = (color1.green + color2.green)/2
    mean_blue = (color1.blue + color2.blue)/2

    # creating a new color with the values procured above
    resulting_color = Color(rgb=(mean_red, mean_green, mean_blue))
    return resulting_color.hex_l

# Testing
color1 = ["#882d6d", "#dd3c19", "#153ab2"]
color2 = ["#64a5a9", "#43b215", "#30b215"]
for i in range (0,3):
    print (average_color(Color(color1[i]), Color(color2[i])))
