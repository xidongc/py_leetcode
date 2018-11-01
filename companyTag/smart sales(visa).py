#
# Complete the 'deleteProducts' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ids
#  2. INTEGER m
#
import collections
def deleteProducts(ids, m):
    # Write your code here
    if not ids:
        return 0
    timesDict = collections.defaultdict(int)
    for num in ids:
        timesDict[num] += 1
    valueList = sorted(list(timesDict.values()))
    i = 0
    while i < len(valueList) and m >= valueList[i]:
        m -= valueList[i]
        i += 1
    return len(valueList) - i

print(deleteProducts([1,2,3,1,2,2], 2))