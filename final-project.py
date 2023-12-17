# Michael Hecox
# Final Project check-in

def readfile(lineNumber):
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
    return ("05", "north")

def main():
    # initialize game
    position, orientation = load()
    playing = True
    while playing == True:
        
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
            descline = readfile(roomdata)
            print(descline)
            roomdata = roomdata + 1
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
            targetroom = readfile(roomdata)
            targetroom = targetroom[2:]
            #print(targetroom)
            if targetroom == "00":
                print("can't do that")
            else:
                position = targetroom
        elif playerInput == "move south":
            roomdata = roomdata + 1
            targetroom = readfile(roomdata)
            targetroom = targetroom[2:]
            #print(targetroom)
            if targetroom == "00":
                print("can't do that")
            else:
                position = targetroom
        elif playerInput == "move west":
            roomdata = roomdata + 2
            targetroom = readfile(roomdata)
            targetroom = targetroom[2:]
            #print(targetroom)
            if targetroom == "00":
                print("can't do that")
            else:
                position = targetroom
        elif playerInput == "move east":
            roomdata = roomdata + 3
            targetroom = readfile(roomdata)
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
            targetroom = readfile(roomdata)
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
            targetroom = readfile(roomdata)
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
            targetroom = readfile(roomdata)
            targetroom = targetroom[2:]
            #print(targetroom)
            if targetroom == "00":
                print("can't do that")
            else:
                position = targetroom
        else:
            print("can't do that")
        print("")
    return

main()