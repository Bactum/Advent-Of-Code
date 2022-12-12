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

with open(file, 'r') as read:
    data = read.readlines()
    data2 = []
    for i in data:
        data2 = list((i.replace('    ', '*').replace('[', '').replace(']','')))
    print(data2.remove('\n'))
    

end_time = timeit.default_timer()

print(f'Runtime: {end_time - start_time} ms')