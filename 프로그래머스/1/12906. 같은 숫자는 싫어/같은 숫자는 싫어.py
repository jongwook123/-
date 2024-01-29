def solution(arr):
    answer = []
    for s in arr:
        if len(answer) == 0:
            answer.append(s)
        else:
            if answer[-1] == s:
                pass
            else:
                answer.append(s)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    return answer