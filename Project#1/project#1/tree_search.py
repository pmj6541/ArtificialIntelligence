import numpy as np
import csv
import random
import math

THRESHOLD = 1
cities = []
CHECKDEGEE = True


def distance(x,y): #
    dist = np.linalg.norm(np.array(x)-np.array(y))
    return dist

def getDegreeScore(pre, now, front):
    rad1 = math.atan2(float(cities[pre][1])-float(cities[now][1]),float(cities[pre][0])-float(cities[now][0]))
    deg1 = (rad1 * 180 / math.pi + 360)%360
    rad2 = math.atan2(float(cities[front][1])-float(cities[now][1]),float(cities[front][0])-float(cities[now][0]))
    deg2 = (rad2 * 180 / math.pi + 360)%360
    check = abs(deg1-deg2)%180
    return -(check/600)+2.0



with open('./csv/TSP.csv', mode='r', newline='') as tsp: # 
    reader = csv.reader(tsp)
    for row in reader:
        cities.append(row)

def citiesDist(startIndex, preCity, checkDegree): # 
    dist = []
    nowDist = 0.0
    now = 0
    score = []
    for i in cities:
        if startIndex != now and i[2]:
            nowCity = [float(cities[startIndex][0]), float(cities[startIndex][1])]
      
            destCity = [float(i[0]), float(i[1])]
            nowDist = distance(nowCity,destCity)
            if checkDegree:
                if preCity != -1:
                    score.append([nowDist * getDegreeScore(preCity, startIndex, now), now])              
                else :
                    score.append([nowDist,now])
            else:
                score.append([nowDist,now])
        now+=1
    
    score.sort(key=lambda x:x[0])
    dist = score[0:THRESHOLD]


    return dist


def getTreeSolution():
    traveling = []

    nextCity = 0
    nowCity = 0
    preCity = -1
    traveling.append(0)
    for i in cities:
        i.append(True)
    for i in range(999):
        dist = citiesDist(nowCity, preCity, CHECKDEGEE)
        cities[nowCity][2] = False
        nextCity = dist[random.randrange(0,len(dist))][1]
        traveling.append(nextCity)
        preCity = nowCity
        nowCity = nextCity
    for i in cities:
        i.pop()

    return traveling

