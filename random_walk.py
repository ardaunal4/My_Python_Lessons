import random
import math
# from decimal import Decimal
"""  
def random_walk(n):

    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N', 'S', 'W', 'E'])
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'W':
            x = x - 1
        elif step == 'E':
            x = x + 1
    return (x, y)

for i in range(5):
    walk = random_walk(100000000)
    print(walk, "Distance from home = ", '%.2f' %math.sqrt(walk[0]**2 + walk[1]**2))
"""

def random_walk_2(n):
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y) 

number_of_walks = 10000

for walk_length in range(1,31):
    no_transport = 0 #number of walks 4 or fewer blocks from home
    for i in range(number_of_walks):
        (x, y) = random_walk_2(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_percentage = float(no_transport) / number_of_walks
    print("Walk size = ", walk_length, " \ % of no transport = ", 100 * no_transport_percentage)


        