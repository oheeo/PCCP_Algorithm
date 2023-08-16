# 재귀 순열
arr = ['A', 'B', 'C']  # 재료 리스트
sel = [0, 0, 0]
check = [0, 0, 0]

def perm(depth):
    if depth == 3:
        print(sel)
        return
    
    for i in range(3):
        if not check[i]:
            check[i] = 1
            sel[depth] = arr[i]
            perm(depth+1)
            check[i] = 0
perm(0)

# 조합 2개 뽑기
arr = ['A', 'B', 'C']
for i in range(3):
    for j in range(i+1, 3):
        print(arr[i], arr[j])

# 중복 조합 2개 뽑기
arr = ['A', 'B', 'C']
for i in range(3):
    for j in range(i, 3):
        print(arr[i], arr[j])