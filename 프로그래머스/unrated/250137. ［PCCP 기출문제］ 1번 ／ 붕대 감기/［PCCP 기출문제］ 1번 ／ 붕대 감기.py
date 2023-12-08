def solution(bandage, health, attacks):
    HP = health  # 현재 체력

    for i in range(len(attacks) - 1):
        HP -= attacks[i][1]  # 몬스터의 공격을 받음

        if HP <= 0:
            return -1  # 캐릭터가 죽으면 -1을 반환

        T = attacks[i + 1][0] - attacks[i][0] - 1  # 다음 공격 사이의 시간 간격
        if T > 0:
            Q = (T // bandage[0]) * bandage[2]  # 추가 회복량
            AHP = T * bandage[1] + Q  # 총 회복량
            HP = min(health, HP + AHP)  # 현재 체력이 최대 체력을 초과하지 않도록 업데이트

    HP -= attacks[-1][1]  # 마지막 몬스터의 공격을 받음

    if HP <= 0:
        return -1  # 캐릭터가 죽으면 -1을 반환

    return min(health, HP)  # 생존한 경우 남은 체력 반환
