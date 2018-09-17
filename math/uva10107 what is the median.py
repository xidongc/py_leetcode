import sys
import bisect
numList = []
for line in sys.stdin:
    # pos = bisect.bisect(numList,int(line))
    bisect.insort(numList,int(line))
    pos = len(numList) // 2
    if len(numList) % 2 == 0:
        print((numList[pos] + numList[pos-1]) // 2)
    else:
        print(numList[pos])

