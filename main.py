play = "yes"
# Code for selecting the word from themes
import random 
themes = {
    "Superheros/Villians ": ["Spiderman", "Deadpool", "", "Riddler", "Thanos", "Batman"],
    "Animals": ["Elephant", "Giraffe", "", "Lion", "Gorilla", "Tiger"],
    "Dinosaurs": ["Velociraptor", "Triceratops", "Spinosaurus", "", "Tyrannosaurus"]
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

def intro():
    answer = input ("Hello, welcome to our Hangman game. Do you know how to play Hangman? (yes/no)").upper().lower()
    if answer == "yes":
        print("Great, our Hangman game will have different themes which are animals, villains, superheroes, dinosaurs and cartoons.")
        input("press enter to start")
    else:
        print("That isn't an answer")
    if answer == "no":
        print("The aim of this game is to guess a random word before the hangman has been drawn.")
        print("Our Hangman game will have different themes which are animals, villains, superheroes, dinosaurs and cartoons.")
        input("Press enter to start")
    print ("The chosen theme is {}".format (theme))
    print("The game will now start.")



theme, word = choose_word()

Livesremaining = 11

def main():
    global Livesremaining
   
# Hangman figure display


def show_hangman(tries):

    stages = [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

    # Welcome the player to the quiz



#Code to see the current progress and display
def main():
    theme, word = choose_word()
    guessed_letters = set()
    attempts_remaining = 6

    print(f"The chosen theme is {theme}.")
    print("The game will now start.")
    
    while attempts_remaining > 0:
        print(f"\nWord: {display_current_progress(word, guessed_letters)}")
        print(f"Attempts remaining: {attempts_remaining}")
        print(show_hangman(6 - attempts_remaining))
        guess = input("Guess a letter: ").upper()
        
        if guess in guessed_letters:
            print(f"You have already guessed the letter'{guess}'.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good answer '{guess}' is in the word.")
        else:
            guessed_letters.add(guess)
            attempts_remaining -= 1
            print(f"Unlucky, '{guess}' is not in the word.")
        
        if word_guessed(word, guessed_letters):
            print(f"Congratulations! You've guessed the word '{word}' correctly.")
            break
    else:
        print(f"Game over! The word was '{word}'. Better luck next time.")


#MAIN CODE 
intro()
main()

if Livesremaining == 0:

        print("Game over")
    
    # Conclusion
print("\nThank you for starting our Hangman game! We hope you have a great time playing.")
print("Remember, the goal is to guess the word before the hangman is fully drawn. Good luck!")


#Replay
play = input("Do you want to play again?").lower()