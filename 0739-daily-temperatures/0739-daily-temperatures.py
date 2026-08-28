class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack=[]
        n=len(temp)
        res=[0]*n
        for i in range(n-1, -1, -1):
            while stack and temp[i]>=temp[stack[-1]]:
                stack.pop()
            if not stack:
                res[i]=0
            else:
                res[i]=stack[-1]-i
            stack.append(i)
        return res