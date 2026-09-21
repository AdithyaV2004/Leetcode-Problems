class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=[[0]*n for _ in range(m)]   
        c=0
        for x in range(m):
            for y in range(n):
                if grid[x][y]=="1" and not visited[x][y]:
                    c+=1
                    visited[x][y]=1
                    q=deque([(x, y)])
                    while q:
                        i, j=q.popleft()
                        if i-1>=0 and grid[i-1][j]=='1' and not visited[i-1][j]:
                            q.append((i-1, j))
                            visited[i-1][j]=True
                        if i+1<m and grid[i+1][j]=='1' and not visited[i+1][j]:
                            q.append((i+1, j))
                            visited[i+1][j]=True
                        if j-1>=0 and grid[i][j-1]=='1' and not visited[i][j-1]:
                            q.append((i, j-1))
                            visited[i][j-1]=True
                        if j+1<n and grid[i][j+1]=='1' and not visited[i][j+1]:
                            q.append((i, j+1))
                            visited[i][j+1]=True                    
        return c