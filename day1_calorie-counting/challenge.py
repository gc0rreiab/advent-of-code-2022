import sys

class Elf:
    def __init__(self, id, calories):
        self.id = id
        self.calories = calories
    
Elves = []

file = open('input.txt', 'r')
lines = file.readlines()
current_id = 0
current_calories = 0

#create a list of Elves
for line in lines:
    if line == '\n':
      elf =  Elf(current_id, current_calories)
      Elves.append(elf)
      current_id = current_id + 1
      current_calories = 0
    else:
      current_calories = current_calories + int(line)

#find the three Elves with the most calories
topThree = []
for elf in Elves:
  if len(topThree) < 3:
    topThree.append(elf)
  elif elf.calories > topThree[2].calories:
      topThree[2] = elf
  topThree.sort(key=lambda x: x.calories, reverse=1)
      
#Part 1 result 
print("Top three: ")
print(f'1: {topThree[0].calories}')
print(f'2: {topThree[1].calories}')
print(f'3: {topThree[2].calories}')

#Part 2 result
print(f'Total: {topThree[0].calories + topThree[1].calories + topThree[2].calories}')

exit()

