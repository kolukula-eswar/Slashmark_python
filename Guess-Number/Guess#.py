import random
import time

def intro():
    print("May I ask you for your name?")
    name = input()
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 200.")
    time.sleep(0.5)
    print("Go ahead. Guess!")

def pick():
    number = random.randint(1, 200)
    guesses_taken = 0
    while guesses_taken < 6:
        time.sleep(0.25)
        enter = input("Guess: ")
        try:
            guess = int(enter)
            if 1 <= guess <= 200:
                guesses_taken += 1
                if guesses_taken < 6:
                    if guess < number:
                        print("The number you guessed is too low.")
                    elif guess > number:
                        print("The number you guessed is too high.")
                    else:
                        print("Congratulations! You guessed the number.")
                        break
                    print("Try Again!")
            else:
                print("The number is not in the range of 1 to 200.")
        except ValueError:
            print("That's not a valid number. Please enter a valid number.")

    if guess != number:
        print("Sorry, you ran out of attempts. The number I was thinking of was", number)

play_again = "yes"
while play_again.lower() in ("yes", "y"):
    intro()
    pick()
    play_again = input("Do you want to play again? (yes/no): ")
