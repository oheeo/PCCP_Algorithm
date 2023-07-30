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


# 문자열도 사실은 컨테이너 자료형이었다.
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
print(new_word)

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
