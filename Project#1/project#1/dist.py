import numpy as np
import csv

cities = []

def distance(x, y):
    dist = np.linalg.norm(np.array(x)-np.array(y))
    return dist

with open('./csv/TSP.csv', mode='r', newline='') as tsp:
    reader = csv.reader(tsp)
    for row in reader:
        cities.append(row)

def total_cost(sol_list):
    idx = sol_list.index(0)

    front = sol_list[idx:]
    back = sol_list[0:idx]

    sol_list = front + back

    sol_list.append(int(0))


    total_cost = 0

    for idx in range(len(sol_list)-1):
        pos_city_1 = [float(cities[sol_list[idx]][0]), float(cities[sol_list[idx]][1])]
        pos_city_2 = [float(cities[sol_list[idx+1]][0]), float(cities[sol_list[idx+1]][1])]
        dist = distance(pos_city_1, pos_city_2)
        total_cost += dist
    return total_cost
