import random

print("This is guessing game (The number you guessed and computer guessed matched you win.)")


input_number = int(input("Guess The number between (1 to 5) : \n"))

computer_number = random.randint(1, 5)

if input_number == computer_number:
    print(f"\nThe Number you guessed is {input_number} and computer guessed is {computer_number}")
    print("\tYou are WIN !!!")
else:
    print(f"\nThe number you guessed is {input_number} and computer guessed is {computer_number}")
    print("\tYou LOSE !!!")