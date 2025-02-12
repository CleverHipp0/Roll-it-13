import random

# Initialise round points
user_points = 0
comp_points = 0
double_user = "no"

# Roll the dice for the user and see if they have got doubles
user_one = random.randint(1, 6)
user_two = random.randint(1, 6)

if user_one == user_two:
    double_user = "yes"

# Roll the dice for the computer
comp_one = random.randint(1, 6)
comp_two = random.randint(1, 6)

# Update the points
user_points += user_one + user_two
comp_points += comp_one + comp_two

# Output the points

print("\nInitial Points")
print(f"User    - Roll 1: {user_one} \t| Roll 2: {user_two} \t| Total: {user_points} ")
print(f"Computer    - Roll 1: {comp_one} \t| Roll 2: {comp_two} \t| Total: {comp_points} ")

# Let the user know if they qualify for double points
if double_user == "yes":
    print("Congratulations you will earn double points")
