# 문제 4. 신고 결과 받기
# 신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다. 무지가 개발하려는 시스템은 다음과 같습니다.
# 각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
# 신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
# 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
# k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
# 유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.
# 이용자의 ID가 담긴 문자열 배열 id_list, 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 report, 정지 기준이 되는 신고 횟수 k가 매개변수로 주어질 때, 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 하도록 solution 함수를 완성해주세요.
# (예시) id_list ["muzi", "frodo", "apeach", "neo"] / report ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"] / k=2 / result [2,1,1,0]

'''
문제 조건 정리

1명 -> 한번에 1명씩 제한없이 신고 가능.
    -> 1명 여러번 신고 가능 but, 1회로 처리.
    
k번 신고당함 -> 정지, 신고한 유저들에게 메일로 발송함. (자료구조로 id저장하고 있어야.)
            정지먹을때마다 보내는게 아니라, 전체 input이 다 주어지고나서 취합해서 메일을 보냄.
            
원하는 자료구조 모양 -> frodo가 muzi에게 여러번 신고당해도 1로 체크만 되길 원함. (가산되길 원하면 +=1로 수정가능)
{'frodo' : 
    {'muzi':1,
    'appeach':1,
    }
}
frodo가 신고를 받았는데, muzi, appeach가 신고했다는 뜻.
취합은 report_dict[id_value]의 len을 돌려서 k이상인지 판별하고, 된다면 그 key들을 돌려서(dict에 대한 for loop은 key를 대상으로 돌려줍니다.) id list에 넣어주기.
'''

# 방법 1
import collections   # defaultdict()를 쓰기 위해

def solution(id_list, report, k):
    answer = []

    report = list(set(report))
    # set은 중복 불가 (한 유저가 한 유저를 여러번 신고해도 결과는 한번만 허용)
    # set으로 중복 제거하고 다시 list로 변경

    reportHash = collections.defaultdict(set)
    # reportHash key(신고자)의 value(신고당한사람)는 set{} 자료구조
    # reportHash = {'신고자1': {'신고당한사람1', '신고당한사람2'}, '신고자2': {'신고당한사람1', '신고당한사람2'}}

    stoped = collections.defaultdict(int)
    # value를 카운팅하니까 int (default값은 0)
    # stoped = {'신고당한사람1':신고당한횟수, '신고당한사람2':신고당한횟수}

    for x in report:  # 첫번째 x는 muzi frodo니까 둘을 분리시켜야함
       
        a, b = x.split(' ')
        # a 는 신고한 사람, b는 신고당한 사람을 공백에 의해 분리시킴
       
        reportHash[a].add(b)
        # reportHash에 key는 신고한 사람 a이고, a에게 신고당한 b를 추가함

        stoped[b]+=1
        # stoped에 b라는 사람이 신고당했다고 +1 카운팅함

    for name in id_list:
        mail = 0   # 메일 받을 횟수
        for user in reportHash[name]:
        # reportHash[name] : name 유저에게 신고당한 유저
            if stoped[user] >= k:
            # 신고당한 user의 횟수가 k보다 크거나 같으면
                mail+=1
                # 신고한 name에게 메일 전송 횟수 추가
        answer.append(mail)

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], 
               ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 
               2))


# 방법 2
# 그래프