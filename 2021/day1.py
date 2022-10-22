import os

#file = os.path.join("./data", "input1.txt")
file= "./Advent-Of-Code/2021/data/input1.txt"

data = []
count = 0
old_count = 0
count_2 = 0
old_count_2 = 0

with open(file) as read:
    for line in read:
        data.append(line)
    for d in data:
        if old_count == 0:
            old_count = int(d)
        if int(d) > old_count:
            count += 1
        old_count = int(d)
    for a in range(0, len(data) - 3):
        if int(data[a]) + int(data[a + 1]) + int(data[a + 2]) > old_count_2:
            count_2 += 1
        old_count_2 = int(data[a]) + int(data[a + 1]) + int(data[a + 2])
print(f"Day 1 Part 1: {count} \nDay 1 Part 2: {count_2}")
