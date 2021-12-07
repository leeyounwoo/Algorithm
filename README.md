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






#### 2) 절대값

```python
abs(-1) # ==> 1
```





#### 3) 문자를 아스키로, 아스키 코드를 문자로

- ord(문자): 아스키 코드를 반환해준다
- chr(숫자): 숫자에 맞는 아스키 코드를 반환해준다





#### 4) join 함수

> **''.join(리스트)**
>
> **'구분자'.join(리스트)**

- join 함수는 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환하는 함수

  ~~~python
  array = ["Hi", "my", "name", "is", "Lee"]
  
  str1 = " ".join(array)
  # Hi my name is Lee
  ~~~

- <span style="color: red;">>> 예외: 리스트 배열이 모두 문자열이어야 에러가 발생하지 않는다.</span>

- 리스트 배열이 정수형일 때는 리스트 정수형을 리스트 문자열로 변환한 뒤 문자열로 바꾼다.

  ~~~python
  a = [0, 1, 2, 3]
  
  str1 = " ".join(str(i) for i in a)
  # 0 1 2 3
  ~~~

  

