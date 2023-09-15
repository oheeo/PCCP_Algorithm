# 파이썬 입출력
# nums = input('입력해주세요: ')
# print(nums, type(nums))

# nums = list(map(int, input().split()))
# print(nums, type(nums))
# 1 2 3 입력시 [1, 2, 3] 출력

# 2차원 리스트 받기
# nums_matrix = [list(map(int, input().split())) for _ in range(3)]
# print(nums_matrix, type(nums_matrix))
# 1 2 3
# 4 5 6
# 7 8 9
# 입력시 [[1, 2, 3], [4, 5, 6], [7, 8, 9]] <class 'list'> 출력


# 함수
def some_func(param1, param2):
    return [param1, param2]

print(some_func(1, 2))  # [1, 2]


# 재귀함수 : 함수 내에서 동일한 함수가 실행되는 함수
def fibo(n):
    if n < 2 :  # 1은 더 쪼개지지 않음
        return n
    else:
        return fibo(n-1) + fibo(n-2)  # 재귀 호출
print(fibo(10))  # 55


# 참고(효율적인 메모이제이션)
memo = [0, 1]
def fibo(n):
    if n >= 2 and n >= len(memo):
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]
print(fibo(10))  # 55


# 이진검색
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def binary_search(low, high, target):
    if low > high:
        return '찾지 못 함'
    
    mid = (low + high)  // 2
    if target == nums[mid]:
        return mid
    elif target < nums[mid]:
        return binary_search(low, mid-1, target)
    elif target > nums[mid]:
        return binary_search(mid+1, high, target)

print(binary_search(0, len(nums)-1, 7))  # 6


print("-----------------------------------------")


# 리스트
user = ['alex', 3, True]

# 딕셔너리
user = {'name': 'alex', 'age':3, 'license':True}

# 여러 자료구조 섞어서
users = {
	'total_user': 3,
	'information': [
			{'name': 'alex', 'age':3, 'license':True},
			{'name': 'june', 'age':7, 'license':False},
			{'name': 'peter', 'age':4, 'license':False}
	]
}


# 제어문 if, 반복문 for

# 어떤 광산에서는 채굴한 광물들의 등급을 상품인 1등급부터 하품인 3등급까지 나누어 등급을 매긴 후, 해당 정보를 저장해서 관리합니다.
# A 광산은 10개의 광물을 채굴하였고 각각 등급은 다음과 같습니다.
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
# 채굴한 광물들 중 1등급 광물이 존재하는지 여부는 어떻게 알 수 있을까요?

# 방법 1 : in 연산자를 활용합니다.
if 1 in gems:
	print(True)
else:
	print(False)
        
        
# 방법 2 : for문과 제어문을 섞어 활용합니다.
grade1 = False  # 특정 변수(flag)를 통해 여부를 저장하는 편이 좋습니다.
for i in gems:
    if i == 1:
        grade1 = True
        break  # 효율성을 위한 미리 브레이크
print(grade1)


# 1, 2, 3등급 광물은 각각 몇 개가 있는지 어떻게 기록하면 좋을까요?
# 자유롭게 구조화 합니다.
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
grades = {1:0, 2:0, 3:0}

for i in gems:
    grades[i] += 1

print(grades)


# 만약 광물의 등급의 합계가 15 이하면 성공, 23 이하면 보통, 30을 초과하면 실패라고 할 때, 올해의 등급에 따른 성공 척도를 출력하려면 어떻게 해야 할까요?
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
result = sum(gems)

if result <= 15:
    print('성공')
elif 15 < result <= 23:
    print('보통')
else:
    print('실패')


# 실전 문제풀이
# max(), min() 함수의 직접 구현
nums = [7, 1, 2, 4, 6, 8, 3]

# 최댓값
max_num = -1  # 작은 수로 초기화
for num in nums:
    if max_num < num:
        max_num = num

print(max_num)

min_num = 9999  # 큰 수로 초기화
for num in nums:
    if min_num > num:
        min_num = num
print(min_num)


print("-----------------------------------------")


# 스트링 알고리즘


# 파이써닉 코드
# word = input('단어를 입력하세요: ')

# if word == word[::-1]:
#     print('회문입니다')
# else:
#     print('회문이 아닙니다')


# 반복문 사용
# word = input('단어를 입력하세요: ')

# reversed_word = ''
# for i in word:
#     reversed_word = i + reversed_word

# if word == reversed_word:
#     print('회문입니다')
# else:
#     print('회문이 아닙니다')


# two pointer 활용
# word = input('단어를 입력하세요: ')

# left = 0 # 시작 인덱스
# right = len(word)-1 # 마지막 인덱스

# is_palindrome = True
# while left < right:  # 왼쪽과 오른쪽이 유지될때까지 돌아라!
#     if word[left] == word[right]:  # 같은 경우라면 아직은 회문 조건을 만족함
#         left += 1  # 왼쪽 포인터를 한칸 오른쪽으로 증가시키고
#         right -= 1  # 오른쪽 포인터를 한 칸 왼쪽으로 감소
#         continue
#     else:  # 다른 경우라면 그 즉시 안된다고 표시하고 break
#         is_palindrome = False
#         break

# print(is_palindrome)


# 문자열 포함 여부 검사하기
t = 'hello world' # text
p = 'wor'         # target pattern

def find_word(p, t):
    N = len(t)
    M = len(p)

    for i in range(N-M+1):
        cnt = 0
        for j in range(M):
            if t[i+j] == p[j]:
                cnt += 1
            else:
                break

        if cnt == M:
            return i

    return '못찾았음'

print(find_word(p, t))


print("-----------------------------------------")


# 2차원 리스트

# 행 우선 순회
matrix = [[3, 7, 9],
		      [4, 2, 6],
	    	  [8, 1, 5]]

trails = []  # 순회 궤적 담아줄 리스트

for r in range(3):
    for c in range(3):  # r 이 하나 고정된 상태에서 각각
        trails.append(matrix[r][c])

print(trails)  # [3, 7, 9, 4, 2, 6, 8, 1, 5]


# 행으로 순회, 열은 역순으로
matrix = [[3, 7, 9],
		      [4, 2, 6],
	    	  [8, 1, 5]]

trails = []  # 순회 궤적 담아줄 리스트

for r in range(3):
    for c in range(2, -1, -1):  # 역순인데, 새끼 리스트의 길이 - 1 시작!
        trails.append(matrix[r][c])

print(trails) # [9, 7, 3, 6, 2, 4, 5, 1, 8]


# 행 우선 순회, 지그재그로
matrix = [[3, 7, 9],
		  [4, 2, 6],
	      [8, 1, 5]]

trails = []  # 순회 궤적 담아줄 리스트

for r in range(3):
    if r % 2 == 0:
        for c in range(3):
            trails.append(matrix[r][c])
    elif r % 2 == 1:
        for c in range(2, -1, -1):
            trails.append(matrix[r][c])

print(trails) # [3, 7, 9, 6, 2, 4, 8, 1, 5]


# 열 우선 순회
matrix = [[3, 7, 9],
		      [4, 2, 6],
	    	  [8, 1, 5]]

trails = []

for r in range(3):
    for c in range(3):
        trails.append(matrix[c][r])  # 여기가 바뀝니다.

print(trails)  # [3, 4, 8, 7, 2, 1, 9, 6, 5]


# 전치
matrix = [[3, 7, 9],
		      [4, 2, 6],
	    	  [8, 1, 5]]

for r in range(3):
    for c in range(3):
        if r > c: # r < c로 해도 됩니다.
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

for i in range(3):
    print(matrix[i])
# [3, 4, 8]
# [7, 2, 1]
# [9, 6, 5]

# zip을 활용한 전치하기 => 원소가 튜플이 됩니다.
zipped_matrix = list(zip(*matrix))
print(zipped_matrix) # [(3, 4, 8), (7, 2, 1), (9, 6, 5)]

# 전치 완료 후, 원소를 리스트로 활용하고 싶을 때
transposed_matrix = list(map(list, zip(*matrix)))
print(transposed_matrix)
# [[3, 4, 8], [7, 2, 1], [9, 6, 5]]


# 회전
# 오른쪽으로 90도 회전시킨 이차원 리스트
n = 3
rotated_matrix = [[0] * n for _ in range(n)]  # 초기화

for i in range(n):
    for j in range(n):
        rotated_matrix[i][j] = matrix[n-j-1][i]
# rotated_matrix 결과

[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]

# 왼쪽으로 90도 회전시킨 이차원 리스트
n = 3
rotated_matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        rotated_matrix[i][j] = matrix[j][n-i-1]
# rotated_matrix 결과

[
    [3, 6, 9],
    [2, 5, 8],
    [1, 4, 7]
]

# zip을 이용한 오른쪽 90도 회전
rotated_matrix = list(zip(*matrix[::-1]))
# rotated_matrix 결과

[
    (7, 4, 1),
    (8, 5, 2),
    (9, 6, 3)
]

# zip을 이용한 왼쪽 90도 회전
rotated_matrix = list(zip(*matrix))[::-1]
# rotated_matrix 결과

[
    (3, 6, 9),
    (2, 5, 8),
    (1, 4, 7)
]


print("-----------------------------------------")


# 스택, 큐, DFS,BFS
# 스택
# 웹 서핑을 하다가 뒤로 가는 경우를 코드로 구현
# visits = [] # 방문 기록지
# # 1. 처음으로 구글에 방문
# visits.append('google') #  ['google']

# # 2. 그다음 인스타그램에 방문
# visits.append('instagram') # ['google', 'instagram']

# # 3. 그다음 페이스북에 방문
# visits.append('facebook') # ['google', 'instagram', 'facebook']

# # 4. 뒤로가기 버튼을 누름
# visits.pop()
# print(visits) # ['google', 'instagram'] => 다시 인스타그램 페이지로 돌아옴


# class를 활용한 스택의 직접 구현 코드
# class Stack:
#     def __init__(self,n):
#         self.top = -1
#         self.stack = [0]*n

#     def push(self,data):
#         if self.top == len(self.stack) - 1:
#             return None
#         self.top += 1
#         self.stack[self.top] = data

#     def pop(self):
#         if self.top == -1:
#             return None
#         self.top -= 1
#         return self.stack[self.top+1]

# my_stack = Stack(10)
# my_stack.push('alex')
# print(my_stack)
# print(my_stack.pop())
# print(my_stack)


# DFS 깊이 우선 탐색
# 인접 행렬로 정리
V, E = map(int, input().split())  # Vertex(포도알), Edge(선) 갯수

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]  # 인접행렬 기본틀 + 0번 포도알은 안씀

for _ in range(E):  # 간선 갯수만큼 돌면서 연결 정보를 받음
    start, end = map(int, input().split())  # 시작점과 끝점
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1  # 양방향 그래프니까!!
print(adj_matrix)

# adj_matrix print 결과

# [[0, 0, 0, 0, 0, 0, 0, 0],  => 0번 포도알은 존재하지 않음
#  [0, 0, 1, 1, 0, 0, 0, 0],  => 1번 포도알은 2, 3번으로 갈 수 있음
#  [0, 1, 0, 0, 1, 1, 0, 0],  => 2번 포도알은 1, 4, 5번 가능
#  [0, 1, 0, 0, 0, 0, 0, 1],  => 3번 포도알은 1, 7번 가능
#  [0, 0, 1, 0, 0, 0, 1, 0],  => 4번 포도알은 2, 6번 가능
#  [0, 0, 1, 0, 0, 0, 1, 0],  => 5번 포도알은 2, 6번 가능
#  [0, 0, 0, 0, 1, 1, 0, 1],  => 6번 포도알은 4, 5, 7번 가능
#  [0, 0, 0, 1, 0, 0, 1, 0]]  => 7번 포도알은 3, 6번 가능


# 인접 리스트로 정리
V, E = map(int, input().split())

adj_list = [[] for _ in range(V + 1)]

for _ in range(E):
    start, end = map(int, input().split())
    adj_list[start].append(end)
    adj_list[end].append(start)  # 양방향
print(adj_list)
# adj_list = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]


# 왜 stack을 쓰고 깊이 우선 탐색이지?
# 최초 시행
visited = []
stack = [1]

# stack pop => 1 후에 갈 수 있는걸 골라보니? 2, 3번 포도알로 갈 수 있었음.
visited = [1]
stack = [2, 3] 

# 그런 다음 다음 pop은 stack이니까 뒤부터 3이 튀어나옴 + 3이 갈 수 있는 7이 더해짐.
visited = [1, 3]
stack = [2, 7]  # 1은 visited에 있으니까 안들어감

# 7을 뽑아냄
visited = [1, 3, 7]
stack = [2, 6]

# 이런식으로 2는 계속 기다리고, 3 -> 7 -> 6 식으로 쭉쭉 "깊게" 뻗어나감!


# DFS 풀이법
# 스택 + 인접 행렬 (공간 복잡도 높으나, 단방향 그래프인 경우 전치로 방향 전환 유리)
V, E = map(int, input().split())  # Vertex, Edge 갯수

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]  # 인접행렬 기본틀

for _ in range(E):  # 간선 갯수만큼 돌면서 연결 정보를 받음
    start, end = map(int, input().split())  # 시작점과 끝점
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1  # 양방향 그래프니까!!

stack = [1]  # 맨처음 시작점은 1번 포도알
visited = []  # 궤적 기록용

while stack:  # 스택이 빌때까지 돌아라!
    current = stack.pop()  # 우선 스택에서 현재 위치 하나 뽑고
    if current not in visited:  # 방문하지 않은 곳이라면,
        visited.append(current)  # 방문했다고 체크해줌
		
		# 위의 if문 안으로 넣으면 더 좋습니다.
    for destination in range(V+1):  # current 입장에서 어디로 갈 수 있는지 모조리 체크
        if adj_matrix[current][destination] and destination not in visited:  # 갈수있고 + 방문 안했으면!
            stack.append(destination)  # 다음 갈 곳으로 Stack에 저장

print('이동경로:', *visited)

# 이동경로: 1 3 7 6 5 2 4


# 스택 + 인접 리스트 (공간 복잡도 낮음)
V, E = map(int, input().split())  # Vertex, Edge 갯수

adj_list = [[] for _ in range(V + 1)]  # 인접리스트 기본틀

for _ in range(E):  # 간선 갯수만큼 돌면서 연결 정보를 받음
    start, end = map(int, input().split())  # 시작점과 끝점
    adj_list[start].append(end)
    adj_list[end].append(start)  # 양방향 그래프니까!!

stack = [1]  # 맨처음 시작점은 1번 포도알
visited = []  # 궤적 기록용

while stack:  # 스택이 빌때까지 돌아라!
    current = stack.pop()  # 우선 스택에서 현재 위치 하나 뽑고
    if current not in visited:  # 방문하지 않은 곳이라면,
        visited.append(current)  # 방문했다고 체크해줌

    for destination in adj_list[current]:
        if destination not in visited:  # 갈 수 있고 + 방문 안했으면!
            stack.append(destination)  # 다음 갈 곳으로 Stack에 저장

print('이동경로:', *visited)

# 이동경로: 1 3 7 6 5 2 4


# 재귀 + 인접 행렬 (가독성은 좋으나 재귀 자체가 좀 느림)
# 주의: 재귀함수를 활용하는 경우 return을 쓰면 끊길 수 있음
def dfs(n):
    if n not in visited:  # 우선 visited 없으면 넣어줌
        visited.append(n)

    for destination in range(V+1):
        if adj_matrix[n][destination] and destination not in visited:
            dfs(destination)  # 다음 재귀 깊이로 이동

V, E = map(int, input().split())  # Vertex, Edge 갯수

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]  # 인접행렬 기본틀

for _ in range(E):  # 간선 갯수만큼 돌면서 연결 정보를 받음
    start, end = map(int, input().split())  # 시작점과 끝점
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1  # 양방향 그래프니까!!

visited = []  # 궤적 기록용

dfs(1)  # 1번 포도알부터 시작!

print('이동경로:', *visited)
# 이동경로: 1 2 4 6 5 7 3 => 이거 다른거 주의!!
# main이 종료되어야 sub가 실행된다는 것을 생각
# 다음 main은 이전 main의 sub임
# (main) (sub1) (sub2) ...
# 1
# 1-2 / 1-3
# 1-2-4 / 1-2-5 / 1-3
# 1-2-4-6 / 1-2-4-5 / 1-2-5 / 1-3
# 1-2-4-6-5 / 1-2-4-6-7 / 1-3 # main이 5를 갔으니 sub 1-2-5, sub 1-2-4-5는 시작도 못함
# (1-2-4-6-5) / 1-2-4-6-7 / 1-3 # main 종료 및 기록됨, 이전 main 1-2-4-6이 main이 됨
# (1-2-4-6-5)-7 / 1-3 # main이 7을 갔으니 sub 1-2-4-6-7은 시작도 못함
# (1-2-4-6-5)-7-3 # main이 3을 갔으니 sub 1-3은 시작도 못함
# main 종료, sub는 없음

# 일반적으로 재귀함수를 이용한 DFS는 미로찾기 등의 문제에서 가로 * 세로가 12 X 12 이상이 되면 maximum recursion depth 에러가 뜰 수 있으므로 지양합니다. 그러므로 DFS 문제는 Stack을 활용하여 푸는 방식이 좋습니다.


# DFS 연습 문제
# 연속한 1의 갯수 찾기 -> 델타 탐색 응용

# N*N크기의 배열이 주어졌을때 1의 개수는 몇개인지 세어보기 dfs를 이용해서
# 하나의 시작 1로 부터 붙어져 있는 연속된 1의 개수 세어보기 => 2, 13이 답이 됨.
# 7
# 0000011
# 0000000
# 0011100
# 0010111
# 0110010
# 0011100
# 0000000

# 방향잡기(상,우,하,좌)
dr = [-1,0,1,0]
dc = [0,1,0,-1]
# 행과 열의 좌표가 들어옴
def DFS(r, c):
    global cnt
    # 해당 arr[r][c] 자리값이 1이므로 방문체크와 동시에 카운트를 1증가
    arr[r][c] = 0
    cnt += 1
    # 4방 탐색
    for i in range(4):
        # 새로운 좌표값을 활용
        nr = r + dr[i]
        nc = c + dc[i]
        
        # 새로운 좌표값을 활용한 범위검사
        # 범위를 벗어나면 다른 방향을 탐색
        # if 0<=nr<N and 0<=nc<N: 조건도 가능(파이썬에서만)
        if nr<0 or nr>= N or nc <0 or nc>=N:
            continue
        # 이미 방문을 했어도 종료(이것이 없으면 무한으로 방문)
        # 이 아래 조건을 위에 한꺼번에 쓸거면 단축평가 오른쪽엔 가능함 근데 이거 따로쓸거면 맵 제한조건보다 위에 두면 조짐. 
        if arr[nr][nc] == 0:
            continue
        # 걸러낼 조건을 모두 걸러내면 재귀가 가능
        DFS(nr, nc)  # 또 한 뎁스 들어가라!!
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]  # 행의 길이만큼 만들어준다.

# 입력이 끝났으면 처음 시작 위치 찾기
for i in range(N):  # 행우선순회 하면서 전부다 보되
    for j in range(N):
        if arr[i][j] == 1:  # 그자리가 1이야?
            cnt = 0  # prep 하고
            DFS(i, j)  # dfs 해!
            print(cnt)


# 추가 참고 코드
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def BFS(r, c):
    # Q를 초기화
    Q = []
    Q.append((r, c))
    dist[r][c] = 1
    # Q에 요소가 존재할때까지만 돌 것(빈 컨테이너가 되면 멈춰버린다)
    