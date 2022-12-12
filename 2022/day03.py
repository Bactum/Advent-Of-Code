# type: ignore 
import timeit

start_time = timeit.default_timer()

import os
import string
from datetime import date

from aocd import submit
from aocd.models import Puzzle

today = date.today()

dd = today.strftime("%d")
yyyy = today.strftime("%Y")

os.system('aocd ' + dd + ' ' + yyyy + '  > ./Advent-Of-Code/' + yyyy + '/data/day' + dd + '.txt')

file = './Advent-Of-Code/' + yyyy + '/data/day' + dd + '.txt'

with open(file, 'r', newline='\n') as read:
    data = read.read().split('\n')
    part_1_step = []
    part_2_step = []
    part_1_value = ''
    part_2_value = ''
    Part_1_sum = 0
    Part_2_sum = 0
    for i in range(len(data)):
        part_1_step=[data[i][:len(data[i])//2], data[i][len(data[i])//2:]]
        part_1_value = set(part_1_step[0]).intersection(part_1_step[1])
        for char in part_1_value:
            Part_1_sum += string.ascii_letters.index(char) + 1
    for j in range(len(data)//3):
        part_2_value = set(data[j*3]).intersection(data[j*3+1], data[j*3+2]) 
        for char in part_2_value:
            Part_2_sum += (string.ascii_letters.index(char) +1)

print(f'Solution Day {dd}: \nPart 1: {Part_1_sum}\nPart 2: {Part_2_sum}')


end_time = timeit.default_timer()

print(f'Runtime: {end_time - start_time} ms')