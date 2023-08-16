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


# 재귀 조합
# 5C3
arr = ['A', 'B', 'C', 'D', 'E']
sel = [0, 0, 0]


def combination(idx, sidx):
    if sidx == 3:  # sel 길이 범위를 벗어나면 sel이 확정됐다는 소리니까 print
        print(sel)
        return

    if idx == 5:  # 얘도 벗어나지 않아야 함
        return

    sel[sidx] = arr[idx]  # sidx가 가리키는 위치에 idx가 가리키는 재료를 넣음
    combination(idx+1, sidx+1)  # 첫번째로는 두개의 화살표가 동시에 오른쪽으로 가보고
    combination(idx+1, sidx)  # 두번째로는 arr 쪽 화살표만 혼자 가봄.


combination(0, 0)