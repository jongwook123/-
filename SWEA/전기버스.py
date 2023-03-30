def solve(station_list, K, M, N):
    station_list = [0] + station_list + [N]
    last = cnt = 0
    for i in range(1, M + 2):
        # 충전기 사이가 K보다 크면 충전할 수 없음.
        if station_list[i] - station_list[i - 1] > K:
            return 0
        # i이동할 수 없는 경우 앞쪽에서 충전
        if station_list[i] > last + K:
            last = station_list[i - 1]
            cnt += 1
    return cnt


T = int(input())
for tc in range(1, T + 1):
    # K = 이동할수 있는 정류장 수
    # N = 정류장
    # M = 충전 정류장 개수
    K, N, M = input().split()
    K = int(K)
    N = int(N)
    M = int(M)
    station_list = list(map(int, input().split()))
    ans = solve(station_list, K, M, N)

    print(f'#{tc} {ans}')











