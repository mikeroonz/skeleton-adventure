# Skeleton-adventure

A simple and extensible example of a text adventure.  Shows how complexity can be moved out of code and into data structures.

## Code walkthrough

It's common for beginners to write a lot of if-then-else code, which does work
and is initially easy to understand.  At some point in adding features, it becomes simpler
overall to make more sophistocated use of data structures with more general purpose 
code where differences in behaviour are controlled by the data.

This example makes heavy use of the Python built-in dictionary type, nesting a dictonary within a dictionary.
See https://docs.python.org/3/tutorial/datastructures.html#dictionaries.

Only the dict rooms and the starting value for current_room and end_room need be changed to
handle a completely different group of rooms, direction mapping and items.
The 19 lines of the "game loop" would remain the same.  The "game loop" is contained
within the `if __name__ == "__main__":` block and continues to run until the player
reaches the end_room or uses the 'Q' command to quit.

The rooms data structure is a dict that contains dicts and lists.  Here's the structure
with keys and values labelled and their data types indicated.

	rooms <dict> = {
		room_name <key/string>: <value/dict> {
			exits <key/string>: <value/dict> { direction <key/string> : destination <value/string>, ... },
			items <key/string>: <value/list> [ item <string>, ... ] 
			}, ...
		}

Note that the difference in "exits" haing a dict value and "items" having a list value
is why the exits are enclosed in '{}' characters and the items are in '[]' characters.
Exit directions needed to be mapped to the destination room, that's why the key "exits"
has a dict value.  Items don't need mapping to anything, so the "items" key has a list
value.

The dict has a key for every room.  For every room, there is a value that's a dict 
of the information for that room.  The keys in that dict are "exits" and "items".

The key "exits" has a dict as its value.  That dict maps exit directions to the 
destination room in that direction.  Keys are the directions, and values are the 
destination rooms.

The key "items" is a bit simpler - the value is just a list of items in that room.
If there are no items in the room, the key just isn't there.

For the room "East Wing", there are no items, so there's no key for items in the dict.
Before the list of items is printed, first check that there are items, otherwise
Python will stop with an exception.

	...
	if "items" in rooms[current_room],keys():
		...

Interactive debugging:

	if __name__ == "__main__":
		...

This line is there so that 'adventure' can be imported as a module for unit testing
and exploring via REPL.

	>python adventure.py

runs the adventure game

	>python
	Python 3.(something)...
	Type "help", "copyright", "credits" or "license" for more information.
	>>>from adventure import *`

runs the adventure.py file but since the __name__ is not "__main__" when
you do this, the program will stop after setting up the rooms.
Now you can try out python commands on the rooms data structure:

	>>>print(rooms["Foyer"]["exits"])
	{'N': 'Dining Room', 'E': 'East wing'}
	>>>print(rooms["Foyer"]["exits"].keys())
	dict_keys(['N', 'E'])	


## Suggestions for extension

### New room, new item

Both these changes can be done by just adding to the 'rooms' dict.  No change to 
the 'game loop' is needed.
Add a new room, a kitchen to the north of the dining room.  Test that this works by
running the code and going 'N' from the dining room - you should be in the kitchen.
Now go 'S' from the kitchen and you should be back in the dining room.

Add a new item 'EggWhisk' to appear in the kitchen.

### Advanced - item handling

Add item handling

	>get lantern
	OK you now have : lantern

	>light lantern
	With what?

	>get match
	OK you now have : lantern, match

	>light lantern
	OK the lantern lights up the Foyer, you can now see another exit to the West

Now the dict for the rooms info needs to be changed to include another exit from the Foyer.
This will require adding code to the 'game loop'.

### Expert - items interact with the environment

Add key items and a locked door.  The player must collect the key from one room, take it
to the locked door and unlock it.  Make sure the door can only be unlocked if the player
has the key.

