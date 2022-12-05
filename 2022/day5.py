# type: ignore 
import timeit
import re

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
#file = 'C:\\Users\\daniel.weigel\\Documents\\Visual Studio 2022\\GIT\\Advent-Of-Code\\2022\\data\\day05.txt'
file = 'C:\\Users\\daniel.weigel\\Documents\\Visual Studio 2022\\GIT\\Advent-Of-Code\\2022\\data\\example.txt'

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

with open(file, 'r',  newline='\n') as read:
    data = read.readlines()#.split('\n')
    for lines in data:
        newlist.append(lines.replace('    ', ' [_] ').strip())
    for i in range(len(newlist)):
        print(newlist[i])
    



    print(newlist[:(containers-1)])
    print(newlist[(containers+1):])
    





end_time = timeit.default_timer()

print(f'Runtime: {end_time - start_time} ms')