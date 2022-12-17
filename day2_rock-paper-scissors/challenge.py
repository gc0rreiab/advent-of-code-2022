import sys

class Round:
    def __init__ (self, oponent_play, your_play):
        self.oponent_play = oponent_play
        self.your_play = your_play
        self.score = 0

    def scoreCalculation(self):
        pts = 0
        #Score for the shape used
        if self.your_play == 'R':
            pts = pts + 1
        elif self.your_play == 'P':
            pts = pts + 2
        else:
            pts = pts + 3
        
        #Score for the outcome of the round
        if self.oponent_play == self.your_play:
            #It's a Draw
            pts = pts + 3
        elif self.oponent_play == 'R' and self.your_play == 'P' or self.oponent_play == 'P' and self.your_play == 'S' or self.oponent_play == 'S' and self.your_play == 'R':
            #You won
            pts = pts + 6
        else:
            #You lose
            pts = pts + 0

        self.score = pts  


          
file = open('input.txt', 'r')
lines = file.readlines()

totalScore = 0

for line in lines:
    l = line.split()
    l[0] = 'R' if l[0]=='A' else 'P' if l[0]=='B' else 'S'
    l[1] = 'R' if l[1]=='X' else 'P' if l[1]=='Y' else 'S'
    # print(l)
    r = Round(l[0], l[1])
    r.scoreCalculation()

    totalScore = totalScore + r.score

print(totalScore)

exit()
