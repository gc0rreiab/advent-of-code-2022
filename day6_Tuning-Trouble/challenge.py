import sys

file = open('input.txt', 'r')
line = file.readline().rstrip('\n')

start_of_packet_marker = ['', '', '', '']
i = 0
for c in list(line):
    i = i + 1
    start_of_packet_marker.pop(0)
    start_of_packet_marker.append(c)    
    if len(set(start_of_packet_marker)) == len(start_of_packet_marker):
        break

#Start-Packet-Marker
print(start_of_packet_marker)
#Part 1 Solution
print(i)