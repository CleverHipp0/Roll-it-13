def yes_no(question):
    """Input question, out put whether they said yes or no"""
    while True:

        # Asks a question a lowers it
        yes_no_raw = input(question).lower()

        # acceptable answers in lists
        yes_acceptable = ("yes", "y")
        no_acceptable = ("no", "n")

        # Checks the list to see if it's an acceptable answer and returns it
        if yes_no_raw in yes_acceptable:
            return yes_acceptable[0]

        elif yes_no_raw in no_acceptable:
            return no_acceptable[0]

        # print error
        else:
            print("That is not an acceptable answer. Please answer with <yes> or <no>.")


def instructions():
    """Prints Instructions"""
    print('''
    *** Roll It 13 Instructions ***

    - Roll the dice to score points to win
    ''')


def integer_checker(question, minimum):
    """Simple integer checker number must be more than or equal to minimum"""

    # Sets up an error message.
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

# Ask if they want instructions
want_instructions = yes_no("Do you want instructions? ")

if want_instructions == "yes":
    instructions()

game_goal = integer_checker("\nWhat is the game goal? ", 13)
print(f"\nSelected game goal: {game_goal}")
