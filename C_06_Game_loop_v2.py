import random


def statement_generator(decoration, decoration_time, statement):
    """Makes a statement fancy by adding decorative characters"""

    print(f"\n{decoration * decoration_time} {statement} {decoration * decoration_time}")


def initial_points(which_user):
    """Roll the dice and return the total / if double points apply"""

    double = "no"

    # Roll the dice for the user and see if they have got doubles
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two

    print(f"{which_user}    - Roll 1: {roll_one} \t| Roll 2: {roll_two} \t| Total: {total} ")

    return total, double


def game_round():

    # Roll the dice for the user and see if they have got doubles
    initial_user = initial_points("User")
    initial_comp = initial_points("Comp")

    # Initialise round points
    u_points = initial_user[0]
    c_points = initial_comp[0]

    double_user = initial_user[1]

    # Let the user know if they qualify for double points
    if double_user == "yes":
        print("Congratulations you will earn double points.")

    # assume the user goes first

    first = "User"
    second = "Computer"
    player_1_points = u_points
    player_2_points = c_points

    # if the user has fewer points they start the game
    if u_points < c_points:
        print("You start because your initial roll was less than the computer.\n")

    #  if they user and computer roll equal points, the user is player one
    elif u_points == c_points:
        print("The initial rolls were the same, the user starts! ")

    # if the computer has fewer points, switch the computer to 'player 1'
    else:
        player_1_points, player_2_points = player_2_points, player_1_points
        first, second = second, first

    # Loop until we have a winner

    while player_1_points < 13 and player_2_points < 13:
        print()
        input("Press <enter> to continue this round\n")

        # First person rolls the die and score is updated
        player_1_roll = random.randint(1, 6)
        player_1_points += player_1_roll

        print(f"{first}: Rolled a {player_1_roll} - has {player_1_points} points")

        # If the first person's score is equal to or over 13, end the round
        if player_1_points >= 13:
            break

        # second person rolls the die (and score is updated)
        player_2_roll = random.randint(1, 6)
        player_2_points += player_2_roll

        print(f"{second}: Rolled a {player_2_roll} - has {player_2_points} points")

        print(f"{first}: {player_1_points}  |   {second}: {player_2_points}")

    # print("End of round.")

    # associate player points with either the user or the computer
    u_points = player_1_points
    c_points = player_2_points

    # Switch the user and computer points if the computer goes first
    if first == "Computer":
        u_points, c_points = c_points, u_points

    # Work out who won...
    if u_points > c_points:
        winner = "user"
    else:
        winner = "computer"

    round_feedback = f"The {winner} won."

    # double the users points if needed
    if winner == "user" and double_user == "yes":
        u_points += u_points

    # Output round results
    statement_generator("-", 5, "Results")
    print(f"User Points: {u_points}  |  Computer Points: {c_points}")
    print(f"{round_feedback}\n")

    return u_points, c_points, winner


def run_and_loop():
    # set scores to zero at the start of the game

    comp_score = 0
    user_score = 0
    round_number = 0

    game_goal = int(input("Game Goal Please: "))    # number checker
    print()

    # loop rounds
    while comp_score < game_goal and user_score < game_goal:

        round_number += 1
        statement_generator("🎲", 3, f"Round {round_number}")

        # Get game data
        round_data = game_round()

        # Add the correct points
        if round_data[2] == "user":

            user_points = round_data[0]
            comp_points = 0

        else:

            comp_points = round_data[1]
            user_points = 0

        # update scores
        comp_score += comp_points
        user_score += user_points

        # show scores
        print()
        statement_generator("*", 3, "Game Update")
        print(f"User score: {user_score} | Computer Score: {comp_score}")
        print()

    # at the end show final scores

    statement_generator("🏁", 3, "Game over")

    if user_score > comp_score:
        print("\nThe user won")
    else:
        print("\nThe computer won")

    print(f"User score: {user_score} | Computer Score: {comp_score}")


# Main routine goes here
run_and_loop()
