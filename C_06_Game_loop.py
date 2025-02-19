# set scores to zero at the start of the game

comp_score = 0
user_score = 0

game_goal = int(input("Game Goal Please: "))    # number checker

# loop rounds
while comp_score < game_goal and user_score < game_goal:

    # For testing
    comp_points = int(input("Enter the computer points at the end of the round: "))
    user_points = int(input("Enter the user points at the end of the round: "))

    # update scores
    comp_score += comp_points
    user_score += user_points

    # show scores
    print("\n*** Game Update ***")    # statement gen
    print(f"User score: {user_score} | Computer Score: {comp_score}")

# at the end show final scores

if user_score > comp_score:
    print("\nThe user won")
else:
    print("\nThe computer won")
