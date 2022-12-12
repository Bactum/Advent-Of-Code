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

#file = './Advent-Of-Code/' + yyyy + '/data/day' + dd + '.txt'
file = './Advent-Of-Code/' + yyyy + '/data/example.txt'
#file = 'C:\\Users\\daniel.weigel\\Documents\\Visual Studio 2022\\GIT\\Advent-Of-Code\\' + yyyy + '\\data\\example.txt'
#file = 'C:\\Users\\daniel.weigel\\Documents\\Visual Studio 2022\\GIT\\Advent-Of-Code\\' + yyyy + '\\data\\day' + dd + '.txt'
current_Monkey = {}

Monkeys = {}

Monkey = 0
lines = []
with open(file, 'r', newline='\n') as read:
    data = read.readlines()
    for line in data:
        lines.append(line.replace(',','').split())
    print(lines)
    for elements in lines:
        if elements[0] == 'Monkey':
            Monkey = elements[1]
            current_Monkey[str(Monkey)] = {}
        elif (elements[0] == 'Starting') and (elements[1] == 'items:'):
            current_Monkey[str(Monkey)]['Starting items'] = [elements[2:]]
        elif (elements[0] == 'Operation:') and (elements[1] == 'new') and (elements[2] == '='):
            current_Monkey[str(Monkey)]['New Worries'] = []
            if elements[4] == '+':
                for i, tile in enumerate(current_Monkey[str(Monkey)]['Starting items']):
                    temp = int(tile[i]) + int(elements[5])
                    current_Monkey[str(Monkey)]['New Worries'].append(temp)
            elif elements[4] == '-':
                for i, tile in enumerate(current_Monkey[str(Monkey)]['Starting items']):
                    temp = int(tile[i]) - int(elements[5])
                    current_Monkey[str(Monkey)]['New Worries'].append(temp)
            elif elements[4] == '*':
                for i, tile in enumerate(current_Monkey[str(Monkey)]['Starting items']):
                    temp = int(tile[i]) * int(elements[5])
                    current_Monkey[str(Monkey)]['New Worries'].append(temp)
            elif elements[4] == '/':
                for i, tile in enumerate(current_Monkey[str(Monkey)]['Starting items']):
                    temp = int(tile[i]) / int(elements[5])
                    current_Monkey[str(Monkey)]['New Worries'].append(temp)
        elif (elements[0] == 'Test'):
            current_Monkey[str(Monkey)]['Test'] = [elements[3]]
        elif (elements[1] == 'true'):
            for i, checking in enumerate(current_Monkey[str(Monkey)]['New Worries']):
                if checking//current_Monkey[str(Monkey)]['Test'].value() == True:
                    current_Monkey[str(Monkey)]['New Worries'].pop(int(i))
                    Monkeys[str(elements[5])] = {'New Worries':[checking]}
#        else:
#            current_Monkey
    
    
    
        
end_time = timeit.default_timer()

print(f'Runtime: {end_time - start_time} ms')