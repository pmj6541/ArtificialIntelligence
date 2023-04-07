from visualize import VisPlot
from util import Util
import paths

data_df = Util.getData(paths.CSV, "TSP.csv")
sol_df = Util.getSolution(paths.CSV, "sol_random_GA.csv")
data_list = data_df.values
sol_list = []

for item in sol_df.values:
    sol_list.append(item[0])

vis = VisPlot()
vis.set_size(100, 120)

start_flag = True

for item in data_list:
    if start_flag:
        start_flag = False
        vis.draw_point(item[0], item[1], color="red", size=20)
    else:
        vis.draw_point(item[0], item[1])

for idx in range(len(sol_list)-1):
    vis.draw_line(data_list[sol_list[idx]], data_list[sol_list[idx+1]])

vis.draw_line(data_list[sol_list[len(sol_list)-1]], data_list[sol_list[0]])
vis.save("img.png")
vis.show()
