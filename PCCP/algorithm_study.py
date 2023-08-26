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

# 재귀함수
