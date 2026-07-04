import random

print("=" * 40)
print("   STONE PAPER SCISSORS GAME")
print("=" * 40)

choices = ["stone", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    print("\nChoose one:")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "4":
        print("\nGame Over!")
        print(f"Your Score: {user_score}")
        print(f"Computer Score: {computer_score}")

        if user_score > computer_score:
            print("🎉 You Won the Game!")
        elif computer_score > user_score:
            print("💻 Computer Won the Game!")
        else:
            print("🤝 It's a Tie!")

        break

    if choice == "1":
        user = "stone"
    elif choice == "2":
        user = "paper"
    elif choice == "3":
        user = "scissors"
    else:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("\nYou chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a Tie!")

    elif (user == "stone" and computer == "scissors") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissors" and computer == "paper"):
        print("🎉 You Win!")
        user_score += 1

    else:
        print("💻 Computer Wins!")
        computer_score += 1

    print(f"\nScore -> You: {user_score} | Computer: {computer_score}")