"""
1,2,3 짝을 맞춰야하는데
123,132,231,213,312,324 어떤 순서로 맞추는게 빠른지 -> 순열 구해서 인덱스 dfs
123도 어떤 1로 먼저 가야되는지 -> 2가지 경우
bfs
최솟값 출력
"""
from collections import defaultdict, deque
from itertools import permutations
from copy import deepcopy

def bfs(board, start, end):
    if start==end: 
        return 0
    q, visit = deque([[start[0], start[1], 0]]), {start}
    while q:                    # BFS
        x, y, c = q.popleft()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x+dx, y+dy     # Normal move
            cx, cy = x, y
            while True:             # Ctrl + move
                cx, cy = cx+dx, cy+dy
                if not (0 <= cx <= 3 and 0 <= cy <= 3):
                    cx, cy = cx-dx, cy-dy
                    break
                elif board[cx][cy] != 0:
                    break

            if (nx, ny) == end or (cx, cy) == end:  # 도착 최단 경로
                return c+1

            if (0 <= nx <= 3 and 0 <= ny <= 3) and (nx, ny) not in visit:
                q.append((nx, ny, c+1))
                visit.add((nx, ny))
            if (cx, cy) not in visit:
                q.append((cx, cy, c+1))
                visit.add((cx, cy))


def dfs(board, cdict, curr, case, cost): # 격자 카드, 좌표, 순열경우, 비용
    if len(case)==0: # 모든 카드를 확인한 경우
        return cost

    idx = case[0]+1 # 현재 선택해야할 카드의 종류

    # 현재위치에서 A1까지의 조작 횟수 + A1->A2까지의 조작 횟수 + 2(카드 선택)
    choice1 = bfs(board, curr, cdict[idx][0]) + bfs(board, cdict[idx][0], cdict[idx][1]) + 2
    choice2 = bfs(board, curr, cdict[idx][1]) + bfs(board, cdict[idx][1], cdict[idx][0]) + 2

    # 선택한 카드는 board에서 0으로 변경
    new_board = deepcopy(board)
    new_board[cdict[idx][0][0]][cdict[idx][0][1]] = 0
    new_board[cdict[idx][1][0]][cdict[idx][1][1]] = 0

    # 더 작은값으로
    if choice1 < choice2:
        return dfs(new_board, cdict, cdict[idx][1], case[1:], cost + choice1)
    else:
        return dfs(new_board, cdict, cdict[idx][0], case[1:], cost + choice2)

    
    
def solution(board, r, c):
    answer = float('inf')

    # 카드
    cdict = defaultdict(list)
    for row in range(4):
        for col in range(4):
            num = board[row][col]
            if num != 0:
                cdict[num].append((row, col))

    # 순열
    for case in permutations(range(len(cdict)), len(cdict)):
        answer = min(answer, dfs(board, cdict, (r, c), case, 0))

    return answer

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0))