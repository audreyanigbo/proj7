import json
import random 

def main():
    # TODO: allow them to choose from multiple JSON files?
    with open('spooky_mansion.json') as fp:
        game = json.load(fp)
        
        print_instructions()
        
    print("You are about to play '{}'! Good luck!".format(game['__metadata__']['title']))
    print("")
    play(game)
        

def play(rooms):
    # Where are we? Look in __metadata__ for the room we should start in first.
    current_place = rooms['__metadata__']['start']
    # The things the player has collected.
    stuff = ['Cell Phone; no signal or battery...']
    
    room_list = ['entranceHall', 'basement', 'attic', 'attic2', 'balcony', 'kitchen', 'dumbwaiter']
    cat_location = 'balcony'
    #print(cat_location)
    
    while True:
        # Figure out what room we're in -- current_place is a name.
        here = rooms[current_place]
        # Print the description.
        

    
            
        black_cat = rooms[cat_location]
        list_cat_exits = black_cat['exits']
        cat_exit = random.choice(list_cat_exits)
        cat_location = cat_exit['destination']
        
        if cat_location == current_place:
            print("There's a cat in this room!")
        
        print(cat_location)

        #print(here["description"]) 

        # TODO: print any available items in the room...
        print(here)
        
        # e.g., There is a Mansion Key.

        # Is this a game-over?
        if here.get("ends_game", False):
            break

        # Allow the user to choose an exit:
        usable_exits = find_visable_exits(here)
        # Print out numbers for them to choose:
        for i, exit in enumerate(usable_exits):
            print("  {}. {}".format(i+1, exit['description']))
            
         
             
        # See what they typed:
        action = input("> ").lower().strip()
        
        if action == "help":
            print_instructions()
            continue 

        # If they type any variant of quit; exit the game.
        if action in ["quit", "escape", "exit", "q"]:
            print("You quit.")
            break

        # TODO: if they type "stuff", print any items they have (check the stuff list!)
        
        if action == "stuff":
            for i in stuff:
                print (i)
            if len(stuff) == 0:   
                    print ("You have nothing")
            continue 
        # TODO: if they type "take", grab any items in the room.
        
        if action == "take":
            for item in here['items']:
                stuff.append(item)
            here['items'] = []
            continue
        
        
        if action == "drop":
            for i in range(len(stuff)):
                print(i + 1, stuff[i])
    
            chosen_item = input("Which item would you like to drop?")
            n = int(chosen_item)-1
            if n > len(stuff)-1:
                print("Your number is too big!")
            else:
                        
                    
                here['items'].append(stuff[n])
                stuff.pop(n)
            
    
                
        # TODO: if they type "search", or "find", look through any exits in the room that might be hidden, and make them not hidden anymore!
        if (action == "search") or  (action == "find"):
             for i in here['exits']:
                #if i['hidden'] == True:
                    i['hidden'] = False
                    print (i['hidden'])
                 
                     
                 
             
             
        # Try to turn their action into an exit, by number.
        try:
            num = int(action) - 1
            selected = usable_exits[num]
            print(selected)
            if "required_key" in selected:
                if selected['required_key'] not in stuff:
                    print("The door is locked! Look for a key!")
                    continue 
            current_place = selected['destination']
            print("...")
        except:
            print("I don't understand '{}'...".format(action))
        
    print("")
    print("")
    print("=== GAME OVER ===")
      
            
def find_visable_exits(room):
    """
    Given a room, and the player's stuff, find a list of exits that they can use right now.
    That means the exits must not be hidden, #and if they require a key, the player has it.

    RETURNS
     - a list of exits that are visible (not hidden) #and don't require a key!
    """
    usable = []
    for exit in room['exits']:
        if exit.get("hidden", False):
            continue

        usable.append(exit)
         
    return usable


    
    
    
def print_instructions():
    print("=== Instructions ===")
    print(" - Type a number to select an exit.")
    print(" - Type 'stuff' to see what you're carrying.")
    print(" - Type 'take' to pick up an item.")
    print(" - Type 'quit' to exit the game.")
    print(" - Type 'search' to take a deeper look at a room.")
    print("=== Instructions ===")
    print("")

if __name__ == '__main__':
    main()
