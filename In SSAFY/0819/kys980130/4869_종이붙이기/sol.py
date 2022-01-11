import sys
sys.stdin = open('input.txt')

def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return paper(n - 1) + paper(n - 2) * 2

def paper_memo(n):
    paper = [1, 3]
    for i in range(2, n):
        paper.append(paper[i-1] + paper[i-2] * 2)
    return paper[n-1]

TC = int(input())
for tc in range(TC):
    num = int(input()) // 10
    print('#{} {}'.format(tc+1, paper_memo(num)))