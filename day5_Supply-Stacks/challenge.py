import sys

class Puzzle:
    def __init__(self, s1, s2, s3, s4, s5, s6, s7, s8, s9):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6
        self.s7 = s7
        self.s8 = s8
        self.s9 = s9

#File Interpretation 
file = open('input.txt', 'r')
lines = file.readlines()
puzzle_input = lines[0:8]
rearrangement_procedure_input = lines[10:]

#Create stacks and Puzzle Object
s1 = []
s2 = []
s3 = []
s4 = []
s5 = []
s6 = []
s7 = []
s8 = []
s9 = []

for line in puzzle_input:
    l = line.rstrip('\n').replace('    ',' ').replace('[','').replace(']','').split(' ')
    #print(l)
    if l[0] != '' : s1.append(l[0])
    if l[1] != '' : s2.append(l[1])
    if l[2] != '' : s3.append(l[2])
    if l[3] != '' : s4.append(l[3])
    if l[4] != '' : s5.append(l[4])
    if l[5] != '' : s6.append(l[5])
    if l[6] != '' : s7.append(l[6])
    if l[7] != '' : s8.append(l[7])
    if l[8] != '' : s9.append(l[8])

p = Puzzle(s1, s2, s3, s4, s5, s6, s7, s8, s9)




exit()


