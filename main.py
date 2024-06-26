play = "yes"
# Code for selecting the word from themes
import random 
themes = {
    "Superheros/Villians ": ["Spiderman", "Deadpool", "Riddler", "Thanos", "Batman"],
    "Animals": ["Elephant", "Giraffe", "Lion", "Gorilla", "Tiger"],
    "Dinosaurs": ["Velociraptor", "Triceratops", "Spinosaurus","Tyrannosaurus"]
}
def choose_word():
    theme = random.choice(list(themes.keys()))
    word = random.choice(themes[theme]).upper()
    return theme, word

#Functions to the current progress 
def display_current_progress(word, guessed_letters):
    display = [letter if letter in guessed_letters else "_" for letter in word]
    return " ".join(display)

#Functions to see the letters guessed 
def word_guessed(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

# Welcome the player to the qui
def intro():
    answer = input ("Hello, welcome to our Hangman game. Do you know how to play Hangman? (yes/no)").upper().lower()
    if answer == "yes":
        print("Great, our Hangman game will have different themes which are animals, villains, superheroes, dinosaurs and cartoons.")
        input("press enter to start")
    if answer == "no":
        print("The aim of this game is to guess a random word before the hangman has been drawn.")
        print("Our Hangman game will have different themes which are animals, villains, superheroes, dinosaurs and cartoons.")
        input("Press enter to start")
    else:
        print("That isn't an answer")



theme, word = choose_word()

Livesremaining = 9

   
# Hangman figure display

def show_hangman(tries):

    stages = [
                """
                   
                   |      
                   |      
                   |    
                   |      
                   |     
                   -
                """
                ,
                """
                   --------
                   |      
                   |      
                   |    
                   |      
                   |     
                   -
                """
                ,
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
                ,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """
                ,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      
                   |     
                   -
                """
                ,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """
                ,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """
                ,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     
                   -
                """
                ,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """
                ,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """
                ,
              
    ]
    
    return stages[tries]

    



#Code to see the current progress and display
def main():
    theme, word = choose_word()
    guessed_letters = set()
    attempts_remaining = 8
    tries = 9

    print(f"The chosen theme is {theme}.")
    print("The game will now start.")
    
    while attempts_remaining > 0:
        print(f"\nWord: {display_current_progress(word, guessed_letters)}")
        print(f"Attempts remaining: {attempts_remaining}")
        print(show_hangman(10 - tries))
        guess = input("Guess a letter: ").upper()
        
        if guess in guessed_letters:
            print(f"You have already guessed the letter'{guess}'.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good answer '{guess}' is in the word.")
        else:
            guessed_letters.add(guess)
            attempts_remaining -= 1
            tries -=1
            print(f"Unlucky, '{guess}' is not in the word.")
        
        if word_guessed(word, guessed_letters):
            print(f"Congratulations! You've guessed the word '{word}' correctly.")
            break
        if attempts_remaining == 0:
            print(show_hangman(10 - tries))
            print("Game over! The word was {}. Better luck next time".format (word))

    
    


#MAIN CODE 
intro()



#Replay
while play == "yes":
     main()
     play = input("Do you want to play again?").lower()
# Conclusion
print("\nThank you for starting our Hangman game! We hope you have a great time playing.")


     