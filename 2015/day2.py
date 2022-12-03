# type: ignore 

import timeit

import numpy as np

start_time = timeit.default_timer()

#file= "./Advent-Of-Code/2015/data/example.txt"
file= "./Advent-Of-Code/2015/data/day2.txt"

boxes = []
boxes_sorted = []
feet = []
lack = 0
sum_of_feet = 0
sum_of_ribbon = 0


with open(file) as data:
    input = data.read().split('\n')
    for index, boxes in enumerate(range(len(input))):
        boxes = input[index].split('x')
        l = int(boxes[0])
        w = int(boxes[1])
        h = int(boxes[2])
        feet =[2*l*w, 2*w*h, 2*h*l]
        boxes_sorted = np.sort([int(boxes[0]), int(boxes[1]), int(boxes[2])])
        lack = boxes_sorted[0] * boxes_sorted[1]
        sum_of_feet += lack + feet[0] + feet[1] + feet[2]
        sum_of_ribbon += 2*boxes_sorted[0] + 2*boxes_sorted[1] + l * w * h
        
print(f'Solution 2015 Day 2:\n\nPart 1: {sum_of_feet}\nPart 2: {sum_of_ribbon}\n')
        
end_time = timeit.default_timer()

print(f'Runtime: {end_time - start_time} ms')