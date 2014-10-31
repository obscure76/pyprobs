__author__ = 'obscure'

class Solution:

    def __init__(self):
        self.d = {'ab': 1, 'abc':1, 'aes':1, 'owls':1, 'owl':1}
        self.mat = [['a', 'b', 'c', 'd'],['d', 'e', 'f', 'g'], ['o', 'w', 'l', 's']]

    def getMoves(self, l, r):
        pass

    def checkword(self, ls, rs, le, re):
        pass
    
    def findWords(self):
        print(len(self.d))
        print(len(self.mat))
        for i in range(0, len(self.mat)):
            for j in range(0, len(self.mat[i])):
                moves = self.getMoves(i, j)
                for move in moves:
                    pass


if __name__ == '__main__':
    s = Solution()
    s.findWords()