import random

def get_user_choice():
    while True:
        user = input("Enter 'rock,' 'paper,' or 'scissors': ").lower()
        if user in ['rock', 'paper', 'scissors']:
            return user
        else:
            print("Invalid choice. Please enter 'rock,' 'paper,' or 'scissors'.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "User wins"
    else:
        return "Computer wins"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\n--- Rock, Paper, Scissors ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = winner(user_choice, computer_choice)
        print(result)

        if 'User' in result:
            user_score += 1
        elif 'Computer' in result:
            computer_score += 1

        print(f"\nScore - You: {user_score}, Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

play_game()



