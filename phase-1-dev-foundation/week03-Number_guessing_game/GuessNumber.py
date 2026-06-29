import random

secret_number = random.randint(1, 100)

print("GAME Start!!!")

wins = 0
lose = 0
high_score = 0

round = 0
max_attempt = 0
current_attempt = 0
won = False


i = 0
difficulty = input("Select EASY or HARD: ").lower()
if difficulty == "easy":
    max_attempt = 10
elif difficulty == "hard":
    max_attempt = 5
else:
    print("Invalid difficulty")
    exit()

while current_attempt < max_attempt:
    print(f"attempt {current_attempt + 1} of {max_attempt}:")
    try:
        guess = int(input("Enter Guess: "))
    
        if guess == secret_number:
            print(f"You won. The number was {secret_number}")
            round += 1
            won += 1
            won  = True

            score = max_attempt - current_attempt
            if score > high_score:
                high_score = score
            break

        elif guess < secret_number:
            print("Too low")    
        elif guess > secret_number:
            print("Too High") 
        current_attempt += 1

    except ValueError:
        print("Invalid number")  

if not won:
    print(f"\nGame Over. The number was {secret_number}")
    lose += 1    

    print("\nScore_board")
    print("Wins:", wins)     
    print("loses:", lose)
    print("Highscore:", high_score)

    replay = input("\nPlay again? (yes/no): ").lower()
    if replay != "yes":
        print("Thanks for playing")

        exit()




    



    

    

