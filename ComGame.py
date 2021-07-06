print("this game by command type (help) to help")
com1 = "empty"
move = False
while True:
    com1 = input(">")
    com1 = com1.lower()
    if com1 == "help" :
        print("command: help for help")
        print( "command: move to move ")
        print("command: stop to stop")
        print( " command : quit to exit")
    elif com1 == "move":
        if move == False:
            print( "moving ....")
            move = True
        else:
                print("already mvoing")
    elif com1 == "stop":
        if move == True:
            move = False
            print("[stopped]<>")
        else:
                print("already stopped!!!")
    elif com1 == "quit":
                    print("quitting.....exiting program")
                    break;
    else :
        print("invalid command type (help) to get helped")



