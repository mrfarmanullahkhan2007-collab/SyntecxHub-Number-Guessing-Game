import random

class guess_game:
    def __init__(self, player_name):
        self.player_name = player_name
        self.bestScore = None

    def play_easy_game(self):
        Easy_guess_num = random.randint(1, 10) 
        turns = 0
        print(f"\nWelcome to Easy Game: {self.player_name}")
        while True:
            try:
                user_input = int(input("Enter a number between 1 to 10: "))
                turns += 1
                if user_input == Easy_guess_num:
                    print(f"Congratulations! You Win in {turns} attempts...")
                    # Record check
                    if self.bestScore is None or turns < self.bestScore:
                        self.bestScore = turns
                        print("🏆 New Record Set!")
                  
                    print(f"Your best (lowest) Attempts: {self.bestScore}")
                    break
                elif user_input < Easy_guess_num:
                   print("Low value you guessed.")
                elif user_input > Easy_guess_num:
                  print("High value you guessed.")
            except ValueError:
                print("ERROR: Please enter a valid value.........")
                
    def play_moderate_game(self):
        moderate_guess_num = random.randint(1, 50) 
        turns = 0
        print(f"\nWelcome to Moderate Game: {self.player_name}")
        while True:
            try:
                user_input = int(input("Enter a number between 1 to 50: "))
                turns += 1
                if user_input == moderate_guess_num:
                    print(f"Congratulations! You Win in {turns} attempts...")
                    if self.bestScore is None or turns < self.bestScore:
                        self.bestScore = turns
                        print("🏆 New Record Set!")
                    print(f"Your best (lowest) Attempts: {self.bestScore}")
                    break
                elif user_input < moderate_guess_num:
                   print("Low value you guessed.")
                elif user_input > moderate_guess_num:
                  print("High value you guessed.")
            except ValueError:
                print("ERROR: Please enter a valid value.........")

    def play_difficult_game(self):
        different_guess_num = random.randint(1, 100) 
        turns = 0
        print(f"\nWelcome to Difficult Game: {self.player_name}")
        while True:
            try:
                user_input = int(input("Enter a number between 1 to 100: "))
                turns += 1
                if user_input == different_guess_num:
                    print(f"Congratulations! You Win in {turns} attempts...")
                    if self.bestScore is None or turns < self.bestScore:
                        self.bestScore = turns
                        print("🏆 New Record Set!")
                    print(f"Your best (lowest) Attempts: {self.bestScore}")
                    break
                elif user_input < different_guess_num:
                    print("Low value you guessed.")
                elif user_input > different_guess_num:
                    print("High value you guessed.")
            except ValueError:
                print("ERROR: Please enter a valid value.........")

if __name__ == "__main__":
    user_name = input("Enter player name: ")
    
    game = guess_game(user_name) 
    
    while True: # Repetition Loop
        print("\nCHOOSE LEVEL!")
        print("1. EASY GAME (1-10)")
        print("2. MODERATE GAME (1-50)")
        print("3. DIFFICULT GAME (1-100)")
        
        choice = input("Your level (1/2/3): ").strip()
        
        if choice == '1':
            game.play_easy_game()
        elif choice == '2':
            game.play_moderate_game()
        elif choice == '3':
            game.play_difficult_game()
        else:
            print("......Error: Invalid Level......")
            continue
            
      
        user_choice = input("\nDo you want to play again (y/n)? ").lower().strip()
        if user_choice != "y":
            print(f"Thanks for playing, {user_name}! Final Best Score: {game.bestScore}")
            print("GOODBYE.")
            break