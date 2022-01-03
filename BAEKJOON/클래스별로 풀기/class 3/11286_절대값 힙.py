import sys


class MinHeap:
    def __init__(self):
        self.data = [0]

    def insert(self, item):
        self.data.append(item)
        i = len(self.data) - 1
        while i > 1:
            if abs(self.data[i]) < abs(self.data[i//2]):
                self.data[i], self.data[i//2] = self.data[i//2], self.data[i]
                i //= 2
            elif abs(self.data[i]) == abs(self.data[i//2]):
                if self.data[i] < self.data[i//2]:
                    self.data[i], self.data[i // 2] = self.data[i // 2], self.data[i]
                    i //= 2
                else:
                    break
            else:
                break

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.minHeapify(1)
        else:
            data = 0
        return data

    def minHeapify(self, i):
        left = 2 * i
        right = (2 * i) + 1
        smallest = i
        # 왼쪽 자식이 존재하는지, 그리고 왼쪽 자식의 (키) 값이 부모보다 더 큰지 판단.
        if left < len(self.data):
            if abs(self.data[i]) > abs(self.data[left]):
                smallest = left
            elif abs(self.data[i]) == abs(self.data[left]):
                if self.data[i] > self.data[left]:
                    smallest = left
        # 오른쪽 자식이 존재하는지, 그리고 지금까지 최대값보다 오른쪽 자식의 값이 더 큰지 판단
        if right < len(self.data):
            if abs(self.data[smallest]) > abs(self.data[right]):
                smallest = right
            elif abs(self.data[smallest]) == abs(self.data[right]):
                if self.data[smallest] > self.data[right]:
                    smallest = right
        # 오른쪽 자식 혹은 왼쪽 자식이 더 큰 경우, 값 교환 + 재귀호출
        if smallest != i:
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            self.minHeapify(smallest)


sys.stdin = open('input.txt')
n = int(input())
ans = MinHeap()
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    # print(num)
    if num:
        # print('not', num)
        ans.insert(num)
        # print(ans.remove())
    else:
        print(ans.remove())
    # print(ans.data)