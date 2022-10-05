import random


def user_walks(remaining_pencils):
    while True:
        try:
            selected_pencils = int(input())
        except ValueError:
            print("Possible values: '1', '2' or '3'")
        else:
            if selected_pencils in (1, 2, 3):
                if remaining_pencils - selected_pencils >= 0:
                    return selected_pencils
                else:
                    print("Too many pencils were taken")
            else:
                print("Possible values: '1', '2' or '3'")


def winning_bot_strategy(pencils_left):
    lower_bound = 0
    upper_bound = 0

    for i in range(-3, pencils_left, 4):
        lower_bound = i
        upper_bound = lower_bound + 4

    if lower_bound < pencils_left < upper_bound:
        return pencils_left - lower_bound
    else:
        return random_bot_walks(pencils_left)


def random_bot_walks(remaining_pencils):
    if remaining_pencils == 1:
        return 1
    return random.randint(1, 3)


print("How many pencils would you like to use:")
while True:
    try:
        pencils = int(input())
    except ValueError:
        print("The number of pencils should be numeric")
    else:
        if pencils > 0:
            break
        else:
            print("The number of pencils should be positive")

user, bot = "John", "Jack"
print(f"Who will be the first ({user}, {bot}):")

while True:
    player = input()
    if player in (user, bot):
        break
    else:
        print(f"Choose between '{user}' and '{bot}'")

while pencils > 0:
    print("|" * pencils)
    print(f"{player}'s turn:")

    if player == bot:
        choosing_a_bot = winning_bot_strategy(pencils)
        print(choosing_a_bot)
        pencils -= choosing_a_bot
        player = user
    else:
        pencils -= user_walks(pencils)
        player = bot

    if not pencils:
        print(f"{player} won!")
        exit()
