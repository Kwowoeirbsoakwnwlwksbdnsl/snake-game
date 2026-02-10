import random

print("Welcome to Snake 🐍 Water 💧 Gun 🔫 Game!")
print("Choices: s = Snake, w = Water, g = Gun")

choices = ['s', 'w', 'g']

while True:
    user = input("\nEnter your choice (s/w/g) or q to quit: ").lower()

    if user == 'q':
        print("Thanks for playing!")
        break

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print(f"Computer chose: {computer}")

    # Game logic
    if user == computer:
        print("It's a Draw!")

    elif (user == 's' and computer == 'w') or \
            (user == 'w' and computer == 'g') or \
            (user == 'g' and computer == 's'):
        print("You Win! 🎉")

    else:
        print("Computer Wins! 😄")
