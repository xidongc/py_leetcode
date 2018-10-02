#
# Complete the 'getMinimumDifference' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY a
#  2. STRING_ARRAY b
#
# Anagram: 

def getMinimumDifference(a, b):
    if not a or not b:
        return max(len(a),len(b)) * [-1]
    res = []
    for i in range(min(len(a),len(b))):
        diffSum = 0
        strA,strB = a[i],b[i]
        if len(strA) == len(strB):
            mapA = {char:strA.count(char) for char in strA}
            for char in mapA.keys():
                diffSum += mapA[char] - strB.count(char) if mapA[char] > strB.count(char) else 0
            res.append(diffSum)
        else:
            res.append(-1)
    return res


