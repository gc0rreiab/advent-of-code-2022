import sys

class Pairs:
    def __init__ (self, ranges):
        self.min1 = int(ranges[0])
        self.max1 = int(ranges[1])
        self.min2 = int(ranges[2])
        self.max2 = int(ranges[3])

    def findOverlap(self):
        #Part 1
        overlap = 0
        if (self.max2-self.max1 < 0 and self.min2-self.min1 < 0) or (self.max2-self.max1 > 0 and self.min2-self.min1 > 0):
            overlap = 0
        else:
            overlap = 1
        #Part 2
        overlapAtAll = 0  
        if self.min1 in range(self.min2, self.max2+1) or self.max1 in range(self.min2, self.max2+1) or self.min2 in range(self.min1, self.max1+1) or self.max2 in range(self.min1, self.max1+1):
            overlapAtAll = 1
        else:
            overlapAtAll = 0
            
        return overlap, overlapAtAll


file = open('input.txt', 'r')
lines = file.readlines()

total = 0
total2 = 0

for line in lines:
    line = line.rstrip('\n').replace(',','-')
    ranges = line.split('-')
    #print(ranges)
    p = Pairs(ranges)
    r1, r2 = p.findOverlap()
    if r1:
        total = total + 1
    if r2:
        total2 = total2 + 1

#Part 1 Solution 
print(total)
#Parte 2 Solution
print(total2)

exit()


