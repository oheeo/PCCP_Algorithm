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