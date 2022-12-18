import sys

class Rucksack:
    def __init__ (self, items):
        self.items = items
        self.compartments1, self.compartments2 = items[:len(items)//2], items[len(items)//2:]
        self.error = 0
        self.priorities = 0

    def findError(self):
        e = list(set(self.compartments1) & set(self.compartments2))
        self.error = e[0]
        #calculate the priority
        if self.error.isupper():
            #Ascii table properties
            self.priorities = ord(self.error) - 38
        else:
            self.priorities = ord(self.error) - 96
            
#Part 2
class Group():
    def __init__ (self, items):
        self.items1 = items[0]
        self.items2 = items[1]
        self.items3 = items[2]
        self.badge = 0
        self.priorities = 0

    def findBadge(self):
        b = list((set(self.items1) & set(self.items2)) & set(self.items3))
        self.badge = b[0]
        #calculate the priority
        if self.badge.isupper():
            #Ascii table properties
            self.priorities = ord(self.badge) - 38
        else:
            self.priorities = ord(self.badge) - 96

file = open('input.txt', 'r')
lines = file.readlines()

total1 = 0
total2 = 0

i = 0
items = ['','','']
for line in lines:
    line = line.rstrip('\n')

    #Solve part 1
    r = Rucksack(line)
    r.findError()
    total1 = total1 + r.priorities

    #Solve part 2
    items[i] = line
    if i == 2:
        g = Group(items)
        g.findBadge()
        total2 = total2 + g.priorities
        i = 0
    else:
        i = i + 1

#Part 1 result
print(total1)
#Part 2 result
print(total2)

exit()