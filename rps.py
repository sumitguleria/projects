import random

user_win=0
computer_win=0

options=["rock","paper","scissors"]
#list bnai ek rock papaer scissor ki or usko naam diya options
while True:
    user_input=input("typle rock/paper/scissors or Q to quit:").lower()
    if user_input=="q":
         break

    if user_input not in options:
         continue
        
    random_number = random.randint(0, 2)
       
    computer_pick = options[random_number]
    print("computer picked",computer_pick + ".")

    if user_input =="rock" and computer_pick== "scissors":
        print("you won")
        user_win += 1
        
    elif user_input =="scissors" and computer_pick== "paper":
        print("you won")
        user_win += 1
        
    elif user_input =="paper" and computer_pick== "rock":
        print("you won")
        user_win += 1
    elif user_input== computer_pick:
        print("tie")
    else:
        print("you lost")
        computer_win += 1
print("your score is:",user_win)
print("computer score is:",computer_win)
print("thats it")



