import sys

# game loop
while True:
    max_height = 0
    target_index = 0
    
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        
        if mountain_h > max_height:
            max_height = mountain_h
            target_index = i

    # The index of the mountain to fire on.
    print(target_index)
