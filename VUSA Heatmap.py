#!/usr/bin/env python
# coding: utf-8

# In[1]:

#This is a simulation created for my undergraduate thesis
#VUSA = Very unfriendly seating algorithm
#The mission is to take a grid of empty seats (e.g. in a theater) and fill them, one by one, with people
#Rules:
#1. The first person will take a corner seat (this is optional)
#2. Another person will take a seat unless every seat is orthagonally adjacent to a filled seat.
#3. Each subsequent person will chose from the unfilled seats with maximum room (chosen uniformly at random)

#There is a shortcut process when the number of seats is anti-optimal (see "The very unfriendly seating arrangement problem pdf)

#This program runs several trials, then creates a heatmap of the most chosen seats and a picture of the seats chosen more than average

import random 


#returns an x-by-y array of "-"s
def Field(x,y): 
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append("-")
    return array
  
    
#Prints an array nicely, as a grid   
def ShowArray(array):
    for i in range(len(array)):
        line = ""
        for j in range(len(array[i])):
            line = line + " " + str(array[i][j])
        print(line)
    print("")

def ShowArrayThin(array):
    for i in range(len(array)):
        line = ""
        for j in range(len(array[i])):
            line = line + str(array[i][j])
        print(line)
    print("")  
    
    
#optimal case varies depending on the parity of our dimensions (for cattycorner allowed)
def OptimalFill(array):
    x = len(array)
    y = len(array[0])
    if x % 2 == 0 or y % 2 == 0:
        return int(x*y/2)
    else:
        return int((x*y+1)/2)

    
#the square of Euclidean distance, used for quickly finding the nearest occupied seat
def EDistance(x1,y1,x2,y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)

#returns the number of times "X" is in an array
def Count(array):
    num = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == "X":
                num = num + 1
    return num


#Returns the minimum Edistance from (x,y) to an "X" (a filled seat) 
def ERoom(array,x,y):
    R = EDistance(0,0,len(array),len(array[0])) + 1
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == "X": 
                if EDistance(i,j,x,y) < R:
                    R = EDistance(i,j,x,y)  
                if EDistance(i,j,x,y) == 1:
                    return 1
    return R


def CountH(array):
    num = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == "H":
                num = num + 1
    return num


#marks all spaces with maximal room with an "H" for 'HERE!'
def MarkAllBest(array):
    Currentbestroom = 0
    Full = False 
    for i in range(len(array)):        
        for j in range(len(array[i])):
            CRoom = ERoom(array,i,j)
            if array[i][j] == "-" and CRoom > Currentbestroom:
                Currentbestroom = CRoom

    for i in range(len(array)):
        for j in range(len(array[i])):
            if Currentbestroom == 1:
                Full = True 
                break
            if ERoom(array,i,j) == Currentbestroom: 
                array[i][j] = "H"
                
                
def ChooseFromBest(array,num):
    dum = 1
    done = False 
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == "H":
                if done == False:               
                    if dum == num:
                        array[i][j] = "X"
                        done = True 
                    else:
                        dum = dum + 1
                        array[i][j] = "-"
                else:
                    array[i][j] = "-"
                    
#exhanges "X" for int 1 and "-" for int 0                    
def Quantify(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == "X":
                array[i][j] = 1
            else:
                array[i][j] = 0
                
#(unused) option to make the first chosen seat random, otherwise it's always one of the corners                   
def StartRandom(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = "H"
            
    
def ArrayIncrease(start,inc):
    if len(start) != len(inc) or len(start[0]) != len(inc[0]):
        print("ERROR: ARRAY DIMENSIONS DIFFER")
    else:
        for i in range(len(start)):
            for j in range(len(start[i])):
                start[i][j] = start[i][j] + inc[i][j]
                
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

#########################################################################################################################
#End of definitions.
#Choose height, width, and number of trials. The program will run the VUSA many times and create a Heatmap
#Darker squares are the ones visited more often.
#Finally, it will also print a picture of the seats that had above average visits.

height = 15
width = 15

#Change Show to "N" if you don't want to see the progress as it goes
Show = "Y"
trials = 100

print(height*width)


Sum = Field(height,width)
Quantify(Sum)
ShowArray(Sum)

for t in range(trials):
    print("")
    plot = Field(height,width)
    
    plot[0][0] = "H"
    plot[0][-1] = "H"
    plot[-1][0] = "H"
    plot[-1][-1] = "H"
    
    StartRandom(plot)
    
    choice = int(random.randint(1,CountH(plot)))
    #print("Choice = " + str(choice))
    ChooseFromBest(plot,choice)
    
    for j in range(OptimalFill(plot)):
        MarkAllBest(plot)
        if CountH(plot) != 0:    
            if Show == "Y":
                print("Step = " + str(t) + "." + str(j))
                ShowArray(plot)
            choice = int(random.randint(1,CountH(plot)))
            #print("Choice = " + str(choice) + "\n\n")
            ChooseFromBest(plot,choice)
        else:
            ShowArray(plot)
            break
        
    Quantify(plot)
    #ShowArray(plot)
    
    ArrayIncrease(Sum,plot)
    
    print("Step = " + str(t))
    print("SUM = ")
    ShowArray(Sum)
    

    
for i in range(len(Sum)):
    for j in range(len(Sum[0])):
        Sum[i][j] = Sum[i][j]/trials


print("Average Number of People: ")
ShowArray(Sum)

AvgTotal = 0
for i in range(len(Sum)):
    for j in range(len(Sum[0])):
        AvgTotal = AvgTotal + Sum[i][j]
        
Avg = AvgTotal/(height*width)
        
print("AvgTotal = " + str(AvgTotal))
print("Avg = " + str(Avg))
        
HeatMap = Field(height,width)
AboveAvg = Field(height,width)

for i in range(len(Sum)):
    for j in range(len(Sum[0])):
        f = int(255*(1 - Sum[i][j]))
        HeatMap[i][j] = colored(f,f,f,'■')
        
        if Sum[i][j] > Avg:
            AboveAvg[i][j] = colored(0,0,0,'■')
        else:
            AboveAvg[i][j] = colored(255,255,255,'■')
        

ShowArray(HeatMap)
ShowArray(AboveAvg)
    






