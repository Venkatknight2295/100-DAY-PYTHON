# word_list = ["venkat","kiang", "bufafer","thinangs"]
# import random
# chosen_word = random.choice(word_list)
# display = []
# for _ in range(len(chosen_word)):
#     display += "_"
# print(display)
   
# guess = input(" ").lower
# for position in range(len(chosen_word)):
#    letter = chosen_word[position]
# if letter == guess:
#  display[position] = letter 
# print(f"{display}") 

word_list = ["venkat" , "king" , "kituriuee"]  
import random 
chosen_word = random.choice(word_list)  
display = []
for u in range(len(chosen_word)):
    display += "_" 
print(display)    
print(f"{chosen_word}")
guess = input("guess the word").lower()
for position in range(len(chosen_word)):
    letter = chosen_word[position]
for n in chosen_word:
  if n == guess:
    print ("right")
  else:
      print("wrong")  
    