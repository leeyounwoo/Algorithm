T = int(input())

for tc in range(T):
     numbers = list(map(int, input().split()))
     N = numbers[0]
     M = numbers[1]
          
     test_list = []
     for test in range(N):
          test_list.append(list(map(int, input().split())))
     
     max_num = 0
     for y_num in range(N-M+1):
          for x_num in range(N-M+1):
               sum_num = 0
               for i in range(y_num, M + y_num):
                    for j in range(x_num, M+x_num):
                         sum_num += test_list[i][j]
               if sum_num > max_num:
                    max_num = sum_num
     print(f'#{tc+1} {max_num}')     