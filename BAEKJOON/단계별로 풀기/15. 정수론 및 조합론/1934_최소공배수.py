from math import gcd


for T in range(int(input())):
    num1, num2 = map(int, input().split())
    print(num1 * num2 // gcd(num1, num2))