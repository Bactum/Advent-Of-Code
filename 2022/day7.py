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

tree = []
current_Directory = ''
depth = 0
with open(file, 'r') as read:
    data = read.read().split('\n')
    for index, lines in enumerate(data):
        if '$ cd /' in lines:
            depth = 0
            tree.append(['- ' + lines])
        elif '$ ls' in lines:
            

#        elif 'dir ' in lines and lines[1].isalpha():
#            depth += 1
#            tree.append(['\t- ' + lines])
#        elif lines[:3].isdigit():
#            if data[index-1] == '$ ls':
#                current_Directory = data[index-2]
#            elif 'dir ' in data[index-1]:
#                current_Directory = data[index-1]           
#            for i, element in enumerate(tree):
#                if ('\t- ' + current_Directory) in element:
#                            tree[i].append('\t\t-' + lines.split(' ')[1] + ' size: ' + lines.split(' ')[0])
#    for i, lines in enumerate(tree):
#        print(*tree[i])


  
        

end_time = timeit.default_timer()

print(f'Runtime: {end_time - start_time} ms')