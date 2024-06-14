import getpass

def get_hint(secret, guess):
    correct_position = sum(s == g for s, g in zip(secret, guess))
    correct_digit = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - correct_position
    return correct_position, correct_digit

def get_valid_guess(length):
    while True:
        guess = input(f"Enter your {length}-digit guess: ")
        if len(guess) == length and guess.isdigit():
            return guess
        print(f"Invalid input. Please enter a {length}-digit number.")

def play_round(setter, guesser):
    print(f"Player {setter}, set your secret number.")
    secret = getpass.getpass("Set your multi-digit secret number (it will be hidden): ")
    while not (secret.isdigit() and len(secret) > 0):
        print("Invalid input. Please enter a multi-digit number.")
        secret = getpass.getpass("Set your multi-digit secret number (it will be hidden): ")
        print(f"player {guesser},Now its time to guess the number!")

    attempts = 0
    while True:
        guess = get_valid_guess(len(secret))
        attempts += 1
        if guess == secret:
            print(f"Player {guesser} guessed the number in {attempts} attempts!")
            return attempts
        correct_position, correct_digit = get_hint(secret, guess)
        print(f"Hint: {correct_position} correct positions, {correct_digit} correct digits in wrong positions.")

def main():
    print("Welcome to the Mastermind Game!")
    attempts_player_2 = play_round(1, 2)  
    attempts_player_1 = play_round(2, 1)  
    
    if attempts_player_1 < attempts_player_2:
        print("Player 1 wins and is crowned Mastermind!")
    elif attempts_player_1 > attempts_player_2:
        print("Player 2 wins and is crowned Mastermind!")
    else:
        print("It's a tie! Both players guessed in the same number of attempts.")

if __name__ == "__main__":
    main()
