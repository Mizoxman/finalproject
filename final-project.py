# Michael Hecox
# Final Project check-in

def readfileline(lineNumber):
    # returns the data from the specified line of the layout file
    hand = open("layout.txt")
    count = 0
    for line in hand:
        line = line.rstrip()
        count = count + 1
        if count == lineNumber:
            contents = line
        
    hand.close()
    return contents

def load():
    # placeholder until I get a saving and loading system working
    # eval() function to convert strings to dictionaries found at https://www.tutorialspoint.com/How-to-convert-a-String-representation-of-a-Dictionary-to-a-dictionary-in-Python
    playerInv = readfileline(417)
    playerInv = eval(playerInv[4:])
    room1Inv = readfileline(418)
    room1Inv = eval(room1Inv[4:])
    room2Inv = readfileline(419)
    room2Inv = eval(room2Inv[4:])
    room3Inv = readfileline(420)
    room3Inv = eval(room3Inv[4:])
    room4Inv = readfileline(421)
    room4Inv = eval(room4Inv[4:])
    room5Inv = readfileline(422)
    room5Inv = eval(room5Inv[4:])
    room6Inv = readfileline(423)
    room6Inv = eval(room6Inv[4:])
    room7Inv = readfileline(424)
    room7Inv = eval(room7Inv[4:])
    room8Inv = readfileline(425)
    room8Inv = eval(room8Inv[4:])
    return ("05", "north", playerInv, room1Inv, room2Inv, room3Inv, room4Inv, room5Inv, room6Inv, room7Inv, room8Inv)

def printInventory(Inventory):
    for key in Inventory:
        print(Inventory[key], key)
    if len(Inventory) == 0:
        print("nothing")
    return

def main():
    # initialize game
    position, orientation, playerInv, room1Inv, room2Inv, room3Inv, room4Inv, room5Inv, room6Inv, room7Inv, room8Inv = load()
    roomInvMapping = {'01': room1Inv, '02': room2Inv, '03': room3Inv, '04': room4Inv, '05': room5Inv, '06': room6Inv, '07': room7Inv, '08': room8Inv}
    playing = True
    while playing == True:
        
        if 'compass' in playerInv:
            knowDirection = True
        else:
            knowDirection = False
        
        if orientation == "north":
            offset = 0
        elif orientation == "south":
            offset = 13
        elif orientation == "west":
            offset = 26
        elif orientation == "east":
            offset = 39
        
        roomdata = (((int(position) - 1) * 52) + offset + 4)

        for x in range(5):
            descline = readfileline(roomdata)
            print(descline)
            roomdata = roomdata + 1
        print("you can see:")
        printInventory(roomInvMapping[position])
        if knowDirection == True:
            print("you are facing " + orientation)
        print("")
        playerInput = input("what do you want to do? ")
        print("")
        playerInput = playerInput.lower()
        # movement code, definitely a way to make this cleaner, worry about that after it works consistently
        if playerInput == "exit":
            playing = False
        elif playerInput == "quit":
            playing = False
        elif playerInput == "turn north":
            orientation = "north"
        elif playerInput == "turn south":
            orientation = "south"
        elif playerInput == "turn west":
            orientation = "west"
        elif playerInput == "turn east":
            orientation = "east"
        elif playerInput == "turn left":
            if orientation == "north":
                orientation = "west"
            elif orientation == "south":
                orientation = "east"
            elif orientation == "west":
                orientation = "south"
            elif orientation == "east":
                orientation = "north"
        elif playerInput == "turn right":
            if orientation == "north":
                orientation = "east"
            elif orientation == "south":
                orientation = "west"
            elif orientation == "west":
                orientation = "north"
            elif orientation == "east":
                orientation = "south"
        elif playerInput == "move north":
            roomdata = roomdata + 0
            targetroom = readfileline(roomdata)
            targetroom = targetroom[2:]
            #print(targetroom)
            if targetroom == "00":
                print("can't do that")
            else:
                position = targetroom
        elif playerInput == "move south":
            roomdata = roomdata + 1
            targetroom = readfileline(roomdata)
            targetroom = targetroom[2:]
            #print(targetroom)
            if targetroom == "00":
                print("can't do that")
            else:
                position = targetroom
        elif playerInput == "move west":
            roomdata = roomdata + 2
            targetroom = readfileline(roomdata)
            targetroom = targetroom[2:]
            #print(targetroom)
            if targetroom == "00":
                print("can't do that")
            else:
                position = targetroom
        elif playerInput == "move east":
            roomdata = roomdata + 3
            targetroom = readfileline(roomdata)
            targetroom = targetroom[2:]
            #print(targetroom)
            if targetroom == "00":
                print("can't do that")
            else:
                position = targetroom
        elif playerInput == "move forward":
            if orientation == "north":
                roomdata = roomdata + 0
            elif orientation == "south":
                roomdata = roomdata + 1
            elif orientation == "west":
                roomdata = roomdata + 2
            elif orientation == "east":
                roomdata = roomdata + 3
            targetroom = readfileline(roomdata)
            targetroom = targetroom[2:]
            #print(targetroom)
            if targetroom == "00":
                print("can't do that")
            else:
                position = targetroom
        elif playerInput == "move left":
            if orientation == "north":
                roomdata = roomdata + 2
            elif orientation == "south":
                roomdata = roomdata + 3
            elif orientation == "west":
                roomdata = roomdata + 1
            elif orientation == "east":
                roomdata = roomdata + 0
            targetroom = readfileline(roomdata)
            targetroom = targetroom[2:]
            #print(targetroom)
            if targetroom == "00":
                print("can't do that")
            else:
                position = targetroom
        elif playerInput == "move right":
            if orientation == "north":
                roomdata = roomdata + 3
            elif orientation == "south":
                roomdata = roomdata + 2
            elif orientation == "west":
                roomdata = roomdata + 0
            elif orientation == "east":
                roomdata = roomdata + 1
            targetroom = readfileline(roomdata)
            targetroom = targetroom[2:]
            #print(targetroom)
            if targetroom == "00":
                print("can't do that")
            else:
                position = targetroom
        elif playerInput == "inventory":
            # print contents of player inventory
            print("you are carrying: ")
            printInventory(playerInv)
        else:
            print("can't do that")
        print("")
    return

main()