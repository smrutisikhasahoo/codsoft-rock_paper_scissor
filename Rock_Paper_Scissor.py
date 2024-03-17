import random

Done=False
Wins, Losses, Ties=0, 0, 0

Name={'R': "rock", 'P': "paper", 'S': "Scissors"}

Loses={'R': 'P','P': 'S','S': 'R'}

while not Done:
    Choice=input("Please choose Your Next Move(R,P,S)(Q To Quit):--").upper()
    CPU_Choice=random.choice(['R','P','S'])

    if Choice == CPU_Choice:
        print(f"It is a Tie !! You both choose  {Name[Choice]}")
        Ties+=1
    elif Choice in ['R','P','S']:
        if CPU_Choice == Loses[Choice]:
            print(f"CPU WINS !!,YOU CHOOSE  {Name[Choice]},The cpu chooose  {Name[CPU_Choice]}")
            Losses+=1
        else:
            print(f"YOU WINS !!,YOU CHOOOSE {Name[Choice]},CPU CHOOSE   {Name[CPU_Choice]}")
            Wins+=1
    elif Choice =="Q":
        Done=True
    else:
        print("---------------INVALID COMMANTSS-----------------")

    print(F"\n---------------------------CURRENT STATES:\t{Wins} WINS,\t {Losses} LOSESS,\t{Ties} TIES")