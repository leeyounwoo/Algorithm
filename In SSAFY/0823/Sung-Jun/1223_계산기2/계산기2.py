import sys
sys.stdin = open('input.txt')

# T = 10
# for tc in range(1):
#     num_lem = int(input())
#     char_list = input()
#     print(char_list)
#
#     stack = []
#     result = []
#     for char in char_list:
#         if char not in ['+', '*']:
#             result.append(char)
#         else:
#             if stack == []:
#                 stack.append(char)
#             elif char == '+':
#                 if stack[-1] == '*' or stack[-1] == '+':
#                     while stack:
#                         result.append(stack.pop())
#                     stack.append(char)
#                 else:
#                     stack.append(char)
#             elif char == '*':
#                 if stack[-1] == '*':
#                     for w in stack:
#                         if w == '+':
#                             break
#                     result.append(stack.pop())
#
#                 else:
#                     stack.append(char)
#     print(result)
#
#     total = []
#     for check in result:
#         if check in ['*', '+']:
#             a = total.pop()
#             b = total.pop()
#             if check == '+':
#                 total.append(b + a)
#             elif check == '*':
#                 total.append(b * a)
#         else:
#             total.append(int(check))
#     print(total)

for tc in range(1):
    number = int(input())
    char = input()
    print(char)
    order_num = '(+*)'

    stack = []
    result = ''
    for check in range(number):
        if char[check] not in ['+', '*', '(', ')']:
            result += char[check]
        else:
            if stack == []:
                stack.append(char[check])
            elif char[check] == '(':
                stack.append(char[check])
            elif char[check] == '+':
                if order_num.find(stack[-1]) < order_num.find(char[check]):
                    stack.append(char[check])
                else:
                    result += stack.pop()
            elif char[check] == '*':
                if order_num.find(stack[-1]) < order_num.find(char[check]):
                    stack.append(char[check])
                else:
                    result += stack.pop()
            else:
                if stack[-1] == '(':
                    stack.pop()
                    pass
                else:
                    result += stack.pop()
    print(result)


