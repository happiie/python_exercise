
#Create calculator for area of shape

from math import pi

while True:

    op = input("""

Area Calculator for Basic Shapes
================================

    1. Square
    2. Rectangle
    3. Triangle
    4. Circle

Choose a shape [1-4] that you want calculate its area: """)

    if op=='1':
        x = float(input("\nEnter length of a sided : "))
        z=x*x
        print("Area of square is %.1f" % (z))

    elif op=='2':
        x = float(input('\nEnter length : '))
        y = float(input('Enter base : '))
        z=x*y
        print("Area of rectangle is %.1f" % (z))

    elif op=='3':
        x = input('''
Enter Height : ''')
        y = input('Enter Base : ')
        z=(int(x)*int(y))/2
        print("Area of triangle is ", z)


    elif op=='4':
        x = float(input('\nEnter radius : '))
        z=x*x*pi
        print("Area of circle is %.1f" % (z))

    else:
        print('''
*** Sorry. Wrong input.''')
