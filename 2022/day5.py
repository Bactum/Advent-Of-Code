# type: ignore 
import re
import timeit

start_time = timeit.default_timer()

#import os
from datetime import date

#from aocd import submit
#from aocd.models import Puzzle

today = date.today()

dd = today.strftime("%d")
yyyy = today.strftime("%Y")

#os.system('aocd ' + dd + ' ' + yyyy + '  > ./Advent-Of-Code/' + yyyy + '/data/day' + dd + '.txt')

#file = './Advent-Of-Code/' + yyyy + '/data/day' + dd + '.txt'
file = './Advent-Of-Code/' + yyyy + '/data/example.txt'

newlist=[]
one = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
nine = []
containers = 0
boxes = []
boxes2 = []
boxes_rotate =  []

def rotate(array):
    R, C = len(array), len(array[0])
    newArr = [[None] * R for _ in range(C)]
    for c in range(C):
        for r in range(R-1, -1, -1):
            newArr[C-c-1][r] = array[r][c]
    return newArr    

with open(file, 'r',  newline='\n') as read:
    data = read.readlines()#.split('\n')
    for lines in data:
        newlist.append(lines.replace('    ', '_').replace('[', '').replace(']','').replace(' ', '').strip())
    for i in range(len(newlist)):
        if newlist[i] == '':
            break
        elif newlist[i] != '':
            containers += 1
    boxes = newlist[:(containers-1)]
    boxes_rotate = rotate(list(boxes))
    for i in range(len(boxes_rotate)):
        for j in range(len(boxes_rotate[0])):
            if boxes_rotate[i][j] == '_':
                boxes_rotate[i].pop(0)
        print(boxes_rotate)
                
    
    





end_time = timeit.default_timer()

print(f'Runtime: {end_time - start_time} ms')