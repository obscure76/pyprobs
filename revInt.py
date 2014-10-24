__author__ = 'obscure'

class solution:
    def __init__(self):
        pass

    def revInt(self, v):
        n = int(v)
        x = int(0)
        count = 0
        while n > 0 and count < 4:
            x = int(x * 10 + n%10)
            n = int(n/10)
            count += 1
            print(n)
        print(x)

if __name__ == '__main__':
    s = solution()
    s.revInt(123)