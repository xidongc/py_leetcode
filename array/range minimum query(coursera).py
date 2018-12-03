# import sys
length, rangeNum = input().strip().split(' ')
length, rangeNum = int(length), int(rangeNum)
numList = list(map(int,input().strip().split(' ')))
rangeList = []
count = 0
for i in range(rangeNum):
    rangeList.append(list(input().strip().split(' ')))
for range in rangeList:
    start,end = int(range[0]), int(range[1])+1
    print(min(numList[start:end]))