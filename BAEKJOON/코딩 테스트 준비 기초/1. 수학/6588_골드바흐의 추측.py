import sys

def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')
n=1000000
a = [False,False] + [True]*(n-1)
primes=[]
flag = [False] * (n+1)

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    flag[i] = True
    for j in range(2*i, n+1, i):
        a[j] = False

while True:
    number = int(input())
    if number == 0:
        break
    for a in primes:
        if flag[number - a]:
            print('{} = {} + {}'.format(number, a, number - a))
            break