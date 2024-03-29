"""
주식 하나를 산다.
원하는 만큼 가지고 있는 주식을 판다.
아무것도 안한다.
날 별로 주식의 가격을 알려주었을 때, 최대 이익이 얼마나 되는지 계산을 해달라고 부탁했다.
예를 들어 날 수가 3일이고 날 별로 주가가 10, 7, 6일 때, 주가가 계속 감소하므로 최대 이익은 0이 된다.
그러나 만약 날 별로 주가가 3, 5, 9일 때는 처음 두 날에 주식을 하나씩 사고, 마지막날 다 팔아 버리면 이익이 10이 된다.

입력의 첫 줄에는 테스트케이스 수를 나타내는 자연수 T가 주어진다.
각 테스트케이스 별로 첫 줄에는 날의 수를 나타내는 자연수 N(2 ≤ N ≤ 1,000,000)이 주어지고,
둘째 줄에는 날 별 주가를 나타내는 N개의 자연수들이 공백으로 구분되어 순서대로 주어진다. 날 별 주가는 10,000이하다.

3
3
10 7 6
3
3 5 9
5
1 1 3 1 2

0
10
5
"""
import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    N=int(input())
    a=list(map(int, input().split()))

    maxVal=a[-1]  #  최댓값 초기화
    res=0
    for i in range(N-1,-1,-1):
        maxVal=max(maxVal, a[i]) #  최댓값
        res+=maxVal-a[i]  # 최댓값 차 더하기 (사고 팔 때 가격 차)

    print(res)

