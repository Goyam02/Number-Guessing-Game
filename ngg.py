import random
import emoji
from colorama import init, Fore, Style

init(autoreset=True)

def ngg():
    print(Style.BRIGHT + Fore.RED + "Welcome to the Random Number Guessing Game!")
    print(Fore.YELLOW + "The rules are as follows:")
    print(Style.BRIGHT + Fore.BLUE + "1. The game generates a random number between 1 and 99.")
    print(Style.BRIGHT + Fore.BLUE + "2. You have 7 attempts to guess the correct number.")
    print(Style.BRIGHT + Fore.BLUE + "3. After each guess, you will receive feedback:")
    print(Fore.CYAN + "   - 'Too High!' if your guess is higher than the number.")
    print(Fore.CYAN + "   - 'Too Low!' if your guess is lower than the number.")
    print(Fore.CYAN + "   - 'Congratulations!' if you guess correctly.")
    print(Style.BRIGHT + Fore.BLUE + "4. You must enter a valid number between 1 and 99. Invalid inputs will not count as attempts.")
    print(Style.BRIGHT + Fore.BLUE + "5. After 3 failed attempts, you might receive a hint.")
    print(Style.BRIGHT + Fore.BLUE + "6. If you guess correctly within 7 attempts, you win!")
    print(Style.BRIGHT + Fore.BLUE + "7. If you fail to guess within 7 attempts, the game reveals the correct number and ends.")
    print(Style.BRIGHT + Fore.BLUE + "8. You can choose to play again after the game ends.")
    print(Style.BRIGHT + Fore.YELLOW + "Good luck!")

    random_number = random.randint(1, 99)
    # print(random_number)

    attempts = 7
    for attempt in range(1, attempts + 1):
        try:
            user_input = int(input(Fore.YELLOW + "Enter your choice (1-99): "))
            
            if user_input < 1 or user_input > 99:
                print(Fore.RED + "Invalid input! Please enter a number between 1 and 99.")
                continue
            
            if user_input == random_number:
                print(emoji.emojize(Fore.GREEN + f"Congratulations! You guessed it correctly! :check_mark_button:"))
                break
            elif user_input > random_number:
                print(Fore.RED + "Too High! Try again.")
            else:
                print(Fore.RED + "Too Low! Try again.")

            if attempt == 3:
                hint = "even" if random_number % 2 == 0 else "odd"
                print(Fore.CYAN + f"Hint: The number is {hint}.")

            remaining_attempts = attempts - attempt
            if remaining_attempts > 0:
                print(Fore.YELLOW + f"You have {remaining_attempts} attempts left.")
            else:
                print(Fore.RED + f"Sorry, you've used all your attempts. The correct number was {random_number}. Better luck next time!")

        except ValueError:
            print(Fore.RED + "Invalid input! Please enter a valid number.")

    print(Style.BRIGHT + Fore.GREEN + "Game Over! Thank you for playing.")
    play_again = input(Fore.BLUE + "Would you like to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        ngg()

ngg()