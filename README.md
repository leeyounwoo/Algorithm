# 문제 풀면서 배운 점들

## 1. 파이썬 기초

#### 1) 다양한 입력함수

1. input()
   - 기본적으로 문자열을 입력

2. sys.stdin.readline()

   - 한 줄에 여러 입력 값을 받을 수 있음

   - __import sys__를 사용해야 함

   - 기본적으로 개행문자(줄 바꿈 문자)를 포함하고 있음.

     ==> 공백 없이 출력할 수 있게 하는 함수 사용

     - rstrip(): 오른쪽 공백 삭제
     - lstrip(): 왼쪽 공백 삭제
     - strip(): 왼쪽, 오른쪽 공백을 삭제

   ~~~python
   import sys
   
   a, b = map(int, sys.stdin.readline().rstrip().split())
   print(a + b)
   ~~~

   