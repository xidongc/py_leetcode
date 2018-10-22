# Complete the numberOfPairs function below.
#
def numberOfPairs(a, k):
    if not a:
        return 0
    aList = sorted(a)
    left,right = 0,len(aList)-1
    # res = 0
    resList = []
    while left < right:
        sum = aList[left] + aList[right]
        if sum == k:
            tmp = (aList[left], aList[right])
            if tmp not in resList:
                resList.append(tmp)
            # res += 1
            left += 1
            right -= 1
        elif sum < k:
            left += 1
        else:
            right -= 1
    return len(resList)
    # return res
# 去重小心，6+6 == 12，不能随意用去重
print(numberOfPairs([6,6,3,9,3,5,1],12))