import random
import matplotlib.pyplot as plt

def random_walk(length, speed):
    x, y = 0, 0
    for i in range(length):
        dx, dy = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
        y = y + float(speed)*dy
        x = x + float(speed)*dx
    return (x, y)

sim_size = 1000
home_prob_list = []
walk_length_list = []

for walk_length in range(1, 101):
    home = 0
    for i in range(sim_size):
        x, y = random_walk(walk_length, 1)
        distance = abs(x) + abs(y)
        if distance <= 4:
            home = home + 1
        home_prob = float(home)/sim_size
    home_prob_list.append(home_prob)
    walk_length_list.append(walk_length)
plt.figure(figsize=(15, 5))
print (walk_length_list)
print (home_prob_list)
plt.scatter(walk_length_list, home_prob_list)
plt.show()