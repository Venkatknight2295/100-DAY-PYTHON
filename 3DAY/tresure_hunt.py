print("Welcome to Tresure Island \n Your mission is to find the treasure")
direction= input("left or right ").lower()
if direction == "left":
  action = input("swim or wait").lower()
  if action == "wait":
     door = input ("which door").lower()
     if door == "yellow":
       print("you win")
     else: 
       print("game over")
  else:
    print("game over")
else:
  print("Game over")





