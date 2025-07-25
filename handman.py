import random
sports = ["Tennis","Cricket","Football","Rugby","Baseball","Kabbadi","Badminton"] # here we have choosen the the sports
# print("Sporting names",sports)

stages = [
    '''
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
       |
    ''',
    '''
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
       |
    ''',
    '''
       ------
       |    |
       |    O
       |   /|\\
       |    
       |
       |
    ''',
    '''
       ------
       |    |
       |    O
       |    
       |    
       |
       |
    ''',
    '''
       ------
       |    |
       |    
       |    
       |    
       |
       |
    ''',
    '''
       ------
       |    
       |    
       |    
       |    
       |
       |
    ''',
    '''
    (No person yet)
    '''
]

guessing_word=random.choice(sports)# guessed random word

# print("random words:",guessing_word) 
starting_letter = guessing_word[0]
remaining_word = len(guessing_word) -1
underscore = ['_'] * remaining_word
display = [starting_letter] + underscore
print("Hint:",' '.join(display))



wrong_guess = 0
max_options_to_guess = 6

while True:
    guess = input("Guess a letter: ").lower()
    print("Word which guessed",guess)

    if guess in guessing_word:
        print("Keep going your doing gr8")

        for index,letter in enumerate(guessing_word):
            if letter == guess:
                display[index] = guess
    
        current_display = ' '.join(display)
        print("Current word:", current_display)

        if '_' not in display:
            print("🎉Congrats baby you won!!!!")
            break
    else:
        print("Opps its not right !!!!")
        wrong_guess = wrong_guess+1

        print(f"Wrong guesses: {wrong_guess}/{max_options_to_guess  }")

    print(stages[max_options_to_guess - wrong_guess])
    
    if wrong_guess >= max_options_to_guess:
        print("💔Game over try again!!!")
        break
