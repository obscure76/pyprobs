__author__ = 'obscure'

class Solution:

    def __init__(self):
        pass

    def mult(self, s1, s2):
        res = []
        for i in range(0, len(s1) + len(s2)+1):
            res.append('0')
        if len(s1) > len(s2):
            a = s1
            b = s2
        else:
            a = s2
            b = s1
        k = 0
        print(a,b)
        for i in range(len(b)-1, -1, -1):
            carry = 0
            for j in range(len(a)-1, -1, -1):
                p =  int((ord(a[j])-ord('0')) * (ord(b[i]) - ord('0')))
                p += carry
                p += ord(res[k+len(a)-1-j]) - ord('0')
                res[k+len(a)-1-j] = str(int(p%10))
                carry = p/10
            k += 1;
            print(carry, j)
            if carry > 0:
                res[k+len(a)-1-j] = str(carry)
            print(res)


        for i in range(len(res)-1, -1, -1):
            #print(res[i])
            pass


if __name__ == '__main__':
    s = Solution()
    s.mult('123', '567')
