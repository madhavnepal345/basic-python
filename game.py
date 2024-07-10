import random
random_number= random.randint(1, 20)
guesses=1
while True:
    user_guess=int(input("Enter the gussed number: "))
    if user_guess==random_number:
        print(f"Congratulations 🥳🥳🥳🥳🥳! You guessed at {guesses} attempt.")
        break
    
    elif user_guess<random_number:
        print("Your guess is too low. Try again.")
        guesses+=1
    else:
        print("Your Guess is too high")
        guesses+=1

    