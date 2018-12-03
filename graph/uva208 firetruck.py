import sys, collections
caseCount = 0
for line in sys.stdin:
    # Get the destination
    line = line.strip()
    if line.isdigit():
        des = line
        streetDict = collections.defaultdict(list)
    # Not the last row
    elif line != '0 0':
        s1,s2 = line.split(' ')
        streetDict[s1].append(s2)
        streetDict[s2].append(s1)
    #     Start to calculate routesres.add(' '.join(visited))
    else:
        caseCount += 1
        # res = set()
        res = []
        # 只用dfs会超时，把和终点联通的点保存下来
        connectList = []
        def dfs(des):
            for num in streetDict[des]:
                if num not in connectList:
                    connectList.append(num)
                    dfs(num)
        dfs(des)

        def helper(start, des, streetDict, visited):
            if start == des:
                # res.add(' '.join(visited))
                res.append(' '.join(visited))
                return
            for num in streetDict[start]:
                if num not in visited and num in connectList:
                    helper(num, des, streetDict, visited + [num])
        helper('1',des,streetDict,['1'])
        print('CASE ' + str(caseCount) + ':')

        for row in res:
            print(row)
        print('There are ' + str(len(res)) + ' routes from the firestation to streetcorner ' + str(des) + '.')


