__author__ = 'obscure'
import sys

fib = []


def fibonacci(n):
    global fib
    i = 4
    while(i<=n):
        fib[i] = fib[i-1]+fib[i-2]+fib[i-3]
        i += 1


def main(argv):
    if(len(sys.argv)<2):
        print 'usage fib.py <n>'
    fib.append(0)
    fib.append(1)
    fib.append(2)
    fib.append(4)
    n = int(sys.argv[1])
    for i in range(4, n+1):
        fib.append(0)
    fibonacci(n)
    print fib[n]

if(__name__ == '__main__'):
    sys.exit(main(sys.argv))
