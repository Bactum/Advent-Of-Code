# type: ignore
import timeit

start_time = timeit.default_timer()

#file= "./Advent-Of-Code/2022/data/example.txt"
file= "./Advent-Of-Code/2022/data/day1.txt"

with open(file) as read:
    data=read.read().split('\n')
    print(data)
#data = []
#tempsums = []
#sums = []
#sumssorted = []
#
#with open(file) as read:
#    for line in read:
#        data.append(line)
#    for d in data:
#        if d != '\n':
#          tempsums.append(int(d))
#        elif d == '\n':
#            sums.append(sum(tempsums))  
#            tempsums.clear()    
#sums.sort()
#
#for i in range(1, 4):
#    sumssorted.append(sums[-i])
#
#print(f'Solution Day 1: \nPart 1: {max(sums)}\nPart 2: {sum(sumssorted)}')
#
#end_time = timeit.default_timer()
#
#print(f'Runtime: {end_time - start_time} ms')