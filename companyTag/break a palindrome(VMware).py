#
# Complete the 'breakPalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def breakPalindrome(s):
    # Write your code
    #     Change this string into string list
    sList = list(map(str, s))
    for i in range(len(sList)):
        #     Check for the char that is not 'a'
        if sList[i] != 'a':
            #     Copy this list and change the char that is not 'a' to 'a'
            newList = sList
            newList[i] = 'a'
            newStr = ''.join(newList)
            #     Check whether this new string is palindrome or not
            if newStr != newStr[::-1]:
                return newStr
    #     If no requirements meet, return 'IMPOSSIBLE'
    return "IMPOSSIBLE"

# bab->aab
# acca->aaca
# aaa->IMPOSSIBLE