import random

print("        Guess Game           ")
name = input("Enter Your Name: ")
nbr = random.randint(1, 100)
guess = -1
count = 0
while nbr != guess:
    guess = int(input("Enter nbr for guess: "))
    if guess < nbr:
        print("little higher")
    if guess > nbr:
        print("little less")
    count += 1
else:
    print(
        f"Congratulation perfect guess {name}! you have guessed in {count} times.\n             Well done! keep it up."
    )
