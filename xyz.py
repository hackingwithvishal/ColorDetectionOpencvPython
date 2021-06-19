from graphics import *

# Open the window
win = GraphWin()

# Create and draw a point
p = Point(10, 10)
p.draw(win)

# Create and draw a circle
c = Circle(Point(100, 100), 15)
c.draw(win)

# Manipulate our circle
c.setFill('red')
c.setOutline('green')
c.move(-20, -20)
