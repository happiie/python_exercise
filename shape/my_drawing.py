from shape import Triangle, Rectangle, Oval

rec1 = Rectangle()
rec1.set_height(100)
rec1.set_width(200)
rec1.set_color('blue')
rec1.set_x(100)
rec1.set_y(100)

rec1.draw()

rec2 = Rectangle()
rec2.set_width(50)
rec2.set_height(150)
rec2.set_color('yellow')
rec2.set_y(200)
rec2.set_x(180)

rec2.draw()

ova = Oval()
ova.randomize(100,140)
ova.set_color('purple')
ova.draw()


tri = Triangle(400,400,500,140,400,100)
tri.set_color('red')
tri.draw()
