class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        nl=[]
        for i in grid:
            for j in i:
                nl.append(j)
        k%=len(nl)
        nl=nl[-k:]+nl[:-k]
        m=len(grid)
        n=len(grid[0])
        ng=[]
        for i in range(m):
            ng.append([])
            for j in range(n):
                ng[i].append(nl[i*n+j])
        return ng

