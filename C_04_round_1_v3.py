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


# Main routine goes here

# Roll the dice for the user and see if they have got doubles
initial_user = initial_points("User")
initial_comp = initial_points("Comp")

# Initialise round points
user_points = initial_user[0]
comp_points = initial_comp[0]

double_user = initial_user[1]

# Let the user know if they qualify for double points
if double_user == "yes":
    print("Congratulations you will earn double points.")

# assume the user goes first

first = "User"
second = "Computer"
player_1_points = user_points
player_2_points = comp_points

# if the user has fewer points they start the game
if user_points < comp_points:
    print("You start because your initial roll was less than the computer.\n")

#  if they user and computer roll equal points, the user is player one
elif user_points == comp_points:
    print("The initial rolls were the same, the user starts! ")

# if the computer has fewer points, switch the computer to 'player 1'
else:
    player_1_points, player_2_points = player_2_points, player_1_points
    first, second = second, first

# Loop until we have a winner

while player_1_points < 13 and player_2_points <13:
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
user_points = player_1_points
comp_points = player_2_points


# Switch the user and computer points if the computer goes first
if first == "Computer":
    user_points, comp_points = comp_points, user_points

# Work out who won...
if user_points > comp_points:
    winner = "user"
else:
    winner = "computer"

round_feedback = f"The {winner} won."

# double the users points if needed
if winner == "user" and double_user == "yes":
    user_points += user_points

# Output round results
statement_generator("-", 5, "Results")
print(f"User Points: {user_points}  |  Computer Points: {comp_points}")
print(f"{round_feedback}\n")


