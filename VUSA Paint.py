#!/usr/bin/env python
# coding: utf-8

# In[14]:

#This is a simulation created for my undergraduate thesis
#VUSA = Very unfriendly seating algorithm
#The mission is to take a grid of empty seats (e.g. in a theater) and fill them, one by one, with people
#Rules:
#1. The first person will take a corner seat (this is optional)
#2. Another person will take a seat unless every seat is orthagonally adjacent to a filled seat.
#3. Each subsequent person will chose from the unfilled seats with maximum room (chosen uniformly at random)

#There is a shortcut process when the number of seats is anti-optimal (see "The very unfriendly seating arrangement problem pdf)

#This program also treats the final lattice as a map where diagonal lines of filled seats are seen as borders. 
#Auxillary borders are added to the outside
#An empty space is given the next letter, then its region is filled with the same letter (think "FILL" in MSPaint)
#Repeat until no spaces are empty


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

    
#typical Euclidean distance, but not squared so it can calc faster, since we're just concered with =, > or <
def EDistance(x1,y1,x2,y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)

#simply returns the number of times "X" is in an array
def Count(array):
    num = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == "X":
                num = num + 1
    return num


#Returns the minimum Edistance from (x,y) to an X 
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
            

            
#############################################################################################################################            
#2nd project results (Color 1 Maze)

#We have to add 2 outer layers of filled seats to "keep the paint from spilling out" (To keep the checked squares in bounds)
def Wall(array):
    out = [[]]
    for d in range(len(array[0]) + 2):
        out[0].append("1")    
    for i in range(len(array)):
        out.append(["1"])
        for j in range(len(array[i])):
            out[i+1].append(array[i][j])
        out[i+1].append("1")     
    out.append([])     
    for e in range(len(array[0]) + 2):
        out[-1].append("1")
        
    for i in range(len(out)):
        for j in range(len(out[0])):
            if out[i][j] == "X":
                out[i][j] = "1"
                       
    return out
    
    
def Flow(maze,i,j):
    up = maze[i-1][j]
    down = maze[i+1][j]
    left = maze[i][j-1]
    right = maze[i][j+1]
    
    return ((up == "-") or (down == "-") or (left == "-") or (right == "-")) and maze[i][j] != "1"


def Spread(array,i,j):
    
    Letter = array[i][j]
    
    m = i
    n = j
    
    for s in range(len(array)*len(array[0])):
        up = array[m-1][n]
        down = array[m+1][n]
        left = array[m][n-1]
        right = array[m][n+1]
    
        if up == "-":
            array[m-1][n] = Letter
            #print("up filled (%d,%d)" % (m,n))
            #ShowArray(array)
        if down == "-":
            array[m+1][n] = Letter
            #print("down filled (%d,%d)" % (m,n))
            #ShowArray(array)
        if left == "-":
            array[m][n-1] = Letter
            #print("left filled (%d,%d)" % (m,n))
            #ShowArray(array)
        if right == "-":
            array[m][n+1] = Letter
            #print("right filled (%d,%d)" % (m,n))
            #ShowArray(array)
        
        #set as variables instead of calculating each time
        FlowUp = Flow(array,m-1,n)
        FlowDown = Flow(array,m+1,n)
        FlowLeft = Flow(array,m,n-1)
        FlowRight = Flow(array,m,n+1)
        
        
        #fork in the road checker
        if (FlowUp and FlowDown == True):
            Spread(array,m-1,n)
            Spread(array,m+1,n)
            
        if (FlowLeft and FlowRight == True):
            Spread(array,m,n-1)
            Spread(array,m,n+1)
            
        #keeps the spread flowing
        if FlowUp == True:
            Spread(array,m-1,n)
            #print("Flow Up (%d,%d)" % (m,n))
        elif FlowDown == True:
            Spread(array,m+1,n)
            #print("Flow Down (%d,%d)" % (m,n))
        elif FlowLeft == True:
            Spread(array,m,n-1)
            #print("Flow Left (%d,%d)" % (m,n))
        elif FlowRight == True:
            Spread(array,m,n+1)
            #print("Flow Right (%d,%d)" % (m,n))
        else:
            #print("Break")
            break
    

    
def FillWithNumbers(maze):
    global graph
    
    K = "A"
    for i in range(2,len(maze)-2):
        for j in range(2,len(maze[0])-2):
            
            if maze[i][j] == "-":
                maze[i][j] = K
                K = chr(ord(K) + 1)
                
                Spread(maze,i,j)
    
    #once the filling is done, we try to calculate what other letters each letter is adjacent to
    
    
    K = chr(ord(K) - 1)
    #print("\nFinal Letter = %s\n" % (K))  
    
    LetterList = []
    for i in range(ord(K)-ord("A")+1):
        LetterList.append([chr(ord("A")+i)])
        
    #print(LetterList)
    #print()
    
    
    for i in range(2,len(maze)-2):
        for j in range(2,len(maze[0])-2):
            
            current = maze[i][j]
            n = ord(maze[i][j]) - ord("A")
            
            up = maze[i-1][j]
            down = maze[i+1][j]
            left = maze[i][j-1]
            right = maze[i][j+1]
            
            NW = maze[i-1][j-1]
            NE = maze[i-1][j+1]
            SW = maze[i+1][j-1]
            SE = maze[i+1][j+1]
            
            if up == "1" and left == "1" and NW != current and NW != "1":
                newnum = True
                for k in range(len(LetterList[n])):
                    if LetterList[n][k] == NW:
                        newnum = False
                if newnum == True:
                    LetterList[n].append(NW)
                    #ShowArray(LetterList)
            
            if up == "1" and right == "1" and NE != current and NE != "1":
                newnum = True
                for k in range(len(LetterList[n])):
                    if LetterList[n][k] == NE:
                        newnum = False
                if newnum == True:
                    LetterList[n].append(NE)
                    #ShowArray(LetterList)
                    
            if down == "1" and left == "1" and SW != current and SW != "1":
                newnum = True
                for k in range(len(LetterList[n])):
                    if LetterList[n][k] == SW:
                        newnum = False
                if newnum == True:
                    LetterList[n].append(SW)
                    #ShowArray(LetterList)
                    
            if down == "1" and right == "1" and SE != current and SE != "1":
                newnum = True
                for k in range(len(LetterList[n])):
                    if LetterList[n][k] == SE:
                        newnum = False
                if newnum == True:
                    LetterList[n].append(SE)
                    #ShowArray(LetterList)
            
    ShowArray(maze)
    #ShowArray(LetterList)
    graph = LetterList  
    
    
def ColorTable(graph):
    table = []
    for i in range(len(graph)):
        table.append([graph[i][0]])
        for j in range(len(graph)):
            table[i].append(0)
            
    for i in range(len(graph)):
        for j in range(1,len(graph[i])):
            position = ord(graph[i][j]) - ord("A")
            adjcolor = table[position][1]
            
            if adjcolor != 0:
                table[i][adjcolor + 1] = adjcolor
                
        for k in range(2, len(graph)):
            if table[i][k] == 0:
                table[i][1] = k-1
                break 
        
    return(table)



def PaintWalls(array):
    #print("Number Seated: %d" % Count(array))
    array = Wall(Wall(array))
    FillWithNumbers(array)
    
    Tab = ColorTable(graph)
    Pal = ["\033[41m","\033[42m","\033[43m","\033[44m","\033[45m","\033[46m","\033[47m"]
    for i in range(len(array)):
        for j in range(len(array[i])):
            Letter = array[i][j]
            if Letter == "1":
                array[i][j] = "\033[40m 1"
            else:
                array[i][j] = "\033[47m " + Letter
                
    #ShowArrayThin(array)    
    print("\033[49mNumber of sections: %d" % len(Tab))



            
def Paint(array):
    print("Number Seated: %d" % Count(array))
    array = Wall(Wall(array))
    FillWithNumbers(array)
    print(array)
    Tab = ColorTable(graph)
    Pal = ["\033[41m","\033[42m","\033[43m","\033[44m","\033[45m","\033[46m","\033[47m"]
    for i in range(len(array)):
        for j in range(len(array[i])):
            Letter = array[i][j]
            if Letter == "1":
                array[i][j] = "\033[40m 1"
            else:
                color = Tab[ord(Letter) - ord("A")][1] - 1
                array[i][j] = Pal[color] + " " + Letter
                
    ShowArrayThin(array)    
    print("\033[49mNumber of sections: %d" % len(Tab))
    
    
    
#A shortcut to quickly fill out sub-optimal squares    
def Stratify(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if (i%3 == 0) and (j%3 == 0):
                array[i][j] = "X"
            elif (i%3 == 1) and (j%3 == 1):
                n = random.randint(0,1)
                #print("n = %d" % n)
                if n == 0:
                    array[i][j] = "X"
                    array[i+1][j+1] = "X"
                if n == 1:
                    array[i+1][j] = "X"
                    array[i][j+1] = "X"    


##########################################################################################################################       
#ACTUAL COMMANDS 

trials = int(input("How many trials to run? "))
print("Trials: %d" % trials)

C = input("Anti-optimal squares only? (Y/N) ")
Show = "N"

if C == "Y":
    n = int(input("Set n (Choose an integer 1<n<6 for nice pictures)(Side length = 3*2^(n-1)+1): "))
    height = int(3*(2**(n-1))+1)
    width = int(3*(2**(n-1))+1)
    print("Side length = %d" % height)
    trials2 = trials
    trials = 0

elif C == "N":
    height = int(input("Set Height: "))
    width = int(input("Set Width: "))
    trials2 = 0
    Show = input("Show each filling step? (Y/N)")
    


for i in range(trials):
    print("")
    print("Trial = " + str(i))
    plot = Field(height,width)

    plot[0][0] = "H"
    plot[0][-1] = "H"
    plot[-1][0] = "H"
    plot[-1][-1] = "H"
    
    choice = int(random.randint(1,CountH(plot)))
    #print("Choice = " + str(choice))
    ChooseFromBest(plot,choice)
 
    for j in range(OptimalFill(plot)):
        MarkAllBest(plot)
        if CountH(plot) != 0:    
            if Show == "Y":
                ShowArray(plot)
            choice = int(random.randint(1,CountH(plot)))
            #print("Choice = " + str(choice) + "\n\n")
            ChooseFromBest(plot,choice)
        else:
            ShowArray(plot)
            Paint(plot)
            break
            

for i in range(trials2):
    print("")
    print("Trial = " + str(i))
    plot = Field(height,height)
    Stratify(plot)
    ShowArray(plot)
    bwplot = plot
    PaintWalls(bwplot)
    Paint(bwplot)
    #print(bwplot)
    
    





