# 문제. 토마토

# 입력받고 셋팅(덱, 델타, 큐)
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

C, R = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(R)]

queue = deque()

# 2중 for문으로 초기점 탐색(큐에 추가)
for r in range(R):
    for c in range(C):
        if box[r][c] == 1:
            queue.append((r, c))

# BFS 돌기
    # 큐가 빌 때까지
while queue:
    # 하나씩 꺼내서
    r, c = queue.popleft()
    # 4방탐색
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
    # 조건을 만족하면(범위조건, 0인지)
        if 0 <= nr < R and 0 <= nc < C and box[nr][nc] == 0:
    # 원본 배열 변형하고 다음 좌표를 큐에 넣을 것
            box[nr][nc] = box[r][c] + 1
            queue.append((nr, nc))

# 정답 판별
    # 배열을 다시 돌면서 0이 있는지 확인
ans = -1  # 토마토가 없으면 -1을 출력할 거라서
for row in box:
    if row.count(0) > 0:
        ans = 0
        break
    ans = max(ans, max(row))

print(ans - 1)
    # 있으면 -1
    # 없으면 배열의 최대값 -1