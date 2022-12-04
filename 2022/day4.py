# type: ignore 
import timeit

start_time = timeit.default_timer()

import os
from datetime import date

from aocd import submit
from aocd.models import Puzzle

today = date.today()

dd = today.strftime("%d")
yyyy = today.strftime("%Y")

os.system('aocd ' + dd + ' ' + yyyy + '  > ./Advent-Of-Code/' + yyyy + '/data/day' + dd + '.txt')

file = './Advent-Of-Code/' + yyyy + '/data/day' + dd + '.txt'
#file = './Advent-Of-Code/2022/data/example.txt'

step_1 = []
step_2 = []
integrated = 0
intersected = 0

with open(file, 'r', newline='\n') as read:
    for lines in read:
        data = lines.split(',')
        step_1 = data[0].split('-')
        step_2 = data[1].split('-')
        if ((int(step_1[0]) >= int(step_2[0])) and (int(step_1[1]) <= int(step_2[1])) or (int(step_1[0]) <= int(step_2[0])) and (int(step_1[1]) >= int(step_2[1]))):
            integrated += 1
        if ((int(step_1[1]) >= int(step_2[0])) and (int(step_2[1]) >= int(step_1[0]))):
            intersected += 1

print(f'Solution Day {dd}: \nPart 1: {integrated}\nPart 2: {intersected}')

end_time = timeit.default_timer()

print(f'Runtime: {end_time - start_time} ms')