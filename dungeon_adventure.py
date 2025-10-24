import random


def main():
    def setup_player():
        """
        Prompts the user to create their player profile.

        Returns:
            dict: A dictionary containing player stats with the following keys:
                - "name" (str): Player's name (entered by user)
                - "health" (int): Starting health, set to 10
                - "inventory" (list): Starts as an empty list
        Example:
            >>> setup_player()
            Enter your name: Ailene
            {'name': 'Ailene', 'health': 10, 'inventory': []}
        """
        # TO DO: Ask the user for their name using input()
        # TO DO: Initialize a dictionary with keys: "name", "health", and "inventory"
        # TO DO: Return the dictionary
        name = input("Please enter your name: ").capitalize()

        dict_players = {'name': name, 'health': 10, 'inventory': []}
        # print(dict_players)
        return dict_players

    def create_treasures():
        """
        Creates a dictionary of treasures, where each treasure has a value.

        Returns:
            dict: Example:
                {
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
                }
        Tip:
            You can customize treasures or randomize the values using random.randint(3, 12).
        """
        # TO DO: Create a dictionary of treasure names and integer values
        # TO DO: Return the dictionary
        dict_treasures = {
            "gold coin": random.randint(3, 12),
            "ruby": random.randint(3, 12),
            "sword": random.randint(3, 12),
            "potion": random.randint(3, 12),
            "silver coin": random.randint(3, 12),
            "emerald": random.randint(3, 12),
            "jewel": random.randint(3, 12)
        }
        # print(dict_treasures)
        return dict_treasures

    def display_options(room_number):
        """
        Displays available options for the player in the current room.

        Args:
            room_number (int): The current room number.

        Output Example:
            You are in room 3.
            What would you like to do?
            1. Search for treasure
            2. Move to next room
            3. Check health and inventory
            4. Quit the game
        """
        # TO DO: Print the room number and the 4 menu options listed above
        dict_options = {
            "1": "Search for treasure",
            "2": "Move to next room",
            "3": "Check health and inventory",
            "4": "Quit the game",
        }

        print(f"You are in room {room_number}")
        print("What would you like to do?")
        for x, y in dict_options.items():
            print(f"{x}. {y}")

        playerChoice = int(input("Enter your choice (1-4): "))
        return playerChoice

    def search_room(player, treasures):
        """
        Simulates searching the current room.

        If the outcome is 'treasure', the player gains an item from treasures.
        If the outcome is 'trap', the player loses 2 health points.

        Args:
            player (dict): The player's current stats.
            treasures (dict): Dictionary of available treasures.

        Behavior:
            - Randomly choose outcome = "treasure" or "trap"
            - If treasure: choose a random treasure, add to player's inventory,
              and print what was found.
            - If trap: subtract 2 from player's health and print a warning.
        """
        # TO DO: Randomly assign outcome = random.choice(["treasure", "trap"])
        # TO DO: Write an if/else to handle treasure vs trap outcomes
        # TO DO: Update player dictionary accordingly
        # TO DO: Print messages describing what happened
        outcome = random.choice(["treasure", "trap"])

        if outcome == "treasure":
            treasureGained = random.choice(list(treasures.keys()))
            player['inventory'].append(treasureGained)
            print(f"You found a(n) {treasureGained}!")
        elif outcome == "trap":
            player['health'] -= 2
            print(
                f"Warning! You fell into a trap which has taken your health down to {player['health']}")
        return player

    def check_status(player):
        """
        Displays the player’s current health and inventory.

        Args:
            player (dict): Player stats including health and inventory.

        Example Output:
            Health: 8
            Inventory: ruby, gold coin
        or:
            Health: 10
            Inventory: You have no items yet.
        """
        # TO DO: Print player health
        # TO DO: If the inventory list is not empty, print items joined by commas
        # TO DO: Otherwise print “You have no items yet.”

        print(f"Health: {player['health']}")

        if player['inventory']:
            print(f"Inventory: {', '.join(player['inventory'])}")
        else:
            print("You have no items yet.")
        return player

    def end_game(player, treasures):
        """
        Ends the game and displays a summary.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary for item value lookup.

        Output:
            Prints player’s final health, inventory contents, and total score value.
        """
        # TO DO: Calculate total score by summing the value of collected treasures
        # TO DO: Print final health, items, and total value
        # TO DO: End with a message like "Game Over! Thanks for playing."
        totalScore = sum(treasures.values())
        print(f"Final health: {player['health']}")

        if player['inventory']:
            print(f"Final inventory: {', '.join(player['inventory'])}")
        else:
            print("You finished with no inventory. Sad.")

        print(f"Your final score is: {totalScore}")
        print("Game Over! Thanks for playing.")

    def run_game_loop(player, treasures):
        """
        Main game loop that manages the rooms and player decisions.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary.

        Flow:
            - There are 5 rooms (use for loop range(1, 6))
            - Inside each room, use a while loop for player actions:
                1. Search room
                2. Move to next room
                3. Check status
                4. Quit
            - Health below 1 ends the game early.
        """
        # TO DO: Loop through 5 rooms (1–5)
        # TO DO: Inside each room, prompt player choice using input()
        # TO DO: Use if/elif to handle each choice (1–4)
        # TO DO: Break or return appropriately when player quits or dies
        # TO DO: Call end_game() after all rooms are explored
        currRoom = 1  # starting room

        while currRoom <= 5:
            choice = display_options(currRoom)

            if choice == 1:
                search_room(player, treasures)
            elif choice == 2:
                print(f"Moving to room {currRoom + 1}...\n")
                currRoom += 1  # move to next room
            elif choice == 3:
                print("Checking player status:")
                check_status(player)
            elif choice == 4:
                print("You chose to quit.")
                end_game(player, treasures)
                return
            else:
                print("Invalid choice! Please enter 1-4.\n")
                continue

            # Check if player died during any action
            if player["health"] < 1:
                print("You have died!")
                end_game(player, treasures)
                return

        # All rooms explored
        print("You have explored all rooms!")
        end_game(player, treasures)

    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)


if __name__ == "__main__":
    main()
