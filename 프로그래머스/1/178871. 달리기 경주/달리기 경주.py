def switch(s,players):
    a = players.index(s)
    players[a] , players[a-1] = players[a-1],players[a]
    return

def solution(players, callings):
    playerDict = {}
    # 딕셔너리로 재배치
    for idx, player in enumerate(players):
        playerDict[player] = idx
    
    for call in callings:
        # 인덱스 추출
        index = playerDict.get(call)
        
        # 딕셔너리에서 스위치
        playerDict[call] = index - 1
        
        frontPlayer = players[index - 1]
        
        playerDict[frontPlayer] = index
        
        players[index - 1] = call
        players[index] = frontPlayer
        
    answer = players
    return answer