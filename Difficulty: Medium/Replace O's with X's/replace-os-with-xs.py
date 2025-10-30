from collections import deque
class Solution:
    def fill(self, grid):
        # Code here
        m,n = len(grid),len(grid[0])
        visited = set()
        def BFS(r,c):
            q = deque([(r,c)])
            marked = []
            visited.add((r,c))
            flag =  True
            while q:
                l = len(q)
                for _ in range(l):
                    x,y = q.popleft()
                    marked.append((x,y))
                    for (dx,dy) in [(0,1),(1,0),(-1,0),(0,-1)]:
                        nx,ny = x+dx,y+dy
                        if nx<0 or ny<0 or nx>=m or ny>=n:# or (nx,ny) in visited:#grid[nx][ny] == 'X':
                            flag = False
                            continue
                        if (nx,ny) in visited or grid[nx][ny] == 'X':
                            continue
                        q.append((nx,ny))
                        visited.add((nx,ny))
            if flag:
                for x,y in marked:
                    grid[x][y] = 'X'
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'O' and (i,j) not in visited:
                    BFS(i,j)
        return grid