import os

#file = os.path.join("./data", "input1.txt")
file= "./Advent-Of-Code/2022/data/day1.txt"

data = []
tempsums = []
sums = []
sumssorted = []

with open(file) as read:
    for line in read:
        data.append(line)
    for d in data:
        if d != '\n':
          tempsums.append(int(d))
        elif d == '\n':
            sums.append(sum(tempsums))  
            tempsums.clear()    
sums.sort()

for i in range(1, 4):
    sumssorted.append(sums[-i])

print(f'Lösung: \nDay 1: {max(sums)}\nDay2 : {sum(sumssorted)}')