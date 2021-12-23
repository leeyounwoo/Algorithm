import sys

sys.stdin = open('input.txt')
n, m = map(int, sys.stdin.readline().rstrip().split())
site_password = {}
for i in range(n):
    site, password = map(str, sys.stdin.readline().rstrip().split())
    site_password[site] = password
for i in range(m):
    site = sys.stdin.readline().rstrip()
    print(site_password[site])