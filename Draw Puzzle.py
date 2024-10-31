#!/usr/bin/env python
# coding: utf-8

# In[2]:


#draws puzzles and tracks the direction of the nubs as entries of the form NESW a matrix "puz"
#i.e. if puz[0][0] == -01- it means the north and west sides are straight, the east side is an "innie" and the west is an "outie"


import turtle
import random

height = int(input("Set height: "))
width = int(input("Set width: "))

pen = turtle.Pen()

window = turtle.Screen()

def showarray(array):
    for i in range(len(array)):
        line = ""
        for j in range(len(array[i])):
            line = line + " " + str(array[i][j])
        print(line)
    print("")


def bord():
    pen.forward(60)
    
    pen.right(90)
    
def lnub():
    pen.forward(20)
    pen.left(90)
    pen.forward(10)
    pen.right(90)
    pen.forward(20)
    pen.right(90)
    pen.forward(10)
    pen.left(90)
    pen.forward(20)
    

    
def rnub():
    pen.forward(20)
    pen.right(90)
    pen.forward(10)
    pen.left(90)
    pen.forward(20)
    pen.left(90)
    pen.forward(10)
    pen.right(90)
    pen.forward(20)
    



def nub():
    x = random.randint(0,1)
    if x == 0:
        rnub()
    if x == 1:
        lnub()

        
def move(m,n):
    pen.up()
    pos = pen.position()
    x = pos[0]
    y = pos[1]
    pen.goto(x+m,y+n)
    pen.setheading(0)
    pen.down()    
        

    
####################################################################################################################




puz = []
for i in range(height):
    puz.append([])
    for j in range(width):
        puz[i].append("----")

showarray(puz)


startx = -335
starty = 270

#swap these commands to watch the turtle slowly
turtle.tracer(0)
#turtle.speed(10)

pen.up()
pen.goto(startx,starty)
pen.down()

for i in range(2):
    pen.forward(60*width)
    pen.right(90)
    pen.forward(60*height)
    pen.right(90)

for i in range(1,height):
    pen.up()
    pen.goto(startx, starty-60*i)
    pen.down()
    for j in range(width):
        x = random.randint(0,1)
        if x == 0:
            rnub()
            
            a = list(puz[i-1][j])
            a[2] = "1"
            puz[i-1][j] = str(a[0])+str(a[1])+str(a[2])+str(a[3])
            
            b = list(puz[i][j])
            b[0] = "0"
            puz[i][j] = str(b[0])+str(b[1])+str(b[2])+str(b[3])    
            
        if x == 1:
            lnub()
            
            a = list(puz[i-1][j])
            a[2] = "0"
            puz[i-1][j] = str(a[0])+str(a[1])+str(a[2])+str(a[3])
            
            b = list(puz[i][j])
            b[0] = "1"
            puz[i][j] = str(b[0])+str(b[1])+str(b[2])+str(b[3])  
        
for i in range(1,width):
    pen.up()
    pen.goto(startx+60*i, starty)
    pen.setheading(-90)
    pen.down()
    for j in range(height):
        x = random.randint(0,1)
        if x == 0:
            rnub()
            
            r = list(puz[j][i-1])
            r[1] = "0"
            puz[j][i-1] = str(r[0])+str(r[1])+str(r[2])+str(r[3])
            
            l = list(puz[j][i])
            l[3] = "1"
            puz[j][i] = str(l[0])+str(l[1])+str(l[2])+str(l[3])
            
        if x == 1:
            lnub()
            
            r = list(puz[j][i-1])
            r[1] = "1"
            puz[j][i-1] = str(r[0])+str(r[1])+str(r[2])+str(r[3])
            
            l = list(puz[j][i])
            l[3] = "0"
            puz[j][i] = str(l[0])+str(l[1])+str(l[2])+str(l[3])
            
            
            
showarray(puz)        
        
turtle.update()
window.exitonclick()
 
turtle.done()





