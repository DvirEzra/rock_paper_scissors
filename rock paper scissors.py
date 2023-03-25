import random


def get_user_choice():
    choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid input. Please enter rock, paper, or scissors: ").lower()
    return choice


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"


def play_round(round_num):
    print(f"Round {round_num}")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}, and computer chose {computer_choice}.")
    winner = determine_winner(user_choice, computer_choice)
    print(winner)
    return winner


def play_game():
    play_again = True
    while play_again:
        user_wins = 0
        computer_wins = 0
        num_rounds = 0

        print("Let's play Rock-Paper-Scissors!")

        while user_wins < 3 and computer_wins < 3:
            num_rounds += 1
            winner = play_round(num_rounds)

            if winner == "You win!":
                user_wins += 1
            elif winner == "Computer wins!":
                computer_wins += 1

            print(f"Score: You {user_wins} - Computer {computer_wins}")

        if user_wins > computer_wins:
            print("You win the game!")
        else:
            print("Computer wins the game.")

        play_again = input("Do you want to play again? (y/n) ").lower() == 'y'


play_game()

