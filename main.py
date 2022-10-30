import random


wincount = 0
losscount = 0
drawcount = 0

while True:
    RPS = ["Rock", "Paper", "Scissors"]
    AI = random.choice(RPS)
    YourMove = input()
    print(AI)
    if YourMove == "rock":
        if AI == "Rock":
            print("Draw")
            drawcount = drawcount + 1
        elif AI == "Scissors":
            print("You win!")
            wincount = wincount + 1
        elif AI == "Paper":
            print("You lose!")
            losscount = losscount + 1
        print(wincount, losscount, drawcount)

    if YourMove == "paper":
        if AI == "Rock":
            print("You win!")
            wincount = wincount + 1
        elif AI == "Scissors":
            print("You lose!")
            losscount = losscount + 1
        elif AI == "Paper":
            print("Draw")
            drawcount = drawcount + 1
        print(wincount, losscount, drawcount)

    if YourMove == "scissors":
        if AI == "Rock":
            print("You lose!")
            losscount = losscount + 1
        elif AI == "Scissors":
            print("Draw")
            drawcount = drawcount + 1
        elif AI == "Paper":
            print("You win!")
            wincount = wincount + 1
        print(wincount, losscount, drawcount)