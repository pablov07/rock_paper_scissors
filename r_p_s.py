"""
Simple Rock, Paper, Scissors game using the random library
"""
import random

options = ("rock", "paper", "scissors")
running = True

while running:

    user_choice = None
    computer = random.choice(options)

    while user_choice not in options:
        user_choice = input("Enter rock, paper, scissors: ")

    print(f"Player: {user_choice}")
    print(f"Computer: {computer}")

    if user_choice == computer:
        print("It's a tie")

    elif user_choice == "rock" and computer == "scissors":
        print("You win")

    elif user_choice == "paper" and computer == "rock":
        print("You win")

    elif user_choice == "scissors" and computer == "paper":
        print("You win")

    else:
        print("You lose")

    #Adding a play again option for users to play more
    play_again = input("Play again? (y): ").lower()

    if play_again == "y":
        running = True
    else:
        print("Thanks for playing!")
        exit()
