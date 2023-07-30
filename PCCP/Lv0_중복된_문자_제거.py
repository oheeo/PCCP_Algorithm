# 문제 1. 중복된 문자 제거
# 문자열 my_string이 매개변수로 주어집니다. my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.
# (예시) "We are the world"에서 중복된 문자 "e", " ", "r" 들을 제거한 "We arthwold"을 return합니다.

# 방법 1
# for문으로 문자 하나하나 돌면서 if문에서 중복된 문자는 넣지 않는다.
def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer += i
    return answer

print(solution("We are the world"))  # We arthwold

# 방법 2
# dict.fromkeys(word)
# dict으로 변환 후 join 함수 사용 (파이썬 3.6부터 dict 순서 보장)
def solution(my_string):
    answer = ''.join(dict.fromkeys(my_string))
    return answer

print(solution("We are the world"))  # We arthwold

# 방법 3
# 파이썬 3.6 이전엔 dict 순서 보장이 안됐기에 OrderedDict으로 변환 후 join 함수 사용
def solution(my_string):
    from collections import OrderedDict
    answer = ''.join(dict.fromkeys(my_string))
    return answer

print(solution("We are the world"))  # We arthwold


# 강사님 정답
def solution(my_string):
    answer = ''
    exclusive_letters = set(my_string)  # set은 그 자체로 중복을 제거
    for letter in my_string:  
        if letter in exclusive_letters:  # O(1)의 빠른 containment test
            answer += letter  # 앞쪽부터 차례로 이어붙이고
            exclusive_letters.discard(letter)  # 쓴 것은 제외해줌 O(1)
    return answer

print(solution("We are the world"))  # We arthwold
