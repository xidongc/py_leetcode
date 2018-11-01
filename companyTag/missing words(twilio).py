def missingWords(s, t):
    # Write your code here
    i,j = 0,0
    missingList = []
    sList = s.split(' ')
    tList = t.split(' ')
    while j < len(tList) and i < len(sList):
        if sList[i] == tList[j]:
            j += 1
        else:
            missingList.append(sList[i])
        i += 1
    missingList.extend(sList[i:])
    return missingList
print(missingWords('I A A U H T I P ','A H T I'))
# t is the substring of s
# order matters
# output all the missing words as a list