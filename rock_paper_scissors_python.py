import random
#rock paper scissors game using python.

user_input = input("Enter rock, paper scissors : ")

def computerchoice():
    arr = ["rock","paper","scissors"]
    computerChoice =random.randint(0,2)
    return arr[computerChoice]
def userVScomputer(player,computer):
    if player == computer:
        print(f"player : {user_input}\ncomputer : {computer}\nTie!")
    else:
        if player=="rock" and computer=='paper':
            print(f"player : {user_input}\ncomputer : {computer}\nComputer won!")
        elif player=="paper" and computer=="scissors":
            print(f"player : {user_input}\ncomputer : {computer}\nComputer Won")
        elif player=="scissors" and computer=="rock":
            print(f"player : {user_input}\ncomputer : {computer}\nComputer won!")
        elif computer=="scissors" and player=="rock":
            print(f"player : {user_input}\ncomputer : {computer}\nYou won!")
        else:
            invalid()
            # print(player)
            # print(computer)

def invalid():
    print("You entered wrong word, Enter rock, paper and scissors only!")

def empty():
    print("You didnt enter anything!\nInput is empty")
if user_input=="":
    empty()
else:
    userVScomputer(user_input,computerchoice())