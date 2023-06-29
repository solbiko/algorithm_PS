from heapq import heappush, heappop

def solution(n, s, a, b, fares):
    INF = int(1e9)
    answer=INF
    graph = [[] for _ in range(n+1)]
    
    for f in fares:
        i,j,k = f
        graph[i].append((j, k))
        graph[j].append((i, k))

    def dijk(start):    # s를 시작점으로하는 다익스트라
        q = []
        distance = [INF] * (n+1)

        heappush(q, (0, start))
        distance[start] = 0
        
        while q:
            dist, now = heappop(q)
            if distance[now] < dist:
                continue
                
            for g in graph[now]:
                cost = dist + g[1]
                if cost < distance[g[0]]:
                    distance[g[0]] = cost
                    heappush(q, (cost, g[0]))
        return distance
   
 
    d=[[]]+[dijk(i) for i in range(1, n+1)]
    
    for i in range(1,n+1):
        print(i)
        print(d[s][i],d[i][a], d[i][b])
        answer = min(d[s][i]+d[i][a]+d[i][b], answer)
    
    return answer