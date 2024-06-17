# Code for selecting the word from theme
import random 
themes = {
    "Superheros/Villians ": ["Spiderman", "Deadpool", "", "Riddler", "Thanos"],
    "Animals": ["Elephant", "Giraffe", "", "Lion", "Gorilla"],
    "Dinosaurs": ["Velociraptor", "Triceratops", "Spinosaurus", "", "Tyrannosaurus"]
}
def choose_word():
    theme = random.choice(list(themes.keys()))
    word = random.choice(themes[theme]).upper()
    return theme, word

# Welcome the player to the quiz
answer = input ("Hello, welcome to our Hangman game. Do you know how to play Hangman?").upper().lower()
# Tell the player the themes on the game if they say yes
if answer == "yes":
    print("Great, our Hangman game will have different themes which are animals, villains, superheroes, dinosaurs and cartoons.")
    input("press enter to start")
# Tell the player how to play the game if they answer no
if answer == "no":
    print("The aim of this game is to guess a random word before the hangman has been drawn.")
    print("Our Hangman game will have different themes which are animals, villains, superheroes, dinosaurs and cartoons.")
    input("Press enter to start")

