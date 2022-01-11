import sys
sys.stdin = open('input.txt')



for tc in range(10):
  n = int(input())
  data = list(map(int, input().split()))
  result = 0
  for i in range(2, n-2):
      around = max([data[i - 2], data[i - 1], data[i + 1], data[i + 2]])
      if(data[i] > around):
          result += data[i] - around

  print(f"#{tc + 1} {result}")