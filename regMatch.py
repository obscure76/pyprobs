__author__ = 'obscure'
class Solution:
    def findMatch(self, s, p, i, j) :
        lens = len(s)
        lenp = len(p)
        while i< lens and j <lenp :
            if p[j] == '*' :
                if j+1 == lenp:
                    return True
                else :
                    while j < lenp and p[j] == '*' :
                        j += 1
                    if j+1 >= lenp:
                        return True
                    k = i
                    temp = False
                    while k < lens:
                        if s[k] == p[j] :
                            temp = temp or self.findMatch(s, p, k+1, j+1)
                            if temp :
                                return True
                        k += 1
                    if i == lens:
                        return False
            elif p[j] == '?' :
                i += 1
                j += 1
            elif s[i] == p[j] :
                i += 1
                j += 1
            else:
                return False
        if i == lens and j == lenp :
            return True
        return False
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        return self.findMatch(s , p, 0 , 0)

if __name__ == '__main__':
    m = Solution()
    print m.isMatch("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb", "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a")