__author__ = 'midhun'


class Sum2:
    def __init__(self):
        pass

    def findpairs(self, l, S):
        d = dict()
        for i in l:
            d[i] = i
        for i in range(0, len(l)/2):
            if S-l[i] in d:
                print l[i], S-l[i]


if __name__ == '__main__':
    s = Sum2()
    s.findpairs([2,4,5,19,6,8], 23)
