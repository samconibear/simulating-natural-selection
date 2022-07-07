import random
import matplotlib.pyplot as plt

length_of_study = 30
moves = 20
world_size = 50
number_of_foods = 170
initial_pop_size = 100


def reset():
    global pop_size
    global population
    pop_size = initial_pop_size
    population = []
    for a in range(pop_size):
        #            [x, y, food, speed, energy]
        population.append([0, 0, 0, 1, 0])
        a += 1
    speed = 1
    x = 0
    y = 0
    avrg_speed = 0


def one_step_movement():  # Simulates one step for all members of the population
    for i in range(pop_size):
        for s in range(population[i][3]):
            dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
            population[i][0] += (dx)
            population[i][1] += (dy)
            if (population[i][0], population[i][1]) in food:
                population[i][2] += 1
            # if population[i][4] == 0:


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


def generate_food():
    food_distributions = []
    for fd in range(number_of_foods):
        food_distributions.append(random.choice(all_coordinates))
    return food_distributions


print(generate_grid())


def one_day_movement():
    global pop_size
    global population
    global food
    global avrg_spd
    tot_speed = 0
    starved = 0
    population_temp = []
    food = generate_food()
    print('Food positions: ', food)
    for i in range(pop_size):


    print('Starting: ', len(population), population)
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
        avrg_spd = tot_speed / pop_size
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
    day = 0
    # while pop_size >= 1:
    while pop_size >= 1:
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
        if pop_size >= 500:
            days_lasted.append(day)
            plt.plot(no_food, days_lasted)
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
