import sys
sys.stdin = open('input.txt')

for tc in range(1):
    text_length = int(input())
    text = list(map(str, input()))
    print(text)
    stack = []
    numbers =[]
    answer = 0
    for i in text:
        if i == '+' or i == '*':
            stack.append(i)
            if len(numbers) == 2:
                b = numbers.pop()
                a = numbers.pop()

                if i == '+':
                    answer = int(a) + int(b)
                    numbers.append(answer)
                if i == '*':
                    answer = int(a) * int(b)
                    numbers.append(answer)

        else:
            numbers.append(i)

        if len(numbers) == 1:
            print(numbers[0])
