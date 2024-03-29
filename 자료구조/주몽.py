"""
갑옷을 만드는 재료들은 각각 고유한 번호를 가지고 있다.
갑옷은 두 개의 재료로 만드는데 두 재료의 고유한 번호를 합쳐서 M(1 ≤ M ≤ 10,000,000)이 되면 갑옷이 만들어 지게 된다.
야철대장은 자신이 만들고 있는 재료를 가지고 갑옷을 몇 개나 만들 수 있는지 궁금해졌다.
이러한 궁금증을 풀어 주기 위하여 N(1 ≤ N ≤ 15,000) 개의 재료와 M이 주어졌을 때 몇 개의 갑옷을 만들 수 있는지 출력

첫째 줄에는 재료의 개수 N(1 ≤ N ≤ 15,000)이 주어진다.
두 번째 줄에는 갑옷을 만드는데 필요한 수 M(1 ≤ M ≤ 10,000,000) 주어진다. 그리고 마지막으로 셋째 줄에는 N개의 재료들이 가진 고유한 번호들이 공백을 사이에 두고 주어진다.
고유한 번호는 100,000보다 작거나 같은 자연수이다.
"""
n=int(input())
m=int(input())
a = list(map(int, input().split()))

a.sort() # 크기 비교이므로 정렬, ~15,000 nlogn사용

# 투 포인터
l=0
r=n-1
cnt=0
while l<r: # 재료는 고유하기 때문에 같을 수 없음
    sum=a[l]+a[r]
    if sum<m:
        l+=1
    elif sum>m:
        r-=1
    else:
        cnt+=1
        l+=1
        r-=1

print(cnt)