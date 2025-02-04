def yes_no(question):
    """Input question, out put whether they said yes or no"""
    while True:

        # Asks the question a lowers it
        yes_no_raw = input(question).lower()

        # acceptable answers in lists
        yes_acceptable = ("yes", "y")
        no_acceptable = ("no", "n")

        # Checks the list to see if it's an acceptable answer and returns it
        if yes_no_raw in yes_acceptable:
            return yes_acceptable[0]

        elif yes_no_raw in no_acceptable:
            return no_acceptable[0]

        else:
            print("That is not an acceptable answer. Please answer with <yes> or <no>.")


def instructions():
    """Prints Instructions"""
    print('''
    *** Roll It 13 Instructions ***

    - Roll the dice to score points to win
    ''')


# Main routine goes here

# Ask if they want instructions
want_instructions = yes_no("Do you want instructions? ")

if want_instructions == "yes":
    instructions()

print("continue")
