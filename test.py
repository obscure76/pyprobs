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
            b = s2
        k = 0
        for i in range(len(b)-1, -1, -1):
            carry = 0
            for j in range(len(a)-1, -1, -1):
                p =  int((ord(a[j])-ord('0')) * (ord(b[i]) - ord('0')))
                p += carry
                p += ord(res[k+j]) - ord('0')
                carry = p/10
                res[k+j] = str(int(p%10))
            if carry > 0:
                res[k+j] = str(carry)
            k += 1
        for j in range(len(res)-1, -1, -1):
            print(res[j])


if __name__ == '__main__':
    s = Solution()
    s.mult('123', '567')
    print()
