import random
play_again = True
while play_again :
    number = random.randint(1 , 100)
    guess = int(input("The number is between 1and 100. Guess what it is: "))
    while number != guess :
        if guess < number :
            print("Too low. Try again. ")
        else:
            print("Too high. Try again. ")
        guess = int(input("Guess again: "))
    print("Congratulations! You guessed the right number: ",number)
    play_again_input = input("do you want to play again? (yes or no) ")
    play_again = play_again_input.lower() in ["yes", "y"]
 