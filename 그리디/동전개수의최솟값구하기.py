"""
동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값 출력
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
"""
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
a=[]
for _ in range(n):
    a.append(int(input()))

cnt=0
for i in range(n-1,-1,-1):
    if a[i]<=m:
        cnt+=m//a[i]
        m%=a[i]
print(cnt)