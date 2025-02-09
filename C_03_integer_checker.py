# Sets up an error message.
error = "Please insert a number whole or equal to 13."

# Creates a loop the goes until an acceptable answer is entered
while True:
    try:

        # Asks for the desired game goal
        game_goal = int(input("What is the game goal? "))

        # if the game goal is less than 13 it outputs an error
        if game_goal < 13:
            print(error)

        else:

            # Makes sure the game goal is equal to or greater than 13 and breaks the loop
            print(f"Selected game goal: {game_goal}")

    except ValueError:

        # If there is a value error then it will print the error.
        print(error)
