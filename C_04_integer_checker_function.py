# Sets up an error message.

def integer_checker(question, minimum):
    """Simple integer checker number must be more than or equal to minimum"""

    error = "Please insert a number whole or equal to 13."

    # Creates a loop the goes until an acceptable answer is entered
    while True:
        try:

            # Asks for the desired game goal
            response = int(input(question))

            # if the game goal is less than 13 it outputs an error
            if response < minimum:
                print(error)
            # if it is greater or equal to 13 return the response
            else:

                return response

        except ValueError:

            # If there is a value error then it will print the error.
            print(error)


# Main routine goes here
game_goal = integer_checker("What is the game goal? ", 13)
print(f"Selected game goal: {game_goal}")



