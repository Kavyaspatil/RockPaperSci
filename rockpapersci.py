import random
user_wins=0
computer_wins=0
options=["rock","paper","scissors"]
while True:
    user_input=input( "TYPE: 'rock' or 'paper' or 'scissors' or 'q' for quitting. : ").lower()
    if user_input=="q":
        break
    if user_input not in options:
        continue
    random_number=random.randint(0,2)
    computer_pick=options[random_number]
    print("Computer picked ", computer_pick)
    if user_input=="rock" and computer_pick=="scissors":
        print("YOU WON!!!")
        user_wins+=1
    elif user_input=="paper" and computer_pick=="rock":
        print("YOU WON!!!")
        user_wins+=1
    else:
        print("YOU LOST!")
        computer_wins+=1
print("YOU WON ",user_wins,"TIMES")
print("The Computer Won!!",computer_wins,"Times")
print("GOODBYE!!!!")
