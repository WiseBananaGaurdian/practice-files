command = ""
car_on = False
while True:
    command = input("> ").upper()
    if command == "START" and car_on == False:
        car_on = True
        print("The car has started")
    elif command == "START" and car_on == True:
        print("The car is already running")
    elif command == "STOP" and car_on == True:
        car_on = False
        print("The car has stopped")
    elif command == "STOP" and car_on == False:
        print("The car was stopped already")
    elif command == "HELP":
        print("""
START -- Starts the car
STOP -- Stops the car
HELP -- Prints this
QUIT -- Quits the game""")
    elif command == "QUIT":
        break
    else:
        print("The game doesn't understand this command. To see all commands, type help.")
