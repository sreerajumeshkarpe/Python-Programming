import random 
words=['python','apple','rose','grapes','laptop','mouse']
word=random.choice(words)

letters = len(word)
timesGuessed = 0

print("What word am I thinking of? You get 5 chances. ")
print("The word is ", letters, "letters long")

if word=='python':
   print("coding language")
elif word=='apple':
   print("a red fruit")
elif word=='rose':
   print("a beautiful flower")
elif word=='grapes':
   print("nashik is famous for this fruit")
elif word=='laptop':
   print("portable computer is called")
else:
   print("an input device")
while timesGuessed <= 5:
     guess = input("What is your guess? ")
     timesGuessed += 1

     if guess != word:
        print("I\'m sorry, that is not correct")
     elif guess == word:
         print("You guessed the correct word!")
         break
     elif timesGuessed == 5:
         print("You have run out of tries.")
     else:
         break
print("The correct word was", word)
print("Thank you for playing! Please press Enter to exit")

    


