import sys

class Enemy:
    """
    Class that defines an enemy
    """
    
    def __init__(self, name, distance):
        """
        Constructor
        """
        # enemy name
        self.name = name
        
        # enemy distance from cannon
        self.distance = distance
    
    def __lt__(self, other):
        """
        Comparison method. Needed for sorting.
        """
        return self.distance < other.distance

# game loop
while True:
    enemy_1 = input()  # name of enemy 1
    dist_1 = int(input())  # distance to enemy 1
    enemy_2 = input()  # name of enemy 2
    dist_2 = int(input())  # distance to enemy 2

    # Create enemy objects
    enemy1 = Enemy(enemy_1, dist_1)
    enemy2 = Enemy(enemy_2, dist_2)

    # Sort the enemy objects based on distance
    enemies = [enemy1, enemy2]
    enemies.sort()

    # Shoot the closest enemy
    print(enemies[0].name)
