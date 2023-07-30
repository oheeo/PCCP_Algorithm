# 문제 3. 숫자 문자열과 영단어
# 네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.
# (예시) "23four5six7" -> 234567 (not String 형태)

# 방법 1
# tmp 라는 임시 문자열을 담아둘 변수 선언
# isnumeric() : 문자열이 숫자인지 체크
def solution(s):
    answer = ""
    tmp = ""
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in s:
        if(i.isnumeric()):   # i 가 숫자면 answer 에 추가
            answer += i
        else:
            tmp += i   # i 가 문자면 tmp 에 담고
            if tmp in arr:   # tmp 와 동일한 문자가 arr 안에 있다면
                answer += str(arr.index(tmp))   # tmp 와 동일한 arr의 인덱스를 문자로 변환 후 answer 에 추가
                tmp = ""   # tmp 초기화
    return int(answer)

print(solution("23four5six7"))  # 234567


# 방법 2
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

print(solution("23four5six7"))  # 234567


# 방법 3
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)

print(solution("23four5six7"))  # 234567


# 강사님 정답
# 숫자와 영어 표를 보자마자 딕셔너리 쓰라는 거! 특정 두가지 자료를 링크하는 것
def solution(s):
    nums = {
        'zero': '0', 'one': '1', 'two': '2',
        'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    for n in nums:
        s = s.replace(n, nums[n])

    return int(s)

print(solution("23four5six7"))  # 234567
