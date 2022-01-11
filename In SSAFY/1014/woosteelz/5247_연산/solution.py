from collections import deque


# def make_num(temp_queue):
#     global cnt
#     while temp_queue:
#         temp_len = len(temp_queue)
#         for _ in range(temp_len):
#             temp = temp_queue.popleft()
#             if 0 < temp+1 <= 1000000 and not visited[temp+1]:
#                 temp_queue.append(temp+1)
#                 visited[temp+1] = 1
#             if 0 < temp-1 <= 1000000 and not visited[temp-1]:
#                 temp_queue.append(temp-1)
#                 visited[temp-1] = 1
#             if 0 < temp*2 <= 1000000 and not visited[temp*2]:
#                 temp_queue.append(temp*2)
#                 visited[temp*2] = 1
#             if 0 < temp-10 <= 1000000 and not visited[temp-10]:
#                 temp_queue.append(temp-10)
#                 visited[temp-10] = 1
#         if visited[M]:
#             return cnt+1
#         cnt += 1

def make(queue):
    while queue:
        curr = queue.popleft()
        for i in range(4):
            if i == 0:
                if curr + 1 <= 1000000 and not visited[curr + 1]:
                    queue.append(curr + 1)
                    visited[curr + 1] = visited[curr] + 1
            elif i == 1:
                if 0 < curr - 1 and not visited[curr - 1]:
                    queue.append(curr - 1)
                    visited[curr - 1] = visited[curr] + 1
            elif i == 2:
                if curr * 2 <= 1000000 and not visited[curr * 2]:
                    queue.append(curr * 2)
                    visited[curr * 2] = visited[curr] + 1
            elif i == 3:
                if 0 < curr - 10 and not visited[curr - 10]:
                    queue.append(curr - 10)
                    visited[curr - 10] = visited[curr] + 1
            if visited[M]:
                return visited[M] - 1


TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    cnt = 0
    visited = [0] * 1000001
    queue = deque()
    queue.append(N)
    visited[N] = 1

    print(f"#{tc} {make(queue)}")
