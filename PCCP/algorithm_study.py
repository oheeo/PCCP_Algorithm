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
word = input('단어를 입력하세요: ')

if word == word[::-1]:
    print('회문입니다')
else:
    print('회문이 아닙니다')

