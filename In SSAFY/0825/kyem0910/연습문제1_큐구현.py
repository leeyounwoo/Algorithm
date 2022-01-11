from collections import deque

# deque 방식(일반 방식 시간초과날때 사용)
de_queue = deque([])
de_queue.append(1)
de_queue.append(2)
de_queue.append(3) # de_queue : [1,2,3]

de_queue.popleft()
de_queue.popleft()
de_queue.popleft()

# 일반 리스트 사용방식
queue = []

queue.append(1)
queue.append(2)
queue.append(3) # queue: [1,2,3]

print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))