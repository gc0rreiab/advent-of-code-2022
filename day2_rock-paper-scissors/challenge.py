import sys

class Round:
    def _init_ (self, oponent_play, your_play):
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

for line in lines:
    #code here



exit()


# 1st Column: what the opponent is going to play
# A: Rock
# B: Paper
# C: Scissors

# 2nd Column: what I should play
# X: Rock
# Y: Paper
# Z: Scissors

# Total Score: sum of your scores for each round.
# Single round Score: the score for the shape (1 for Rock, 2 for paper, 3 for scissors)
#                   + the score for the outcome of the round (0 if lose, 3 if draw, 6 if win)

Formas de ganhar

R - P
P - S
S - R