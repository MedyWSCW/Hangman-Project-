# Code for selecting the word from theme
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

def display_hangman(tries):
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
    # Welcome the player to the quiz


# MAIN CODE

intro()



if Livesremaining == 0:

        print("Game over")
    
    # Conclusion
print("\nThank you for starting our Hangman game! We hope you have a great time playing.")
print("Remember, the goal is to guess the word before the hangman is fully drawn. Good luck!")


if __name__ == "__main__":
    main()

