# VMware

# Just from experience with these types of problems, it's usually easier to find out the opposite of what doesn't overlap. The following cases they don't overlap:
# Case 1:if the maximum of rec1 is less than or equal to the minimum from rec2 in the x
# Case 2:if the maximum of rec1 is less than or equal to the minimum from rec2 in the y
# Case 3: just swap rec1 and rec2 in Case 1
# Case 4:Just swap rec1 and rec2 in Case 2
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return not (rec1[0] >= rec2[2] or rec2[0] >= rec1[2] or rec1[1] >= rec2[3] or rec2[1] >= rec1[3] )