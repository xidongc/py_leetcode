class Solution(object):

    def compareVersion(self, version1, version2):
        v1_list = version1.split('.')
        v2_list = version2.split('.')

        for i in range(0, max(len(v1_list), len(v2_list))):
            v1 = int(v1_list[i]) if len(v1_list) > i else 0
            v2 = int(v2_list[i]) if len(v2_list) > i else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0
