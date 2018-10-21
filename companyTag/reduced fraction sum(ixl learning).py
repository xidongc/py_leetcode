#
# Complete the 'reducedFractionSums' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY expressions as parameter.
#

def reducedFractionSums(expressions):
    # Write your code here
    if not expressions:
        return expressions
    res = []
    for expression in expressions:
        fracOne,fracTwo = expression.split('+')
        numeratorOne, denominatorOne = fracOne.split('/')
        numeratorTwo, denominatorTwo = fracTwo.split('/')
        numerator = int(numeratorOne)*int(denominatorTwo) + int(numeratorTwo)*int(denominatorOne)
        denominator = int(denominatorOne)*int(denominatorTwo)
        if numerator%denominator == 0:
            res.append(str(numerator/denominator))
        else:
            lcn = findLCN(numerator,denominator)
            res.append(str(numerator//lcn) + "/" + str(denominator//lcn))
    return res
def findLCN(a,b):
    res = 1
    bound = min(a,b) // 2 + 1
    for i in range(2,bound):
        while a%i == 0 and b%i == 0:
            res *= i
            a,b = a/i,b/i
    return res