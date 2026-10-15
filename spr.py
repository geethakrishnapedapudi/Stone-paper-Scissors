# Online Python compiler (interpreter)
# Write and run Python online using this ed
import random
print("Welcome to the Rock Paper Scissor Game!...")
print("1-Rock")
print("2-Paper")
print("3-Scissors")
choices=["rock","paper","scissors"]
up=0
cp=0

while True:
  print("---GAME RULES----")
  print("rock vs scissors---->rock wins")
  print("scissors vs paper---->scissors wins")
  print("paper vs rock----->paper wins")
  try:
    choice=int(input("Enter the choice:"))
  except ValueError:
    print("Enter the valid input(1-3)")
    continue
 
  while choice<1 or choice>3:
    choice=int(input("enter a valid input:"))
    
  user_choice=choices[choice-1]
  print("your choice is:",user_choice)
  print("Now its computer turn....")
  comp_choice=random.randint(1,3)
  computer_choice = choices[comp_choice-1]
  print("computer choice is:",computer_choice)
  print(user_choice,"vs",computer_choice)
  if computer_choice==user_choice:
     print("Game Tied...")
     up=up+1
     cp=cp+1
  elif((user_choice=="rock" and computer_choice=="scissors")or (user_choice=="scissors" and computer_choice=="paper")or (user_choice=="paper" and computer_choice=="rock")):
     print("YOU WON")
     up=up+1
  else:
     print("....Computer Won...")
     cp=cp+1
  while True:
    ans =input("Do you want to continue(y/n):").lower()
    if ans in ["y","n"]:
        break
    print("do you want to continue:")
  if ans=='n':
      break
  print()
print("Your Score is:",up)
print("Computer Score is:",cp)
print("\n Thank You for playing")
