__author__ = 'obscure'

class Solution:

    def __init__(self):
        pass

    def mergeLists(self, l):
        len1 = len(l[0])
        len2 = len(l[1])
        i = j = 0
        res = list()
        k = 0
        while i<len1 and j <len2:
            if l[0][i] < l[1][j]:
                res.append(l[0][i])
                i += 1
            else:
                res.append(l[1][j])
                j += 1
        if i < len1:
            while i < len1:
                res.append(l[0][i])
                i += 1
        if j < len2:
            while j < len2:
                res.append(l[1][j])
                j += 1
        print(res)

if __name__ == '__main__':
    s = Solution()
    s.mergeLists([[1,3],[2,4]])