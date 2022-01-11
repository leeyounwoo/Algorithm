from collections import deque

#deque 방식
de_queue = deque([])
de_queue.append(1)
de_queue.append(2)
de_queue.append(3) # de_queue: [1, 2, 3]

de_queue.popleft()
de_queue.popleft()
de_queue.popleft()

queue = []

queue.append(1)
queue.append(2)
queue.append(3) # queue: [1, 2, 3]

print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))