# Splinerlands Hangman by holoz0r - from day 7 of "100 days of code" in Python 

import random
from hangmanart import *
from hangmanwords import word_list

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
print(logo)
#Testing code
# print(f'Pssst, the solution is {chosen_word}.')
failures=[]
display = []
for _ in range(word_length):
    display += "_"
    
print("Your word to solve is: ",display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess in display:
        print("You already guessed this letter, its in the word!")
    
    if guess in failures:
        print(f"You have already guessed these letters: ", failures)
    
    if guess not in chosen_word and lives >0:
      lives -= 1
      failures.append(guess)
      print(f"You entered {guess} and that isn't in the word.")
      print(f"You have already guessed these letters: ", failures)
      print(f"You have {lives} lives left.")
      if lives == 0:
        end_of_game = True
        print("You Lose!")
        print(f"The Correct answer was {chosen_word}.")
    print(f"{' '.join(display)}")

    if "_" not in display:
      end_of_game = True
      print("You win.")

    print(stages[lives])
