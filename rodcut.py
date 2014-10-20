__author__ = 'obscure'

r = []


def rodCut(n, p):
    globals()
    for j in range(1, n):
        temp = -1.0
        for i in range(1,j):
            temp = max(temp, p[i]+r[j-i])
        r[j]=temp
    print r[n-1]

if __name__ == '__main__':
    p = [1.0, 5.0, 8.0, 9.0, 10.0, 17.0, 17.0, 20.0, 24.0, 30.0]
    for i in range(len(p)):
        r.append(0.0)
    rodCut(10, p)


