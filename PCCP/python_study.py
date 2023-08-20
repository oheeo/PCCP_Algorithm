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


# --------------------------------------------------------------


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


print("-------------------------------------------------------")


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


print("-------------------------------------------------------")


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


print("-------------------------------------------------------")


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


print("-------------------------------------------------------")


# 함수

# 함수명(식별자) 작성 규칙
# 1) 알파벳, 언더바(_), 숫자로 구성되어야 한다.
# 2) 첫 글자에는 숫자가 올 수 없다.
# 3) 대소문자를 구별한다.
# 4) 띄어쓰기가 필요한 경우 언더바(_)로 구분한다.
# 5) 예약어로 지을 수 없다.

def get_bigger(x, y):
    if x > y:
        return x
    else:
        return y
    
a = 5
b = 10
bigger1 = get_bigger(a, b)

c = 6
d = 3
bigger2 = get_bigger(c, d)  # 10 6

print(bigger1, bigger2)


# 선언과 호출
def add(x, y):  # 선언
    return x + y

result = add(1, 2)  # 호출
print(result)  # 3


# 파이썬 내장 함수
numbers = [1, 2, 3, 4, 5]
length = len(numbers)  # 내장함수 len 호출 및 반환값 할당
print(length)  # 내장함수 print 호출
# 5


# 함수와 메서드의 차이?
# 메서드는 함수 중에서도 특정 타입에 종속된 함수를 지칭
# 예를 들어, append는 독립적으로 쓰이지 않고 리스트에서만 사용 가능하다.
# 그래서 리스트.append() 와 같이 점(.)을 찍고 사용한다.
# 반면 len() 과 같은 함수는 독립적으로 사용되기 때문에 함수라고 부른다.
# 모든 메서드는 함수이지만, 모든 함수가 메서드는 아니다.


# 매개변수 O, 반환값 X
def hello(name):
    print(f"Hello! {name}!")  # 출력이 목적이므로 값을 굳이 반환 X
hello("hee")  # 반환값이 없으므로 변수에 할당할 필요가 없음
hello("alex")


# 매개변수 X, 반환값 O
# 1부터 10까지의 정수 중 짝수만 골라서 리스트로 반환하는 함수
# 항상 정해진 동작만 수행하고 그 값을 반환
def even_numbers():
    a = []
    for i in range(1, 11):
        if i % 2 == 0:
            a.append(i)  # range에서 짝수면 a[]에 추가
    
    return a

numbers = even_numbers()
print(numbers)
# [2, 4, 6, 8, 10]


# 매개변수 X, 반환값 X
# 입력 없이 항상 정해진 처리만 하면서 값도 반환할 필요가 없는 경우
def welcome():
    print("Welcome to Python world!")

welcome()
# Welcome to Python world!


print("-------------------------------------------------------")


# 자주 사용하는 내장 함수와 메서드

# 자주 사용하는 내장 함수

a = [1, 2, 3, 4, 5]
# len(A) : 입력된 A의 길이(원소의 개수)를 반환
print(len(a))
# 5

# sum(A) : 입력된 A의 모든 원소의 합을 반환
print(sum(a))
# 15

# max(A) : 입력된 A의 원소 중 최댓값을 반환
print(max(a))
# 5

# min(A) : 입력된 A의 원소 중 최솟값을 반환
print(min(a))
# 1

# sorted(A) : 입력된 A를 오름차순으로 정렬 후, 그 결과를 리스트로 반환
# 새로운 리스트를 만드는 것이므로 기존 값에 직접적으로 변화를 주진 않음
# 옵션으로 reverse : 내림차순으로 정렬하려면 해당 옵션을 True로
a = [3, 1, 0, 5, 11]
print(sorted(a))  # 오름차순 [0, 1, 3, 5, 11]
print(sorted(a, reverse=True))  # 내림차순 [11, 5, 3, 1, 0]
print(a)  # 기존 리스트에 변화를 주진 않음 [3, 1, 0, 5, 11]

# reversed(A) : 입력된 A를 뒤집은 결과를 반환
# reversed 함수만 사용하면 이상한 값이 나오므로, list() 내장 함수를 이용해 형 변환을 해줘야함
a = [1, 2, 3, 4, 5]
print(reversed(a))  # <list_reverseiterator object at 0x000001E426573CD0>
print(list(reversed(a)))  # [5, 4, 3, 2, 1]
print(a)  # [1, 2, 3, 4, 5]


# 자주 사용하는 리스트 메서드

a = [1, 2, 3, 4, 5]
# .append(x) : 리스트의 맨 마지막에 새로운 원소 x를 삽입
a.append(6)
print(a)  
# [1, 2, 3, 4, 5, 6]

# .insert(i, x) : 리스트의 i번째에 새로운 원소 x를 삽입
a = [1, 2, 3, 4, 5]
a.insert(1, 10)
print(a)  # [1, 10, 2, 3, 4, 5]

# .pop() : 리스트의 맨 마지막 원소를 삭제 후 반환
a = [1, 2, 3, 4, 5]
b = a.pop()
print(a)  # [1, 2, 3, 4]
print(b)  # 5

# .pop(i) : 리스트의 i번째 원소를 삭제 후 반환
a = [1, 2, 3, 4, 5]
b = a.pop(3)
print(a)  # [1, 2, 3, 5]
print(b)  # 4

# .remove(x) : 리스트에서 특정 원소 x 중 첫 번째 원소를 삭제
# .pop()과는 달리 반환값은 없다.
a = [1, 2, 3, 4, 5]
a.remove(3)
print(a)  
# [1, 2, 4, 5]


# .sort() : 리스트를 오름차순으로 정렬 (원본 리스트 자체를 정렬함. 반환값 없다.)
# 옵션으로 reverse=True 를 주면 내림차순으로 정렬
# sorted() 함수는 이자로 들어온 리스트를 정렬한 새로운 리스트로 반환한다. 원본 리스트는 정렬되지 않는다.
a = [3, 5, 1, 4, 2]
a.sort()  # 오름차순

b = [3, 5, 1, 4, 2]
b.sort(reverse=True)  # 내림차순

print(a)  # [1, 2, 3, 4, 5]
print(b)  # [5, 4, 3, 2, 1]


# .reverse() : 리스트를 반대로 뒤집는다.
a = [1, 2, 3, 4, 5]
a.reverse()
print(a)  
# [5, 4, 3, 2, 1]

# .extend(A) : 리스트의 마지막에 A의 원소들을 덧붙여서 확장함
a = [1, 2, 3, 4, 5]
a.extend([6, 7, 8])
print(a)  
# [1, 2, 3, 4, 5, 6, 7, 8]

# .count(x) : 리스트에서 원소 x의 개수를 반환
a = [3, 5, 1, 4, 2, 5]
print(a.count(5))  
# 2

# .index(x) : 리스트에서 원소 x가 처음 등장하는 인덱스를 반환
a = [3, 5, 1, 4, 2, 5]
print(a.index(5))  
# 1


# 자주 사용하는 문자열 메서드

# .split(기준 문자) : 문자열을 일정 기준으로 나누어 리스트로 반환
# 기존 문자열은 변경 X
s = "kyle,alex,justin,ken"
print(s.split(","))  
# ['kyle', 'alex', 'justin', 'ken']

# 기존 문자의 기본값은 공백이다.
s = "I play the piano"
print(s.split())
# ['I', 'play', 'the', 'piano']


# .strip(제거할 문자) : 문자열의 왼쪽과 오른쪽에서 특정 문자를 제거하여 새로운 문자열로 반환
# 기존 문자열은 변경 X
s = "aHello worlda"
print(s.strip("a"))
# Hello world

# 제거할 문자의 기본값은 공백이다.
s = " Hello world "
print(s.strip())
# Hello world

# 제거할 문자를 여러 개 넣으면, 해당하는 문자들을 양쪽에서 모두 제거한 새로운 문자열을 반환함
s = "Hello world"
print(s.strip("Hd"))
# ello worl


# .find(찾는 문자) : 문자열에서 찾는 문자가 처음으로 나타나는 인덱스를 반환함
s = "python"
print(s.find("t"))
# 2

# 찾는 문자가 없다면 -1 을 반환
s = "python"
print(s.find("j"))
# -1


# .index(찾는 문자) : 문자열에서 찾는 문자가 처음으로 나타나는 인덱스를 반환함
s = "python"
print(s.index("t"))
# 2

# 찾는 문자가 없다면 에러 발생
# s = "python"
# print(s.index("j"))


# .count(개수를 셀 문자) : 문자열에서 특정 문자의 개수를 반환함
s = "hello python"
print(s.count("l"))
# 2

# 길이가 2 이상인 문자열의 개수도 셀 수 있다.
s = "banana"
print(s.count("na"))
# 2


# .replace(기존 문자, 새로운 문자) : 문자열에서 기존 문자를 새로운 문자로 치환한 새로운 문자열을 반환함
# 기존 문자열은 변경 X
s = "I play the piano"
print(s.replace("piano","violin"))
# I play the violin

# 기존 문자를 빈 문자열("")로 치환하여 마치 해당 문자를 삭제한 효과도 가능
s = "python"
print(s.replace("p",""))
# ython


# 삽입할 문자.join(리스트) : 리스트의 문자열 원소들 사이에 각각 특정 문자를 삽입한 결과를 새로운 문자열로 반환함
words = ["I", "play", "the", "piano"]
print("$".join(words))
# I$play$the$piano

# 삽입할 문자를 공백(" ")으로 지정하면 띄어쓰기를 한 효과
words = ["I", "play", "the", "piano"]
print(" ".join(words))
# I play the piano

# 삽입할 문자를 빈 문자열("")로 지정하면 하나의 문자열로 합치는 효과
words = ["a", "p", "p", "l", 'e']
print("".join(words))
# apple

# 리스트의 모든 원소들이 문자열이 아니면 에러 발생
# numbers = [1, 2, "3", "4", "5"]
# print("".join(numbers))


print("-------------------------------------------------------")


# 모듈 : 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것
import module1
print(module1.add(1, 2))
# 3


# random 모듈 : 난수(무작위 수)를 다루는 기능을 제공
# random.randint(시작 숫자, 끝 숫자) : 시작 숫자부터 끝 숫자까지의 수 중에서 1개의 정수를 무작위로 반환
import random
number = random.randint(1, 5)  # 1, 2, 3, 4, 5 중 무작위로 1개를 반환
print(number)

# random.choice(리스트) : 리스트 내의 원소 중 1개를 무작위로 반환
import random
numbers = [10, 20, 30, 40, 50]
number = random.choice(numbers)
print(number)

# random.sample(리스트, 개수) : 리스트 내의 원소 중 지정한 개수만큼 무작위로 뽑아서 리스트에 담아 반환
import random
numbers = [10, 20, 30, 40, 50]
samples = random.sample(numbers, 3)  # 리스트 numbers에서 무작위로 3개를 반환하여 리스트에 담음
print(samples)
# [20, 10, 30]


 # time 모듈 : 시간을 다루는 기능을 제공
 # time.sleep(초) : 일정 시간(초) 동안 프로그램의 동작을 일시정시 할 수 있다.
import time
for i in range(5):
    time.sleep(1)  # 1초 동안 프로그램 동작을 정지
    print(f"1초 기다린 후, {i} 출력")
# 1초 기다린 후, 0 출력
# 1초 기다린 후, 1 출력
# 1초 기다린 후, 2 출력
# 1초 기다린 후, 3 출력
# 1초 기다린 후, 4 출력
