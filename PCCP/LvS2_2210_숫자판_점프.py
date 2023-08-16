# 문제. 숫자판 점프
# 5×5 크기의 숫자판이 있다. 각각의 칸에는 숫자(digit, 0부터 9까지)가 적혀 있다. 이 숫자판의 임의의 위치에서 시작해서, 인접해 있는 네 방향으로 다섯 번 이동하면서, 각 칸에 적혀있는 숫자를 차례로 붙이면 6자리의 수가 된다. 이동을 할 때에는 한 번 거쳤던 칸을 다시 거쳐도 되며, 0으로 시작하는 000123과 같은 수로 만들 수 있다. 
# 숫자판이 주어졌을 때, 만들 수 있는 서로 다른 여섯 자리의 수들의 개수를 구하는 프로그램을 작성하시오.
# 입력: 다섯 개의 줄에 다섯 개의 정수로 숫자판이 주어진다.
# 출력: 첫째 줄에 만들 수 있는 수들의 개수를 출력한다.


# 입력받고 셋팅(델타, input, 케이스)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

board = [input().split() for _ in range(5)]

cases = set()  # 6개가 될 때마다 이 cases에 담기

# DFS 돌기(재귀 함수)
    # 재귀함수(r, c, num)
def dfs(r, c, num):
        # len(num) 6되면 케이스에 넣고 함수 종료
    if len(num) == 6:
        cases.add(num)
        return
    
        # 4방탐색
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        # 다음 갈 곳이 보드에 있다면
        if 0 <= nr < 5 and 0 <= nc < 5:
        # 다음 칸 숫자를 이어붙이고 다음 재귀로
            dfs(nr, nc, num + board[nr][nc])

# 2중 for문을 모든 경우를 돌면서 탐색
for r in range(5):
    for c in range(5):
        dfs(r, c, board[r][c])

# 정답은 set 길이
print(len(cases))