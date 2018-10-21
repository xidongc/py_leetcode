import sys
import math
import collections
import string
#

count = 0
curStr = ""
queue = collections.deque()
for word in string.ascii_lowercase:
    queue.append(word)
map = dict()
while len(curStr) < 6 and queue:
    curStr = queue.popleft()
    pos = ord(curStr[-1])
    if len(curStr) < 5:
        for i in range(pos+1, ord('z') + 1):
            queue.append(curStr+chr(i))
    count += 1
    map[curStr] = count
# print(map)
for line in sys.stdin:
    line = line.strip('\n')
    if line in map:
        print(str(map[line]))
    else:
        print('0')
