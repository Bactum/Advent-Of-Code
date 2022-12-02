# type: ignore
import timeit

start_time = timeit.default_timer()

#file= "./Advent-Of-Code/2022/data/example.txt"
file= "./Advent-Of-Code/2015/data/day1.txt"

openbracket=0
closedbracket=0
counting=0
base=0

with open(file) as read:
    for line in read:
        openbracket = line.count('(')
        closedbracket = line.count(')')
    for i in line:
        if (counting >= 0 and base > -1):
            if i == '(':
                counting += 1
                base += 1
            elif i == ')':
                counting +=1
                base -= 1
print(f'Day 1:\nPart 1: {openbracket-closedbracket}\nPart 2: {counting}')
end_time = timeit.default_timer()

print(f'Runtime: {end_time - start_time} ms')