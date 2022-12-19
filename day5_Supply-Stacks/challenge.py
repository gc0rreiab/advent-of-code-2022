import sys

class Stacks:
    def __init__(self, s1, s2, s3, s4, s5, s6, s7, s8, s9):
        self.stacks = [s1, s2, s3, s4, s5, s6, s7, s8, s9]

    def rearrangement(self, moves, origin, destination):
        for i in range(moves):
            crate_to_swap = self.stacks[origin-1].pop(0)
            self.stacks[destination-1].insert(0,crate_to_swap)

#File Interpretation 
file = open('input.txt', 'r')
lines = file.readlines()
puzzle_input = lines[0:8]
rearrangement_procedure_input = lines[10:]

#From puzzle collumns create lists and use it to create the Stacks Object
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
s = Stacks(s1, s2, s3, s4, s5, s6, s7, s8, s9)

#Read and perform rearrangement procedures on stack Object s
good_indices = [1, 3, 5]
for line in rearrangement_procedure_input:
    rearrangement_data = [list(line.rstrip('\n').split(' '))[i] for i in good_indices]
    #print(rearrangement_data)
    s.rearrangement(int(rearrangement_data[0]), int(rearrangement_data[1]), int(rearrangement_data[2]))

#Part 1 Solution
for i in range(9):
    print(s.stacks[i][0], end = '')
exit()
 
