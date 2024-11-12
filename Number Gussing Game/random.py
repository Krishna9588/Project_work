import random


def determine_winner(user_choice, system_choice):
    if user_choice == system_choice:
        return "Draw"
    elif (user_choice == "snake" and system_choice == "water") or \
            (user_choice == "water" and system_choice == "gun") or \
            (user_choice == "gun" and system_choice == "snake"):
        return "User wins!"
    else:
        return "System wins!"


def snake_water_gun_game():
    choices = ["snake", "water", "gun"]
    user_choice = input("Enter your choice (snake/water/gun): ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please choose snake, water, or gun.")
        return

    system_choice = random.choice(choices)
    print(f"System chose: {system_choice}")

    result = determine_winner(user_choice, system_choice)
    print(result)


if __name__ == "__main__":
    snake_water_gun_game()

# while True:
#     # Get user input
#     try:
#         a = int(input("Enter your choice (1: Length, 2: Weight, 3: Temperature, 4: Time, 0: Exit): "))
#     except ValueError:
#         print("Please enter a valid number.")
#         continue
#
#     if a == 0:
#         print("Exiting...")
#         break
#     elif a in options:
#         options[a]()
#     else:
#         print("Invalid Input")
