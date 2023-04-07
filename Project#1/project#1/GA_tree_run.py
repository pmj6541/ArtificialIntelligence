import dist
from selection import Selection
from crossover import Crossover
from mutation import Mutation
import csv

N = 100         # 초기집단의 수
ITERATOR = 1000 # 유전 알고리즘의 반복횟수

# treesearch를 초기집단으로 해서 유전알고리즘을 한 번 돌리는 과정
fitness = Selection.sort_distance_tree(N)
result_list = fitness[0][0]
result_cost = fitness[0][1]
selection_list_cost = []
sol_list_cost = []
for i in range(N):
    selection_list_cost.append([])
    selection_list_cost[i] = Selection.ranking(fitness, N)
for i in range(N):
    sol_list_cost.append([])
    if(i % 2 == 0):
        sol_list_cost[i].append(Crossover.order(selection_list_cost[i][0], selection_list_cost[i+1][0]))
    else:
        sol_list_cost[i].append(Crossover.order(selection_list_cost[i][0], selection_list_cost[i-1][0]))
for i in range(N):
    sol_list_cost[i][0] = Mutation.reverse(sol_list_cost[i][0])
    sol_list_cost[i].append(dist.total_cost(sol_list_cost[i][0]))
    if(result_cost > sol_list_cost[i][1]):
        result_list = sol_list_cost[i][0]
        result_cost = sol_list_cost[i][1]


# 처음 유전알고리즘을 진행해서 나온 자식을 통해 유전알고리즘을 100번 더 수행하는 과정
for i in range(ITERATOR):
    fitness = Selection.sort_distance_genetic(sol_list_cost)
    for i in range(N):
        selection_list_cost[i] = Selection.ranking(fitness, N)
    for i in range(N):
        if(i % 2 == 0):
            sol_list_cost[i][0] = Crossover.order(selection_list_cost[i][0], selection_list_cost[i+1][0])
        else:
            sol_list_cost[i][0] = Crossover.order(selection_list_cost[i][0], selection_list_cost[i-1][0])
    for i in range(N):
         sol_list_cost[i][0] = Mutation.reverse(sol_list_cost[i][0])
         sol_list_cost[i][1] = dist.total_cost(sol_list_cost[i][0])
         if(result_cost > sol_list_cost[i][1]):
            result_list = sol_list_cost[i][0]
            result_cost = sol_list_cost[i][1]
f = open('./csv/sol_tree_GA.csv', mode='w', newline='')
wr = csv.writer(f)
for i in result_list:
        wr.writerow([i])
print(result_list)
print(result_cost)