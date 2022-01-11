from collections import deque

queue = deque()
# queue = []


queue.append(1)
queue.append(2)
queue.append(3)

print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

