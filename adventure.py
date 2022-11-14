"""adventure - rudimentary adventure game """

rooms = {
        "Foyer": {
            "exits": {"N": "Dining Room", "E": "East Wing"},
            "items": ["lantern", "match"]
            },
        "Dining Room": {
            "exits": {"S": "Foyer"},
            "items": ["knife"]
            },
        "East Wing": {
            "exits": {"W": "Foyer"},
            }
        }

current_room="Foyer"
end_room="East Wing"

if __name__ == "__main__":
    print("Good luck adventurer - commands are N, S, W, E and Q to quit.")
    while current_room != end_room:
        print()
        print("you are in ",current_room)
        print("exits are ",list(rooms[current_room]["exits"].keys()))

        if "items" in rooms[current_room].keys():
            print("items here are ",rooms[current_room]["items"])

        user_command = input("your command >")

        if user_command == "Q":
            exit()
            
        if user_command in rooms[current_room]["exits"].keys():
            current_room = rooms[current_room]["exits"][user_command]
        else:
            print("you cannot go that way")

    print("Congratulations - you've completed the adventure!")
