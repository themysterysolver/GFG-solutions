class Solution:
    def ratInMaze(self, maze):
        # code here
        #D<L<R<U
        m,n = len(maze),len(maze[0])
        if maze[0][0] == 0 or maze[m-1][n-1] == 0:
            return []
        visited = set()
        visited.add((0,0))
        result = []
        
        def backtrack(x,y,path):
            if (x,y) == (m-1,n-1):
                result.append(path)
            else:
                for dx,dy,d in [(1,0,"D"),(0,-1,"L"),(0,1,"R"),(-1,0,"U")]:
                    nx,ny = x+dx,y+dy
                    if nx<0 or ny<0 or nx>=m or ny>=n or maze[nx][ny]==0 or (nx,ny) in visited:
                        continue
                    visited.add((nx,ny))
                    backtrack(nx,ny,path+d)
                    visited.remove((nx,ny))
        backtrack(0,0,"")
        return result