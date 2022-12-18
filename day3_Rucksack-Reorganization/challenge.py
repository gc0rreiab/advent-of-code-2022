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
            self.priorities = ord(self.error) - 38
        else:
            self.priorities = ord(self.error) - 96



file = open('input.txt', 'r')
lines = file.readlines()

total = 0

for line in lines:
    line = line.rstrip('\n')
    r = Rucksack(line)
    r.findError()
    total = total + r.priorities

#Part 1 result
print(total)

exit()



# Elfs are devided into groups of three


