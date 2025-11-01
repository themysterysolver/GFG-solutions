from collections import deque,defaultdict
class Solution:
    def findOrder(self, n, prerequisites):
        # code here 
        adL = defaultdict(list)
        indegree = [0]*n
        for v,u in prerequisites:
            adL[u].append(v)
            indegree[v]+=1
        q = deque([])
        for idx,val in enumerate(indegree):
            if val == 0:
                q.append(idx)
        order = []
        while q:
            l = len(q)
            for _ in range(l):
                node = q.popleft()
                order.append(node)
                for ad in adL[node]:
                    indegree[ad]-=1
                    if indegree[ad] == 0:
                        q.append(ad)
        return order if len(order) == n else []