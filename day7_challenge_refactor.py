#######################################################
# HANGMAN GAME
#######################################################
# NOTES:
# While loop structure
# # set condition to start the loop
# # set condition to end the loop 
# enumerate and range function, index
# initializing the variables
# indentations!


import random
from hangman_words import word_list
from hangman_art import stages, logo

#Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = [ardvark, baboon, camel]
chosen_word = random.choice(word_list)
#word_length = len(chosen_word)

end_of_game = False
lives = 6

#Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
#for _ in range(word_length):
#    display += _

# code with append
for letter in chosen_word:
	display.append('_')

while not end_of_game:
    guess = input(Guess a letter: ).lower()

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(fYou've already guessed letter {guess}.)
    #Check guessed letter
    for index, letter in enumerate(chosen_word):
        letter = chosen_word[index]
        #print(fCurrent position: {position}\n Current letter: {letter}\n Guessed letter: {guess})
        if letter == guess:
            display[index] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(fYou guessed letter {guess}, that's not is the word. You lose a life.)
        if lives == 0:
            end_of_game = True
            print(You lose.)
        
    #Join all the elements in the list and turn it into a String.
    print(f{' '.join(display)})

    #Check if user has got all letters.
    if _ not in display:
        end_of_game = True
        print(You win.)

    #Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])