import sys

class Marker:

    def __init__(self):
        self.datastream_buffer = ''
        self.marker = []
        self.charsToBeProcessed = 0
    
    def checkStartMarker(self, datastream_buffer, n):
        start_of_packet_marker = [''] * n
        i = 0
        for c in list(datastream_buffer):
            i = i + 1
            start_of_packet_marker.pop(0)
            start_of_packet_marker.append(c)    
            if len(set(start_of_packet_marker)) == len(start_of_packet_marker):
                break
        self.charsToBeProcessed = i
        self.marker = start_of_packet_marker


file = open('input.txt', 'r')
datastream_buffer = file.readline().rstrip('\n')

m = Marker()

#Uncomment for Part 1 Solution (start-of-packet marker)
m.checkStartMarker(datastream_buffer, 4)

#Part 2 Solution (start-of-message marker)
m.checkStartMarker(datastream_buffer, 14)

#Start-Marker
print(m.marker)
#Solution
print(m.charsToBeProcessed)