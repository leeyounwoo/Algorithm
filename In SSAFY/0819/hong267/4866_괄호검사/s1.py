import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    sentence = input()

    inspection = [] # 여는 괄호를 넣기 위한 stack
    result = 1 # 올바른 괄호 페어 확인 결과
    for i in range(len(sentence)):
        if sentence[i] == '(': # 여는 괄호가 나오면 stack에 추가
            inspection.append(sentence[i])
        elif sentence[i] == '{': # 여는 괄호가 나오면 stack에 추가
            inspection.append(sentence[i])
        elif sentence[i] == ')': # 닫는 소괄호가 나오면
            if len(inspection) == 0: # 이때 스택이 비어있으면
                result = 0 # 올바른 괄호 페어가 아니기에 결과 0을 반환
                break
            elif inspection[-1] == '(': # 만약 페어의 마지막 요소가 여는 소괄호라면
                inspection.pop() # 괄호 페어가 맞으므로 pop 해줌
            else:
                result = 0
                break
        elif sentence[i] == '}': # 닫는 중괄호가 나오면
            if len(inspection) == 0: # 이때 스택이 비어있으면
                result = 0 # 올바른 괄호 페어가 아니기에 결과 0을 반환
                break
            elif inspection[-1] == '{': # 만약 페어의 마지막 요소가 닫는 중괄호라면
                inspection.pop() # 괄호 페어가 맞으므로 pop 해줌
            else:
                result = 0
                break

    if inspection: # 여는 괄호가 남아있을 수도 있으므로 마지막으로 확인
        result = 0

    print('#{0} {1}'.format(tc, result))
