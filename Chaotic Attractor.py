#!/usr/bin/env python
# coding: utf-8

# In[2]:


#The famous project of iteratively selecting one of 3 points in the plane at random, moving halfway to it and marking a point, and repeating 

import turtle
import random


if 1 == 1:
    x1 = int(input("x1 = "))
    y1 = int(input("y1 = "))
    x2 = int(input("x2 = "))
    y2 = int(input("y2 = "))
    x3 = int(input("x3 = "))
    y3 = int(input("y3 = "))
    


minx = min(x1,x2,x3) - 100
miny = min(y1,y2,y3) - 100
maxx = max(x1,x2,x3) + 100
maxy = max(y1,y2,y3) + 100

startx = random.randint(minx,maxx)
starty = random.randint(miny,maxy)



run = int(input("How many points? "))

#pos = pen.position()


pen = turtle.Pen()

window = turtle.Screen()
window.setworldcoordinates(minx,miny,maxx,maxy)

def point():
    pen.up()
    pen.setheading(90)
    pen.forward(0.5)
    pen.right(90)
    pen.down()
    pen.forward(0.5)
    pen.right(90)
    pen.forward(1)
    pen.right(90)
    pen.forward(1)
    pen.right(90)
    pen.forward(1)
    pen.right(90)
    pen.forward(0.5)
    pen.up()
    pen.right(90)
    pen.forward(0.5)
    
def bigpoint():
    pen.up()
    pen.setheading(90)
    pen.forward(1)
    pen.right(90)
    pen.down()
    pen.forward(1)
    pen.right(90)
    pen.forward(2)
    pen.right(90)
    pen.forward(2)
    pen.right(90)
    pen.forward(2)
    pen.right(90)
    pen.forward(1)
    pen.up()
    pen.right(90)
    pen.forward(1)
    
turtle.tracer(0)
#pen.speed(10)

#draw starting points
pen.up()
pen.goto(x1,y1)
bigpoint()
pen.goto(x2,y2)
bigpoint()
pen.goto(x3,y3)
bigpoint()

pen.goto(startx,starty)
point()

for i in range(run):
    c = random.randint(1,3)
    print(c)
    
    if c == 1:
        pen.setheading(pen.towards(x1,y1))
        t = pen.distance(x1,y1) / 2
        pen.up()
        pen.forward(t)
        point()
        
    if c == 2:
        pen.setheading(pen.towards(x2,y2))
        t = pen.distance(x2,y2) / 2
        pen.up()
        pen.forward(t)
        point()

    if c == 3:
        pen.setheading(pen.towards(x3,y3))
        t = pen.distance(x3,y3) / 2
        pen.up()
        pen.forward(t)
        point()

        



turtle.update()
window.exitonclick()
turtle.done()


# In[ ]:





# In[ ]:




