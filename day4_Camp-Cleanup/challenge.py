import sys

class Pairs:
    def __init__ (self, ranges):
        self.min1 = int(ranges[0])
        self.max1 = int(ranges[1])
        self.min2 = int(ranges[2])
        self.max2 = int(ranges[3])

    def findOverlap(self):
        overlap = 0
        if (self.max2-self.max1 < 0 and self.min2-self.min1 < 0) or (self.max2-self.max1 > 0 and self.min2-self.min1 > 0):
            overlap = 0
        else:
            overlap = 1
        return overlap


file = open('input.txt', 'r')
lines = file.readlines()

total = 0

for line in lines:
    line = line.rstrip('\n').replace(',','-')
    ranges = line.split('-')
    #print(ranges)
    p = Pairs(ranges)
    if p.findOverlap():
        total = total + 1

    

#Part 1 Solution 
print(total)

exit()