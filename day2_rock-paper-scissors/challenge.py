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

totalScore1 = 0
totalScore2 = 0

for line in lines:
    l = line.split()

    l[0] = 'R' if l[0]=='A' else 'P' if l[0]=='B' else 'S'
    l[1] = 'R' if l[1]=='X' else 'P' if l[1]=='Y' else 'S'    
    r = Round(l[0], l[1])
    r.scoreCalculation()
    totalScore1 = totalScore1 + r.score

    #Solve parte 2
    if l[1] == 'R':
        #need to lose
        l[1] = 'P' if l[0]=='S' else 'R' if l[0]=='P' else 'S'
    elif l[1] == 'P':
        #need to end the round in a draw
        l[1] = 'P' if l[0]=='P' else 'R' if l[0]=='R' else 'S'
    else:
        #need to win
        l[1] = 'S' if l[0]=='P' else 'P' if l[0]=='R' else 'R'
    r2 = Round(l[0], l[1])
    r2.scoreCalculation()
    totalScore2 = totalScore2 + r2.score


#Part 1 result
print(totalScore1)

#Part 2 result
print(totalScore2)

exit()
