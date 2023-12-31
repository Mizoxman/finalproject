# Michael Hecox
# Student ID # 00243521
# Course # CIS-153-L8
# Final Project
# simple text adventure game framework

import re

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

def loadNew():
    # loads starting game state
    
    # find the start of where the inventories are stored
    hand = open("layout.txt")
    count = 0
    for line in hand:
        line = line.rstrip()
        count = count + 1
        if re.search('{', line):
            break
    hand.close()
    #print(count)
    
    # eval() function to convert strings to dictionaries found at https://www.tutorialspoint.com/How-to-convert-a-String-representation-of-a-Dictionary-to-a-dictionary-in-Python
    playerInv = readfileline(count)
    playerInv = eval(playerInv[4:])
    room1Inv = readfileline(count + 1)
    room1Inv = eval(room1Inv[4:])
    room2Inv = readfileline(count + 2)
    room2Inv = eval(room2Inv[4:])
    room3Inv = readfileline(count + 3)
    room3Inv = eval(room3Inv[4:])
    room4Inv = readfileline(count + 4)
    room4Inv = eval(room4Inv[4:])
    room5Inv = readfileline(count + 5)
    room5Inv = eval(room5Inv[4:])
    room6Inv = readfileline(count + 6)
    room6Inv = eval(room6Inv[4:])
    room7Inv = readfileline(count + 7)
    room7Inv = eval(room7Inv[4:])
    room8Inv = readfileline(count + 8)
    room8Inv = eval(room8Inv[4:])
    return ("05", "north", playerInv, room1Inv, room2Inv, room3Inv, room4Inv, room5Inv, room6Inv, room7Inv, room8Inv)

def printInventory(Inventory):
    for thing in Inventory:
        print(Inventory[thing], thing)
    if len(Inventory) == 0:
        print("nothing")
    return

def turn(orientation,turning,knowDirection):
    # handle player turning
    cardinals = ['north', 'south', 'west', 'east']
    left = {'north': 'west', 'west': 'south', 'south': 'east', 'east': 'north'}
    right = {'north': 'east', 'east': 'south', 'south': 'west', 'west': 'north'}
    if turning in cardinals:
        if knowDirection == True:
            orientation = turning
        else:
            print("don't know " + turning)
    elif turning == 'left':
        orientation = left[orientation]
    elif turning == 'right':
        orientation = right[orientation]
    else:
        print("can't do that")
    return orientation

def move(orientation,roomdata,knowDirection,direction):
    # handle player movement
    cardinals = {'north': 0, 'south': 1, 'west': 2, 'east': 3}
    forward = {'north': 0, 'south': 1, 'west': 2, 'east': 3}
    left = {'north': 2, 'south': 3, 'west': 1, 'east': 0}
    right = {'north': 3, 'south': 2, 'west': 0, 'east': 1}
    if direction in cardinals:
        if knowDirection == True:
            roomdata = roomdata + cardinals[direction]
            targetroom = readfileline(roomdata)
            targetroom = targetroom[2:]
        else:
            targetroom = "00"
            print("Don't know " + direction)
    elif direction == 'forward':
        roomdata = roomdata + forward[orientation]
        targetroom = readfileline(roomdata)
        targetroom = targetroom[2:]
    elif direction == 'left':
        roomdata = roomdata + left[orientation]
        targetroom = readfileline(roomdata)
        targetroom = targetroom[2:]
    elif direction == 'right':
        roomdata = roomdata + right[orientation]
        targetroom = readfileline(roomdata)
        targetroom = targetroom[2:]
    else:
        targetroom = "00"
    return targetroom

def invTransfer(playerInv, roomInv, thing):
    #moves an object between 2 inventories, and erases its entry in an inventory if the count falls to 0
    if thing not in playerInv:
        playerInv[thing] = 1
    else:
        playerInv[thing] = playerInv[thing] + 1
    roomInv[thing] = roomInv[thing] - 1
    roomInv2 = dict()
    for thing in roomInv:
        if roomInv[thing] > 0:
            roomInv2[thing] = roomInv[thing]
    return (playerInv, roomInv2)

def main():
    # initialize game
    position, orientation, playerInv, room1Inv, room2Inv, room3Inv, room4Inv, room5Inv, room6Inv, room7Inv, room8Inv = loadNew()
    roomInvMapping = {'01': room1Inv, '02': room2Inv, '03': room3Inv, '04': room4Inv, '05': room5Inv, '06': room6Inv, '07': room7Inv, '08': room8Inv}
    playing = True
    # start of main loop
    while playing == True:
        
        # checks if the player is holding a compass, which enables or disables certain information and movement options
        if 'compass' in playerInv:
            knowDirection = True
        else:
            knowDirection = False
        
        # represents the way the room data is formatted in the text file, so that it may be extracted seamlessly
        if orientation == "north":
            offset = 0
        elif orientation == "south":
            offset = 13
        elif orientation == "west":
            offset = 26
        elif orientation == "east":
            offset = 39
        roomdata = (((int(position) - 1) * 52) + offset + 4)
        
        # print room description
        for x in range(5):
            descline = readfileline(roomdata)
            print(descline)
            roomdata = roomdata + 1
        # print contents of room inventory
        print("you can see:")
        printInventory(roomInvMapping[position])
        if knowDirection == True:
            print("you are facing " + orientation)
        print("")
        playerInput = input("what do you want to do? ")
        print("")
        playerInput = playerInput.lower()
        
        # split player inputs for easier parsing in some instances
        playerInput1 = playerInput[0:4]
        playerInput2 = playerInput[5:len(playerInput)]
        
        # quit game
        if playerInput1 == "exit":
            playing = False
        elif playerInput1 == "quit":
            playing = False
        # player turning code
        elif playerInput1 == "turn":
            orientation = turn(orientation, playerInput2, knowDirection)
        # player movement code
        elif playerInput1 == "move":
            targetroom = move(orientation, roomdata, knowDirection, playerInput2)
            if targetroom == "00":
                # 00 represents invalid movement, any attempts to walk through walls results in the target being set as room 00, which then prevents any movement
                print("can't do that")
            else:
                position = targetroom
        # print contents of player inventory
        elif playerInput == "inventory":
            print("you are carrying: ")
            printInventory(playerInv)
        elif playerInput1 == "take":
            # take objects you find in rooms and add them to your inventory
            if playerInput2 in roomInvMapping[position]:
                playerInv, roomInvMapping[position] = invTransfer(playerInv, roomInvMapping[position], playerInput2)
            else:
                print("there is no " + playerInput2)
        elif playerInput1 == "drop":
            # drop objects out of your inventory into the current room
            if playerInput2 in playerInv:
                roomInvMapping[position], playerInv = invTransfer(roomInvMapping[position], playerInv, playerInput2)
            else:
                print("you don't have a " + playerInput2)
        # this basically just resets the loop without taking any actions
        elif playerInput1 == "look":
            print("you take a look around")
        else:
            print("can't do that")
        print("")
    return

main()