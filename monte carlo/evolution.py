import random
import matplotlib.pyplot as plt
from nugget import unit

length_of_study = 30
moves = 100
world_size = 50
number_of_foods = 10
initial_pop_size = 10
units = []

for i in range(initial_pop_size):
    i = unit(0, 0, 0, 1, moves)
    units.append(i)

print(units)

def generate_grid():
    global all_coordinates
    all_coordinates, neg_coords, pos_coords = [], [], []
    for x in range(world_size):
        for y in range(world_size):
            all_coordinates.append((-x, -y))
            pos_coords.append((x, y))
    all_coordinates.reverse()
    all_coordinates.pop()
    all_coordinates.extend(pos_coords)
    edges = all_coordinates.copy()
    # for i in edges:
    #     edges.pop(i)
    # print(edges)

def generate_food():
    food_distributions = []
    for fd in range(number_of_foods):
        food_distributions.append(random.choice(all_coordinates))
    return food_distributions

generate_grid()
food = generate_food()
for i in range(pop_size):
    units[i].move(food)
    print(units[i].x, units[i].y)

def reset():
    global pop_size
    global population
    pop_size = initial_pop_size
    population = []
    for a in range(pop_size):
        #            [x, y, food, speed]
        population.append([0, 0, 0, 1, moves])
        a += 1
    speed = 1
    x = 0
    y = 0
    avrg_speed = 0

def one_step_movement(): #Simulates one step for all members of the population
    for i in range(pop_size):
        for s in range(population[i][3]):
            if population[i][4] == 0:  # running out of energy
                break
            dx, dy = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
            population[i][0] += (dx)
            population[i][1] += (dy)
            population[i][4] -= 1
            #if (population[i][0], population[i][1]) in edges:
            if (population[i][0], population[i][1]) in food: #the eating of food
                population[i][2] += 1
                w = food.index((population[i][0], population[i][1]))
                food.pop(w)

def one_day_movement():
    global pop_size
    global population
    global food
    global avrg_spd
    global food_distributions
    tot_speed = 0
    starved = 0
    population_temp = []
    generate_food()
    food = generate_food()
    print('Food positions: ',food)
    for i in range(pop_size):
        population[i][3] += random.choice([1, -1, 0, 0])
        population[i][0], population[i][1], population[i][2] = 0, 0, 0
        population[i][4] = moves
    print('Starting: ', len(population) ,population)
    for k in range(moves):
        one_step_movement()
    print('Finish: ', len(population), population)
    for a in range(pop_size):
        if population[a][2] == 0:
            starved += 1
        elif population[a][2] == 1:
            population_temp.append(population[a].copy())
        else:
            population_temp.append(population[a].copy())
            population_temp.append(population[a].copy())
        tot_speed = tot_speed + population[a][3]

    print('Died of starvation: ', starved)
    try:
        avrg_spd = tot_speed/pop_size
        print('Average speed: ', avrg_spd)
    except:
        print('All population have died')
        avrg_speed = 0
    pop_size = len(population_temp)
    print('population size: ', pop_size)
    population = population_temp

def study():
    global day_list
    global speed_list
    speed_list = []
    day_list = []
    reset()
    day=0
    #while pop_size >= 1:
    while day <= 40:
        day += 1
        print('Day: ', day)
        one_day_movement()
        day_list.append(day)
        speed_list.append(avrg_spd)
        avrg_speed = 0
        print('Surviving: ', population)
        print('-----------------------------------------------------------------')
        if pop_size == 0:
            return day
        #if pop_size >= 500:
            #days_lasted.append(day)
            #plt.plot(no_food, days_lasted)
            #plt.show()

study()

# no_food = []
# i=100
# days_lasted = []
# for i in range(200):
#     no_food.append(i)
#     number_of_foods = no_food[i]
#     days_lasted.append(study())
#     print(number_of_foods)
