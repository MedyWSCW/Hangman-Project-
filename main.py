play = "yes"
# Code for selecting the word from theme
from distutils.dep_util import newer
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
<<<<<<< HEAD

def display_hangman(tries):
=======
def show_hangman(tries):
>>>>>>> 953e7a86073a6f46cb74be270759cea0f44cb0ea
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
<<<<<<< HEAD
    # Welcome the player to the quiz

=======

# MAIN CODE

    while play == "yes":
    # Welcome the player to the quiz
        answer = input ("Hello, welcome to our Hangman game. Do you know how to play Hangman?").upper().lower()

    # Tell the player the themes on the game if they say yes

    if answer == "yes":
        print("Great, our Hangman game will have different themes which are animals, villains, superheroes, dinosaurs and cartoons.")
        input("press enter to start")
    else:
        print("That isn't an answer")

    # Tell the player how to play the game if they answer no

    if answer == "no":
        print("The aim of this game is to guess a random word before the hangman has been drawn.")
        print("Our Hangman game will have different themes which are animals, villains, superheroes, dinosaurs and cartoons.")
        input("Press enter to start")

    
    print ("The chosen theme is {}".format (theme))


    print("The game will now start.")


answer = input ("Hello, welcome to our Hangman game. Do you know how to play Hangman? (yes/no)").upper().lower()

# Tell the player the themes on the game if they say yes

if answer == "yes":
    print("Great, our Hangman game will have different themes which are animals, villains, superheroes, dinosaurs and cartoons.")
    input("press enter to start")
else:
    print("That isn't an answer")

# Tell the player how to play the game if they answer no

if answer == "no":
    print("The aim of this game is to guess a random word before the hangman has been drawn.")
    print("Our Hangman game will have different themes which are animals, villains, superheroes, dinosaurs and cartoons.")
    input("Press enter to start")

  
print ("The chosen theme is {}".format (theme))


print("The game will now start.")




>>>>>>> 953e7a86073a6f46cb74be270759cea0f44cb0ea

# Main Code

intro()



if Livesremaining == 0:

        print("Game over")
    
    # Conclusion
print("\nThank you for starting our Hangman game! We hope you have a great time playing.")
print("Remember, the goal is to guess the word before the hangman is fully drawn. Good luck!")


#Replay
play = input("Do you want to play again?").lower()