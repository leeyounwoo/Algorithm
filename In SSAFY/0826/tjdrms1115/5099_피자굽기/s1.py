import sys
sys.stdin = open('input.txt')


# 피자입니다.
class Pizza:
    def __init__(self, idx, cheese):
        self.idx = idx
        self.cheese = cheese


# 원형 큐입니다.
class CircularQueue:

    def __init__(self, size):
        self.size = size+1
        self.q = [None] * (size+1)
        self.front = size
        self.rear = size

    def is_full(self):
        if (self.rear + 1) % self.size == self.front:
            return True
        return False

    def is_empty(self):
        if self.rear == self.front:
            return True
        return False

    def enQ(self, item):
        try:
            if self.is_full():
                raise IndexError
            self.rear = (self.rear + 1) % self.size
            self.q[self.rear] = item
        except IndexError:
            print('Queue is full')

    def deQ(self):
        index = (self.front + 1) % self.size
        item = self.q[index]
        if item:
            self.q[index] = None
            self.front = (self.front + 1) % self.size
        return item


# 테스트 케이스의 개수를 입력받습니다.
T = int(input())

# 테스트 케이스만큼 코드를 실행하고 결과를 저장합니다.
answer = []
for tc in range(1, T+1):
    # 입력갑을 입력받습니다.
    N, M = map(int, input().split())
    # 피자번호와 치즈량을 속성으로 갖는 Pizza클래스를 생성해
    # 리스트에 추가합니다.
    pizza_list = []
    for idx, cheese in enumerate(list(map(int, input().split()))):
        pizza_list.append(Pizza(idx+1, cheese))

    # 화덕을 원형 큐로 만듧니다.
    stove = CircularQueue(N)
    # 우선 피자 N개를 채우고 시작합니다.
    for _ in range(N):
        stove.enQ(pizza_list.pop(0))

    # 마지막 피자의 번호를 저장할 변수입니다.
    result = 0
    # 피자가 화덕에 있는 동안 돌아갑니다.
    while True:
        # 피자를 꺼내 확인합니다.
        cur_pizza = stove.deQ()
        # 치즈가 반으로 줄었습니다.
        cur_pizza.cheese //= 2
        # 치즈가 아직 남았으면 다시 넣습니다.
        if cur_pizza.cheese > 0:
            stove.enQ(cur_pizza)
        # 치즈가 안남았다면 빼고 다른 피자를(남아있다면) 넣습니다.
        elif len(pizza_list) > 0:
            stove.enQ(pizza_list.pop(0))
        # 화덕이 비었으면 마지막으로 꺼낸 피자의 번호를 저장합니다.
        elif stove.is_empty():
            result = cur_pizza.idx
            break

    # 결과를 출력합니다.
    answer.append(result)

for tc in range(1, T+1):
    print('#{} {}'.format(tc, answer[tc-1]))
