print("Hello 1")
print('Hello 2')  # 주석
# print("Hello 3")
print(type("Hello123@##$"))
print("큰따옴표 안에 '작은따옴표' 사용하기")

print(type(100))
print(type(0))
print(type(-15))

print(type(1.2))
print(type(-3.5))
print(type(4.0))  # 정수형 4 라고 생각할 수 있지만, 소수점이 존재하므로 실수형이다.

print(type(True))
print(type(False))

print(type(int('123')))  # 문자열 '123' 을 정수형으로 변환
# print(type(int('1.5')))  # 정수형으로 변환될 수 있을때만 가능

if False:
    print("조건이 참입니다.")
else:
    print("조건이 거짓입니다.")
print("들여쓰기 안하면 무조건 실행됩니다.")

number = 3
if number % 2 == 0:
    print("짝수 입니다.")
else:
    print("홀수 입니다.")

age = 15
if age >= 30:
    print("30대")
else:
    if age >= 20:
        print("20대")
    else:
        print("미성년자")

if age >= 30:
    print("30대")
elif age >= 20:  # else if를 줄여서 elif
    print("20대")
elif age >= 10:
    print("10대")
else:
    print("어린이")



# 컨테이너 : 여러개의 데이터를 한 곳에 저장할 수 있는 자료형

# List
numbers = [10, 20, 30, 40, 50]
print(numbers)
print(type(numbers))  # <class 'list'>
# len() : 리스트의 길이를 알 수 있는 함수
print(len(numbers))  # 5
print(numbers[1])  # 20 (1번째)

data = [10, 1.5, "hi", True]
print(data)
print(type(data))  # <class 'list'>

empty = []
print(empty)  # []

a = [1, 2]
b = [3, 4]
c = a + b
print(c)  # [1, 2, 3, 4]
d = a * 3  # 반복된(혹은 같은) 원소가 여러 개 있는 리스트 만들 때 유용
print(d)  # [1, 2, 1, 2, 1, 2]


# List Slicing (자르기)
a = [10, 20, 30, 40, 50]
#     0   1   2   3   4  번째
#    -5  -4  -3  -2  -1  번째

print(a[2:3])  # [30]

print(a[2:4])  # [30, 40]

print(a[2:-1])  # [30, 40]

a[1:4:2]  # 1에서 4까지 자르는데 2간격으로
print(a[1:4:2])  # [20, 40]

print(a[0:4:3])  # [10, 40]  0에서 4까지 자르는데 3간격으로

a[::-1]  # 리스트를 뒤집을 때 많이 사용
print(a[::-1])  # [50, 40, 30, 20, 10]


# List 에 삽입, 삭제
a.append(60)  # 삽입
print(a)  # [10, 20, 30, 40, 50, 60]

a.pop()  # 리스트 a의 마지막 원소 60을 삭제
print(a)  # [10, 20, 30, 40, 50]

a.pop(2)  # 리스트 a의 2번째 원소 30을 삭제
print(a)  # [10, 20, 40, 50]

b = a.pop()  # 리스트 a의 마지막 원소 50을 삭제하고 b에 반환
print(b)  # 50

b = a.pop(1)  # 리스트 a의 1번째 원소 20을 삭제하고 b에 반환
print(b)  # 20


# 문자열도 사실은 컨테이너 자료형
# "hello" 문자열은 "h", "e", "l", "l", "o" 5개의 문자가 연속으로 나열된 집합체이다.
hello = "Hello World!"
print(len(hello))  # 12 (공백, 느낌표 포함)
print(hello[1])  # 1번째 원소인 "e" 출력

a = "안녕"
b = a * 3
print(b)  # 안녕안녕안녕

# 문자열은 리스트와 달리 원소를 수정할 수 없다. (원소의 삽입, 삭제도 불가능)
# 문자열 덧셈과 슬라이싱을 이용하여 마치 수정한 것 같은 효과를 줄 수 있다.
word = "python"
new_word = "j" + word[1:]
print(new_word)  # jython

# Formatting : 문자열 안에 변수의 값을 삽입하는 방법
name = "hee"
age = 20
sentence1 = f"{name}는 {age}살 입니다."
sentence2 = f"내년이 되면 {age + 1}살 입니다."
print(sentence1)
print(sentence2)


# 레인지 (range) : 연속된 정수 목록을 저장하는 컨테이너 자료형
# range(start, end, step)
range(1, 11)      # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
range(1, 11, 2)   # 1, 3, 5, 7, 9
range(10, 0, -1)  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
range(0, 5)       # 0, 1, 2, 3, 4
range(5)          # 0, 1, 2, 3, 4 (start가 생략되어 range(0, 5)와 같음)

# 그런데 range()를 단순히 출력할 땐 원소의 값을 확인하기 어렵다.
a = range(1, 11)
print(a)  # range(1, 11)
print(type(a))  # <class 'range'>

# for문으로 각각의 원소를 출력할 수 있다.
for i in range(1, 11):
    print(i, end=" ")  # 1 2 3 4 5 6 7 8 9 10
    # end는 줄바꿈없이 바로 출력한다
    # end="," 이렇게 적으면 1,2,3,4,5,6,7,8,9,10 출력


# 컨테이너 형 변환
# 문자열 -> 리스트
a = "python"
b = list(a)
print(b)  # ['p', 'y', 't', 'h', 'o', 'n']

# 레인지 -> 리스트
a = range(10)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
print(a)  # range(0, 10)
b = list(a)
print(b)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# 원소 in 컨테이너
numbers = [1, 2, 3, 4, 5]
print(1 in numbers)  # True
print(6 in numbers)  # False

# 원소 not in 컨테이너
word = "python"
print("p" not in word)  # False
print("j" not in word)  # True

classroom = ["hee", "min", "ken", "alex"]
if "hee" in classroom:
    print("hee는 출석했습니다")
else:
    print("hee는 결석했습니다.")



# 반복문
# for 반복문 : 반복 횟수가 정해져 있는 경우
# for 변수 in 컨테이너
names = ["hee", "min", "ken", "alex"]
for name in names:
    print(f"안녕! {name}!")
# 안녕! hee!
# 안녕! min!
# 안녕! ken!
# 안녕! alex!

word = "hello"
for char in word:
    print(char)
# h
# e
# l
# l
# o

# 짝수 출력
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 2 == 0:
        print(number)
# 2
# 4
# 6
# 8
# 10

# 홀수 출력
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 2 == 1:
        print(number)
# 1
# 3
# 5
# 7
# 9

# for i in range(n)
for i in range(3):
    print(i)
# 0
# 1
# 2

for i in range(1, 11, 2):
    print(i)
# 1
# 3
# 5
# 7
# 9

for i in range(3):
    print("이 문장은 3번 반복됩니다.")
# 이 문장은 3번 반복됩니다.
# 이 문장은 3번 반복됩니다.
# 이 문장은 3번 반복됩니다.

# i 를 인덱스로 사용하여 원소에 접근할 수 있다.
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i])
# 1
# 2
# 3
# 4
# 5

# 짝수번째 인덱스의 원소만 출력
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    if i % 2 == 0:
        print(numbers[i])
# 1
# 3
# 5


# while 반복문 : 반복 횟수가 정해져 있지 않은 경우 (사용자가 반복 횟수 조절)
# 조건문의 결과가 True일 경우 반복, False일 경우 중단
# 증감식이 없으면 무한루프 발생 (break로 종료할 수도 있다.)
# 조건문에 들어가는 변수에 대한 초기화 필수

number = 1  # 초기화
while number <= 5:  # 조건
    print(number)
    number += 1  # 증감식이 있어야만 반복을 종료할 수 있다.
# 1
# 2
# 3
# 4
# 5

# while문으로 리스트 순회
numbers = [10, 20, 30, 40, 50]
i = 0  # 초기화
while i < len(numbers):  # 조건
    print(numbers[i])
    i += 1  # 증감식
# 10
# 20
# 30
# 40
# 50

# while문을 조건문과 함께 사용하기 -> 필터링
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0  # 초기화
# 짝수만 출력
while i < len(numbers):
    if numbers[i] % 2 == 0:
        print(numbers[i])
    i += 1  # 증감식
# 2
# 4
# 6
# 8
# 10

# 리스트가 빌 때까지 삭제하면서 그 삭제한 원소를 출력하기
# 리스트는 원소가 1개 이상이면 True, 원소가 없으면 False
numbers = [1, 2, 3, 4, 5]
while numbers:  # 조건 (numbers가 비는 순간 반복 종료)
    delete_number = numbers.pop()
    print(delete_number)

print(numbers)  # []


# break : 반복문을 강제 종료 (for문, while문 사용 가능)
# 특정 조건을 만족했을 때 반복문 종료

# for문에서 break
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

    # 원소 3을 만난 경우 반복 종료
    if number == 3:
        print("반복을 종료합니다.")
        break
# 1
# 2
# 3
# 반복을 종료합니다.


# while문에서 break
numbers = [1, 2, 3, 4, 5]
i = 0
while True:
    print(numbers[i])

    # 원소 3을 만난 경우 반복 종료
    if numbers[i] == 3:
        print("반복을 종료합니다.")
        break

    i += 1
# 1
# 2
# 3
# 반복을 종료합니다.


# 같은 들여쓰기 레벨에서 break의 아래 부분은 결코 실행 X, 코드 작성 X
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

    # 원소 3을 만난 경우 반복 종료
    if number == 3:
        print("반복을 종료합니다.")
        break
        Print("이 부분은 실행되지 않습니다.")
# 1
# 2
# 3
# 반복을 종료합니다.


# cuntinue : 다른 반복으로 강제 이동 (for문, while문 사용 가능)
# 특정 조건을 만족했을 때 더 이상 아래 부분을 실행하지 않고, 다음 반복으로 넘어간다.
# 필터링이라고 생각 (continue를 두어 원하는 데이터만 출력 가능)

# for문에서 continue
number = [1, 2, 3, 4, 5]
for number in numbers:
    if number % 2 == 0:  # 만약 짝수라면
        continue  # 아래를 실행하지 않고 다음 반복으로 넘어감
    print(number)  # 홀수만 출력
# 1
# 3
# 5

# while문에서 continue
number = 0
while number < 5:
    number += 1  # 증감식
    if number % 2 == 0:  # 만약 짝수라면
        continue  # 아래를 실행하지 않고 다음 반복으로 넘어감
    print(number)  # 홀수만 출력
# 1
# 3
# 5

# 1부터 20까지의 정수 중 2의 배수도 아니고 3의 배수도 아닌 정수만 출력
for i in range(1, 21):
    if i % 2 == 0:
        continue  # 2의 배수라면 다음 반복으로 넘어감
    if i % 3 == 0:
        continue  # 3의 배수라면 다음 반복으로 넘어감
    print(i)
# 1
# 5
# 7
# 11
# 13
# 17
# 19

# 같은 들여쓰기 레벨에서 continue의 아래 부분은 결코 실행X, 코드 작성X
number = 0
while number <= 5:
    number += 1

    if number % 2 == 0:
        continue
        print("이 부분은 실행되지 않습니다.")
        
    print(number)
# 1
# 3
# 5



# 반복문 (Loop)
# 컨테이너 자료형의 여러 원소들에 대해 특정 처리를 할 때 유용

numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):  # range(5) = 0, 1, 2, 3, 4
    if i % 2 == 0:  # 짝수 번째 인덱스에 위치한 원소 (리스트의 크기와 상관없이 항상 짝수 번째 원소 출력)
        print(numbers[i])
# 1
# 3
# 5


numbers = [1, 2, 3, 4, 5]
for i in numbers:  # 1, 2, 3, 4, 5
    if i % 2 == 0:  # 짝수인 원수의 값 (리스트에 있는 짝수 값들 출력)
        print(numbers[i])
# 3
# 5



# 리스트, 딕셔너리, 조건문, 반복문

# 여러 자료구조를 섞어서 표현
user = {
    'total_user': 3,
    'information': [
        {'name': 'alex', 'age': 3, 'license': True},
        {'name': 'june', 'age': 7, 'license': False},
        {'name': 'peter', 'age': 4, 'license': False}
    ]
}


# 제어문 if, 반복문 for
# [문제] 어떤 광산에서는 채굴한 광물들의 등급을 상품인 1등급부터 하품인 3등급까지 나누어 등급을 매긴 후, 해당 정보를 저장해서 관리합니다.
# A 광산은 10개의 광물을 채굴하였고 각각 등급은 다음과 같습니다.
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]

# 채굴한 광물들 중 1등급 광물이 존재하는지 여부는 어떻게 알 수 있을까요?
# 방법 1 : in 연산자
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
if 1 in gems:
    print(True)
else:
    print(False)
# True

# 방법 2 : for문과 제어문
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
grade1 = False  # 특정 변수를 통해 여부를 저장하는 편이 좋습니다.
for i in gems:
    if i == 1:
        grade1 = True
        break  # 효율성을 위한 미리 브레이크
print(grade1)
# True

# 1, 2, 3등급 광물은 각각 몇 개가 있는지 어떻게 기록하면 좋을까요?
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
grades = {1:0, 2:0, 3:0}
for i in gems:
    grades[i] += 1  # 딕셔너리는 인덱스 1부터 시작
print(grades)
# {1: 2, 2: 3, 3: 5}

# 만약 광물의 등급의 합계가 15 이하면 성공, 23 이하면 보통, 30을 초과하면 실패라고 할 때, 올해의 등급에 따른 성공 척도를 출력하려면 어떻게 해야 할까요?
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
result = sum(gems)

if result <= 15:
    print('성공')
elif 15 < result <= 23:
    print('보통')
else:
    print('실패')
# 보통


# [문제] max(), min() 함수의 직접 구현
nums = [7, 1, 2, 4, 6, 8, 3]

# 최댓값
max_num = 1  # 작은 수로 초기화
for num in nums:
    if max_num < num:
        max_num = num  # max_num = 7->8
print(max_num)  # 8

# 최솟값
min_num = 9999  # 큰 수로 초기화
for num in nums:
    if min_num > num:
        min_num = num  # min_num = 7->1
print(min_num)  # 1