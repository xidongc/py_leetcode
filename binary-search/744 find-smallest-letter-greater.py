class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if len(letters) == 0:
            return None

        start = 0
        end = len(letters) - 1

        while start < end - 1:
            mid = start + (end - start)//2
            if ord(letters[mid]) <= ord(target):
                start = mid + 1
            else:
                end = mid

        if ord(letters[start]) > ord(target):
            return letters[start]
        elif ord(letters[end]) > ord(target):
            return letters[end]
        else:
            return letters[0]
