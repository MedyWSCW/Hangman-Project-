answer = input ("Hello, welcome to our Hangman game. Do you know how to play Hangman?").upper().lower()
if answer == "yes":
    print("Great, our Hangman game will have different themes which are animals, villains, superheroes, dinosaurs and cartoons.")
    input("press enter to start")
if answer == "no":
    print("The aim of this game is to guess a random word before the hangman has been drawn.")
    print("Our Hangman game will have different themes which are animals, villains, superheroes, dinosaurs and cartoons.")
    input("Press enter to start")
