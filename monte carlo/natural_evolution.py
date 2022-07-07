import random
import copy
import matplotlib.pyplot as plt
from nugget import unit
from pprint import pprint

mutation_chance = 999
length_of_study = 0
moves = 5
world_size = 50
number_of_foods = 500
initial_pop_size = 5
sight_range = 10


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
    edge = world_size - 1
    edges = []
    pos_edges = []
    pos_edges2 = []
    for x in range(world_size):
        edges.append((-x, edge))
        pos_edges.append((x, edge))
    edges.reverse()
    edges.pop()
    edges.extend(pos_edges)
    for y in range(world_size):
        edges.append((edge, -y))
        pos_edges2.append((edge, y))
    edges.pop()
    pos_edges2.pop(0)
    pos_edges2.pop(-1)
    edges.extend(pos_edges2)

def generate_food():
    food_distributions = []
    for fd in range(number_of_foods):
        food_distributions.append(random.choice(all_coordinates))
    return food_distributions

generate_grid()
food = generate_food()
# for i in range(initial_pop_size):
#     population[i].move(food)

def reset():
    global pop_size
    global population
    pop_size = initial_pop_size
    population = []
    for i in range(initial_pop_size):
        k = unit(i, 0, 0, 0, 1, moves, sight_range)
        population.append(k)
        print(population[i].x, population[i].y)
    #population = []
    # for a in range(pop_size):
    #     #            [x, y, food, speed]
    #     a = unit(48, 0, 0, 1, moves)
    #     population.append(a)
    #     print(population[a].x)
    speed = 1
    x = 0
    y = 0
    avrg_speed = 0

def one_step_movement(): #Simulates one step for all members of the population
    for i in range(pop_size):
        for s in range(population[i].speed):
            consumed = copy.copy(population[i].move(food, world_size))
            if consumed is not None:
                food.pop(consumed)
            #print(i, '| food:', population[i].food, '| energy:',population[i].energy, '| Speed:', population[i].speed, '| Coordinates: ' ,population[i].x, population[i].y)

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
        if random.randint(0,mutation_chance-1) == 1:
            population[i].speed += 1
        if random.randint(0,mutation_chance-1) == 2:
            population[i].speed -= 1
        population[i].food = 0
        population[i].energy = moves
    print('Starting: ', len(population) ,population)
    for k in range(moves):
        one_step_movement()
    print('Finish: ', len(population), population)
    for a in range(pop_size):
        if population[a].food == 0:
            starved += 1
        elif population[a].food == 1:
            population_temp.append(copy.copy(population[a]))
        else:
            population_temp.append(copy.copy(population[a]))
            population_temp.append(copy.copy(population[a]))
        tot_speed = tot_speed + population[a].speed
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
    days_lasted=[]
    #while pop_size >= 1:
    while day <= length_of_study:
        day += 1
        print('Day: ', day)
        one_day_movement()
        day_list.append(day)
        speed_list.append(avrg_spd)
        avrg_speed = 0
        print('Surviving')
        #for ii in range(pop_size):
            #pprint(ii, population[ii].__dict__)
        print('-----------------------------------------------------------------')
        if pop_size == 0:
            return day
        #if pop_size >= 500:
        days_lasted.append(day)
    plt.plot(days_lasted, speed_list)
    plt.xlabel('Day')
    plt.ylabel('Average Species Speed')
    plt.show()

study()


# no_food = []
# i=100
# days_lasted = []
# for i in range(200):
#     no_food.append(i)
#     number_of_foods = no_food[i]
#     days_lasted.append(study())
#     print(number_of_foods)
