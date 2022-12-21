# type: ignore 
import timeit

start_time = timeit.default_timer()

import os
from datetime import date

#from aocd import submit
#from aocd.models import Puzzle

today = date.today()

dd = today.strftime("%d")
yyyy = today.strftime("%Y")

#os.system('aocd ' + dd + ' ' + yyyy + '  > ./Advent-Of-Code/' + yyyy + '/data/day' + dd + '.txt')

#file = './Advent-Of-Code/' + yyyy + '/data/day' + dd + '.txt'
#file = './Advent-Of-Code/' + yyyy + '/data/example.txt'
file = 'C:\\Users\\daniel.weigel\\Documents\\Visual Studio 2022\\GIT\\Advent-Of-Code\\' + yyyy + '\\data\\example.txt'
#file = 'C:\\Users\\daniel.weigel\\Documents\\Visual Studio 2022\\GIT\\Advent-Of-Code\\' + yyyy + '\\data\\day' + dd + '.txt'

tree = {'/':{}}
current_dir = ''

with open(file, 'r', newline='\n') as read:
    data = read.read().split('\n')
    for i, lines in enumerate(data):
        each_line = lines.split(' ')
        if each_line[0] == '$':
            if each_line[1] == 'cd':
                if each_line[2].isalpha():
                    current_dir = str(each_line[2])
                    if str(each_line[2]) in tree:
                        continue
                    else:
                        tree[str(each_line[2])] = {}
                elif each_line[2] == '/':
                    current_dir = str(each_line[2])
                elif each_line[2] == '..':
                    continue
            if each_line[1] == 'ls':
                continue
        elif each_line[0] == "dir":
            if str(each_line[1]) in tree:
                continue
            else:
                continue
        elif each_line[0].isnumeric():
            tree[str(current_dir)].update({each_line[1]: int(each_line[0])})

print(tree['a'])

for key in tree:
    summe = 0
    summe = sum(tree[key])
    print(summe)
    

            
                   

                
                
        
        


  
        

end_time = timeit.default_timer()

print(f'Runtime: {end_time - start_time} ms')