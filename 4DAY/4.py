import random
# 0 = "rock"
# 2 = scissiors
# 1 = paper
user_input = input("choose from the following rock or paper or scissiors ")
compute_choice = random.randint(0,1)
print(f"computer chose the following {compute_choice}")

if user_input == 0 and compute_choice == 2:
  print("you win")
elif user_input == 2 and compute_choice == 0:
  print ("")
elif user_input == compute_choice:
  print("draw")
elif  compute_choice > user_input:
   print("you lose")



#didnt continue as i got idea of it
