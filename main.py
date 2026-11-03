from game import (
    create_player,
    move_to_jungle,
    move_to_cave,
    cross_bridge,
    restore_lighthouse,
    check_energy
)


def play_game():

    print("\n================================")
    print("       MYSTERY ISLAND")
    print("       THE LOST LIGHTHOUSE")
    print("================================")
    print("You are stranded on a mysterious island.")
    print("Find the items you need and restore the Lighthouse.")
    print("Be careful! Your energy is limited.")

    name = input("\nEnter your name: ").strip()

    player = create_player(name)

    locations = [
        "Beach",
        "Jungle",
        "Cave",
        "Old Bridge",
        "Lighthouse"
    ]

    while not player["game_over"]:

        print("\nCurrent location:", player["location"])
        print("Energy:", player["energy"])
        print("Inventory:", player["inventory"])

        print("\nWhere would you like to go?")

        for location in locations:
            print(location)

        print("Quit")

        choice = input("Choose a location: ").strip().title()

        if choice == "Quit":
            player["game_over"] = True
            print("You have left the island. Goodbye!")
            continue

        if choice not in locations:
            print("Invalid location. Try again!")
            continue

        if choice == "Jungle" and player["location"] == "Beach":

            search = "no"

            if not player["searched_wreckage"]:
                search = input(
                    "Search the wreckage for supplies? (yes/no): "
                ).strip().lower()

                if search not in ["yes", "no"]:
                    print("Invalid answer. Try again!")
                    continue

                if search == "yes":
                    print("You found food! You gained 2 energy.")
                else:
                    print("You decided to leave the wreckage.")

            if move_to_jungle(player, search):
                print("You entered the Jungle!")
                print("You found a rope!")

        elif choice == "Cave" and player["location"] == "Jungle":

            print("\nYou have two paths to the Cave:")
            print("1. Safe path (costs 1 energy)")
            print("2. Dangerous shortcut (costs 2 energy)")

            path = input("Choose your path (1/2): ").strip()

            if path not in ["1", "2"]:
                print("Invalid path. Try again!")
                continue

            print("\nYou need to find a lantern.")
            print("1. Search carefully (costs 1 energy)")
            print("2. Search quickly (costs 2 energy)")

            search = input("Choose your search method (1/2): ").strip()

            if search not in ["1", "2"]:
                print("Invalid choice. Try again!")
                continue

            if move_to_cave(player, path, search):
                if path == "1":
                    print("You safely followed the Jungle path!")
                else:
                    print("You took the dangerous shortcut!")

                print("You entered the Cave!")

                if search == "1":
                    print("You carefully searched the Cave.")
                else:
                    print("You rushed through the Cave.")

                print("You found a lantern!")

        elif choice == "Old Bridge":

            if cross_bridge(player):
                print("You successfully crossed the Old Bridge!")
            else:
                print("You need to be in the Cave and have a rope!")

        elif choice == "Lighthouse":

            if restore_lighthouse(player):

                print("\nCongratulations,", player["name"])
                print("You restored the Lighthouse!")
                print("A rescue boat is coming!")
                print("YOU WIN!")

            else:
                print("You need to be at the Old Bridge and have a lantern!")

        else:
            print("You cannot move there from your current location!")

        if not check_energy(player):
            print("\nYou have run out of energy!")
            print("GAME OVER!")


def main():

    while True:

        play_game()

        while True:

            replay = input(
                "\nWould you like to play again? (yes/no): "
            ).strip().lower()

            if replay == "yes":
                print("\nRestarting Mystery Island!")
                break

            elif replay == "no":
                print("Thank you for playing Mystery Island!")
                return

            else:
                print("Invalid answer. Please enter yes or no.")


if __name__ == "__main__":
    main()