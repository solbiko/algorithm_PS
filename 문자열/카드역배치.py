"""
1부터 20까지 숫자가 하나씩 쓰인 20장의 카드가 아래 그림과 같이 오름차순으로 한 줄로 놓여있다.
구간 [a, b] (단, 1 ≤ a ≤ b ≤ 20)가 주어지면 위치 a부터 위치 b까지의 카드를 현재의 역순으로 놓는다.
현재 카드가 놓인 순서가 위의 그림과 같고 구간이 [5, 10]으로 주어진다면,
위치 5부터 위치 10까지의 카드 5, 6, 7, 8, 9, 10을 역순으로 하여 10, 9, 8, 7, 6, 5로 놓는다.

오름차순으로 한 줄로 놓여있는 20장의 카드에 대해 10개의 구간이 주어지면,
주어진 구간의 순서대로 위의 규칙에 따라 순서를 뒤집는 작업을 연속해서 처리한 뒤 마지막 카드들의 배치를 구하는 프로그램
5 10
9 13
1 2
3 4
5 6
1 2
3 4
5 6
1 20
1 20

1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20
"""
a=[(i+1) for i in range(20)]

for _ in range(10):
    s,e=map(int, input().split())
    a = a[0:s-1] + list(reversed(a[s-1:e])) + a[e:20]

for i in a:
    print(i, end=" ")