#!/usr/bin/env python3

"""
Number Guessing Game
Project: P01
Mission: M-1.1 — Syntax Soldier
Author: ManchiLearning
Date: May 25, 2026

Design decisions (fill in as you build):
- Why I chose [structure] over [alternative]:
- What I would change in a next version:
"""

import random

def choose_difficulty():
    """
    Asks the player to choose a difficulty level.
    Returns a tuple of (max_attempts, number_range).

    Design decisions: Returns a tuple rather than two separate
    values so the calling function receives everything it needs
    in one clean assignment.
    """
    
    print('\nChoose difficulty:')
    print('1. Easy (10 attempts, range 1-50)')
    print('2. Medium (7 attempts, range 1-100)')
    print('3. Hard (5 attempts, range 1-200)')

    difficulty_settings = {
        '1': (10, 50),
        '2': (7, 100),
        '3': (5, 200)
    }

    while True:
        choice = input('Enter 1, 2, or 3: ').strip()
        if choice in difficulty_settings:
            return difficulty_settings[choice]
        print('Please enter 1, 2, or 3.')
        

def get_valid_guess(number_range):
    """
    Asks the player for a guess and validates it is a number
    within the valid range. Keeps asking until valid input.
    
    Design decisions: Input validation lives in its own function
    rather than inside the game loop. This keeps the game loop
    readable and separates two distinct responsibilities.
    """

    # YOUR CODE HERE
    pass

def play_one_game(max_attempts, number_range):
    """
    Runs one complete game round.
    Returns True if player won, False if player lost.
    """
    secret_number = random.randint(1, number_range)
    attempts_used = 0

    print(f"\nI'm thinking of a number between 1 and {number_range}.")
    print(f"You have {max_attempts} attempts.\n")

    # YOUR CODE HERE
    # Loop for max_attempts
    # Get a valid guess each time
    # Check if too high, too low, or correct
    # If correct: return True
    # If attempts run out: reveal number, return False
    pass


def main():
    """Main program loop. Handles play again logic."""

    print("=" * 40)
    print("\tNUMBER GUESSING GAME")
    print("=" * 40)

    wins = 0
    total_games = 0

    # YOUR CODE HERE
    # Loop: play a game → ask play again → repeat or quit
    # Track wins and total games
    # Show session score when quitting
    pass


if __name__ == "__main__":
    main()