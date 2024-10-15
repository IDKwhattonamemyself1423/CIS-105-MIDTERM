import random

def guessing_game():

    secret_number = random.randint(1, 50)
    

    while True:
        guess = int(input("Guess the number between 1 and 50: "))
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed it right!")
            break
        
guessing_game()
