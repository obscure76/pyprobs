

def solution(A):
    n = len(A)
    result = 0
    for i in xrange(n - 1):
        if (A[i] == A[i + 1] and A[i] ==0):
            result = result + 1
    r = 0
    for i in xrange(n):
        count = 0
        if (i > 0):
            if (A[i - 1] != A[i]):
                count = count + 1
            else:
                count = count - 1
        if (i < n - 1):
            if (A[i + 1] != A[i]):
                count = count + 1
            else:
                count = count - 1
        r = max(r, count)
        print r
    return result + r

if __name__ == '__main__':
    print solution([0,0,0,1,0,0,1,1,1,1,1])