import os

from math import floor
from time import sleep as wait

from Modules.User import User
from Modules.FileIO import Read, Save
from Modules.Generate import Generate

# print("Display users list")
# for i in users:
#     print(f"{i.name} | {i.points}")

# Save(file, users)

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def Reset():
    return False, 0, -1




def Main():
    # Setup
    loggedInAs = User(0, "Guest")
    file = "Users.txt"
    users = Read(file)

    # Main Loop
    while True:
        # Reset guesses
        guessed, guesses, guess = Reset()

        # Log In
        changeUser = input(f"You are logged in as {loggedInAs.name}, would you like to log into another User? (y/n): ").lower()
        if changeUser == "y":
            username = input("Please enter your username: ")
            loggedInAs = User(0, username)

        print(f"Welcome back, {loggedInAs.name}!")
        
        number = Generate(6)
        print("A random number has been chosen.")

        while not guessed:
            print(f"Previous guess: {guess}")
            try:
                guess = int(input("Enter your guess: "))
            except Exception:
                guess = -1
                continue

            guesses += 1
            if guess == number:
                guessed = True
            elif guess > number:
                print("Lower")
            else:
                print("Higher")

        pointsGained = floor(100 / guesses)
        print(f"Congrats! You guessed it in {guesses} tries and earned: {pointsGained} points.")
        loggedInAs.points += pointsGained
        
        print(f"Total points: {loggedInAs.points}")

if __name__ == "__main__":
    Main()