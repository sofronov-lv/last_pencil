import random


def initial_number_of_pencils() -> int:
    print("How many pencils would you like to use:")

    while True:
        try:
            pencils = int(input())
        except ValueError:
            print("The number of pencils should be numeric")
        else:
            if pencils > 0:
                return pencils
            print("The number of pencils should be positive")


def choosing_the_first_player(user: str, bot: str) -> str:
    print(f"Who will be the first ({user}, {bot}):")

    while True:
        name = input()
        if name in (user, bot):
            return name
        print(f"Choose between '{user}' and '{bot}'")


def user_walks(remaining_pencils: int) -> int:
    """
    The user's move is being executed, only numbers from 1 to 3 can be selected
    :param remaining_pencils: the number of pencils left in the game
    :return: number of pencils after user selection
    """
    while True:
        try:
            selected_pencils = int(input())
        except ValueError:
            print("Possible values: '1', '2' or '3'")
        else:
            if selected_pencils in (1, 2, 3):
                if remaining_pencils - selected_pencils >= 0:
                    return selected_pencils
                print("Too many pencils were taken")
            else:
                print("Possible values: '1', '2' or '3'")


def bot_walks(pencils_left: int) -> int:
    """
    Winning bot strategy! If the strategy is not found, selects a random number of pencils from 1 to 3
    :param: pencils_left: the number of pencils left in the game
    :return: number of pencils after bot selection
    """
    step = 4
    lower_bound = 0

    for i in range(1, pencils_left, step):
        lower_bound = i

    upper_bound = lower_bound + step

    if lower_bound < pencils_left < upper_bound:
        number_of_pencils = pencils_left - lower_bound
    elif pencils_left == 1:
        number_of_pencils = 1
    else:
        random.seed()
        number_of_pencils = random.randint(1, 3)

    print(number_of_pencils)
    return number_of_pencils


def main() -> None:
    pencils = initial_number_of_pencils()

    user, bot = "John", "Jack"  # initialization of the player and bot name
    player = choosing_the_first_player(user, bot)

    while pencils > 0:
        print("|" * pencils)
        print(f"{player}'s turn:")

        if player == bot:
            pencils -= bot_walks(pencils)
            player = user
        else:
            pencils -= user_walks(pencils)
            player = bot

        if not pencils:  # determines the winner
            print(f"{player} won!")
            exit()


if __name__ == "__main__":
    main()
