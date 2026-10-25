class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        def rev(i, j):
            while i<j:
                grid[i//n][i%n], grid[j//n][j%n] = grid[j//n][j%n], grid[i//n][i%n]
                i, j = i+1, j-1
        sz=m*n
        k%=sz
        rev(0,sz-1)
        rev(0, k-1)
        rev(k, sz-1)
        return grid
