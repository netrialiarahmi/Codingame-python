import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not to follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Determine the direction for Thor to reach the light of power
    direction = ""

    if initial_ty > light_y:
        direction += "N"
        initial_ty -= 1
    elif initial_ty < light_y:
        direction += "S"
        initial_ty += 1

    if initial_tx > light_x:
        direction += "W"
        initial_tx -= 1
    elif initial_tx < light_x:
        direction += "E"
        initial_tx += 1

    # Print the chosen direction for Thor
    print(direction)
