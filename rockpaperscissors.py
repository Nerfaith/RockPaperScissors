import random

options = ["Rock", "Paper", "Scissors"]

#This is to set up for the computer
computeroption = options[random.randint(0,2)] 

#Player now
playeroption = False 

#Main code now
while playeroption == False:
    playeroption = input("Rock, Paper or Scissors?\n")
    if playeroption == computeroption:
        print("Tie!")
    elif playeroption == "Rock":
        if computeroption == "Paper":
            print("You lose!", computeroption, "covers", playeroption)
        else :
            print("You win!", playeroption, "smashes", computeroption)
    elif playeroption == "Paper":
        if computeroption == "Scissors":
            print("You lose!", computeroption, "cut", playeroption)
        else:
            print("You win!", playeroption, "covers", computeroption)
    elif playeroption == "Scissors":
        if computeroption == "Rock":
            print("You lose!", computeroption, "smashes", playeroption)
        else:
            print("You win!", playeroption, "cut", computeroption)
    else:
        print("Invalid input, please retry")
    playeroption = False
    computeroption = options[random.randint(0,2)]
