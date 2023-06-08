# 문제 2. 한 번만 등장한 문자
# 문자열 s가 매개변수로 주어집니다. s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요. 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.
# (예시) "hello"에서 한 번씩 등장한 문자는 "heo"이고 이를 사전 순으로 정렬한 "eho"를 return 합니다.

# 방법 1
# 주어진 문자열에서 한 요소를 찾아가면서 count()함수를 사용했을때 값이 1인 경우에 answer에 담는다.
# 담긴 answer에서 사전순으로 정렬하기위해 sorted(answer)
# 이렇게하게되면 한문자씩 담기게 되는데 이것을 문자열로 자연스럽게 이어주기 위해서 공백을 join을 사용해준다.
def solution(s):
    answer = ''
    for i in s:
        if s.count(i) == 1:
            answer += i
    return ''.join(sorted(answer))

print(solution('hello'))  # eho

# 참고
s = "adfe"
# s1 = s.sort() # wrong
s2 = sorted(s) # ['a','d','e','f']
s3 = ''.join(sorted(s)) # "adef"


# 방법 2
# 방법 1 과 알고리즘 자체는 같은데 표현하는 형식이 다르다.
def solution(s):
    answer = ''.join(sorted([ ch for ch in s if s.count(ch) == 1 ]))
    # ↓ 이것을 한 줄로 표현 ↑
    # for ch in s:
    #     if s.count(ch) == 1:
    #         answer += i
    # return ''.join(sorted(answer))

    return answer

print(solution('hello'))  # eho