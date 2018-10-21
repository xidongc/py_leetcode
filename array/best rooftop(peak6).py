# Complete the beHappy function below.
import math
import collections
def beHappy(sightRadius, eventsGrid):
    happyMap = collections.defaultdict(int)
    res = [0,0]
    if not eventsGrid or not eventsGrid[0]:
        return res
    dis = 2 ** 32
    maxX = 0
    maxY = 0
    minX = 0
    minY = 0
    for eventGrid in eventsGrid:
        x = eventGrid[0]
        y = eventGrid[1]
        if x < minX:
            minX,minY = x,y if (x - maxX)**2 + (y-maxY)**2 > (minX - maxX)**2 + (minY-maxY)**2 else 0,0
        else:
            maxX,maxY = x,y if (x - minX)**2 + (y-minY)**2 > (minX - maxX)**2 + (minY-maxY)**2 else 0,0
    for eventGrid in eventsGrid:
        x = eventGrid[0]
        y = eventGrid[1]
        worth = eventGrid[2]
        if math.sqrt(x**2 + y ** 2) > sightRadius:
            continue
        if x < maxX and x > minX and y < maxY and y > minY:
            happyVal = worth / 1 + math.sqrt(x**2 + y**2)
            happyMap[(x,y)] += happyVal

    if not happyMap:
        return res
    else:
        maxHappyVal = max(happyMap.values())

    for key,val in happyMap.items():
        if val == maxHappyVal:
            if res == [0,0]:
                res = key
            else:
                if dis > key[0] ** 2 + key[1] ** 2:
                    dis = key[0] ** 2 + key[1] ** 2
                    res = (key[0],key[1])
    return res