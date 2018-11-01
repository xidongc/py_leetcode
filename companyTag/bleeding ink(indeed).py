import sys
sCount = int(input())
# for line in sys.stdin:
    # start of a new sheet
while True:
    line = input()
    if len(line.strip().split(' ')) != 2:
        break
    else:
        h,w = line.strip().split(' ')
        h,w = int(h),int(w)
        sheet = [[0 for _ in range(w)] for _ in range(h)]
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        dotNum = int(input())
        queue = []
        for i in range(dotNum):
            dotLine = input()
            # dotLine = list(map(int,dotLine.strip().split(' ')))
            x,y,darkness = list(map(int,dotLine.strip().split(' ')))
            sheet[x][y] = max(sheet[x][y],darkness)
            if[x,y] not in queue:
                queue.append([x,y])
        queue.sort(key = lambda x: -sheet[x[0]][x[1]])
        while queue:
            curPos = queue.pop(0)
            x,y = curPos[0],curPos[1]
            darkness = sheet[x][y]
            for dir in dirs:
                newx = x + dir[0]
                newy = y + dir[1]
                newdarkness = darkness - 1
                if newx >= 0 and newy >= 0 and newx < h and newy < w and newdarkness > sheet[newx][newy]:
                    queue.append([newx,newy,newdarkness])
                    sheet[newx][newy] = newdarkness
        print(sum(sheet[x][y] for x in range(h) for y in range(w)))



# input
# 2 number of sheets
# 3 4 height&width
# 2 number of dots
# 0 0 255
# 1 2 255
# 5 6
# 4
# 1 0 10
# 2 2 9
# 2 3 5
# 4 2 9
# output
# 3046
# 217