from turtle import Turtle
from random import randint

print('Race On !!!')

force = Turtle()
force.shape('turtle')
force.color('red')

force.penup() #stop draw the line
force.goto(-100, 100) #move to coordinate
force.pendown() #ready to draw line

volt = Turtle()
volt.shape('turtle')
volt.color('blue')
volt.penup()
volt.goto(-100, 40)
volt.pendown()

power = Turtle()
power.shape('turtle')
power.color('yellow')
power.penup()
power.goto(-100, 70)
power.pendown()

ton = Turtle()
ton.shape('turtle')
ton.color('purple')
ton.penup()
ton.goto(-100, 10)
ton.pendown()

for go in range(30):
    force.forward(randint(0,20))
    ton.forward(randint(0,20))
    volt.forward(randint(0,20))
    power.forward(randint(0,20))

