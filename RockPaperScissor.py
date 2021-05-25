import random

def play():
    user = input("enter 'r' for rock, 'p' paper and 's' for scissor\n")
    comp = random.choice(['r','p','s'])

    if user==comp:
        print("its a Tie")

    if iswin(user,comp):
        return 'You Won!!'

    return 'You Lost!!'

def iswin(player,opponent):
    if (player=='r' and opponent=='s') or (player=='p' and opponent=='r') or (player=='s' and opponent==g'p'):
        return True
print(play())
