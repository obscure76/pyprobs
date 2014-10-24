__author__ = 'obscure'

class sqroot:

    def __init__(self):
        pass

    def find_sq_root(self, n):
        x = n * 1.0
        err = 0.0001
        y = 0.0
        while abs(x-y) > err:
            x = (x+y)/2
            y = n/x
        return x

if __name__ == '__main__':
    sq = sqroot()
    print(sq.find_sq_root(.81))
