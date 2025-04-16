import turtle
import time

t = turtle.Turtle()
t.speed(0)

for i in range(100):
    t.forward(i)
    t.right(30)
    time.sleep(0.05)

turtle.done()