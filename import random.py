import random

def play_game():
    while True:
        user_choice = input("Enter your choice (stone/paper/scissors): ").lower()
        possible_choices = ["stone", "paper", "scissors"]
        computer_choice = random.choice(possible_choices)
        
        print(f"\nUser chose {user_choice}, computer chose {computer_choice}.\n")

        if user_choice == computer_choice:
            print(f"Both players selected {user_choice}. It's a tie!")
        elif user_choice == "stone":
            if computer_choice == "scissors":
                print("stone smashes scissors! You win!")
            else:
                print("Paper covers stone! You lose.")
        elif user_choice == "paper":
            if computer_choice == "stone":
                print("Paper covers stone! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("stone smashes scissors! You lose.")
        else:
            print("Invalid input. Please try again.")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    play_game()
