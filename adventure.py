"""adventure - rudimentary adventure game
"""

rooms = {
        "Foyer": {
            "exits": {"N": "Dining Room", "E": "East Wing"},
            "items": ("lantern", "match")
            },
        "Dining Room": {
            "exits": {"S": "Foyer"},
            "items": ("knife")
            },
        "East Wing": {
            "exits": {"W": "Foyer"},
            "items": ()
            }
        }

current_room=next(iter(rooms)) #first key in dict == first room

def exits_from_room(room_name):
    """ returns the exits available from a room """
    return rooms[room_name]["exits"].keys()

def destination_from_room_exit(room_name, direction):
    """ returns the destination room given a starting room
        and a direction """
    return rooms[room_name]["exits"][direction]

def items_in_room(room_name):
    """ reutrns the list of items in a room,
        or None if there aren't any """
    return rooms[current_room]["items"]

if __name__ == "__main__":
    print("Good luck adventurer - commands are N, S, W, E and Q to quit.")
    while current_room != "end_room":
        print()
        print("you are in ",current_room)
        print("exits are ",list(exits_from_room(current_room)))
        if items_in_room(current_room) != ():
            print("items here are ",items_in_room(current_room))
        user_command = input("your command >")
        if user_command in exits_from_room(current_room):
            current_room = destination_from_room_exit(current_room, user_command)
        elif user_command == "Q":
            exit()
        else:
            print("you cannot go that way")
