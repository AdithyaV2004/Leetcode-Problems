class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        ind=[0]*n
        for i, j in edges:
            ind[j]+=1
        champ=-1
        count=0
        for i in range(n):
            if ind[i]==0:
                count+=1
                champ=i
        if count>1:
            return -1
        else:
            return champ