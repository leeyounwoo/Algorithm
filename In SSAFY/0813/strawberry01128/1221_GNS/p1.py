import sys
sys.stdin = open('input.txt')
case_by_case = int(input())
# s1 = #
result = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']



for i in range(case_by_case):
    answer = []
    case, case_number = list(input().split())
    p = list(input().split())
    for i in result:
        for ggune in p:
            if i == ggune:
                answer.append(i)
    print(case)
    for cc in answer:
        print(cc, end=" ")
    print()

# zero = 0
# Zeo = zero
# print(Zeo)


