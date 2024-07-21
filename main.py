import random
import art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against actual answer
def checking(guess, answer, turns):
    """check the guess against answer. Returns remaining turns"""
    if guess > answer:
        print("Too high")
        return turns -1
    elif guess < answer:
        print("Too low")
        return turns -1
    else:
        print(f"You got it right. The answer was {answer}")



# Make function to set difficulty 
def set_difficulty():
    difficulty_level = input("Choose difficulty. Type 'easy' or 'hard': ")
    if difficulty_level == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty_level == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("You entered the incorrect information") 




def game():
    print(art.logo)
    print("Welcome to the number guessing game. \nI'm thinking of a number between 1 and 100!")

    # Choosing a random number between 1 and 100
    answer = random.randint(1,100)
    print(f"Psst, the correct answer is {answer}")

    turns = set_difficulty()

    user_guess = 0
    while user_guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")


        # Let the user guesses a number
        user_guess = int(input("Make a guess: "))

        turns = checking(user_guess, answer, turns)
        if turns == 0:
            print("You've run out guesses. You lose!")
            return
        elif user_guess != answer:
            print("Guess again")

game()