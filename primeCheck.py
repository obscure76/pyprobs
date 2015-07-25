__author__ = 'midhunc'


def printPrime():
    for i in range(1, 100):
        if ((6*i-1)%5 !=0 ):
            print(6*i-1)
        if ((6*i+1)%5 !=0):
            print(6*i+1)

if __name__ == '__main__':
    printPrime();