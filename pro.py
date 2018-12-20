#SREERAJ KARPE
#M_28 
#GUESSING GAME
import random
from easygui import *
 
words=['python','apple','rose','grapes','laptop','mouse']
word=random.choice(words)

letters = len(word)
timesGuessed = 0
msgbox("What word am I thinking of? You get 5 chances.")

if word=='python':
   msgbox("coding language")
elif word=='apple':
   msgbox("a red fruit")
elif word=='rose':
   msgbox("a beautiful flower")
elif word=='grapes':
   msgbox("nashik is famous for this fruit")
elif word=='laptop':
   msgbox("portable computer is called")
else:
   msgbox("an input device")
while timesGuessed <= 5:
    
     guess = easygui.enterbox()
     timesGuessed += 1

     if guess != word:
        msgbox("I\'m sorry, that is not correct")
     elif guess == word:
         msgbox("You guessed the correct word!")
         break
     elif timesGuessed == 5:
         msgbox("You have run out of tries.")
     else:
         break
print("The correct word was", word)
print("Thank you for playing! Please press Enter to exit")
