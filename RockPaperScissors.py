import random as rnd
# scores
p_score = 0
o_score = 0
# main
rockpaperscissors = ["rock", "paper", "scissors"]
print('Welcome to this awesome game of:Rock, Paper, Scissors!')
print('type \'quit\' to leave the game')
run = True
while run:
    opponent = rnd.choice(rockpaperscissors)
    player = input('Make your choice: Rock, Paper, Scissors -> ')
    s_player = player.lower()
    if s_player == opponent:
        print('it\'s a tie')
    elif s_player == "rock":
        if opponent == "paper":
            print('you lose')
            o_score += 1
        else:
            print('you win')
            p_score += 1
    elif s_player == "paper":
        if opponent == "scissors":
            print('you lose')
            o_score += 1
        else:
            print('you win')
            p_score += 1
    elif s_player == "scissors":
        if opponent == "rock":
            print('you lose')
            o_score += 1
        else:
            print('you win')
            p_score += 1
    elif s_player == 'quit':
        run = False
    else:
        continue

    print('the score is: player '+str(p_score)+' opponent '+str(o_score))