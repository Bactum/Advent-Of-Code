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
#file = './Advent-Of-Code/' + yyyy + '/data/example.txt'
#file = 'C:\\Users\\daniel.weigel\\Documents\\Visual Studio 2022\\GIT\\Advent-Of-Code\\' + yyyy + '\\data\\example.txt'
#file = 'C:\\Users\\daniel.weigel\\Documents\\Visual Studio 2022\\GIT\\Advent-Of-Code\\' + yyyy + '\\data\\day' + dd + '.txt'

with open(file, 'r') as read:
    data = read.read()
    print(data)

  
        

end_time = timeit.default_timer()

print(f'Runtime: {end_time - start_time} ms')