import timeit

start_time = timeit.default_timer()

#file= "./Advent-Of-Code/2022/data/example.txt"
file= "./Advent-Of-Code/2022/data/day2.txt"

p1_Value=[]
p2_Value=[]
O_Value=0
Y_Value=0
WL_Value=0
FE_Value=0

def Opponent(line):
    global O_Value
    if (line[0] == 'A'): #Rock
        O_Value=1
    elif (line[0] == 'B'): #Paper
        O_Value=2
    elif (line[0] == 'C'): #Scissor
        O_Value=3
    return O_Value
        
def You(line):
    global Y_Value
    if (line[2] == 'X'): #Rock
        Y_Value=1
    elif (line[2] == 'Y'): #Paper
        Y_Value=2
    elif (line[2] == 'Z'): #Scissor
        Y_Value=3
    return Y_Value


def winloose(O_Value, Y_Value):
    global WL_Value
    if ((O_Value == 1 and Y_Value == 3)): 
        WL_Value=0 #Loose
    elif (O_Value == 2 and Y_Value == 1):
        WL_Value=0 #Loose
    elif (O_Value == 3 and Y_Value == 2):
        WL_Value=0 #Loose
    elif (O_Value == Y_Value):
        WL_Value=3 #Draw
    else:
        WL_Value=6 #Win
    return WL_Value

def forceend(O_Value, Y_Value, line):
    if line[2] == 'X': #Force Loose
        if O_Value == 1:
            Y_Value = 3
            winloose(O_Value, Y_Value)
        elif O_Value == 2:
            Y_Value = 1
            winloose(O_Value, Y_Value)
        elif O_Value == 3:
            Y_Value = 2
            winloose(O_Value, Y_Value)
    elif line[2] == 'Y': #Force Draw
        Y_Value=O_Value
        winloose(O_Value, Y_Value)
    elif line[2] == 'Z': #Force Win
        if O_Value == 1:
            Y_Value = 2
            winloose(O_Value, Y_Value)
        elif O_Value == 2:
            Y_Value = 3
            winloose(O_Value, Y_Value)
        elif O_Value == 3:
            Y_Value = 1
            winloose(O_Value, Y_Value)
    p2_Value.append(Y_Value)
    p2_Value.append(WL_Value) 
    

with open(file) as read:
    for line in read:
        Opponent(line)
        You(line)
        winloose(O_Value, Y_Value)
        p1_Value.append(Y_Value)
        p1_Value.append(WL_Value)
        forceend(O_Value, Y_Value, line) 
        

print(f'Solution Day 2: \nPart 1: {sum(p1_Value)}\nPart 2: {sum(p2_Value)}')

end_time = timeit.default_timer()

print(f'Runtime: {end_time - start_time} ms')